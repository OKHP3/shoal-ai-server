# SHOAL

**Shared Home/Office AI, Locally**

One box on the network. Every device talks to it. No subscriptions. No cloud. Your data stays yours.

> Don't swim with the big fish and risk getting eaten. Play it safe in the warm, clear, shallow waters you control. And when you need to go deep? You're just a few paddles out of the safe harbor to the big ocean.

## What Is a SHOAL?

A SHOAL is a private AI server for your home or small office. One machine runs the AI models (the **reef**). Every laptop, tablet, phone, and Chromebook on your network (the **fish**) talks to it through a browser. Nobody's conversations leave your building. Nobody pays a monthly subscription.

It is the same pattern that made Plex work for home media: one server, every screen. The difference is the server runs AI models instead of movie files, and the monthly cost is electricity instead of six streaming subscriptions.

## The Metaphor

| Term | Meaning |
|------|---------|
| **Reef** | The inference server. Runs Ollama + Open WebUI. Any machine with 16GB+ RAM. |
| **Fish** | Any client device. Laptop, tablet, phone, Chromebook. Just needs a browser. |
| **Shoal** | Your home or office network. The fish swim together. |
| **Ocean** | Cloud APIs (OpenAI, Claude, etc.). Available when you need to go deep. |

## Who Is This For?

- **Hobbyists** who want local AI without cloud dependency or monthly spend
- **Families** who want everyone to have an AI assistant with parental controls, conversations staying in the house
- **Small offices** (real estate, law, design, accounting) who need client data confidentiality and predictable cost
- **Anyone** who already has a Windows laptop and one other device gathering dust

## The Cost Case

| Setup | Year 1 | Year 3 |
|-------|--------|--------|
| 6 ChatGPT Plus seats | $1,440 | $4,320 |
| Mac Mini M4 (the reef) + electricity | $817 | $853 |
| Refurb Dell OptiPlex 32GB (budget reef) | $325 | $397 |

The hardware pays for itself in 3 to 12 months depending on the build. After that, it is electricity only.

But the real case is stronger than cost: your data never leaves your network. Your spend is predictable and fixed. Your AI works during internet outages. You own the hardware and the models.

## Reference Builds

| Build | Hardware | Price | Users | Guide |
|-------|----------|-------|-------|-------|
| Budget Reef | Refurb Dell OptiPlex / HP EliteDesk, 32GB RAM | $200-450 | 1-3 light | [builds/budget-reef.md](builds/budget-reef.md) |
| Sweet Spot Reef | Mac Mini M4 base (16GB/512GB) | $799 | 2-4 light | [builds/sweet-spot-reef.md](builds/sweet-spot-reef.md) |
| Power Reef | Mac Mini M4 Pro 24GB or Mac Studio | $1,399-3,500 | 4-10 active | [builds/power-reef.md](builds/power-reef.md) |

## Software Stack

The de facto stack is **Ollama** (model serving) + **Open WebUI** (multi-user web frontend). Both are free and open source.

- [Ollama](https://ollama.com) handles inference and serves models over the LAN
- [Open WebUI](https://openwebui.com) provides user accounts, role-based access, per-model permissions, and RAG

Every client device accesses the AI through a browser. No app installs. No client-side setup beyond typing a URL.

## Docs

| Document | What It Covers |
|----------|----------------|
| [docs/reef-setup.md](docs/reef-setup.md) | Setting up the inference server (Ollama + Open WebUI) |
| [docs/fish-guide.md](docs/fish-guide.md) | Connecting client devices (Windows, Mac, Chromebook, iPad, Android) |
| [docs/multi-user.md](docs/multi-user.md) | User accounts, roles, groups, kid-safe models |
| [docs/remote-access.md](docs/remote-access.md) | Accessing your SHOAL from outside the house (Tailscale) |
| [docs/cost-comparison.md](docs/cost-comparison.md) | SHOAL vs. cloud subscriptions: the honest math |
| [docs/privacy-case.md](docs/privacy-case.md) | Why local matters: law firms, medical, real estate, families |
| [docs/technology-inventory.md](docs/technology-inventory.md) | Technology inventory, version snapshot, and update policy |
| [docs/openclaw-gateway-integration.md](docs/openclaw-gateway-integration.md) | Extending a reef with an agent gateway (OpenClaw) beyond the core Ollama + Open WebUI stack |

## Repo Structure

```
shoal-ai-server/
├── README.md
├── LICENSE
├── .agents/                     # Repository-local Agent Skills and prompts
├── .github/                     # GitHub maintenance configuration
├── docs/                         # How to set up and run a SHOAL
│   ├── reef-setup.md             # Inference server install (Ollama + Open WebUI)
│   ├── fish-guide.md             # Client device connection guide (all platforms)
│   ├── multi-user.md             # Open WebUI roles, groups, kid-safe models
│   ├── remote-access.md          # Tailscale for out-of-house access
│   ├── cost-comparison.md        # SHOAL vs. cloud: the money math
│   └── privacy-case.md           # Data sovereignty for regulated professions
├── builds/                       # Reference hardware builds
│   ├── budget-reef.md            # $200-450 refurb SFF PC
│   ├── sweet-spot-reef.md        # $799 Mac Mini M4
│   └── power-reef.md             # $1,400+ Mac Mini M4 Pro / Mac Studio
├── configs/                      # Sanitized example configurations
│   └── example-configs/
├── research/                     # Source research (may go stale)
│   ├── 2026-06-research.md       # Initial landscape research
│   └── shared-local-ai-servers-for-soho-smb.md
├── context/                      # Durable project and conversation context
│   └── threads/
├── skills/                       # Publication mirrors for selected local skills
│   └── okhp3-skill-promotion/
└── article/                      # Content play staging
    └── drafts/
```

## Historical Parallel

Remember Plex? One box in the closet, every TV in the house plays your movies. No monthly fee after the hardware.

Remember Windows Home Server? Microsoft shipped a home server OS in 2007, killed it in 2012, and pushed everyone to cloud subscriptions.

SHOAL fills the gap that Microsoft abandoned. One box. Every screen. Your stuff stays yours.

## Project Context

SHOAL is part of the **OverKill Hill P3** ecosystem (Precision, Protocol, Promptcraft).

| Project | Concern |
|---------|---------|
| [Mac Studio Workbench](https://github.com/OKHP3/mac-studio-local-ai-workbench) | Compute infrastructure |
| [Infusing a Soul](https://github.com/OKHP3/infusing-a-soul) | AI persona architecture |
| **SHOAL** (this repo) | Shared server pattern |

## License

MIT. See [LICENSE](LICENSE).

Configuration guides and methodology are shared freely.
Hardware recommendations are current as of June 2026 and will drift.

Technology versions and update tracking are documented in [docs/technology-inventory.md](docs/technology-inventory.md). Enable the Renovate GitHub App to receive pull requests when pinned Open WebUI references have newer stable releases.

---

*Built by Jamie Hill | [OverKill Hill P3](https://overkillhill.com) | [SHOAL Project](https://overkillhill.com/projects/shoal/)*
