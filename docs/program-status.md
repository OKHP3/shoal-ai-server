# SHOAL Program Status

A living tracker across the three repos that make up this household's SHOAL effort, so a new thread can pick up current state without re-deriving it. This page states readiness and blockers; it deliberately keeps machine-specific detail (IPs, exact terminal output, container names) out, per this repo's own documentation-only scope — those live in the other two repos, linked below.

**Last updated: 2026-09-20** (GUI provider-add attempt on the Mac added same day).

## The three repos

| Repo | Role | Readiness |
|---|---|---|
| [mac-studio-local-ai-workbench](https://github.com/OKHP3/mac-studio-local-ai-workbench) | The reef: compute infrastructure on the Mac Studio | High for core infra, degraded on the agent layer (see below) |
| [infusing-a-soul](https://github.com/OKHP3/infusing-a-soul) | A fish: Windows OpenClaw persona deployment (Glee-fully on GJS-LAPTOP) | Low — foundational install done, agent layer unconfigured |
| shoal-ai-server (this repo) | The documented vision and pattern | Reference-complete; real-world adoption not yet verified |

## Where things actually stand

**Core reef infrastructure (LM Studio, Open WebUI, Ollama, Qdrant, SearXNG): fixed and LAN-reachable.** As of 2026-09-12/13, all five were found bound to loopback-only and corrected; live off-host verification confirmed each one, including that Ollama's models are visible over the LAN, not just locally. Full detail and the fix history live in `mac-studio-local-ai-workbench`'s dated docs and status file. This was the original ask that started this program and it is done.

**The Mac's own OpenClaw agent layer broke independently, after that fix.** As of 2026-09-19/20, OpenClaw Control on the Mac Studio shows a failed auto-update (reason: a global install swap failing with a non-zero exit code, package rolled back) and now reports its configured model as unavailable — the same class of problem Windows has had the whole time, but new on the Mac side and unrelated to the LAN-exposure work. This is not yet fixed. The Mac's own documented recovery path for a broken Ask OpenClaw is `openclaw triage` from a real terminal, per the in-app diagnostic panel. Not yet attempted from this program.

**Windows (Glee-fully / GJS-LAPTOP): the persona is installed but has no model configured at all.** The native Companion app is installed, paired to its own local gateway, and startup-persistent. But `agents.defaults` has no model key and no provider is registered anywhere — a clean unconfigured slate, not a broken reference to repair. A step-by-step CLI playbook for wiring in LM Studio as a provider is now documented in `infusing-a-soul`. Not yet run.

**Attempted adding LM Studio as a provider on the Mac's own OpenClaw Control (2026-09-20): blocked by the GUI itself, not just the broken update.** The Models settings page's "Add provider" quick-add form only offers a closed list of named cloud providers (Anthropic, Google, Huggingface, Litellm, Nvidia, Ollama Cloud, OpenAI, Opencode Go, OpenRouter, Together, Xai) with a provider + API-key field pair -- no base-URL override for any of them, including OpenAI. There is no way to point that form at a local server like LM Studio's `http://10.10.1.201:1234/v1`. Selecting "OpenAI" and saving a key there would configure a connection to the real OpenAI cloud API, not LM Studio -- this was not done. This confirms the CLI path (`openclaw config set models.providers.lmstudio.type openai` / `.baseUrl` / `.apiKey`, same pattern as the Windows playbook) is the only way to add LM Studio as a provider on either machine; the GUI's quick-add flow doesn't support it on the Mac. On the Mac specifically this is gated behind fixing the broken update first (blocker #1 below) since the CLI needs a working install to run reliably.

**The Mac's own OpenClaw Gateway (the piece that would let Windows, iPhone, and iPad pair directly to one shared gateway) is still loopback-only.** No GUI setting exposes its bind address; a locate-and-fix playbook is documented in all three repos (the generic pattern here, the household-specific version in the other two). Zero external devices have paired to it. Not yet attempted.

**Remote access (Tailscale) is not installed anywhere in this stack.** The core SHOAL documentation recommends it for reaching the reef from outside the house; nothing has been done toward it yet. Lowest priority — nothing upstream of it works yet either.

## What "done" looks like

The vision this program is chasing: Windows, iPhone, and iPad all reach AI models running on the Mac Studio, without cloud dependency or per-seat subscriptions. Two independent paths get there, and neither is finished:

- **Direct provider path** (faster, narrower): each client's own AI tool (OpenClaw on Windows, eventually something on iPhone/iPad) is configured with the Mac's services as model providers. Blocked today by Windows having no model configured and the Mac's own OpenClaw being freshly broken.
- **Shared gateway path** (slower, matches the fuller vision): every client pairs to one Mac-hosted OpenClaw Gateway as a client. Blocked by the Gateway's loopback-only bind and zero device pairings.

Neither path requires the other to finish first, but the direct provider path is closer and cheaper to unblock.

## Open blockers, ranked by leverage

1. **Fix the Mac's own broken OpenClaw agent.** This is upstream of almost everything else in this stack that uses OpenClaw locally, and it's new since the last pass. Try `openclaw triage` from a real Mac terminal first, per the in-app diagnostic guidance. This is also now confirmed as the blocker for adding LM Studio as a provider on the Mac's own OpenClaw (see finding above) -- the GUI can't do it either way, so a working CLI is required regardless.
2. **Configure a model provider on GJS-LAPTOP.** The playbook is written; someone with terminal access to that machine needs to run it. This is the fastest route to a working end-to-end demo (Windows using the Mac's models), independent of the Gateway.
3. **Open the Mac's OpenClaw Gateway to the LAN.** Needed for the fuller shared-gateway vision (and for iPhone/iPad, which have no other documented path in yet). Playbook written in all three repos.
4. **Pair at least one external device to the Gateway**, once #3 is done, to prove the shared-gateway path actually works end to end.
5. **Install Tailscale**, once something local actually works, for access from outside the house.

## Cross-references

- Mac-side fix history and status: `mac-studio-local-ai-workbench/docs/18-lan-exposure-fix-2026-09-12.md` and `mac-studio-setup/LOCAL_WORKBENCH_STATUS.md`
- Windows-side runbook and blockers: `infusing-a-soul/docs/asus-gateway-runbook.md`
- Gateway locate-and-fix pattern (generic version): [docs/openclaw-gateway-integration.md](openclaw-gateway-integration.md)

---
*Part of [SHOAL: Shared Home/Office AI, Locally](../README.md)*
