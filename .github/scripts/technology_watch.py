#!/usr/bin/env python3
"""Check upstream review baselines, never install or silently accept releases.

Standard library only. Reuses the reporting pattern of the related MIT-licensed
infusing-a-soul project, with SHOAL's existing Renovate ledger as the source.
"""

import argparse
from datetime import datetime, timezone
import gzip
import hashlib
from html.parser import HTMLParser
import json
import os
from pathlib import Path
import re
import sys
from urllib.parse import quote, urlparse
import urllib.request

ROOT = Path(__file__).resolve().parents[2]
TITLE = "Technology release review"
MARKER = "<!-- shoal-technology-watch -->"
FAILURES = {"SOURCE_ERROR", "BASELINE_AHEAD", "SOURCE_MISMATCH"}


def version_key(value, calendar_revision=False):
    """Accept complete stable labels; never read an rc suffix as a final release."""
    match = re.fullmatch(r"(?:docker-)?v?(\d+(?:\.\d+)*)(?:-(\d+))?", value)
    if not match or (match[2] and not calendar_revision):
        raise ValueError("Unsupported stable version label")
    parts = tuple(map(int, match[1].split(".")))
    # 1.2 and 1.2.0 are equal. Calendar revision is a publisher's stable suffix.
    return parts + (0,) * max(0, 3 - len(parts)) + (int(match[2] or 0),)


def request(url, method="GET", payload=None):
    parsed = urlparse(url)
    if parsed.scheme != "https":
        raise ValueError("Sources must use HTTPS")
    headers = {"User-Agent": "shoal-technology-watch", "Accept-Encoding": "gzip"}
    if payload is not None:
        headers["Content-Type"] = "application/json"
    req = urllib.request.Request(
        url, data=None if payload is None else json.dumps(payload).encode(),
        headers=headers, method=method,
    )
    # Credentials are scoped to GitHub's API and never forwarded on redirects.
    if parsed.netloc == "api.github.com":
        req.add_header("Accept", "application/vnd.github+json")
        req.add_header("X-GitHub-Api-Version", "2022-11-28")
        if os.environ.get("GITHUB_TOKEN"):
            req.add_unredirected_header("Authorization", "Bearer " + os.environ["GITHUB_TOKEN"])
    with urllib.request.urlopen(req, timeout=30) as response:
        if urlparse(response.url).scheme != "https":
            raise ValueError("Source redirected away from HTTPS")
        raw = response.read(8_000_001)
    if len(raw) > 8_000_000:
        raise ValueError("Source response exceeded size limit")
    if raw.startswith(b"\x1f\x8b"):
        raw = gzip.decompress(raw)
    return raw.decode("utf-8")


class PythonVersions(HTMLParser):
    def __init__(self):
        super().__init__()
        self.in_anchor = False
        self.label = ""
        self.versions = []

    def handle_starttag(self, tag, attrs):
        if tag == "a":
            self.in_anchor, self.label = True, ""

    def handle_data(self, data):
        if self.in_anchor:
            self.label += data

    def handle_endtag(self, tag):
        if tag == "a" and self.in_anchor:
            match = re.fullmatch(r"Python (\d+\.\d+\.\d+)(?: - [A-Z][a-z]+\.? \d{1,2}, \d{4})?",
                                 self.label.strip())
            if match:
                self.versions.append(match[1])
            self.in_anchor = False


def source_for(item):
    kind, dep = item["datasource"], item["depName"]
    if kind in ("github-releases", "github-tags"):
        if not re.fullmatch(r"[\w.-]+/[\w.-]+", dep):
            raise ValueError("Invalid GitHub dependency")
        suffix = "releases/latest" if kind == "github-releases" else "tags?per_page=100"
        return f"https://api.github.com/repos/{dep}/{suffix}"
    if kind == "npm":
        return f"https://registry.npmjs.org/{quote(dep, safe='@')}/latest"
    if kind == "pypi":
        return f"https://pypi.org/pypi/{quote(dep, safe='')}/json"
    if kind == "node-version":
        return "https://nodejs.org/dist/index.json"
    if kind == "python-version":
        return "https://www.python.org/downloads/source/"
    raise ValueError("Unsupported datasource")


def extract_version(item, value):
    pattern = item.get("extractVersion")
    if pattern:
        pattern = pattern.replace("(?<version>", "(?P<version>")
        match = re.fullmatch(pattern, value)
        if not match:
            raise ValueError("Release tag does not match the ledger extraction rule")
        value = match["version"]
    version_key(value, item["depName"] == "openclaw/openclaw")
    return re.sub(r"^(?:docker-)?v", "", value)


