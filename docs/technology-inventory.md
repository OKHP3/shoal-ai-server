# SHOAL Technology Inventory

**Audit date:** 2026-09-18, America/Chicago. Upstream retrievals continued on 2026-09-19 UTC.
**Repository baseline:** `b3ef495f88c1437d344f0834fb6572ddfa43f575`, confirmed against GitHub main.

The question is which technologies SHOAL uses, which versions are declared or observable, and how to keep them current without breaking a reef.

**Confirmed:** SHOAL is a documentation and reference-build project with executable contributor tooling under `.agents/skills/` and a publication mirror under `skills/`. It has no server application, root package manifest, dependency lockfile, Dockerfile, Compose deployment, or project-wide CI workflow. The earlier inventory incorrectly said there was no JavaScript, Python code, Node.js usage, or package manifest anywhere in the checkout.

This is a dated audit. The ongoing [release review ledger](../.github/technology-versions.json) is a separate, Renovate-managed record. Its values are upstream review baselines, not installed versions or deployment targets. See the [update plan](technology-update-plan.md) for activation and upgrade acceptance.

## Evidence and coverage

The audit inspected all 421 tracked files, including hidden directories: 22 Python files, 17 JavaScript ES modules, two CommonJS files, and seven nested `package.json` files. Python imports use the standard library. JavaScript uses Node built-ins and local modules. All seven manifests declare private packages at `0.1.0`, with no external dependency declarations or runtime engine pins.

The seven packages are `as-is-process-capture`, `decision-model-authoring`, `elicitation-and-interview-facilitation`, `future-state-and-change-strategy`, `publication-and-handoff-packaging`, `process-gap-and-exception-analysis`, and `process-intake-and-scope`, under the `@bp-skill` namespace. Their versions describe imported skills, not Node.js or npm releases. Other skill versions and provenance remain in each `SKILL.md` and the [skill catalog](../.agents/skills/README.md).

**Unknown:** Versions installed on a live reef, fish devices, or Replit. Replit inspection was blocked by connector reauthentication. Local command output below describes the audit workstation only. No Ollama/Open WebUI runtime, container dependency tree, GPU driver, model digest, or remote server was inspected. This covers directly declared technologies and documented host dependencies, not the transitive contents of an uninspected upstream container.

## Documented reef stack

Every latest-release link below is a primary source checked during this audit. GitHub rows use the publisher's non-draft, non-prerelease latest release. Registry rows use current stable package metadata. A new release is an upgrade candidate, not evidence of SHOAL compatibility.

