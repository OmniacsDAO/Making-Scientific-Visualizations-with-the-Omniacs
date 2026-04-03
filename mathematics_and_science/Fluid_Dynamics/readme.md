# Fluid Dynamics — Navier-Stokes Visualized

A cinematic Manim animation that takes the viewer from the intuition of what a fluid is all the way to the full Navier-Stokes equation — one of the most important (and unsolved) equations in all of physics. Features live velocity field arrows, a 3D pressure landscape, dual vortex fields, a laminar-to-turbulent pipe transition, and a closing card on real-world applications.

<img width="962" height="723" alt="image" src="https://github.com/user-attachments/assets/4ce035c4-c87f-4ae4-8424-d34948576bd4" />

[Watch here!](https://www.youtube.com/watch?v=NGBcLhL6-vk)
---

## What's Inside the Video

| Part | Title | What you see |
|------|-------|-------------|
| 0 | Cinematic Title | Title reveal with gold rule, subtitle, tagline |
| 1 | What is a Fluid? | 120 particle dots appear then drift rightward under an applied force |
| 2 | The Velocity Field | 14×9 grid of colour-coded arrows (blue=slow, red=fast), speed legend in top-right corner, yellow tracer streamline |
| 3 | Three Forces Drive Every Fluid | Three pill cards: Pressure ∇p, Viscosity μ∇²u, External Forces f |
| 4 | Pressure Field | 3D colour-gradient pressure landscape with ambient camera orbit |
| 5 | Rotation & Vortices | Dual counter-rotating vortex velocity field, orbit ring, yellow tracer |
| 6 | Laminar vs Turbulent | Pipe with 7 smooth laminar lines → 9 chaotic turbulent lines, Reynolds number callout |
| 7 | The Navier-Stokes Equation | Full equation colour-coded term by term, 6 annotation cards in two columns below |
| 8 | Why Does It Matter? | 5 application facts, Millennium Prize Problem closing note |

---

## Requirements

| Dependency | Version |
|-----------|---------|
| Python | 3.10 or higher |
| Manim Community | v0.18 or higher |
| NumPy | any recent version |
| LaTeX (MiKTeX / TeX Live) | required for MathTex |
| FFmpeg | required for video export |

```bash
pip install manim
```

---

## Running the Animation

**Fast preview:**
```bash
manim -pql fluid_dynamics.py FluidDynamics --disable_caching
```

**High quality (1080p 60fps):**
```bash
manim -pqh fluid_dynamics.py FluidDynamics --disable_caching
```

Output: `media/videos/fluid_dynamics/1080p60/FluidDynamics.mp4`

---

## Colour Palette

| Name | Hex | Used for |
|------|-----|---------|
| C_BG | `#05050f` | Background |
| C_CYAN | `#00e5ff` | Headers, pressure label |
| C_YELLOW | `#ffdd00` | Title rule, tracer streamline, balance note |
| C_ORANGE | `#ff9944` | Viscosity term, turbulent lines |
| C_RED | `#ff3344` | Fast velocity arrows |
| C_GREEN | `#44ff99` | External forces term |
| C_PURPLE | `#cc44ff` | Vortex left rotation |
| C_PINK | `#ff4488` | Vortex right rotation |
| C_GREY | `#aaaacc` | Body text, dim particles |

---

## Key Concepts Covered

- **Fluid particles** — a fluid is a substance that flows under any applied force
- **Velocity field** — every point in space has a velocity vector; colour = speed magnitude
- **Streamlines** — paths traced by passive tracer particles following the velocity field
- **Three forces** — pressure gradient (∇p), viscous diffusion (μ∇²u), body forces (f)
- **Pressure landscape** — pressure field visualised as terrain altitude; fluid flows downhill
- **Vorticity** — counter-rotating vortex pairs; the building block of turbulence
- **Reynolds number** — dimensionless ratio Re = ρuL/μ determines laminar vs turbulent regime
- **Navier-Stokes equation** — `ρ(∂u/∂t + (u·∇)u) = -∇p + μ∇²u + f`
- **Millennium Prize Problem** — proving smooth solutions always exist is worth $1,000,000 and remains unsolved

---

## Notes for Developers

- The velocity field in Part 2 uses `vel(x,y) = (1 + 0.5·sin(πy/2.5), 0.4·sin(πx/2.5))`. This creates a gentle shear flow with visible curvature in the arrows.
- The speed legend bar is positioned at `to_corner(UR)` with `shift(LEFT * 0.85)` so the "Fast" label stays on screen.
- The NS equation annotation cards (Part 7) are in two columns of three, placed at `to_edge(DOWN)` with no connectors. Each card is registered individually before its `FadeIn` to prevent pre-flash.
- The tracer path in Part 2 is set to `opacity=0` before being registered as a fixed-frame object, then restored to `opacity=1` before `Create` — this prevents the full path flashing on screen before the drawing animation runs.

---

## License

Free to use for educational and non-commercial purposes. Attribution appreciated.

---
🤝 Support Visual Math Learning
*Maintained with ❤️ by **Omniacs.DAO** – accelerating digital public goods through data.*

🛠️ Keep public infrastructure thriving. Buy [$IACS](http://dexscreener.com/base/0xd4d742cc8f54083f914a37e6b0c7b68c6005a024) on Base — CA: 0x46e69Fa9059C3D5F8933CA5E993158568DC80EBf
