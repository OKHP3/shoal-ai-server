# Technology Update Plan

**Prepared:** 2026-09-18, America/Chicago.
**Scope:** SHOAL documentation, reference versions, and contributor tooling. A live reef remains an independently operated host.

## Native release monitoring, added 2026-10-22

[Technology release watch](../.github/workflows/technology-watch.yml) runs every Monday at 10:17 UTC, before 06:00 in America/Chicago throughout the year. It also runs after relevant changes reach `main` and supports a manual run. Its [Python standard-library checker](../.github/scripts/technology_watch.py) needs no third-party App, new secret, package installation, or reef access.

The checker reads all 15 existing ledger entries, the two Open WebUI example pins, and the two immutable action pins in its own workflow. It queries primary GitHub, npm, PyPI, Python, and Node release sources. Complete stable labels are required; prerelease labels are rejected. A source error, baseline ahead of the fetched release, or disagreement between Open WebUI's GitHub and PyPI releases fails the check visibly. The Docker example is compared with the publisher's release; the matching container tag must still be checked before accepting a pin update.

Each hosted run writes a dated summary and retains a JSON/Markdown artifact for 14 days. Findings maintain one bot-owned [Technology release review issue](https://github.com/OKHP3/shoal-ai-server/issues?q=is%3Aissue+%22Technology+release+review%22). Repeated unchanged findings do not edit the issue or send repeated comments. Once the reviewed baselines catch up and no source failures remain, the checker closes its issue. It never edits a human-owned issue. New-release findings are successful detection, not checker failures.

Pull requests run the checker's regression tests with read-only access. Canonical-branch monitoring additionally receives `issues: write`; it has no code-write, deployment, approval, or administration permission. Checkout credentials are not persisted. Only GitHub API requests receive the built-in workflow token; registry and vendor requests do not receive it.

Run locally with an explicit approved report destination:

```text
python -B -m unittest discover -s .github/scripts/tests -v
python -B .github/scripts/technology_watch.py --output-dir <approved-report-directory>
```

Local validation on 2026-10-22 passed 14 regression tests and verified all 19 release lookups. The first lookup exposed dated Python link labels; the parser was corrected and a regression fixture added before all lookups passed. The original September inventory remains a dated snapshot. Read the latest [hosted run](https://github.com/OKHP3/shoal-ai-server/actions/workflows/technology-watch.yml) for current candidate versions and source status. A manual or push run proves execution of that trigger, not a future scheduled run.

The workflow detects and tracks review work. Updating a ledger baseline acknowledges reviewed upstream research only. Updating the paired documentation pins requires the acceptance sequence below. No action installs software, substitutes a model, or upgrades a live reef automatically.

## Optional Renovate update proposals

[Renovate configuration](../.github/renovate.json5) checks before 06:00 Monday in `America/Chicago`. It excludes unstable releases, limits concurrent PRs to three, and leaves automatic merging disabled.

Two update paths are configured:

1. The existing regex managers update the actual Open WebUI Docker and pip pins in [reef setup](reef-setup.md). Both share one PR group. Each PR must keep their numeric versions equal and confirm that both artifacts exist.
2. A JSONata manager reads 15 upstream baselines from [technology-versions.json](../.github/technology-versions.json): Ollama, Docker Engine, Tailscale, WSL, Python, Node.js, npm, pip, PowerShell, Git, GitHub CLI, OpenClaw, Homebrew, systemd, and Renovate. It groups changes into an upstream review PR. These values trigger a review; they do not install software or certify compatibility.

Renovate's [JSONata manager](https://docs.renovatebot.com/modules/manager/jsonata/) extracts the dependency name, baseline, datasource, and versioning rule. Docker Engine's `docker-v` tag prefix and Git's `v` prefix are explicitly handled. [Stable-release filtering](https://docs.renovatebot.com/configuration-options/#ignoreunstable) remains enabled. Upstream references intentionally use current stable releases; a production LTS or compatibility constraint is selected during host review.

The [inventory](technology-inventory.md) is a dated research snapshot. The ledger's `seededAtUtc` records initial creation only. On accepting a release-review PR, update the inventory's versions, sources, and verification date. Never present an unchanged snapshot date as a new check or change "unknown installed" to "installed" based on a release feed.

## Activate and verify Renovate if used

The Renovate configuration is published, but hosted App activation has not been verified. No Dependency Dashboard or Renovate PR was present at the 2026-10-22 closeout audit. Native release monitoring above operates independently; absence of Renovate does not prevent detection. Renovate can additionally prepare the version-edit PRs when the owner grants the App access.

1. Publish the reviewed files through the repository's normal branch/PR process and merge to the default branch.
2. Enable the [Renovate GitHub App](https://github.com/apps/renovate) for `OKHP3/shoal-ai-server`, or verify its existing access. Complete onboarding if offered. Do not add a broad personal access token to this repository.
3. Inspect the first Renovate run and Dependency Dashboard. It must discover two Open WebUI declarations and all 15 ledger entries. The current 0.10.2 pins should produce a 0.11.3-or-newer stable proposal if that release remains current. The latest-seeded ledger will normally have no immediate changes.
4. Confirm each PR changes only expected files, includes release links, contains no prerelease/nightly/dev tags, and does not merge itself. Reject a PR if one Open WebUI artifact has not yet reached the matching version.
5. Confirm a real scheduled run the following Monday. If none appears, inspect App access, onboarding, schedule, permissions, and extraction errors before treating monitoring as active. Absence of a PR does not prove everything is current.

The owner/operator performs App activation and acceptance. These instructions are not an unattended host-upgrade job. Neither monitoring route defines a SHOAL server runtime or requires a root dependency installation.

## Review and upgrade sequence

| Stage | Required result |
|---|---|
| Detect | Renovate identifies a stable increment, or a vendor release/advisory prompts review. Source failures and incompatible releases remain unresolved. |
| Assess | Read release notes, migrations, supported OS/CPU/Python/Node ranges, removed configuration keys, data format changes, and relevant advisories. Identify the actual installed version first. |
| Prepare | Keep the prior exact version/image digest and configuration; take an encrypted Open WebUI data backup. Verify restoration into a disposable environment before changing a live reef. |
| Test | Test the candidate in a disposable environment with representative fish. Check two-user sign-in, account/chat separation, permissions, model listing/inference, saved history, and restart persistence. Check RAG/gateway/Tailscale features if used. |
| Update references | Keep Docker and pip examples on the same accepted version. Update the inventory and affected commands together. Check links/paths and run `git diff --check`. |
| Release | Merge the reviewed documentation PR. Schedule the live change with its operator, install the exact accepted release through the supported updater, and repeat smoke tests. |
| Verify / recover | Record installed versions after restart. If checks fail, restore the previous software and matching backup. Reverting a container alone may not reverse a database migration. |

For Open WebUI's Python path, follow its package metadata. At this snapshot it supports 3.11 or 3.12, although Python 3.14.7 is language latest. For contributor helpers, prefer stable Python and Node LTS, run the affected skill's existing tests, and preserve imported skill provenance.

The first backlog is to assess Open WebUI 0.10.2 to 0.11.3, establish stable contributor Python, and assess Node 24.21.0 LTS before npm 12.0.2. This plan does not upgrade the workstation or a remote host automatically.

## Coverage outside Renovate

| Category | Cadence / mechanism | Acceptance evidence |
|---|---|---|
| Docker Desktop, curl, Bash, Zsh, platform Git builds, VS Code | Vendor updater plus monthly official release review | Installed version and relevant commands still work |
| Windows, WSL, macOS, Linux, drivers, launchd, system utilities | Supported vendor/distribution security updates; separate feature migration plan | Correct device/channel, restart completed, reef smoke tests pass |
| Chrome, Edge, Firefox, Safari, fish operating systems | Vendor automatic security updates where supported; monthly smoke test | Sign-in, response streaming, reopening history work |
| Markdown, JSON, JSON5, YAML, TOML, ECMAScript, HTML, and SVG/XML standards | Quarterly review and when a parser/runtime or publishing target changes | Existing content parses/renders correctly; distinguish draft standards from final releases |
| PNG, JPEG, ICO, and vector brand assets | Review when replacing assets or changing browser/OS support | Dimensions, transparency, accessibility, and rendering verified; no automatic re-encoding on a format revision |
| Models | Review selected-tag changes and new candidates | Digest, license, memory/latency and output evaluation recorded privately; no automatic family substitution |
| Imported Agent Skills | Canonical source review through skill promotion process | Source revision, license, focused diff, tests, mirror parity where applicable |
| Research-only products and absent frontend frameworks | No install/update action | Add a real manifest/pin, tests, and inventory row if adopted |
| Hosted services | Vendor manages service version | Verify actual integration behavior; do not invent semver dependencies |

Monthly and quarterly entries are an operator plan, not installed Codex reminders or additional GitHub schedules. The native weekly workflow covers the 19 entries described above. Expedite relevant security releases outside that window after assessing compatibility. Failed lookups, validation, and unsupported hosts remain visibly pending.

## Collect real installed versions

Run only relevant commands on the selected host. These are read-only examples, not commands executed on a reef during this audit:

```text
ollama --version
ollama list
docker version
docker inspect --format '{{.Config.Image}} {{.Image}}' open-webui
python --version
python -m pip show open-webui
tailscale version
wsl --version
node --version
npm --version
git --version
```

For Docker, confirm the running image ID and repository digest, not only its tag. For pip, inspect the environment actually serving Open WebUI. Record model digests and browser/OS versions on real devices. Keep hostnames, private IPs, credentials, user data, and machine-specific reports out of this public repository.

## Completion criteria

Native monitoring requires a successful canonical-branch hosted run, complete source coverage, and its visible report/review issue. Record trigger types accurately: the first future scheduled run remains unobserved until it actually executes. Renovate activation requires its successful hosted extraction and scheduled run separately. Documentation updates require validated examples and links. A live upgrade is complete only after installed-version, backup/restore, and functional checks pass on that host. Local validation does not prove those remote outcomes.

## Validation of this change

Checked locally on 2026-09-18 (2026-09-19 UTC):

| Check | Result |
|---|---|
| Renovate 44.103.2 configuration validator, strict mode | PASS |
| Actual Renovate JSONata extraction and version scheme validation | PASS: all 15 ledger entries |
| Actual Renovate replacement trials in disposable files | PASS: all 15 entries changed only their own baseline |
| Open WebUI extraction and replacement trial | PASS: both 0.10.2 examples moved to 0.11.3 in a disposable copy; repository pins remain 0.10.2 |
| File targeting, Docker tag-prefix extraction, prerelease tag rejection, no-automerge setting | PASS |
| Changed-file local links, Markdown fences, JSON parsing, and `git diff --check` | PASS |
| Windows native RE2 regex engine | WARN: unavailable to the downloaded validator; it used JavaScript RegExp. Hosted engine behavior still needs verification. |
| Hosted Renovate extraction, datasource lookup, PR creation, and scheduled execution | NOT RUN |
| Live reef installation, upgrade, browser smoke tests, and backup/restore | NOT RUN |
| Replit inspection | BLOCKED: connector requires reauthentication |

The version-change trials validate edit behavior, not upstream availability or runtime compatibility. The one-off validator installation used the tool cache and added no repository package dependency.
