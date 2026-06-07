# Sweet Spot Reef: $799 Mac Mini M4

The recommended build for most homes and small offices. Apple Silicon's unified memory architecture means the GPU and CPU share the same RAM pool, which is ideal for LLM inference. The Mac Mini M4 draws 12-15W at idle and about 30W under load, runs silently, and fits in a desk drawer.

## Reference Hardware

| Component | Spec | Price |
|-----------|------|-------|
| Machine | Mac Mini M4 (base, 16GB unified memory, 512GB SSD) | $799 |
| RAM | 16GB unified (shared CPU/GPU) | Included |
| Storage | 512GB SSD | Included |
| GPU | 10-core GPU (integrated, shared memory) | Included |
| Power | 12-15W idle, ~30W load | ~$18/year electricity |

**Total: $799 one-time + approximately $18/year electricity.**

Note: Apple raised the Mac Mini M4 base price from $599 to $799 on May 1, 2026, discontinuing the 256GB storage tier. Verify current pricing before purchase.

## What It Can Run

| Model | Parameters | Speed | Quality |
|-------|-----------|-------|---------|
| Llama 3.1 8B | 8B | ~30-40 tok/s | Good general-purpose |
| Gemma 3 12B | 12B | ~20-28 tok/s | Strong general-purpose |
| Phi-4 | 14B (Q4) | ~18-25 tok/s | Excellent reasoning |

16GB unified memory limits you to models under ~14B parameters at Q4 quantization. For larger models, see [Power Reef](power-reef.md).

## Best For

- Families of 2-6 members
- Small offices (real estate, law, design) with 3-5 users
- Anyone who wants fast, quiet, low-power inference
- The "set it and forget it" deployment (macOS handles updates, sleep/wake works correctly, Ollama auto-starts)

## Why Apple Silicon

Memory bandwidth is the bottleneck for LLM inference, not raw compute. Apple Silicon's unified memory delivers ~100 GB/s bandwidth on the M4, compared to ~25-40 GB/s on typical DDR4 desktop PCs. That is why a $799 Mac Mini outperforms a $1,200 x86 desktop at token generation: the memory can feed the model faster.

## Power and Noise

The Mac Mini M4 draws roughly 12-15W at idle. At US average electricity rates (~$0.17/kWh), running it 24/7 costs about $15-20/year. It is passively cooled under light load (silent) and barely audible under full inference. It fits under a monitor, in a closet, or behind a TV.

## Upgrade Path

If 16GB becomes limiting, the [Power Reef](power-reef.md) (Mac Mini M4 Pro 24GB or Mac Studio) is the natural next step. The base Mac Mini does not support RAM upgrades after purchase.

---
*Part of [SHOAL: Shared Home/Office AI, Locally](../README.md)*
