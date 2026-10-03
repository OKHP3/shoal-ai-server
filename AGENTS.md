# AGENTS.md

## Project identity

- **Project:** SHOAL, Shared Home/Office AI, Locally
- **Repository:** `shoal-ai-server`
- **Suite:** OverKill Hill P3
- **Repository type:** Documentation, research, and reference-build project
- **GitHub:** https://github.com/OKHP3/shoal-ai-server
- **Notion anchor:** https://app.notion.com/p/378812e0ced48179ac30d1af3d90fbd1
- **License:** MIT

## Purpose and status

**Confirmed:** This repository explains and stages a private, shared AI-server pattern for homes and small offices. The documented pattern is one local host, called the reef, running Ollama for inference and Open WebUI for browser-based multi-user access. Client devices, called fish, connect through a browser over the local network. Tailscale is the documented optional path for remote access.

**Confirmed:** The checkout contains Markdown documentation, hardware reference builds, research, empty staging directories, and contributor Agent Skills. The skills include Python and JavaScript helpers, seven private package manifests, and skill-specific tests. There is no SHOAL server implementation, root application/package manifest, container definition, deployment script, or project-wide automated test suite.

**Inferred mission:** Make local AI practical for households and small offices by documenting the hardware, setup, multi-user, privacy, cost, and remote-access decisions needed to operate one shared box.

**Inferred vision:** Provide a clear, approachable reference for a locally controlled AI appliance pattern that is as understandable as a home media server.

Treat the project as content and technical guidance work unless new implementation files are added and this guide is updated with evidence.

## Scope and boundaries

In scope:

- Hardware selection and reference builds for local inference.
- Ollama and Open WebUI setup guidance.
- Browser-based client access and multi-user configuration.
- Privacy, security, cost, and remote-access explanations.
- Research and future article drafts related to shared local AI servers.

Out of scope for the current repository:

- A maintained server runtime or production deployment.
- Claims of guaranteed privacy, performance, uptime, compliance, or cost savings.
- Legal, medical, or security advice. Link to authoritative sources and add appropriate caveats when writing about regulated use.
- Secrets, credentials, personal data, or machine-specific configuration.

## Repository structure

- `README.md`: project overview, SHOAL vocabulary, reference builds, software stack, and document map.
- `assets/brand/`: README/social illustration, project mark, favicons, and home-screen/pinned-tab icons. These are presentation assets, not an application or deployment.
- `docs/branding.md`: asset provenance, publication status, and a future hosted-page metadata template. Repository assets do not activate GitHub social previews or website metadata by themselves.
- `.agents/`: repository-local Agent Skills and prompts used to support project work.
- `.github/`: GitHub maintenance configuration. It does not define an SHOAL runtime.
- `.github/technology-versions.json`: upstream release review baselines consumed by Renovate, not installed versions or deployment targets.
- `docs/`: setup, client-device, multi-user, remote-access, cost, and privacy guidance.
- `builds/`: budget, sweet-spot, and power reference hardware builds.
- `research/`: dated research and source synthesis. Treat prices, model names, product behavior, and performance numbers as time-sensitive.
- `context/`: durable project and conversation context extracts. These are provenance-bearing context artifacts, not server implementation.
- `skills/`: publication mirrors for selected repository-local skills. The active source remains under `.agents/skills/`.
- `article/drafts/`: content staging area. It is currently empty.
- `configs/example-configs/`: reserved for sanitized examples. It is currently empty.
- `.agents/skills/`: repository-local agent skills and their supporting references. These have their own skill-specific instructions.
- `CLAUDE.md`: compatibility pointer to this file.

There are no nested project roots or nested agent guidance files in the current checkout.

## Documented architecture

The repository documents this reference flow:

1. Ollama runs on the reef and serves models locally.
2. Open WebUI provides accounts, chat history, model access, and the browser interface.
3. Fish devices reach Open WebUI over the LAN without a client application.
4. Tailscale may provide private remote reachability without exposing Ollama directly to the public internet.

This is documented architecture, not an implementation owned by this repository. Version-specific commands and product behavior must be checked against current upstream documentation before publication.

## Technology and environments

The documented external stack is:

