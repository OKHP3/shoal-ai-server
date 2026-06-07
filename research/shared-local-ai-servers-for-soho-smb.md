# Shared Local AI Servers for Homes, Hobbyists, and Small Offices: 2026 State-of-the-Art Research Report

## TL;DR

- **A shared local AI server for 2–6 light users is now genuinely practical at the $800–$2,000 hardware tier**, with three credible reference builds: a base Mac Mini M4 (now $799 starting price, 16GB RAM/512GB, after Apple discontinued the $599/256GB SKU on May 1, 2026), a refurbished Dell OptiPlex 7060/7070 micro or HP EliteDesk 800 G5 mini with 32GB RAM (~$180–$450 on eBay), or a Synology Plus-series NAS already in the closet (e.g., DS923+ with 16–32GB RAM at ~$700 all-in). The software stack has converged on **Ollama + Open WebUI**, accessed from any browser-capable client (Windows, Mac, Chromebook, iPad, Android, phone).
- **The historical analogy that resonates is the home media server (Plex/Jellyfin), not Windows Home Server.** Plex — which began in December 2007 when developer Elan Feingold ported XBMC to Mac OS X, formally forked from XBMC in May 2008, and incorporated as Plex Inc. on December 3, 2009 — succeeded because every device already had a thin client (a browser or app) and the "one box, many screens" pattern was intuitive; Windows Home Server and Windows SBS failed primarily because Microsoft mispriced them, gutted features, and chased cloud revenue. Local AI is following the Plex curve, not the WHS curve.
- **The cost case is real but narrower than the marketing suggests.** Six ChatGPT Plus seats = $1,440/year, which breaks even against a $800–$1,500 local rig in 7–13 months and saves 70–85% over three years for teams with moderate use — but if your team only uses flat-fee Plus casually, the breakeven argument collapses. The strongest case for local is **data sovereignty** (legal privilege, real estate client files, medical notes, family conversations) plus **fixed predictable cost**, not raw price-per-token.

---

## Key Findings

1. **The pattern has no settled name yet.** "Home AI server," "personal AI server," "local AI server," "home lab AI," and "private ChatGPT" all circulate; "home AI server" appears the most search-indexed (ai-home-server.com, ToolHalla, Compute Market all use it). For a general-audience article, **"home AI server"** (homes/hobbyists) and **"office AI server"** or **"small-office AI box"** (SMB) read cleanly. The Plex/NAS analogy is the most accessible: *"one box on the network that every device talks to."*

2. **Hardware floor is roughly $135 (Raspberry Pi 5 8GB) for one user on tiny models, $800–$1,000 for 2–6 light users (Mac Mini M4 base or refurb SFF + 32GB RAM), and $1,500–$3,500 for a fast multi-user box (Mac Mini M4 Pro 24GB, used dual-RTX-3090 build, or Mac Studio).** Apple Silicon's unified memory is the dominant value pick for shared inference because memory bandwidth — not raw compute — is the bottleneck.

3. **Ollama + Open WebUI is the de facto stack.** Ollama handles model serving (sets `OLLAMA_HOST=0.0.0.0` for LAN access on port 11434, supports concurrency via `OLLAMA_NUM_PARALLEL`, default queue 512 via `OLLAMA_MAX_QUEUE`). Open WebUI provides multi-user accounts, admin/user/pending roles, group-based access control, per-model visibility, and RAG over uploaded documents.

4. **Real concurrency is limited but adequate for SOHO/SMB.** Ollama serializes requests by default; with `OLLAMA_NUM_PARALLEL=4` and adequate RAM/VRAM you get 4 concurrent inference slots per loaded model, beyond which requests queue FIFO. Practical rule: a single Mac Mini M4 or 32GB SFF can comfortably serve 2–6 *light* users (chat-style, not simultaneous heavy generation). Above ~10 concurrent active sessions, you want vLLM-class serving, not Ollama.

5. **Thin clients work today on essentially every consumer device.** Anything with a modern browser can hit Open WebUI: Chromebooks, iPads, Android phones, Windows laptops, old MacBooks. No client install required. This is the killer feature that the Windows Home Server era never had.