def latest(item, fetch):
    raw = fetch(source_for(item))
    kind = item["datasource"]
    if kind == "github-releases":
        data = json.loads(raw)
        if data.get("draft") is not False or data.get("prerelease") is not False:
            raise ValueError("Publisher did not explicitly mark a stable release")
        value = extract_version(item, data["tag_name"])
    elif kind == "github-tags":
        candidates = []
        for tag in json.loads(raw):
            try:
                candidates.append(extract_version(item, tag["name"]))
            except ValueError:
                pass
        value = max(candidates, key=version_key)
    elif kind == "npm":
        value = json.loads(raw)["version"]
    elif kind == "pypi":
        value = json.loads(raw)["info"]["version"]
    elif kind == "node-version":
        candidates = [r["version"] for r in json.loads(raw)
                      if re.fullmatch(r"v\d+\.\d+\.\d+", r["version"])]
        value = max(candidates, key=version_key).removeprefix("v")
    elif kind == "python-version":
        parser = PythonVersions()
        parser.feed(raw)
        value = max(parser.versions, key=version_key)
    else:
        raise ValueError("Unsupported datasource")
    version_key(value, item["depName"] == "openclaw/openclaw")
    return value


def targets(root=ROOT):
    manifest = json.loads((root / ".github/technology-versions.json").read_text(encoding="utf-8"))
    items = [dict(row, evidence=".github/technology-versions.json: reviewed upstream baseline")
             for row in manifest["technologies"]]
    guide = (root / "docs/reef-setup.md").read_text(encoding="utf-8")
    docker = re.findall(r"ghcr\.io/open-webui/open-webui:v(\d+\.\d+\.\d+)", guide)
    pip = re.findall(r"pip install open-webui==(\d+\.\d+\.\d+)", guide)
    if len(set(docker)) != 1 or len(set(pip)) != 1 or docker[0] != pip[0]:
        raise ValueError("Open WebUI examples must contain matching Docker and pip pins")
    for name, dep, kind, current in [
        ("Open WebUI release for Docker example", "open-webui/open-webui", "github-releases", docker[0]),
        ("Open WebUI Python example", "open-webui", "pypi", pip[0]),
    ]:
        items.append(dict(name=name, depName=dep, datasource=kind, currentValue=current,
                          evidence="docs/reef-setup.md: documented pin, not installed software"))
    workflow = (root / ".github/workflows/technology-watch.yml").read_text(encoding="utf-8")
    uses = re.findall(r"^\s*uses:\s*(\S.*)$", workflow, re.M)
    seen_actions = {}
    for use in uses:
        match = re.fullmatch(r"([\w.-]+/[\w.-]+)@([0-9a-f]{40})\s+# (v\d+\.\d+\.\d+)", use)
        if not match:
            raise ValueError("Workflow actions must have immutable SHA pins and exact version comments")
        if match[1] in seen_actions:
            if seen_actions[match[1]] != (match[2], match[3]):
                raise ValueError("Repeated action references must use the same pin")
            continue
        seen_actions[match[1]] = (match[2], match[3])
        items.append(dict(name=match[1] + " workflow action", depName=match[1], datasource="github-releases",
                          currentValue=match[3], evidence="technology-watch.yml: " + match[2]))
    return items


def audit(items, fetch=request):
    cache, results = {}, []

    def cached(url):
        if url not in cache:
            cache[url] = fetch(url)
        return cache[url]

    for item in items:
        row = dict(item, source=source_for(item), latest=None)
        try:
            row["latest"] = latest(item, cached)
            calendar = item["depName"] == "openclaw/openclaw"
            current_key = version_key(item["currentValue"], calendar)
            latest_key = version_key(row["latest"], calendar)
            row["status"] = ("NEW_RELEASE" if latest_key > current_key else
                             "BASELINE_AHEAD" if latest_key < current_key else "CURRENT")
        except Exception as error:
            row.update(status="SOURCE_ERROR", error=type(error).__name__ + ": release not verified")
        results.append(row)
    webui = [r for r in results if r["depName"] in ("open-webui/open-webui", "open-webui")]
    if len(webui) == 2 and all(r["latest"] for r in webui):
        if version_key(webui[0]["latest"]) != version_key(webui[1]["latest"]):
            for row in webui:
                row.update(status="SOURCE_MISMATCH", error="Open WebUI GitHub and PyPI stable releases differ")
    return results


