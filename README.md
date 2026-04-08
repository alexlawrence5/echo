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

## Requirements for compiling and training
| Component | Minimum                           | Recommended                                                     |
| --------- | --------------------------------- | --------------------------------------------------------------- |
| **CPU**   | Any modern CPU                    | Intel i5 / AMD Ryzen 5                                          |
| **RAM**   | 8 GB                              | 16+ GB                                                          |
| **GPU**   | Optional (training is very small) | NVIDIA GPU with 4–6 GB VRAM (e.g., GTX 1650) speeds up training |
| **Disk**  | 1–2 GB free                       | 5 GB (for code, logs, datasets)                                 |
| **OS**    | Windows                           | GNU/Linux or WSL2                                               |

(WARNING! you can't compile it on Android or iOS. It requires only PC OS.)