6. **The dominant motivation in documented SMB deployments is data sovereignty, not cost.** Law firms cite ABA Formal Opinion 512 (released July 29, 2024 by the ABA Standing Committee on Ethics and Professional Responsibility on confidentiality of client data under GenAI), medical practices cite HIPAA/PHI handling, real estate cite client financial data, and families cite "everyone gets an AI but conversations stay home." The cost-savings argument is secondary, and it falls apart for users who would otherwise pay $20/month flat for ChatGPT Plus rather than burn API tokens.

7. **The Windows Home Server / Windows SBS lesson is directly relevant — and instructive.** Both products solved real SOHO/SMB problems (centralized backup, file sharing, integrated Exchange/SharePoint at one price), had loyal channel-partner ecosystems, and were killed by Microsoft to push customers to cloud subscriptions (Office 365). The current vacuum — no Apple/Microsoft/Synology "buy this box, plug it in, your family/office has private AI" product — looks exactly like the gap WHS once filled.

8. **The biggest content gap is end-to-end, beginner-friendly small-office/family guides.** Reddit (r/LocalLLaMA, r/selfhosted, r/homelab), GitHub issues, marius­hosting, and a sprawl of Medium posts cover individual pieces (Ollama on Synology, Open WebUI multi-user, Tailscale remote access), but **almost no one publishes a single "real estate office of 6 — buy this, install this, your AI is shared and private by Friday" walkthrough.** This is the OverKill Hill P³ content opportunity.

---

## Details

### 1. Existing implementations and documented setups

The clearest reference architecture in current use is **one machine running Ollama on `OLLAMA_HOST=0.0.0.0:11434`, plus Open WebUI as a frontend, optionally with Tailscale for remote access**. Documented variants include:

- **Mac Mini / Mac Studio as always-on server.** Modelfit (modelfit.io/blog/best-llm-mac-mini-m4-16gb) explicitly endorses the desktop-form-factor advantage: *"With Ollama's built-in API server, the Mac Mini can serve requests to any device on your network… The Mini sits under your monitor, draws about 12–15W at idle, and answers requests from your iPad, phone, or other computers — all without sending data to any cloud. Power cost for 24/7 operation: roughly $15–$20 per year at average US electricity rates."* A first-person practitioner writeup on Medium (Bo Liu) describes a Mac Studio M4 Max with 126GB unified memory serving qwen3, qwen3-coder, and gpt-oss models over LAN with CORS enabled.

- **Synology NAS as quietly-hosted AI.** Marius Hosting, Local AI Master (localaimaster.com/blog/ai-synology-nas-setup), and Tim Smith's blog all document running Ollama in Container Manager on Synology Plus-series NAS units. Local AI Master's guidance: *"A Synology Plus-series NAS is a $600–$1500 box that already lives in your home… Adding Ollama via Container Manager turns it into a private LAN AI endpoint for the cost of a $60 RAM upgrade and ten minutes of setup. You get GPT-3.5-class quality from Mistral 7B at 7 tokens per second."* DS923+ at $600 with a 16GB RAM kit is called out as the sweet spot.

- **Windows desktop with NVIDIA GPU as shared box.** blackMORE Ops (blackmoreops.com) documents the Windows-side OLLAMA_HOST/OLLAMA_ORIGINS env-var dance plus firewall rule for `New-NetFirewallRule -DisplayName "Ollama LAN Access" -LocalPort 11434`. This is the dominant gamer/enthusiast pattern: re-use the gaming PC's RTX 3090/4090 as a household inference server.

- **Raspberry Pi 5 (8GB) for very small models.** Documented in the Raspberry Pi Foundation's own projects portal, the Stratosphere Labs benchmark, ItsFOSS, and Kunal Ganglani's blog. Gemma 3 1B and Phi-3 Mini 3.8B are usable; 7B+ is a stretch. Realistic price: ~$135 with case/PSU/SD.

