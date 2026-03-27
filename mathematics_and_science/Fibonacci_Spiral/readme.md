# Fibonacci Spiral & The Golden Ratio
### A Manim CE Mathematical Animation

---

## Overview

A cinematic Manim animation exploring one of nature's most famous numbers — φ (phi) = 1.6180339… — from its humble origins in the Fibonacci sequence all the way to a 3D golden spiral and its appearances in sunflowers, nautilus shells, DNA, and art. Designed to be followed by anyone with no prior mathematical background.

---

## What's Inside the Video

| Part | Title | What you see |
|------|-------|-------------|
| 0 | Cinematic Title | Gold and cyan title reveal with floating particle field |
| 1 | The Fibonacci Sequence | Colour-coded number boxes, brace showing 5+8=13, ratio convergence toward φ |
| 2 | Tiling with Squares | Classic Fibonacci square tiling — each square labelled with its Fibonacci size |
| 3 | The Fibonacci Spiral | Faded background squares, quarter-circle arcs drawn one by one |
| 4 | The Golden Ratio φ | Golden rectangle divided by cyan square, measurement arrows (a and b), remainder rectangle, closed-form equation |
| 5 | Golden Spiral in 3D | Logarithmic golden spiral lifted into a 3D helix — two mirrored spirals, ambient camera orbit |
| 6 | The Mathematics of φ | Four key equations: φ²=φ+1, continued fraction, nested radicals, Fibonacci limit |
| 7 | φ in Nature & the World | Six application cards: Sunflower, Nautilus, Galaxies, Art, DNA, Design |

---

## Requirements

| Dependency | Version |
|-----------|---------|
| Python | 3.10 or higher |
| Manim Community | v0.18 or higher |
| NumPy | any recent version |
| LaTeX (MiKTeX / TeX Live) | required for MathTex equations |
| FFmpeg | required for video export |

```bash
pip install manim
```

---

## Running the Animation

**Fast preview:**
```bash
manim -pql fibonacci_golden.py FibonacciGolden --disable_caching
```

**High quality (1080p 60fps):**
```bash
manim -pqh fibonacci_golden.py FibonacciGolden --disable_caching
```

Output: `media/videos/fibonacci_golden/1080p60/FibonacciGolden.mp4`

---

## Colour Palette

| Name | Hex | Used for |
|------|-----|---------|
| C_GOLD | `#ffdd00` | Title, φ labels, sequence boxes |
| C_CYAN | `#00e5ff` | Headers, cyan square (part a) |
| C_GREEN | `#44ff99` | Exact form equation |
| C_ORANGE | `#ff9944` | Remainder rectangle, b measurement |
| C_PURPLE | `#cc44ff` | 3D spiral gradient |
| C_PINK | `#ff4488` | 3D spiral gradient |
| C_WHITE | `#e8e8f0` | Body text |
| C_DIM | `#aaaacc` | Subtitles, card body text |
| BG | `#05050f` | Background |

---

## Key Concepts Covered

- **Fibonacci sequence** — each term is the sum of the two before it: 1, 1, 2, 3, 5, 8, 13, 21…
- **Ratio convergence** — consecutive Fibonacci ratios converge toward φ ≈ 1.6180339
- **Fibonacci tiling** — squares with Fibonacci side lengths tile a golden rectangle exactly
- **Fibonacci spiral** — quarter-circle arcs through successive Fibonacci squares approximate the golden spiral
- **Golden rectangle** — a rectangle where `(a+b)/a = a/b = φ`; removing the square leaves another golden rectangle
- **Logarithmic golden spiral** — `r(θ) = e^(b·θ)` where b = ln(φ)/(π/2) — grows by φ each quarter turn
- **Key identities** — `φ² = φ + 1`, infinite continued fraction, infinite nested radicals

---

## Notes for Developers

- The 3D spiral in Part 5 uses `b = np.log(PHI) / (PI / 2)` so the radius grows by exactly φ per quarter turn. Two mirrored spirals (z = +t·0.18 and z = −t·0.18) create the double helix effect.
- Part 4 divides the screen into a strict left zone (rectangle + arrows) and right zone (equations) to prevent overlap between the measurement arrows and the formulae.
- Part 7 card titles contain no emoji — Manim renders emoji through Cairo/Pango which often produces broken glyphs on headless render environments.
- `PHI = (1 + np.sqrt(5)) / 2` is defined as a module-level constant and used throughout.

---

## License

Free to use for educational and non-commercial purposes. Attribution appreciated.
