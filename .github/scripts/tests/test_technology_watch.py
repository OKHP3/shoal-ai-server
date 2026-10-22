"""Regression checks for release evidence, partial failure, and issue ownership."""

import importlib.util
import json
from pathlib import Path
import unittest
from unittest.mock import patch

SPEC = importlib.util.spec_from_file_location("technology_watch", Path(__file__).resolve().parents[1] / "technology_watch.py")
watch = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(watch)


def item(dep="owner/project", kind="github-releases", current="1.2.0"):
    return dict(name=dep, depName=dep, datasource=kind, currentValue=current, evidence="test fixture")


def release(version="v1.2.1", **extra):
    return json.dumps(dict(tag_name=version, draft=False, prerelease=False, **extra))


class ReleaseEvidenceTests(unittest.TestCase):
    def test_whole_stable_labels_and_padding(self):
        self.assertEqual(watch.version_key("v1.2"), watch.version_key("1.2.0"))
        for value in ("3.15.0rc1", "v3.2.1-beta", "1.2.3+build", "version 1.2.3"):
            with self.assertRaises(ValueError):
                watch.version_key(value)

    def test_publisher_calendar_revision_is_narrowly_supported(self):
        rows = watch.audit([item("openclaw/openclaw", current="v2026.9.5")],
                           lambda _: release("v2026.10.21-1"))
        self.assertEqual(rows[0]["status"], "NEW_RELEASE")
        with self.assertRaises(ValueError):
            watch.version_key("1.2.3-1")

    def test_github_must_explicitly_publish_stable_release(self):
        for payload in ({"tag_name": "v1.2.1"}, {"tag_name": "v1.2.1", "draft": False, "prerelease": True}):
            rows = watch.audit([item()], lambda _: json.dumps(payload))
            self.assertEqual(rows[0]["status"], "SOURCE_ERROR")

    def test_python_does_not_misread_rc_as_final(self):
        html = ('<a>Python 3.16.0rc1 - Oct. 21, 2026</a>'
                '<a>Python 3.15.1 - Oct. 21, 2026</a><a>Python 3.14.7</a>')
        self.assertEqual(watch.latest(item("python", "python-version"), lambda _: html), "3.15.1")

    def test_node_selects_highest_stable_independent_of_order(self):
        raw = json.dumps([{"version": "v24.20.0"}, {"version": "v27.0.0-rc.1"}, {"version": "v26.9.0"}])
        self.assertEqual(watch.latest(item("node", "node-version"), lambda _: raw), "26.9.0")

    def test_tag_extraction_is_anchored_and_skips_prereleases(self):
        technology = dict(item("moby/moby", "github-tags"), extractVersion=r"^docker-v(?<version>\d+\.\d+\.\d+)$")
        raw = json.dumps([{"name": "docker-v29.9.0-rc1"}, {"name": "docker-v29.8.1"}, {"name": "garbage"}])
        self.assertEqual(watch.latest(technology, lambda _: raw), "29.8.1")

    def test_partial_network_failure_does_not_hide_other_results(self):
        def fetch(url):
            if "bad/project" in url:
                raise OSError("private response data that must not reach report")
            return release()
        rows = watch.audit([item("bad/project"), item("good/project")], fetch)
        self.assertEqual([r["status"] for r in rows], ["SOURCE_ERROR", "NEW_RELEASE"])
        self.assertNotIn("private response", watch.render(rows, "fixture"))

    def test_baseline_ahead_is_a_failure_not_a_successful_downgrade(self):
        rows = watch.audit([item(current="9.0.0")], lambda _: release())
        self.assertEqual(rows[0]["status"], "BASELINE_AHEAD")
        self.assertIn(rows[0]["status"], watch.FAILURES)

    def test_open_webui_sources_must_agree(self):
        def fetch(url):
            return json.dumps({"info": {"version": "0.12.0"}}) if "pypi.org" in url else release("v0.11.3")
        rows = watch.audit([item("open-webui/open-webui", current="0.10.2"),
                            item("open-webui", "pypi", "0.10.2")], fetch)
        self.assertEqual([r["status"] for r in rows], ["SOURCE_MISMATCH", "SOURCE_MISMATCH"])

    def test_real_manifest_and_pins_are_all_covered_without_duplicate_actions(self):
        rows = watch.targets()
        self.assertEqual(len(rows), 19)
        self.assertEqual(sum(r["depName"] == "actions/checkout" for r in rows), 1)
        self.assertEqual(len({r["depName"] for r in rows}), len(rows))


class IssueOwnershipTests(unittest.TestCase):
    def setUp(self):
        self.rows = watch.audit([item()], lambda _: release())

    def test_unchanged_findings_do_not_edit_even_if_report_date_changes(self):
        calls = []
        saved = []
        def api(url, method="GET", payload=None):
            calls.append((method, payload))
            if method == "GET":
                return json.dumps(saved)
            if method == "POST":
                saved.append(dict(number=4, user={"login": "github-actions[bot]"}, body=payload["body"]))
                return '{"number":4}'
            self.fail("unchanged findings caused a PATCH")
        watch.sync_issue(self.rows, watch.render(self.rows, "first date"), "owner/repo", api)
        result = watch.sync_issue(self.rows, watch.render(self.rows, "later date"), "owner/repo", api)
        self.assertIn("Unchanged", result)
        self.assertEqual([m for m, _ in calls], ["GET", "POST", "GET"])

    def test_matching_user_issue_is_never_overwritten(self):
        writes = []
        def api(url, method="GET", payload=None):
            if method == "GET":
                return json.dumps([dict(number=1, user={"login": "owner"}, body=watch.MARKER)])
            writes.append(method)
            return '{"number":2}'
        watch.sync_issue(self.rows, "report", "owner/repo", api)
        self.assertEqual(writes, ["POST"])

    def test_no_findings_only_closes_owned_issue(self):
        writes = []
        def api(url, method="GET", payload=None):
            if method == "GET":
                return json.dumps([dict(number=4, user={"login": "github-actions[bot]"}, body=watch.MARKER)])
            writes.append((url, payload))
            return '{}'
        rows = watch.audit([item()], lambda _: release("v1.2.0"))
        watch.sync_issue(rows, "report", "owner/repo", api)
        self.assertEqual(writes, [("https://api.github.com/repos/owner/repo/issues/4",
                                   {"state": "closed", "state_reason": "completed"})])

    def test_credentials_only_go_to_github_api_and_are_not_redirected(self):
        seen = []
        class Response:
            url = "https://example.org/response"
            def __enter__(self): return self
            def __exit__(self, *args): pass
            def read(self, limit): return b'{}'
        def open_url(req, **kwargs):
            seen.append(req)
            return Response()
        with patch.dict(watch.os.environ, {"GITHUB_TOKEN": "fixture-credential"}), \
                patch.object(watch.urllib.request, "urlopen", side_effect=open_url):
            watch.request("https://api.github.com/repos/owner/repo/releases/latest")
            watch.request("https://pypi.org/pypi/pip/json")
        self.assertEqual(seen[0].unredirected_hdrs["Authorization"], "Bearer fixture-credential")
        self.assertNotIn("Authorization", seen[0].headers)
        self.assertNotIn("Authorization", dict(seen[1].header_items()))


if __name__ == "__main__":
    unittest.main()
