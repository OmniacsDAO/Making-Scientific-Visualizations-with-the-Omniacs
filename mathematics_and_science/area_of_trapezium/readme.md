# 🔷 Area of a Trapezium 

> **Manim animation that proves and applies**  
> \(A=\tfrac12(a+b)h\) for any trapezium with one pair of parallel sides.

<img width="2213" height="1400" alt="image" src="https://github.com/user-attachments/assets/ccda717f-3cab-42a1-a61f-4e6a26a8115b" />


Watch [here]().

---

## Table of Contents
1. [Demo](#demo) • 2. [Features](#features) • 3. [Quick start](#quick-start)  
4. [Scene index](#scene-index) • 5. [Customization](#customization) • 6. [Requirements](#requirements)  
7. [License & support](#license--support)

---

## Features
| # | What you’ll see | Code reference |
|:-:|-----------------|----------------|
| 1 | **Definition & title:** “A trapezium has one pair of parallel sides” | |
| 2 | **Labeled diagram** showing bases *a = 4*, *b = 6* and height *h = 3* with color-coded braces | |
| 3 | **Derivation:** combine two congruent trapezia → parallelogram to obtain \( (a+b)h \) |  |
| 4 | **Formula reveal:** \( \displaystyle A=\frac12(a+b)h \) written on screen |  |
| 5 | **Worked example** with *a = 5, b = 9, h = 4* → area **28 units²** |  |

---

## Quick start

```bash
# clone & enter
git clone https://github.com/OmniacsDAO/TrapeziumArea.git
cd TrapeziumArea

# create virtual-env & install
python -m venv venv && source venv/bin/activate        # Windows: .\venv\Scripts\activate
pip install manim==0.18.* numpy

# render (preview window, 1080 p, 60 fps)
manim -pqh trapeziumarea.py TrapeziumArea
```


## Customization
Variable	Effect
a, b, h (in trapezium_with_labels())	Change default side lengths
Colors (trapezium_color, measurement_color…)	Match your palette
Fonts / font-sizes	Resize for different resolutions

## Requirements

    Python ≥ 3.9
    Manim CE
    0.18+
    A LaTeX distribution (for MathTex)

## License & support

MIT — remix, reuse, and teach away!

💚 Support Digital Public Goods
Enjoy this? Grab some $IACS tokens on Base to fund more open-source STEM media.
Contract: 0x46e69Fa9059C3D5F8933CA5E993158568DC80EBf

Made with love by Omniacs.DAO 📏✨
