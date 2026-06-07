# Power Reef: $1,400+ Mac Mini M4 Pro or Mac Studio

For teams that need larger models, more concurrent users, or faster response times. This tier handles 24B+ parameter models at interactive speeds and can comfortably serve 4-10 active users.

## Reference Builds

### Mac Mini M4 Pro 24GB ($1,399)

| Component | Spec |
|-----------|------|
| Chip | Apple M4 Pro (12-core CPU, 16-core GPU) |
| RAM | 24GB unified memory |
| Storage | 512GB SSD |
| Power | ~25-40W under load |
| Annual electricity | ~$30-40 |

Runs 24B models at Q4 comfortably. Handles 4-6 concurrent light users.

### Mac Studio M4 Max 36GB (~$2,000)

| Component | Spec |
|-----------|------|
| Chip | Apple M4 Max (14-core CPU, 30-core GPU) |
| RAM | 36GB unified memory |
| Storage | 512GB SSD |
| Power | ~40-80W under load |
| Annual electricity | ~$50-70 |

Runs 27B models at Q5-Q6, or 24B models with room for multiple loaded models simultaneously.

### Mac Studio M4 Max 64-128GB (~$2,800-3,500)

The ceiling for consumer-grade local AI. 64GB runs 70B models at Q4. 128GB runs 70B at Q6 or multiple concurrent large models.

## What These Can Run

| Hardware | Model | Speed | Concurrent Users |
|----------|-------|-------|------------------|
| M4 Pro 24GB | Mistral Small 24B (Q4) | ~18-25 tok/s | 4-6 light |
| M4 Max 36GB | Gemma 3 27B (Q5) | ~20-30 tok/s | 6-8 light |
| M4 Max 64GB | Llama 3.1 70B (Q4) | ~12-18 tok/s | 6-10 active |

## Best For

- Small law firms processing client documents
- Design studios with 5-8 creatives
- Offices that need larger, more capable models
- Teams that will outgrow the 16GB Mac Mini quickly
- Power users who want 70B-class model quality locally

## Alternative: Used NVIDIA GPU Build

For teams comfortable with more noise, heat, and power draw:

| Component | Spec | Price |
|-----------|------|-------|
| Used RTX 3090 (24GB VRAM) | NVIDIA Ampere | ~$600-800 |
| Motherboard + CPU + RAM | Intel i5/i7 + 32GB DDR4 | ~$400-600 |
| PSU | 850W+ | ~$100 |

**Total: ~$1,100-1,500.** Faster than Apple Silicon on cold prompts. Draws 300-500W under load. Fan noise is significant.

---
*Part of [SHOAL: Shared Home/Office AI, Locally](../README.md)*