def render(results, checked_at):
    lines = ["# SHOAL technology release check", "", f"Checked at: {checked_at}", "",
             "These are upstream review candidates. No reef, workstation, model, or documentation pin was upgraded.",
             "CURRENT compares a fetched release with the stated baseline; it does not establish an installed version.", "",
             "| Technology | Baseline / pin | Stable retrieved | Result |", "| --- | --- | --- | --- |"]
    for row in results:
        cells = [row["name"], row["currentValue"], row["latest"] or "Unknown", row["status"]]
        lines.append("| " + " | ".join(str(v).replace("|", "\\|").replace("\n", " ") for v in cells) + " |")
    lines += ["", "## Evidence and acceptance", ""]
    for row in results:
        lines.append(f"- {row['name']}: [{row['datasource']}]({row['source']}); {row['evidence']}.")
        if row.get("error"):
            lines.append("  " + row["error"] + ".")
    lines += ["", "Git tags use the highest stable version among the publisher's latest 100 tags.",
              "The Docker example is compared with the publisher's stable release; registry tag availability still requires verification.",
              "Follow docs/technology-update-plan.md: check compatibility and release notes, keep the Open WebUI examples paired,",
              "test backups/restoration and behavior on the actual reef before a live upgrade. Source failures remain unresolved.",
              "Browsers, operating systems, formats, and models retain the separate operator review cadence in that plan.", ""]
    return "\n".join(lines)


def sync_issue(results, report, repository, api=request):
    if not re.fullmatch(r"[\w.-]+/[\w.-]+", repository):
        raise ValueError("Repository must be owner/name")
    base = f"https://api.github.com/repos/{repository}/issues"
    matches = []
    for page in range(1, 101):
        batch = json.loads(api(f"{base}?state=open&per_page=100&page={page}"))
        matches += [i for i in batch if "pull_request" not in i
                    and i.get("user", {}).get("login") == "github-actions[bot]"
                    and MARKER in (i.get("body") or "")]
        if len(batch) < 100:
            break
    else:
        raise ValueError("Issue pagination incomplete")
    if len(matches) > 1:
        raise ValueError("Multiple bot-owned tracking issues require review")
    findings = [r for r in results if r["status"] != "CURRENT"]
    if not findings:
        if matches:
            api(f"{base}/{matches[0]['number']}", method="PATCH",
                payload={"state": "closed", "state_reason": "completed"})
            return "Closed resolved tracking issue"
        return "No findings; no issue change"
    digest = hashlib.sha256(json.dumps(results, sort_keys=True).encode()).hexdigest()
    stamp = f"<!-- findings:{digest} -->"
    body = f"{MARKER}\n{stamp}\n\n{report}"
    if matches:
        issue = matches[0]
        if stamp in issue["body"]:
            return "Unchanged findings; no issue edit"
        api(f"{base}/{issue['number']}", method="PATCH", payload={"body": body})
        return f"Updated tracking issue #{issue['number']}"
    issue = json.loads(api(base, method="POST", payload={"title": TITLE, "body": body}))
    return f"Created tracking issue #{issue['number']}"


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-dir", required=True, type=Path, help="Explicit approved report destination")
    parser.add_argument("--update-issue", action="store_true", help="Use GITHUB_TOKEN to maintain the bot-owned issue")
    args = parser.parse_args(argv)
    results = audit(targets())
    checked_at = datetime.now(timezone.utc).isoformat(timespec="seconds")
    report = render(results, checked_at)
    args.output_dir.mkdir(parents=True, exist_ok=True)
    (args.output_dir / "technology-watch.md").write_text(report, encoding="utf-8")
    (args.output_dir / "technology-watch.json").write_text(
        json.dumps({"checked_at": checked_at, "python": sys.version.split()[0], "results": results}, indent=2) + "\n",
        encoding="utf-8")
    if os.environ.get("GITHUB_STEP_SUMMARY"):
        with open(os.environ["GITHUB_STEP_SUMMARY"], "a", encoding="utf-8") as summary:
            summary.write(report)
    for row in results:
        print(f"{row['name']}: {row['currentValue']} -> {row['latest']} ({row['status']})")
    if args.update_issue:
        if not os.environ.get("GITHUB_TOKEN"):
            raise RuntimeError("GITHUB_TOKEN is required for issue updates")
        print(sync_issue(results, report, os.environ.get("GITHUB_REPOSITORY", "")))
    # Candidate alerts are successful detection; failed lookups are failed checks.
    return 1 if any(row["status"] in FAILURES for row in results) else 0


if __name__ == "__main__":
    sys.exit(main())