- **Practitioner case studies (low-confidence but documented).** Dre Dyson's e-discovery guide claims firms processing 10,000+ documents/day on local Ollama infrastructure within a week of setup using Llama-2-7B-Chat-GGUF Q5_K_M. A vendor blog (CreateAIAgent) cites — without independent verification — a Munich law firm running Llama 3-70B-Q4 inside a VPN and "saving €600/month." **Caveat:** publicly documented, named-firm small-business deployments remain rare; most "case studies" are first-person tinkerer accounts or vendor anecdotes.

### 2. Hardware floor and realistic price points

| Tier | Hardware | Approx. price | Concurrent light users | Notes |
|---|---|---|---|---|
| **Floor** | Raspberry Pi 5 8GB | ~$135 | 1 (toy use) | Gemma 3 1B at ~18–22 tok/s, Phi-3 Mini 3.8B at ~1–2 tok/s. Privacy demo, not real productivity. |
| **Used SFF / mini-PC, CPU-only** | Dell OptiPlex 7060/7070 Micro, HP EliteDesk 800 G5 Mini, 32GB RAM | ~$180–$450 on eBay refurb; ~$780–$880 from Best Buy/Joy Systems for premium configs | 1–3 light users | Phi-3, Gemma 12B, Llama 3.1 8B at 6–10 tok/s CPU-only. Slow but workable for an office of 3–5 with patience. |
| **Apple Silicon (the sweet spot)** | Mac Mini M4 base (16GB/512GB) | $799 (raised from $599 on May 1, 2026 per MacRumors) | 2–4 light users | 8–13B models at Q4 at 20–35 tok/s; 12W idle / 30W under load; ~$15–$20/year electricity. Per Sebastian Raschka's own Substack note: *"I really like the Mac Mini. It's probably the best computer I've ever owned"* (referring specifically to the M4 Pro). |
| **Apple Silicon (recommended)** | Mac Mini M4 Pro 24GB | ~$1,399 | 4–8 light users | 8B–22B models at 20–30 tok/s, 30–40W under load. The realistic SMB pick. |
| **High-end value** | Used 2× RTX 3090 build OR Mac Studio M4 Max 64–128GB | $1,600–$3,500 | 6–10+ active users | 70B models at Q5. Mac Studio is silent, GPU rig is faster on cold prompts but draws 400–500W. |

The mini-PC tier deserves emphasis: **a refurbished Dell OptiPlex 7060 Micro with i7-8700 and 32GB RAM can be acquired for roughly $235–$448 on eBay** (eBay Refurbished/discountcomputerdepot inventory), and an HP EliteDesk 800 G5 Mini i5-9500T with up to 32GB lists in roughly the same band. This is genuinely under $500 for a small-office shared inference box that can run Phi-4, Gemma 3 12B, and Llama 3.1 8B on CPU. Speeds will be 6–12 tok/s — adequate for chat-style use in an office of 3–5, painful for code generation or long synthesis tasks.

### 3. Multi-user access patterns

**Ollama concurrency** (from the official FAQ): `OLLAMA_NUM_PARALLEL` controls parallel requests per loaded model (default auto-selects 4 or 1 based on memory); `OLLAMA_MAX_LOADED_MODELS` controls how many distinct models sit in VRAM/RAM (default 3 or 3×GPU); `OLLAMA_MAX_QUEUE` defaults to 512 FIFO. Per-parallel-slot, the KV cache grows roughly linearly with context length — so 4 parallel users × 8K context noticeably eats RAM/VRAM. Beyond ~10 truly simultaneous heavy users, the community consensus (Markaicode, Local AI Master) is to graduate to vLLM with continuous batching.

**Open WebUI multi-user support is mature.** From the official docs: three roles (`pending`, `user`, `admin`); first signup becomes admin; subsequent sign-ups default to pending until admin approval. RBAC supports user groups, per-model visibility (Public/Private/Restricted), per-knowledge-base access, and additive (grant-only) permissions across five permission categories: Workspace, Sharing, Chat, Features, Settings. From the docs: *"You can restrict access to specific objects (like a proprietary Model or sensitive Knowledge Base) using Groups or individual user grants… Set its visibility to Private or Restricted. Grant Access: Select the specific Groups or individual users that should have 'Read' or 'Write' access."* SSO/LDAP/OAuth are supported for organizations that need it.

