# Area of a Trapezium — **Part 2: Height Unknown** 🔷📏

<img width="1638" height="1120" alt="image" src="https://github.com/user-attachments/assets/d216fd96-bc64-4006-8b7b-fcfc9030001d" />

 **Manim animation that finds the area when the height *isn’t* given.**  
 Walks through three height-finding strategies (focus on the Pythagorean approach) and finishes with a full numeric example.

Watch [here]().
---

## Demo  
*Drop a GIF/thumbnail here once rendered.*

---

## Features

| # | What you’ll see | Code reference |
|:-:|-----------------|----------------|
| 1 | Title & problem setup: “Area of a Trapezium — Height Not Given” |  |
| 2 | Labeled trapezium with known sides *a = 6*, *b = 10*, *c = 5*, *d = 5* but unknown *h* |  |
| 3 | Menu of **three** methods to find height (Pythagoras, coordinates, trigonometry) |  |
| 4 | Detailed **Pythagorean analysis** of right triangle to solve for *h* |  |
| 5 | Final area formula \(A=\tfrac12(a+b)h\) flashed on screen |  |

---

## Quick Start

```bash
# Clone & enter
git clone https://github.com/OmniacsDAO/TrapeziumAreaPart2.git
cd TrapeziumAreaPart2

# Set up Python env
python -m venv venv && source venv/bin/activate        # Windows: .\venv\Scripts\activate
pip install manim==0.18.* numpy

# Render (preview window, 1080 p, 60 fps)
manim -pqh trapeziumareapart2.py TrapeziumAreaPart2

    4 K export:
    manim -pqh --format=mp4 --resolution=3840,2160 trapeziumareapart2.py TrapeziumAreaPart2
```

## Requirements

    Python ≥ 3.9
    Manim CE
    0.18+
    A LaTeX distribution (for MathTex)

## License & Support

MIT — remix, reuse, and teach away!

💚 Support Digital Public Goods
Made with love by Omniacs.DAO ✨
If this project helps you, consider picking up some $IACS tokens on Base to fund more open-source STEM media.
Contract: 0x46e69Fa9059C3D5F8933CA5E993158568DC80EBf
