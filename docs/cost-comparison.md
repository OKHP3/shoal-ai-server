# Cost Comparison: SHOAL vs. Cloud Subscriptions

## The Honest Math

| Setup | Monthly | Year 1 | Year 3 |
|-------|---------|--------|--------|
| 6 x ChatGPT Plus ($20/user) | $120 | $1,440 | $4,320 |
| 6 x ChatGPT Go ($8/user) | $48 | $576 | $1,728 |
| Budget Reef (refurb OptiPlex) | $0* | ~$325 | ~$397 |
| Sweet Spot Reef (Mac Mini M4) | $0* | ~$817 | ~$853 |
| Power Reef (Mac Mini M4 Pro) | $0* | ~$1,417 | ~$1,453 |

*Electricity only: approximately $15-25/year depending on hardware and usage.

## Breakeven Points

| Reef Build | vs. 6x ChatGPT Plus | vs. 6x ChatGPT Go |
|------------|---------------------|---------------------|
| Budget ($300) | ~2.5 months | ~6 months |
| Sweet Spot ($799) | ~7 months | ~17 months |
| Power ($1,399) | ~12 months | ~29 months |

## The Caveat

ChatGPT Plus is a flat fee. You get effectively unlimited chat for $20/month. If your team uses AI casually (a few chats a day, no heavy generation), the per-token math does not apply and the "savings" are really "cost replacement" rather than dramatic reduction.

The local advantage is decisive when:
- Your team burns through API tokens (not flat-fee plans)
- You need data sovereignty (the value of "data never leaves" is hard to price but real)
- You want predictable, fixed costs with no per-seat scaling
- You need AI access during internet outages
- You want to avoid vendor lock-in (models are interchangeable on Ollama)

## What You Give Up

Be honest about the tradeoffs:

| Cloud AI | SHOAL |
|----------|-------|
| GPT-4o / Claude Opus quality | Smaller models (8B-24B), lower quality on complex reasoning |
| Zero hardware maintenance | You maintain the reef (updates, storage, troubleshooting) |
| Instant model upgrades | You pull new models manually |
| Scales to any team size | Practical limit of 2-10 users per reef |
| Works everywhere with internet | Works on your LAN (plus Tailscale for remote) |

The cloud is better AI. SHOAL is private, cheaper, and always-on AI. Different tools for different jobs. And when you need the big ocean? You are just a few paddles out.

---
*Part of [SHOAL: Shared Home/Office AI, Locally](../README.md)*
