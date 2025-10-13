# Area of a Swimming Pool 🏊‍♀️💧

<img width="1665" height="1191" alt="image" src="https://github.com/user-attachments/assets/0e582530-fef5-4ec5-b789-d612bc03c073" />

 **Manim animation that finds the area of a pool-shaped figure** — a rectangle with two semicircular ends.  
 Demonstrates decomposition into simple shapes and shows how to combine their areas for the total surface.



---

## Table of Contents  
1. [Demo](#demo) • 2. [Features](#features) • 3. [Quick Start](#quick-start)  
4. [Scene Index](#scene-index) • 5. [Customization](#customization) • 6. [Requirements](#requirements)  
7. [License & Support](#license--support)

---

## Features

| # | What you’ll see | Code reference |
|:-:|-----------------|----------------|
| 1 | **Setup:** Title card “Area of a Swimming Pool” with clear shape outline |   |
| 2 | Draws **rectangle + two semicircles** to model a pool |   |
| 3 | Labels **length**, **width**, and **radius = width / 2** |   |
| 4 | Step-by-step formula build-up: \(A = L×W + πr^2\) |   |
| 5 | Numeric example substituting *L = 5 m, W = 2.5 m* → total area displayed |   |

---

## Quick Start

```bash
# Clone & enter
git clone https://github.com/OmniacsDAO/SwimmingPoolArea.git
cd SwimmingPoolArea

# Environment setup
python -m venv venv && source venv/bin/activate        # Windows: .\venv\Scripts\activate
pip install manim==0.18.* numpy

# Render (preview, 1080p)
manim -pqh swimmingpoolarea.py SwimmingPoolArea

    4 K export:
    manim -pqh --format=mp4 --resolution=3840,2160 swimmingpoolarea.py SwimmingPoolArea
```



## Requirements

    Python ≥ 3.9
    Manim CE 0.18+
    LaTeX distribution (for MathTex)

## License & Support

MIT — reuse freely for classrooms, tutorials, or your own channels.

💚 Support Digital Public Goods
Made with 💧 by Omniacs.DAO
If this animation helps you, consider grabbing some $IACS tokens on Base to support more open-source STEM media.
Contract: 0x46e69Fa9059C3D5F8933CA5E993158568DC80EBf