**Content filtering for kids is partial but workable.** Open WebUI does not ship dedicated parental controls, but the "curated model" pattern documented in the Models docs is the right primitive: admin defines a child-safe model (specific system prompt, restricted tools, no web search), sets it Public to the "kids" group, and keeps the unrestricted base model Private to adults. Permissions are additive (*"To restrict a feature, it must be disabled in the Global Defaults and disabled in all groups the user belongs to"*) — so the parent locks down Tools Access (which the docs explicitly warn is *"root-equivalent… equivalent to giving them shell access to your server"*), web search, and image upload at the global level, then grants only the safe-mode model to the child user. Inlet/Outlet filter functions can also do real-time prompt and response moderation if needed. For full-LAN content filtering across other AI services (ChatGPT, Claude, Gemini), Aegis (parentalsafety.ai) and Canopy do device/browser-level filtering, but those are orthogonal products.

### 4. Client device requirements (the "thin client" pattern)

Because Open WebUI is a web app, **any device with a modern browser is a sufficient client**:

- **Chromebooks** — Yes, via browser; no Linux/Crostini required if all you need is the web UI. (Crostini only matters if a user wants to run Ollama itself on the Chromebook, which is rare.)
- **iPads** — Yes, via Safari to the Open WebUI URL. No app needed. PWA install works.
- **Android phones / iPhones** — Yes, mobile browser, or native Open WebUI mobile clients.
- **Old Windows laptops / MacBooks** — Yes; the local browser is the entire footprint.
- **Smart TVs and consoles** — Generally not usable interactively, but Plex-style remote-control patterns are emerging.

Tailscale (or any WireGuard-based mesh VPN) is the recommended way to extend access outside the LAN without port-forwarding or exposing Ollama (which has no authentication) to the public internet. This is the same "Plex Pass relay server" pattern, just with a privacy-focused tunnel.

### 5. Privacy and data sovereignty — the actual driver

The documented motivations cluster cleanly:

- **Legal practice.** ABA Formal Opinion 512, released July 29, 2024 by the ABA Standing Committee on Ethics and Professional Responsibility, elaborates duty of confidentiality under GenAI; multiple state bars (California, New York City) have echoed this. The ABA's own guidance on confidentiality risks is the primary citation: *"AI hallucinations, privacy issues… leak of confidential information… are just a few to name. However, the AI governance strategies of many US law firms either are still in a nascent stage of conceptualization or early implementation."* Lawyers running prompts about client matters through ChatGPT is a confidentiality issue that local AI sidesteps entirely.
- **Healthcare.** HIPAA/PHI handling drives HIPAA-compliant AI products (BastionGPT) and motivates local hosting for medical practices that don't want to negotiate BAAs with cloud AI vendors.
- **Real estate.** Client financial information, MLS data, contract negotiation drafts — all the same confidentiality pattern as law firms, with fewer regulatory teeth but the same practical concern.
- **Families.** The documented motivations are softer: keeping kids' conversations private from ad networks, not training cloud models on family chat, having an AI that works during internet outages, fixed cost vs. multiple per-seat subscriptions.

The strongest single quote from current writing is Tailscale's own blog framing: *"There's a one-time, upfront hardware cost, but after that, there are no monthly fees, and zero worries about where your prompts and data are going."*

### 6. Historical pattern comparisons

**Windows Home Server (2007–2013).** Released by Microsoft at CES 2007, based on Windows Server 2003, sold initially only through OEMs (HP MediaSmart Server etc.). Killed in July 2012; final version (WHS 2011) was based on Windows Server 2008 R2 and lost the beloved Drive Extender storage-pooling feature, alienating the enthusiast base. Mainstream support ended Q2 2016; Microsoft folded its features into Windows Server 2012 Essentials at much higher price (~$425 vs. ~$50 for WHS). ServeTheHome's post-mortem identifies poor marketing/evangelism, the Drive Extender removal, and a flawed OEM-only distribution model. **Lesson for local AI:** a great consumer-server product can be killed by misaligned business strategy even when users love it.

