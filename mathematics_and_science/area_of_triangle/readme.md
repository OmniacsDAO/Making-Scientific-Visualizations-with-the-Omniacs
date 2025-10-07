# Understanding Triangle Area 🔺

> **Manim animation that proves (and practises) “Area = ½ × Base × Height.”**  
> Walks from definition ➜ rectangle-halving proof ➜ numeric 6 × 4 example ➜ recap card.

<img width="1751" height="929" alt="image" src="https://github.com/user-attachments/assets/8c910b97-b5e3-43e1-80e1-8610b2c2468d" />

Watch [here]().
---

## Table of Contents
1. [Demo](#demo) • 2. [Features](#features) • 3. [Quick start](#quick-start) • 4. [Scene index](#scene-index)  
5. [Customization](#customization) • 6. [Requirements](#requirements) • 7. [License & support](#license--support)

---


---

## Features
| # | What happens on screen | Code reference |
|:-:|------------------------|----------------|
| 1 | Title + “Every triangle has a **BASE** & **HEIGHT**” intro | |
| 2 | Yellow base line & label, red height line & label appear | |
| 3 | Triangle dragged into a green rectangle → diagonal shows “half” idea | |
| 4 | Formula text `Area = ½ × BASE × HEIGHT` written | |
| 5 | Worked 6 × 4 calculation ⇒ final answer **12 units²** (green fill) | |
| 6 | Closing recap card (“Remember: Area = ½ × Base × Height”) | |

---

## Quick start

```bash
# clone & enter
git clone https://github.com/OmniacsDAO/TriangleArea.git
cd TriangleArea

# create virtual-env & install
python -m venv venv && source venv/bin/activate      # Windows: .\venv\Scripts\activate
pip install manim==0.18.* numpy

# render (preview window, 1080 p, 60 fps)
manim -pqh TriangleArea.py TriangleArea
```


## Customization
Variable (inside construct())	Effect
A, B, C coordinates	Change triangle shape
base_measurement, height_measurement	Swap 6 × 4 for your own numbers
Color constants (YELLOW, RED, …)	Match your brand palette
Font sizes	Scale text for lower-res outputs

## Requirements

    Python ≥ 3.9
    Manim CE
    0.18+
    LaTeX distribution (for MathTex)

## License & support

MIT — remix, reuse, and teach away!

💚 Support Digital Public Goods
If this helped you, grab some $IACS tokens on Base to fund more open-source STEM media.
Contract: 0x46e69Fa9059C3D5F8933CA5E993158568DC80EBf

Made with love by Omniacs.DAO 📐✨
