# Echo - Tiny model
Echo is an tiny educational-purposed model based off its own WhiteRock architecture.


---

## Architecture: WhiteRock

| Component | Standard GPT-2 | WhiteRock |
|-----------|---------------|-----------|
| MLP Expansion | 4x | **2x** |
| Activation | GELU | **ReLU** |
| Position Encoding | Learned | **Fixed Sinusoidal** |
| Block Order | Pre-LayerNorm | **Post-LayerNorm** |

---

## Model Specs

| Spec | Value |
|------|-------|
| Parameters | **2.12M** |
| Layers | **4** |
| Attention Heads | **4** |
| Embedding Dimension | **256** |
| Context Window | **128** |
| Vocab Size | **76** |
