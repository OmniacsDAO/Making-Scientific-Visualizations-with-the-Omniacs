# Riemann Surfaces

A cinematic 3D Manim animation explaining Riemann surfaces from first principles — starting with the complex plane, working through the multi-value problem for √z, and building up to the two-sheeted √z surface and the infinite helicoid of log(z). No prior knowledge of complex analysis required.

> *"What happens when a function has multiple values?"*
> — Complex analysis · Bernhard Riemann · 1851

<img width="835" height="726" alt="image" src="https://github.com/user-attachments/assets/cc0e4d9a-a7a5-4aa4-a69c-4f3dfc4b4d77" />

[Watch here!](https://www.youtube.com/watch?v=qXdsgI7cIWk)

---

## What's Inside the Video

| Part | Title | What you see |
|------|-------|-------------|
| 0 | Title Card | Title reveal with orange rule, subtitle, author credit |
| 1 | The Complex Plane | NumberPlane, z = 2 + 1.5i plotted with real/imaginary components |
| 2 | The Multi-Value Problem | +√2 and −√2 on the real axis, orbit ring, yellow vs cyan traces showing the jump |
| 3 | Riemann Surface for √z | Two-sheeted spiral ramp in 3D, branch point, yellow traveler spiraling smoothly |
| 4 | Riemann Surface for log(z) | Infinite helicoid, level rings, white traveler ascending the staircase |
| 5 | Closing Summary | Key definitions, √z and log(z) examples, punchline equation |

---

## Requirements

| Dependency | Version |
|-----------|---------|
| Python | 3.10 or higher |
| Manim Community | v0.18 or higher |
| NumPy | any recent version |
| LaTeX (MiKTeX / TeX Live) | required for MathTex |
| FFmpeg | required for video export |

Install Manim:
```bash
pip install manim
```

---

## Running the Animation

**Fast preview (low quality — use this first):**
```bash
manim -pql riemann_surfaces.py RiemannSurfaces --disable_caching
```

**High quality (1080p 60fps — use for final export):**
```bash
manim -pqh riemann_surfaces.py RiemannSurfaces --disable_caching
```

**Google Colab:**
```python
!apt install libcairo2-dev libpango1.0-dev ffmpeg > /dev/null 2>&1
!pip install manim -q
!manim -pqh riemann_surfaces.py RiemannSurfaces --disable_caching
from IPython.display import Video
Video("media/videos/riemann_surfaces/1080p60/RiemannSurfaces.mp4", embed=True)
```

Output file will be at:
```
media/videos/riemann_surfaces/1080p60/RiemannSurfaces.mp4
```

---

## File Structure

```
riemann_surfaces.py       ← the Manim scene
media/
  videos/
    riemann_surfaces/
      480p15/             ← low quality preview
      1080p60/            ← high quality output
```

---

## Font & Style Constants

All text styling is controlled by four constants at the top of the file:

```python
NOTE_FONT   = "Arial"     # change this to switch the entire video's font
NOTE_SIZE   = 21          # base size for all explanation text
NOTE_COLOR  = "#c8cce8"   # base colour for all explanation text
NOTE_STROKE = 0.45        # glyph stroke width — gives body on dark backgrounds
HDR_STROKE  = 0.5         # stroke for section headers
```

---

## Colour Palette

| Element | Hex |
|---------|-----|
| Background | `#070712` |
| Title / Step headers | `#00e5ff` |
| Section rule | `#ff9944` |
| √z surface & sheet labels | `#00ffcc` |
| log(z) helicoid gradient | `#9933cc` → `#ff4488` → orange → yellow → teal |
| Branch point | `#ff4444` |
| Traveler dot (Part 3) | yellow |
| Traveler dot (Part 4) | white |
| Punchline text | `#ffdd00` |
| Body text | `#c8cce8` |

---

## Key Concepts Covered

- **The complex plane** — every complex number `z = x + iy` as a 2D point
- **Multi-valued functions** — why `√z` produces two valid answers for every z
- **Branch cuts and branch points** — the seam where the sheets connect at z = 0
- **Two-sheeted Riemann surface for √z** — parameterised as a spiral ramp over `[0, 4π]`
- **The helicoid for log(z)** — infinite staircase, one floor per full orbit of z around the origin
- **Key insight** — Riemann surfaces turn multi-valued functions into single-valued ones by giving each value its own sheet

---

## Notes for Developers

- `√z` is rendered using `MathTex(r"\sqrt{z}")` combined with surrounding `Text` objects in a `VGroup` — this is the only reliable way to get the radical bar properly over the z.
- All labels in 3D parts (Parts 3 and 4) use `add_fixed_in_frame_mobjects()` to pin to the 2D overlay. Each object is registered **individually** right before its own `play()` call to prevent pre-flash glitches.
- The two-sheeted surface is parameterised with `v_range=[0, 4π]` so the same `(x,y)` point appears at two different heights — one per sheet.
- The helicoid uses `v_range=[-4π, 4π]` giving 4 full floors visible above and below the origin.
- The `--disable_caching` flag is strongly recommended during development.

---

## License

Free to use for educational and non-commercial purposes. Attribution appreciated.
---
🤝 Support Visual Math Learning
*Maintained with ❤️ by **Omniacs.DAO** – accelerating digital public goods through data.*

🛠️ Keep public infrastructure thriving. Buy [$IACS](http://dexscreener.com/base/0xd4d742cc8f54083f914a37e6b0c7b68c6005a024) on Base — CA: 0x46e69Fa9059C3D5F8933CA5E993158568DC80EBf