**Windows Small Business Server (2000–2013).** Bundled Exchange, SharePoint, ISA/SQL, and Windows Server at a steeply discounted SMB price. Discontinued by Microsoft in July 2012; final SKU (SBS 2011) sold through Dec 31, 2013. Replaced by Windows Server 2012 Essentials — which crucially **did not include on-premise Exchange**, forcing customers to Office 365 hosted Exchange. The Redmond Channel Partner coverage is brutally clear: Microsoft killed SBS specifically to push customers to cloud subscriptions, against significant partner outrage. **Lesson for local AI:** the small-office "everything in one box" category is a real, durable need that vendors keep abandoning to chase recurring cloud revenue. There is a structural opening here that no major vendor is filling.

**Plex / Jellyfin / Emby home media servers (2007–present).** Plex began as a freeware hobby project in December 2007 when developer Elan Feingold ported XBMC (now Kodi) to Mac OS X; the project formally forked from XBMC in May 2008, was renamed Plex in July 2008, and Plex Inc. was incorporated December 3, 2009. It succeeded by making the "one server, every screen" model trivially easy: clean library scanning, polished native apps on every TV/phone/console, automatic remote access via Plex's relay servers. Jellyfin (FOSS fork of Emby, started December 8, 2018 by Andrew Rabert and Joshua Boniface in response to Emby's decision to take its 4.x release closed-source) has caught up enough that XDA Developers, How-To Geek, and the home-lab community now routinely recommend it for the privacy-conscious. **Why these worked where WHS failed:** thin clients existed everywhere, the value prop ("replace 4 streaming subscriptions") was visceral, and remote access was solved in software not network configuration. **The local AI parallel is exact:** browsers are the thin clients, the value prop is "replace 6 ChatGPT subscriptions and keep your data," and Tailscale solves remote access.

**LAN parties and game servers.** Mostly a cultural touchpoint now, but the social model of "bringing devices to a shared compute resource" still maps. The current equivalent is "kids on Chromebooks, mom on her iPad, dad on his Mac, all hitting the same little box in the closet."

**NAS appliances (Synology, QNAP, UGREEN).** These already sit in millions of closets running Docker. Synology, UGREEN, and the community-driven NAS Compares already publish guides for Ollama on DSM 7.2 Container Manager. The NAS form factor is arguably the *correct* shipping vehicle for a consumer "home AI server" — closet-friendly, quiet, redundant storage, already a known purchase category. Whether Synology will lean into this (the way they leaned into Plex and Photos) is the open question.

### 7. Naming the pattern

Currently in use, ranked by visibility:
- **"Home AI server"** — most common; multiple commercial sites use it as a product term (ai-home-server.com, Compute Market, ToolHalla). Most accessible to general readers.
- **"Personal AI server"** — Lenovo's term in its glossary, used by hobbyists.
- **"Local AI server"** — favored by technical writers; emphasizes the privacy angle.
- **"Private AI"** / **"Private ChatGPT"** — favored when targeting business/legal/medical buyers; emphasizes confidentiality.
- **"AI home lab" / "homelab AI"** — used by the r/homelab / r/selfhosted community.
- **"AI appliance"** — used by emerging vendors (ClawBox, Zima) trying to sell a turn-key box.