| Technology | In-place repository version | Latest stable observed | Update route |
|---|---|---|---|
| Ollama | Unpinned installer in [reef setup](reef-setup.md); installed version unknown | [0.34.2](https://github.com/ollama/ollama/releases/tag/v0.34.2) | Renovate release review; host installer after testing |
| Open WebUI container | `ghcr.io/open-webui/open-webui:v0.10.2` in reef setup | [0.11.3](https://github.com/open-webui/open-webui/releases/tag/v0.11.3) | Renovate edits the image tag in a PR |
| Open WebUI Python package | `open-webui==0.10.2` in reef setup | [0.11.3](https://pypi.org/project/open-webui/0.11.3/) | Same Renovate PR group as the image |
| Docker Desktop | Unpinned; actual Desktop version unknown | [4.91.0](https://docs.docker.com/desktop/release-notes/) | Vendor updater; monthly review |
| Docker Engine / CLI | Unpinned; workstation CLI `29.6.1`, server not queried | [29.8.1](https://github.com/moby/moby/releases/tag/docker-v29.8.1) | Renovate review; host package manager |
| Python for Open WebUI | Was unspecified; guide now states 3.11 or 3.12, no patch pin | Language latest: [3.14.7](https://www.python.org/getit/); Open WebUI requires `>=3.11,<3.13.0a1` | Use the latest supported patch on a compatible Python line |
| pip | Unpinned installer | [26.2.1](https://pypi.org/project/pip/26.2.1/) | Renovate review; update inside the chosen environment |
| Tailscale | Unpinned optional remote access | [1.102.4](https://github.com/tailscale/tailscale/releases/tag/v1.102.4) | Renovate review plus host updater |
| WireGuard | Protocol underneath Tailscale; no separately selected package | No independent SHOAL package version | Update through Tailscale; [architecture source](https://tailscale.com/security) |
| WSL / WSL2 | `wsl --install`, no package pin; WSL2 names the architecture | [2.7.14](https://github.com/microsoft/WSL/releases/tag/2.7.14) | Renovate review; Windows/WSL updater |
| OpenClaw | Optional [gateway example](openclaw-gateway-integration.md), unpinned | [2026.9.5](https://github.com/openclaw/openclaw/releases/tag/v2026.9.5) | Review release/configuration changes before editing examples |

Open WebUI's [quick start](https://docs.openwebui.com/getting-started/quick-start/) supports Python 3.11 and 3.12; its [PyPI metadata](https://pypi.org/pypi/open-webui/json) confirms the constraint. Python 3.14 is not a compatible target for that installation path.

## Contributor tooling and formats

| Technology | Repository use and in-place version | Latest stable observed | Update route |
|---|---|---|---|
| JavaScript | 19 `.mjs`/`.cjs` skill helpers/tests; no language edition pinned | [ECMAScript 2026, edition 17](https://ecma-international.org/publications-and-standards/standards/ecma-262/) | Review features with Node compatibility; a standard is not an installable dependency |
| Node.js | Runs helpers; no engine pin; workstation `24.11.1` | [26.9.0 Current; 24.21.0 LTS](https://nodejs.org/en/blog) | Renovate watches Current; prefer supported LTS for helper execution |
| npm | Seven packages expose `npm test`; no pin; workstation `11.6.2` | [12.0.2](https://registry.npmjs.org/npm/latest) | Renovate review; check Node engines first |
| Python for skills | Standard-library helpers; individual skills state 3.9+ or 3.10+; workstation `3.14.0rc1` | [3.14.7](https://www.python.org/getit/) | Use stable contributor Python and run affected skill tests |
| pip on workstation | `25.1.1`; unnecessary for standard-library helpers | [26.2.1](https://pypi.org/project/pip/26.2.1/) | Environment-specific update |
| Git | Version control and helper subprocesses; no pin; workstation `2.55.0.windows.5` | [2.55.0 upstream](https://git-scm.com/); [2.55.0.windows.5 Windows](https://github.com/git-for-windows/git/releases/tag/v2.55.0.windows.5) | Renovate watches upstream; vendor updates platform build |
| GitHub CLI | Skill maintenance commands; no pin; workstation `2.96.0` | [2.101.0](https://github.com/cli/cli/releases/tag/v2.101.0) | Renovate review plus host updater |
| Renovate | Existing `.github/renovate.json5`; hosted service version not controlled here | [44.103.2](https://github.com/renovatebot/renovate/releases/tag/44.103.2) | Hosted service updates itself; ledger watches releases |
| Markdown | Documents/skills; GitHub renders it; no local renderer pin | [GFM 0.29-gfm](https://github.github.com/gfm/), [CommonMark 0.31.2](https://spec.commonmark.org/) | Review rendering and links |
| JSON | Metadata/fixtures; runtime built-in parsers | [RFC 8259](https://www.rfc-editor.org/info/rfc8259/) | Standards review with runtime updates |
| JSON5 | Renovate filename; contents also parse as JSON | [Specification 1.0.0](https://spec.json5.org/) | Renovate owns its parser; no repository JSON5 package |
| YAML | Skill configuration/fixtures/templates; local minimal parser | [Specification 1.2.2](https://yaml.org/spec/1.2.2/) | Validate supported subset; no PyYAML/npm YAML dependency declared |
| Mermaid | One fenced example in a thread-extraction fixture; no installed renderer | [npm 12.0.0](https://registry.npmjs.org/mermaid/latest) | No dependency to upgrade; preserve fixture provenance |

Latest npm requires Node `^22.22.2 || ^24.15.0 || >=26.0.0`, according to its [registry metadata](https://registry.npmjs.org/npm/latest). Workstation Node 24.11.1 does not meet that requirement. Upgrade and test Node before adopting that npm release.

## Host tools, operating systems, and fish

These are platform choices, not locked application dependencies. Installed versions are unknown unless explicitly listed. Prefer vendor-supported updates for the actual device over arbitrary upstream builds.

| Technology | In-place evidence | Stable reference checked | Maintenance responsibility |
|---|---|---|---|
| Bash / POSIX sh | Shell examples/installer; no pin | [Bash 5.3 release line](https://www.gnu.org/software/bash/manual/html_node/index.html); patch level distribution-specific | Reef OS; sh has multiple implementations |
| Zsh | Gateway shell examples; no pin | [5.9.2](https://www.zsh.org/mla/announce/) | macOS/package manager |
| PowerShell | Windows examples; workstation `7.6.5` | [7.6.6](https://github.com/PowerShell/PowerShell/releases/tag/v7.6.6) | Renovate review; host updater; distinguish Windows PowerShell 5.1 |
| curl | Installer/API checks; workstation `8.21.0` | [8.22.0](https://curl.se/download.html) | Host updater; monthly review |
| systemd | Linux service examples; no pin | [261.3](https://github.com/systemd/systemd/releases/tag/v261.3) | Renovate review; distribution-owned updates |
| launchd / launchctl | macOS service examples; no independent pin | Bundled with macOS | Apple software updates |
| Homebrew | Optional gateway service inspection; no pin | [7.0.4](https://github.com/Homebrew/brew/releases/tag/7.0.4) | Renovate review; Homebrew updater |
| Windows / WSL host | No supported build pin; workstation `10.0.26200.9457`, WSL `2.7.14.0` | [Windows 11 26H1 for specific new devices; 25H2 for existing devices](https://learn.microsoft.com/en-us/windows/release-health/windows11-release-information) | Windows Update for device/channel; plan major migrations separately |
| macOS | No version pin | [27.0](https://support.apple.com/en-us/109033) | Apple updates and hardware compatibility |
| Linux | No globally selected distribution; Ubuntu appears in reference builds | [Ubuntu 26.04.1 LTS](https://ubuntu.com/download/desktop) is a reference, not a universal Linux version | Distribution security updates; scheduled release migration |
| Chrome | Fish browser; no pin | [153.0.8010.52/.53 Windows/macOS; .52 Linux](https://chromereleases.googleblog.com/search/label/Stable%20updates) | Browser updater, then smoke test |
| Edge | Fish browser; no pin | [153.0.4234.48](https://learn.microsoft.com/en-us/deployedge/microsoft-edge-relnote-stable-channel) | Browser updater, then smoke test |
| Firefox | Fish browser; no pin | [156.0](https://www.firefox.com/en-US/firefox/156.0/releasenotes/) | Browser updater, then smoke test |
| Safari / WebKit | Apple fish browser; no project pin | [Safari 27](https://support.apple.com/en-ca/149039); WebKit delivered with the browser | Check the actual OS update offer |
| ChromeOS | Fish OS, no target device/pin | [16765.49.0](https://chromereleases.googleblog.com/search/label/Stable%20updates) | Device updater; availability varies by device |
| Android | Fish OS, no target device/pin | [Android 17](https://developer.android.com/blog/posts/android-17-is-here); vendor build/security patch varies | Device vendor's supported channel |
| iOS / iPadOS | Fish OS, no target device/pin | [27](https://support.apple.com/en-ca/100100) | Apple updates for compatible devices |
| VS Code | Optional editor; workstation `1.138.0` | [1.138](https://code.visualstudio.com/updates/v1_138) | Editor updater |

GitHub, Replit, Notion, and AI chat/editor services are hosted authoring or collaboration services, with no deployable service version selected by SHOAL. File Explorer belongs to Windows. HTTP, TCP/IP, DNS, Wi-Fi, Ethernet, WebSockets, and PWA behavior are protocols/platform capabilities, not separately pinned packages. GPU acceleration, Metal/CUDA, drivers, and container transitive libraries belong to selected hardware and upstream distributions; their versions require an actual reef inspection.

## Models and optional research references

The guide selects [`llama3.1:8b`](https://ollama.com/library/llama3.1/tags), [`gemma3:12b`](https://ollama.com/library/gemma3/tags), and [`mistral-small3.1:24b`](https://ollama.com/library/mistral-small3.1/tags). These tags are available upstream, but no content digests are recorded locally. Builds also discuss other Llama/Gemma sizes and Phi-4. Research mentions Phi-3, Qwen, `qwen3`, `qwen3-coder`, and `llama.cpp`.

There is no single semver-style latest stable across model families, sizes, quantizations, and licenses. A newer family is not a drop-in patch. Record the selected tag/digest and compare memory use and outputs on representative tasks before accepting a replacement. Do not automatically rewrite historical research or substitute models.

Nginx, Apache `htpasswd`, Synology Container Manager, Unraid, and cloud APIs such as OpenAI/Claude occur as optional research examples or comparisons. They have no installed/pinned dependency here. They become upgrade targets if an actual deployment adopts them. Plex and Windows Home Server are analogies.

## Named technologies not implemented here

| Technology | In-place version | Stable release checked for completeness |
|---|---|---|
| TypeScript | No executable source or installed package | [7.0.2](https://registry.npmjs.org/typescript/latest) |
| Vite | No application/configuration/dependency; contributor skill prose only | [8.3.0](https://registry.npmjs.org/vite/latest) |
| Tailwind CSS | No stylesheet pipeline/dependency; contributor guidance only | [4.3.3](https://registry.npmjs.org/tailwindcss/latest) |
| React | No application/dependency; best-practice guidance only | [19.3.0](https://registry.npmjs.org/react/latest) |
| Docker Compose | No deployment file; original inventory listed it for comparison | [5.5.1](https://github.com/docker/compose/releases/tag/v5.5.1) |

Installing these tools would add technologies, not update this solution. Do not infer SHOAL's stack from reusable skill examples or Open WebUI's internal implementation.

## Findings and next action

| Claim | Evidence tier | Consequence / next check |
|---|---|---|
| Open WebUI examples lag stable | Confirmed by pins and GitHub/PyPI | Assess 0.10.2 to 0.11.3 migration; test both install paths |
| Contributor code uses Python and JavaScript | Confirmed by file/import/manifest audit | Maintain contributor runtimes; correct project guide |
| Workstation Python is a release candidate | Confirmed by version command | Use stable contributor Python; not this interpreter for Open WebUI |
| Renovate successfully runs here | Unknown: config exists; GitHub issue/PR query returned none | Verify App access and first extraction/run |
| Live reef is current/compatible | Unknown: no runtime/upgrade test | Capture private versions and run acceptance checks |
| Replit matches GitHub | Unknown: connector requires reauthentication | Authenticate and inspect its repository/runtime |

**Next action:** activate and verify the [update plan](technology-update-plan.md). Maintained references and host upgrades need separate acceptance evidence.
