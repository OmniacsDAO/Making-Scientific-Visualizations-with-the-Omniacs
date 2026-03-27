Lissajous Curves -- Complete Manim Visualization
================================================
Structure:
  1. Title card
  2. Concept introduction

lissajous_curves.py
17 KB
# 🌊 Lissajous Curves Visualization with Manim

This project demonstrates the elegant geometry of **Lissajous Curves** — parametric figures traced by the intersection of two perpendicular harmonic oscillations. The animation is built with [Manim](https://www.manim.community/) and explores how varying the frequency ratios and phase offsets generates a rich family of curves.

![Animation Preview](preview.png)

README.md
3 KB
﻿
# 🌊 Lissajous Curves Visualization with Manim

This project demonstrates the elegant geometry of **Lissajous Curves** — parametric figures traced by the intersection of two perpendicular harmonic oscillations. The animation is built with [Manim](https://www.manim.community/) and explores how varying the frequency ratios and phase offsets generates a rich family of curves.

![Animation Preview](preview.png)

[Watch here!](https://youtu.be/PLACEHOLDER)

## 📐 What's a Lissajous Curve?

A Lissajous Curve is a parametric curve described by:

```
x(t) = A · sin(a·t + δ)
y(t) = B · sin(b·t)
```

They appear in:
- Physics and signal processing (oscilloscope displays)
- Electrical engineering (phase relationships between signals)
- Art and generative design
- Astronomy (orbital resonance patterns)

## 🔍 Features

- Title animation with smooth intro
- Parametric sweep across multiple frequency ratios (a:b)
- Phase offset (δ) animated continuously to show curve evolution
- Color-coded curves per frequency pair
- Smooth fade-out exit animation

## 🎨 Visual Styling

| Feature            | Value                                      |
|--------------------|--------------------------------------------|
| Frequency Ratios   | 1:1, 1:2, 1:3, 2:3, 3:4, and more         |
| Phase Sweep        | 0 to 2π animated continuously              |
| Colors             | Cyan, Magenta, Yellow, Green, Red, Blue    |
| Stroke Width       | 2                                          |
| Background         | Black                                      |
| Curve Animation    | Drawn parametrically + phase-animated      |

## 📦 Requirements

- Python 3.8+
- Manim Community Edition
- NumPy

```bash
pip install manim numpy
```

## ▶️ Run the Animation

```bash
manim -pql lissajous_curves.py LissajousCurves
```

Use `-qh` instead of `-pql` for high quality.

## 📁 Files

- `lissajous_curves.py` — Manim animation script
- `README.md` — Project documentation

## 🎓 Educational Use

Useful for:

- Teaching parametric equations and harmonic motion
- Demonstrating frequency and phase relationships
- Exploring the intersection of math, physics, and art
- Signal processing and oscilloscope education

---
🤝 Support Algorithmic Visualization

*Maintained with ❤️ by **Omniacs.DAO** – accelerating digital public goods through data.*

🛠️ Keep public infrastructure thriving. Buy [$IACS](http://dexscreener.com/base/0xd4d742cc8f54083f914a37e6b0c7b68c6005a024) on Base — CA: 0x46e69Fa9059C3D5F8933CA5E993158568DC80EBf
README.md
3 KB
