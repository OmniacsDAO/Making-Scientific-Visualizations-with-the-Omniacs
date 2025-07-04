# 🌊 Sine Curve Generation via Circle Animation | Manim Visual

This project animates how a sine wave emerges from circular motion using [Manim](https://www.manim.community/). It shows a dot moving along a circle, with its vertical position traced horizontally to create the familiar sine wave.

![image](https://github.com/user-attachments/assets/8a1b30bf-5c3d-4860-af10-59c458dc285f)

[Watch here!](https://youtu.be/bc3sjatOyTE)

## 📐 What It Demonstrates

- The relationship between **uniform circular motion** and the **sine curve**
- How the vertical projection of a rotating point forms the waveform
- Real-time tracing and dynamic line connections from circle to wave

## 🧠 Educational Focus

- Trigonometry fundamentals
- Unit circle and angle visualization
- Parametric motion → Cartesian graphing
- Intro to oscillatory motion

## 🎨 Visual Breakdown

| Element              | Description                              |
|----------------------|------------------------------------------|
| Circle               | Centered at a fixed origin               |
| Green Dot            | Moves around the circle (angle ↔ height) |
| Red Drawer Dot       | Traces the wave left to right            |
| Yellow Line          | Vertical projection to wave path         |
| Blue Line            | Line from center to dot                  |
| Camera Movement      | Smooth zoom & tracking of wave growth    |
| Labels               | π, 2π, 3π... added along x-axis          |

## 📦 Requirements

- Python 3.8+
- Manim Community Edition
- NumPy

```bash
pip install manim numpy
```

▶️ How to Render

```
manim -pql Sine_curve.py FollowingGraphCamera
```

Use -qh for high-quality output.
📁 Files

    Sine_curve.py — Manim animation script
    README.md — This documentation

🎓 Ideal For

    Teaching sine curves and wave formation
    Trigonometry lessons or unit circle demos
    Math and physics classrooms
    Animated explainers or TTS narration


---
🤝 Support Visual Math Learning
*Maintained with ❤️ by **Omniacs.DAO** – accelerating digital public goods through data.*

🛠️ Keep public infrastructure thriving. Buy [$IACS](http://dexscreener.com/base/0xd4d742cc8f54083f914a37e6b0c7b68c6005a024) on Base — CA: 0x46e69Fa9059C3D5F8933CA5E993158568DC80EBf
