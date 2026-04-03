# Gradient Ascent

A cinematic 3D Manim animation explaining gradient ascent — the algorithm that climbs a function toward its maximum by always stepping in the direction of steepest uphill slope. Starting from a plain-English analogy anyone can follow, the video builds through the core equations, a 3D landscape, a top-down contour map, and a live animated ascent with two tracers climbing simultaneously from different starting points.

<img width="1429" height="1448" alt="image" src="https://github.com/user-attachments/assets/9d64b0f0-b7e0-4b32-8193-d3c5bb281e01" />


[Watch here!](https://youtu.be/7TIJYGP28A4)

---

## What's Inside the Video

| Part | Title | What you see |
|------|-------|-------------|
| 1 | Title + Plain English Intro | "Blindfolded on a hilly landscape" — 4 explanation lines revealed one by one |
| 2 | The Idea | Two equations: gradient definition `∇f` and update rule `xₙ₊₁ = xₙ + α∇f(xₙ)` |
| 3 | The 3D Landscape | Colour-gradient multi-peak surface `f(x,y)`, ambient camera rotation |
| 4 | Contour Map | Top-down view with concentric contour rings, two start positions marked |
| 5 | Animated Ascent | Two tracers (pink and green) climb the 3D surface simultaneously, yellow gradient arrows at each step |
| 6 | Learning Rate Matters | Three rows explaining too-small, too-large, and just-right learning rates |

---

## Requirements

| Dependency | Version |
|-----------|---------|
| Python | 3.10 or higher |
| Manim Community | v0.18 or higher |
| NumPy | any recent version |
| LaTeX (MiKTeX / TeX Live) | required for MathTex equations |
| FFmpeg | required for video export |

Install Manim:
```bash
pip install manim
```

---

## Running the Animation

**Fast preview (low quality — use this first):**
```bash
manim -pql gradient_ascent.py GradientAscent --disable_caching
```

**High quality (1080p 60fps — final export):**
```bash
manim -pqh gradient_ascent.py GradientAscent --disable_caching
```

**Google Colab:**
```python
!apt install libcairo2-dev libpango1.0-dev ffmpeg > /dev/null 2>&1
!pip install manim -q
!manim -pqh gradient_ascent.py GradientAscent --disable_caching
from IPython.display import Video
Video("media/videos/gradient_ascent/1080p60/GradientAscent.mp4", embed=True)
```

Output file will be at:
```
media/videos/gradient_ascent/1080p60/GradientAscent.mp4
```

---

## File Structure

```
gradient_ascent.py          ← the Manim scene
media/
  videos/
    gradient_ascent/
      480p15/               ← low quality preview
      1080p60/              ← high quality output
```

---

## The Surface Function

The landscape used in Parts 3–5 is a sum of three Gaussians:

```python
f(x, y) = 1.5·exp(-((x-1)² + (y-1)²) / 0.8)
         +     exp(-((x+1.5)² + (y+0.5)²) / 0.5)
         + 0.8·exp(-((x-0.5)² + (y+1.5)²) / 0.6)
```

This creates three peaks of different heights — demonstrating that gradient ascent converges to a **local** maximum, not necessarily the global one.

---

## Colour Palette

| Element | Hex | Used for |
|---------|-----|---------|
| Background | `#0a0a0f` | Scene background |
| Cyan | `#00e5ff` | Headers, labels |
| Gold | `#ffdd00` | Title rule, gradient arrows, equation 1 |
| Orange | `#ff9944` | Update rule equation |
| Pink | `#ff4488` | Tracer A (starts at −2, −2) |
| Green | `#44ff88` | Tracer B (starts at +2, −1.5) |
| Red | `#ff6666` | "Too large" learning rate row |
| Grey | `#aaaacc` | Explanation text, "too small" row |

---

## Key Concepts Covered

- **The gradient** — `∇f(x,y) = (∂f/∂x, ∂f/∂y)` — the direction of steepest increase at any point
- **The update rule** — `xₙ₊₁ = xₙ + α∇f(xₙ)` — take a step proportional to the gradient
- **Learning rate α** — controls step size; too small = slow, too large = overshoots
- **Local vs global maxima** — two tracers from different starts converge to different peaks
- **Gradient arrows** — yellow Arrow3D objects drawn at each step showing the gradient direction
- **Contour maps** — top-down view showing lines of equal function value

---

## Notes for Developers

- The gradient is computed numerically using central differences with `eps=1e-4` rather than analytically — this keeps the code generalised to any `f(x,y)`.
- The `ascent_path()` function clips coordinates to `[-2.8, 2.8]` to keep tracers on the visible surface.
- All gradient arrows are accumulated in `arrows_all = VGroup()` and faded out together in a single `FadeOut(arrows_all)` call at the end of Part 5 — this prevents yellow arrow remnants persisting into Part 6.
- Part 6 registers each row with `add_fixed_in_frame_mobjects` **individually** right before its own `FadeIn` — registering them all at once causes a pre-flash glitch.
- The `--disable_caching` flag is strongly recommended during development to avoid stale partial renders.

---

## License

Free to use for educational and non-commercial purposes. Attribution appreciated.

---
🤝 Support Visual Math Learning
*Maintained with ❤️ by **Omniacs.DAO** – accelerating digital public goods through data.*

🛠️ Keep public infrastructure thriving. Buy [$IACS](http://dexscreener.com/base/0xd4d742cc8f54083f914a37e6b0c7b68c6005a024) on Base — CA: 0x46e69Fa9059C3D5F8933CA5E993158568DC80EBf
