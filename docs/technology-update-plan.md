# Technology Update Plan

**Prepared:** 2026-09-18, America/Chicago.
**Scope:** SHOAL documentation, reference versions, and contributor tooling. A live reef remains an independently operated host.

## What is configured

[Renovate configuration](../.github/renovate.json5) checks before 06:00 Monday in `America/Chicago`. It excludes unstable releases, limits concurrent PRs to three, and leaves automatic merging disabled.

Two update paths are configured:

1. The existing regex managers update the actual Open WebUI Docker and pip pins in [reef setup](reef-setup.md). Both share one PR group. Each PR must keep their numeric versions equal and confirm that both artifacts exist.
2. A JSONata manager reads 15 upstream baselines from [technology-versions.json](../.github/technology-versions.json): Ollama, Docker Engine, Tailscale, WSL, Python, Node.js, npm, pip, PowerShell, Git, GitHub CLI, OpenClaw, Homebrew, systemd, and Renovate. It groups changes into an upstream review PR. These values trigger a review; they do not install software or certify compatibility.

Renovate's [JSONata manager](https://docs.renovatebot.com/modules/manager/jsonata/) extracts the dependency name, baseline, datasource, and versioning rule. Docker Engine's `docker-v` tag prefix and Git's `v` prefix are explicitly handled. [Stable-release filtering](https://docs.renovatebot.com/configuration-options/#ignoreunstable) remains enabled. Upstream references intentionally use current stable releases; a production LTS or compatibility constraint is selected during host review.

The [inventory](technology-inventory.md) is a dated research snapshot. The ledger's `seededAtUtc` records initial creation only. On accepting a release-review PR, update the inventory's versions, sources, and verification date. Never present an unchanged snapshot date as a new check or change "unknown installed" to "installed" based on a release feed.

## Activate and prove it works

The configuration is prepared locally. No hosted scheduled run or automatic update is claimed by this change.

1. Publish the reviewed files through the repository's normal branch/PR process and merge to the default branch.
2. Enable the [Renovate GitHub App](https://github.com/apps/renovate) for `OKHP3/shoal-ai-server`, or verify its existing access. Complete onboarding if offered. Do not add a broad personal access token to this repository.
3. Inspect the first Renovate run and Dependency Dashboard. It must discover two Open WebUI declarations and all 15 ledger entries. The current 0.10.2 pins should produce a 0.11.3-or-newer stable proposal if that release remains current. The latest-seeded ledger will normally have no immediate changes.
4. Confirm each PR changes only expected files, includes release links, contains no prerelease/nightly/dev tags, and does not merge itself. Reject a PR if one Open WebUI artifact has not yet reached the matching version.
5. Confirm a real scheduled run the following Monday. If none appears, inspect App access, onboarding, schedule, permissions, and extraction errors before treating monitoring as active. Absence of a PR does not prove everything is current.

These are repository configuration instructions, not an unattended host-upgrade job. The owner/operator performs activation and acceptance. No new GitHub Actions workflow, server runtime, or root dependency installation is required for this design.

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
| Markdown, JSON, JSON5, YAML, ECMAScript standards | Quarterly review and when a parser/runtime changes | Existing content parses/renders correctly |
| Models | Review selected-tag changes and new candidates | Digest, license, memory/latency and output evaluation recorded privately; no automatic family substitution |
| Imported Agent Skills | Canonical source review through skill promotion process | Source revision, license, focused diff, tests, mirror parity where applicable |
| Research-only products and absent frontend frameworks | No install/update action | Add a real manifest/pin, tests, and inventory row if adopted |
| Hosted services | Vendor manages service version | Verify actual integration behavior; do not invent semver dependencies |

Monthly and quarterly entries are an operator plan, not installed Codex reminders or GitHub schedules. Expedite relevant security releases outside the weekly window after assessing compatibility. Failed lookups, validation, and unsupported hosts remain visibly pending.

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

Monitoring is active only after successful hosted extraction and a scheduled run. Documentation updates require validated examples and links. A live upgrade is complete only after installed-version, backup/restore, and functional checks pass on that host. Local configuration validation does not prove those remote outcomes.

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
