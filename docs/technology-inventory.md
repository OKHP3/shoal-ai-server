# SHOAL Technology Inventory

**Snapshot date:** 2026-07-20

This repository is a documentation and reference-build project. It does not contain TypeScript, JavaScript application source, Vite, Tailwind, a Python codebase, a package manifest, a Dockerfile, or a supported server runtime. The list below separates technologies actually used by the documented setup from technologies only mentioned as optional examples.

## Technologies used by the documented solution

| Technology | Role in SHOAL | Version in this repository | Latest stable checked | Update source |
|---|---|---|---|---|
| Ollama | Inference server on the reef | Not pinned. The install script retrieves the current release. | [v0.32.1](https://github.com/ollama/ollama/releases/tag/v0.32.1) | [Ollama releases](https://github.com/ollama/ollama/releases) |
| Open WebUI | Browser frontend, accounts, permissions, and RAG | Pinned to `v0.10.2` in `docs/reef-setup.md` | [v0.10.2](https://github.com/open-webui/open-webui/releases/tag/v0.10.2) | [Open WebUI releases](https://github.com/open-webui/open-webui/releases) |
| Docker | Recommended Open WebUI container runtime | Not pinned in the guide | [Docker Desktop 4.80.0](https://docs.docker.com/desktop/release-notes/) | [Docker Desktop release notes](https://docs.docker.com/desktop/release-notes/) |
| Docker Engine | Linux container runtime alternative | Not pinned in the guide | [v29.6.2](https://github.com/moby/moby/releases/tag/docker-v29.6.2) | [Moby releases and tags](https://github.com/moby/moby/releases) |
| Docker Compose | Not currently used by a repository file; `docker run` is documented instead | Not applicable | [v5.3.1](https://github.com/docker/compose/releases/tag/v5.3.1) | [Compose releases](https://github.com/docker/compose/releases) |
| Python | Optional runtime for the non-Docker Open WebUI path | Not pinned; package is pinned to `open-webui==0.10.2` | [3.14.6](https://www.python.org/downloads/release/python-3146/) | [Python downloads](https://www.python.org/downloads/) |
| pip | Package installer for the optional Python path | Not pinned | [26.1.2](https://pypi.org/project/pip/26.1.2/) | [pip on PyPI](https://pypi.org/project/pip/) |
| Tailscale | Optional remote-access mesh VPN | Not pinned | [v1.98.9](https://tailscale.com/changelog) | [Tailscale changelog](https://tailscale.com/changelog) |
| WireGuard | VPN protocol underneath Tailscale | Inherited by Tailscale; not installed or versioned directly | No independent SHOAL version | [Tailscale security](https://tailscale.com/security) |
| WSL2 | Windows path for running the Linux Ollama install | Version not pinned; `wsl --install` is used | Microsoft distributes WSL through Windows and the Microsoft Store, so there is no single repository version | [Microsoft WSL installation](https://learn.microsoft.com/en-us/windows/wsl/install) |
| macOS, Linux, Windows | Supported reef host operating systems | Not pinned | No single cross-platform version | [Reef setup prerequisites](reef-setup.md#prerequisites) |
| Bash, curl, PowerShell, systemd, launchd | Host tools and service managers used in examples | Not pinned | Host-distribution dependent | [Reef setup](reef-setup.md) |
| Modern web browser | Fish/client interface | Not pinned | Browser-vendor dependent | [Fish guide](fish-guide.md) |
| Markdown and Git | Repository documentation and version control | Markdown flavor and Git version are not pinned | No single repository runtime version | [Repository](https://github.com/OKHP3/shoal-ai-server) |

## Not present as implementation technologies

TypeScript, JavaScript application source, Node.js, npm, Vite, Tailwind CSS, React, Vue, Svelte, Python application source, and frontend build tooling were not found in the checkout. JavaScript is only relevant as a language used by external web interfaces, not as code maintained by this repository.

## Mentioned but not part of the supported stack

OpenClaw, Nginx, `htpasswd`, Synology Container Manager, Unraid, browser PWAs, OpenAI, Claude, and other cloud APIs appear as optional examples, comparisons, or future patterns. They have no in-place repository version and are not covered by the automated update configuration.

## Update policy

The repository now pins the Open WebUI image and Python package to a stable release. `.github/renovate.json5` tracks those declarations and opens pull requests when a newer stable release is available. Enable the Renovate GitHub App for this repository to activate the schedule. Ollama, Tailscale, Docker, operating systems, shells, and browsers are installed outside this repository, so their host-level update mechanisms remain responsible for upgrades.