**Recommended editorial frame for OverKill Hill P³:** lead with "home AI server" (for the residential audience) or "office AI server" / "private AI box" (for SMB). Use the **Plex/NAS analogy in the lede** — it's the only frame a non-technical reader instantly recognizes. The Windows Home Server / SBS analogy is the *strategic* frame for the article's argument (someone should be shipping this turn-key and isn't), not the consumer-explanation frame.

### 8. Gaps and opportunities

What is fragmented today, ranked by content opportunity:

1. **End-to-end small-office buying guides.** No mainstream publication has shipped a *"law firm of 6: buy this exact box, install this exact stack, here's the legal-confidentiality argument for your bar association"* walkthrough. The pieces exist (refurb hardware listings, Ollama LAN docs, Open WebUI multi-user docs, ABA Opinion 512), but nobody has stitched them into a decision-ready guide.
2. **Family-friendly setup guides with kids in mind.** The "curated model" pattern in Open WebUI is the right primitive but is buried in developer docs. No one has written *"how to give your 11-year-old an AI homework helper that can't help with anything else."*
3. **Honest cost comparisons.** The breakeven math gets sloppy fast — CraftRigs correctly observes: *"Here's the thing people get wrong: they calculate their API spend from ChatGPT Plus ($20/month) or Claude Pro ($20/month), which doesn't represent actual token throughput. The flat-fee products give you effectively unlimited messages — they're not a valid cost comparison for hardware ROI."* The real argument is **predictable cost + sovereignty + always-on**, not raw price per token.
4. **Turn-key product gap.** No Apple, Microsoft, Synology, or Dell ships "the home AI server appliance." Small vendors (ClawBox, ZimaSpace) are trying. This is a market white space that mirrors the post-WHS / post-SBS vacuum.
5. **Maintenance and updates story.** Almost no guides cover the year-2 problem: who updates Ollama, who patches the OS, what happens when Open WebUI ships a breaking change?

### 9. Cost comparison vs. cloud

The math, with caveats:

| Setup | Annual cost | Notes |
|---|---|---|
| 6 × ChatGPT Plus seats | **$1,440/year** | $20/mo × 6 × 12; the canonical baseline |
| 6 × ChatGPT Go seats | $576/year | $8/mo × 6 × 12 (Go went global January 15, 2026 at $8/month) |
| 6 × ChatGPT Business | $1,800–$2,160/year | $25–$30/user/mo, billed annually |
| Mac Mini M4 base shared | ~$820 one-time + ~$18 electricity | Breakeven vs. 6× Plus: ~7 months |
| Refurb OptiPlex 32GB | ~$300 one-time + ~$25 electricity | Breakeven vs. 6× Plus: ~3 months |
| Mac Mini M4 Pro 24GB | ~$1,399 + ~$25 electricity | Breakeven vs. 6× Plus: ~12 months |

**Documented worked examples:** InsiderLLM's breakeven analysis for a 5-person team paying ~$100/month for ChatGPT Plus: local hardware *"pays for itself in 2–4 months."* PracticalWebTools documents an 8-person agency that *"hit $847. For a team of eight people. In one month"* on its OpenAI bill — for teams in that range, a $1,500 local rig pays back in 6–8 weeks and saves 70–85% over three years. ML Journey's example: *"A team of 10 paying $25/month ($3,000/year) breaks even with a $3,000 hardware investment in one year — while gaining unlimited usage and avoiding ongoing costs."*

**Honest caveats** (from CraftRigs and others): ChatGPT Plus is flat-fee and effectively unlimited for chat use, so users who would otherwise just pay $20/month per seat for casual use may not save money — they trade subscription cost for hardware cost. The math is decisively in local's favor when you also account for API spend, data sovereignty value (impossible to monetize but real for regulated professions), and the asymmetric "we have one less recurring bill" factor.

**The right framing for the article:** local AI is not categorically cheaper, but it converts a recurring variable cost into a one-time fixed cost, removes data-leakage risk, and removes vendor lock-in. For families and small offices that match those preferences, the math just needs to be "good enough" — it doesn't need to be a slam dunk.

### 10. Specific tools and projects worth naming

- **Ollama** (ollama.com) — the inference engine; LAN access via `OLLAMA_HOST=0.0.0.0`. Built-in concurrent batching with `OLLAMA_NUM_PARALLEL`.
- **Open WebUI** (openwebui.com) — the multi-user web frontend; Docker install in one command, RBAC, groups, per-model access.
- **LM Studio** — GUI app; single-user oriented but useful for model evaluation.
- **LocalAI** (localai.io) — OpenAI-API-compatible drop-in replacement, supports many model families.
- **AnythingLLM** (Mintplex Labs) — chat + RAG + role-based access; polished for office use.
- **Text Generation WebUI (oobabooga)** — older, more developer-oriented.
- **vLLM / vllm-mlx** — production-grade serving with continuous batching; the right answer above ~10 concurrent users.
- **Tailscale** — secure remote access; the standard recommendation for letting users hit the AI server from outside the LAN.
- **Nginx + htpasswd** — the standard pattern when you need basic auth in front of Ollama.
- **Synology Container Manager** / **Unraid** — NAS-side container hosts; well-documented for Ollama.

---

## Recommendations

**For a general-audience OverKill Hill P³ article**, ship a three-part piece:

1. **"Why you might want a home AI server"** — lead with the Plex analogy, hit the privacy/cost/always-on trio, name-check law firms and families specifically, surface ABA Opinion 512 for the SMB audience. ~1,500 words.
2. **"The three reference builds"** — Raspberry Pi (curiosity), $300–$500 refurb mini-PC (small office on a budget), $799–$1,000 Mac Mini M4 (the recommended baseline), with one paragraph on the $1,400 Mac Mini M4 Pro upgrade path. Include a small office "you have 5 agents" and a family "you have 2 parents and 3 kids" decision matrix. ~2,000 words.
3. **"Setup walkthrough: Ollama + Open WebUI in one evening"** — installs in DSM Container Manager and on Mac, configure LAN, create users and groups, set up a kid-safe curated model, optional Tailscale. ~1,500 words.

**Editorial cautions to flag for fact-check before publishing** (these will go stale fast):
- Specific model names (Llama 3.1 8B, Gemma 3 12B, Phi-4, Qwen 3) — refresh quarterly.
- ChatGPT pricing tiers — drifted in 2025–2026 with Go ($8) and Business ($25) tiers; OpenAI raises and adjusts limits regularly.
- Hardware prices, especially Mac Mini (Apple raised the base from $599 to $799 on May 1, 2026) and refurb SFF listings.
- Ollama and Open WebUI version-specific behavior (the `OLLAMA_NUM_PARALLEL` auto-default changed; MLX backend in Ollama 0.19+).
- Synology DS923+/DS925+ availability and pricing.

**Thresholds that would change the recommendation:**
- If a major vendor (Apple, Synology, Microsoft, Dell) ships a true turn-key home AI appliance with first-class multi-user support, the DIY/refurb recommendation gets demoted to "if you want to save money."
- If Ollama gains true per-user auth and rate-limiting natively, the "stick nginx or Tailscale in front" recommendation gets simpler.
- If consumer GPUs above 24GB VRAM drop under $500 used, the GPU build tier shifts from $1,500 to ~$800.

---

## Caveats

- **Named-firm case studies are scarce.** Most "law firm using Ollama" or "real estate office running local AI" claims in current public writing are first-person practitioner blogs or vendor-promoted anecdotes. Use first-person language carefully and don't represent unsourced vendor anecdotes (e.g., the "Munich law firm" quote) as verified case studies.
- **Concurrency claims are squishy.** "2–6 light users" is a defensible rule of thumb but real performance depends on model size, context length, prompt complexity, and whether users hit the server simultaneously. Open WebUI itself notes: *"If two people send messages at the same time, Ollama queues the requests and processes them sequentially unless you have configured multiple GPU workers."*
- **Speculation flagged as such.** The argument that "no major vendor ships a turn-key home AI appliance" is correct as of mid-2026; multiple emerging vendors (ClawBox, ZimaSpace, others) are trying. The article should not predict who will win, only that the gap exists.
- **Apple Silicon performance comparisons** between MLX, llama.cpp, and Ollama are evolving rapidly (Ollama 0.19's MLX backend, vllm-mlx, M5 Neural Accelerators). Cite numbers with dates.
- **Privacy is not absolute.** A local AI server still has filesystem-level data; it just isn't sent to a third party. For genuine high-stakes confidentiality (e.g., classified data, M&A negotiations), full-disk encryption, network segmentation, and physical access control still matter.
- **The local AI category is moving fast.** Anything specific in the report — model names, tok/s figures, prices, version numbers — should be re-verified within 60 days before publication.