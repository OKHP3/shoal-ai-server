# Budget Reef: $200-450 Refurbished SFF PC

The cheapest way to stand up a SHOAL. A used small-form-factor office PC with maxed-out RAM can serve 1-3 light users on smaller models using CPU-only inference.

## Reference Hardware

| Component | Spec | Where to Find | Price Range |
|-----------|------|---------------|-------------|
| Machine | Dell OptiPlex 7060/7070 Micro or HP EliteDesk 800 G5 Mini | eBay Refurbished, Amazon Renewed | $180-450 |
| CPU | Intel i5-8500T / i7-8700 or newer | Included | -- |
| RAM | 32GB DDR4 (upgrade if needed) | Crucial, Amazon | $40-60 if upgrading |
| Storage | 256GB+ SSD (usually included) | -- | -- |
| GPU | None (CPU-only inference) | -- | -- |

**Total: approximately $200-450 all-in.**

## What It Can Run

| Model | Parameters | Speed (CPU) | Quality |
|-------|-----------|-------------|---------|
| Phi-4 | 14B | ~4-8 tok/s | Good for general chat, summarization |
| Gemma 3 12B | 12B | ~4-7 tok/s | Good for general chat, light analysis |
| Llama 3.1 8B | 8B | ~8-12 tok/s | Decent for chat, basic tasks |

Speeds are approximate. CPU-only inference on 32GB RAM with an i7-8700. Adequate for chat-style use in an office of 3-5 with patience. Not suitable for long document generation or code synthesis.

## Best For

- Small offices on a tight budget
- Proof-of-concept before investing in better hardware
- Families who want to try local AI before committing
- Anyone with a spare PC in a closet

## Limitations

- CPU-only inference is slow (4-12 tok/s vs. 20-40 tok/s on Apple Silicon)
- 32GB RAM caps you at 12-14B parameter models
- Concurrent users compete for the same CPU, so 2-3 simultaneous users will feel the slowdown
- Fan noise can be noticeable under sustained load

## Upgrade Path

If the budget reef proves the concept, the natural upgrade is the [Sweet Spot Reef](sweet-spot-reef.md) (Mac Mini M4). Keep the OptiPlex as a backup or secondary node.

---
*Part of [SHOAL: Shared Home/Office AI, Locally](../README.md)*