- Ollama for model serving.
- Open WebUI for the multi-user web frontend.
- Docker as the recommended Open WebUI installation path in `docs/reef-setup.md`, with a Python alternative also documented.
- macOS, Linux, or Windows with WSL2 as possible reef environments.
- Tailscale as the documented remote-access option.

There is no server runtime, framework, dependency lockfile, or supported deployment target defined by this repository. Contributor skills use Python standard-library helpers and Node.js scripts/tests. Their nested manifests declare no external packages or shared engine pin. See `docs/technology-inventory.md` for dated evidence and `docs/technology-update-plan.md` for maintenance and activation checks.

## Validation and working commands

There is no project-wide build, test, lint, or deployment command. Individual skills provide their own helpers and tests. Validate Renovate changes with its configuration validator and inspect extraction of both Open WebUI pins and all release-ledger entries. A local check does not prove the hosted App is active. Before changing documentation:

- Confirm referenced local paths exist.
- Check Markdown links and code blocks manually.
- Treat commands in `docs/reef-setup.md` as user-facing examples, not repository scripts.
- Run `git diff --check` before handoff.
- Inspect the final diff and preserve unrelated user changes.

Do not claim that an Ollama or Open WebUI command was executed unless it was actually run in a suitable environment. The repository does not provide that environment.

## Content, security, and operational conventions

- Use the SHOAL vocabulary consistently: reef for the inference host, fish for clients, shoal for the local network, and ocean for cloud APIs.
- Preserve standalone punchy lines. Do not consolidate them into paragraphs.
- Do not use em dashes in generated content.
- Follow the OverKill Hill P3 ROY principle: explanation should earn its space.
- AutoCAD version is R10 when that unrelated brand rule is applicable.
- Label claims as confirmed, inferred, or unknown when evidence matters.
- Keep dates on research and call out information that will drift.
- Re-verify hardware prices, model names, software behavior, concurrency figures, subscription pricing, and legal or regulatory references before publishing.
- Do not present local hosting as absolute privacy. Recommend strong accounts, encrypted backups, restricted network exposure, patching, and physical access controls where relevant.
- Do not expose Ollama's unauthenticated API to the public internet. Keep examples scoped to a trusted LAN or an authenticated private network path.
- Never add credentials, tokens, private URLs, or personal machine paths to tracked files.
- Keep examples sanitized and portable. Avoid editing generated artifacts or external project files.

## Safe change procedure

1. Read `README.md`, the relevant document, and this guide before editing.
2. Check repository status and preserve existing changes.
3. Make the smallest documentation-only change that addresses the request.
4. Update stale claims instead of extending them with unsupported assumptions.
5. Re-read every changed file, verify links and referenced paths, run `git diff --check`, and inspect the diff.
6. Update this guide when the repository gains executable code, a supported runtime, deployment automation, or a new project boundary.

## Known gaps and open questions

- The repository has no implemented server runtime or project-wide automated validation; skill-specific tests are separate contributor tooling.
- Renovate configuration covers Open WebUI pins and upstream review baselines. Hosted App activation and successful scheduled execution must be verified separately.
- The supported production deployment model is undefined.
- Exact upstream versions, model recommendations, hardware prices, and performance figures require periodic refresh.
- Ownership and maintenance responsibilities are not documented in the repository.
- The README describes `article/` and `configs/` staging areas, but both are empty in the current checkout.

Do not turn these gaps into assumptions. Record verified decisions here when the project owner establishes them.

## Related projects

- [mac-studio-local-ai-workbench](https://github.com/OKHP3/mac-studio-local-ai-workbench): compute infrastructure context.
- [infusing-a-soul](https://github.com/OKHP3/infusing-a-soul): AI persona architecture context.

A live reef combining Ollama, Open WebUI, and an OpenClaw agent gateway is documented in those two repos. `docs/openclaw-gateway-integration.md` in this repo carries the generic version of the bind-address-discovery playbook they use; it is documentation-only and machine-agnostic per this repo's scope rules above, with the household-specific IPs, ports, and terminal output living in the other two repos instead.

Keep this file aligned with the repository as it changes. It is the canonical project guide; `CLAUDE.md` should remain a short compatibility pointer unless Claude-specific instructions are genuinely required.

## Imported Claude Cowork project instructions
