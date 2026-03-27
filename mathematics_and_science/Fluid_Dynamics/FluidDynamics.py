"""
Fluid Dynamics — Navier-Stokes Visualized
==========================================
Google Colab:
    !manim -pqh fluid_dynamics.py FluidDynamics --disable_caching

Local (fast preview):
    manim -pql fluid_dynamics.py FluidDynamics --disable_caching
"""

from manim import *
import numpy as np


# ── colour palette ─────────────────────────────────────────────────────────
C_BG     = "#05050f"
C_CYAN   = ManimColor("#00e5ff")
C_YELLOW = ManimColor("#ffdd00")
C_ORANGE = ManimColor("#ff9944")
C_RED    = ManimColor("#ff3344")
C_GREEN  = ManimColor("#44ff99")
C_PURPLE = ManimColor("#cc44ff")
C_PINK   = ManimColor("#ff4488")
C_GREY   = ManimColor("#aaaacc")


class FluidDynamics(ThreeDScene):
    def construct(self):
        self.camera.background_color = C_BG

        # ══════════════════════════════════════════════════════════════════
        # PART 0 — CINEMATIC TITLE
        # ══════════════════════════════════════════════════════════════════
        self.set_camera_orientation(phi=0, theta=-PI / 2)

        title = Text("Fluid Dynamics", font_size=60, color=C_CYAN, weight=BOLD)
        sub   = Text("Visualising the Navier-Stokes Equations",
                     font_size=24, color=C_GREY)
        sub.next_to(title, DOWN, buff=0.45)
        rule = Line(title.get_left(), title.get_right(),
                    color=C_YELLOW, stroke_width=2).next_to(title, DOWN, buff=0.16)
        tag  = Text("The equations that govern every river, wind, and ocean",
                    font_size=17, color=ManimColor("#444466"))
        tag.to_edge(DOWN, buff=0.35)

        self.add_fixed_in_frame_mobjects(title)
        self.play(Write(title), run_time=1.8)
        self.add_fixed_in_frame_mobjects(rule)
        self.play(Create(rule), run_time=0.5)
        self.add_fixed_in_frame_mobjects(sub)
        self.play(FadeIn(sub, shift=UP * 0.3), run_time=0.9)
        self.add_fixed_in_frame_mobjects(tag)
        self.play(FadeIn(tag), run_time=0.6)
        self.wait(3.0)
        self.play(FadeOut(title), FadeOut(rule), FadeOut(sub), FadeOut(tag),
                  run_time=0.7)
        self.remove(title, rule, sub, tag)

        # ══════════════════════════════════════════════════════════════════
        # PART 1 — WHAT IS A FLUID?
        # ══════════════════════════════════════════════════════════════════
        lbl1 = Text("What is a Fluid?", font_size=30, color=C_CYAN, weight=BOLD)
        lbl1.to_edge(UP, buff=0.45)
        self.add_fixed_in_frame_mobjects(lbl1)
        self.play(FadeIn(lbl1), run_time=0.5)

        rng = np.random.default_rng(42)
        n_particles = 120
        px = rng.uniform(-5.5, 5.5, n_particles)
        py = rng.uniform(-3.0, 3.0, n_particles)
        particle_dots = VGroup(*[
            Dot([px[i], py[i], 0], radius=0.055,
                color=interpolate_color(BLUE_C, TEAL_C, float(rng.random())))
            for i in range(n_particles)
        ])
        self.add_fixed_in_frame_mobjects(particle_dots)
        self.play(LaggedStart(*[FadeIn(d, scale=0.5)
                                for d in particle_dots],
                              lag_ratio=0.018, run_time=2.0))

        note1a = Text("A fluid is made of countless tiny particles",
                      font_size=20, color=C_GREY)
        note1a.to_edge(DOWN, buff=0.5)
        self.add_fixed_in_frame_mobjects(note1a)
        self.play(FadeIn(note1a), run_time=0.5)
        self.wait(1.5)

        drift_anims = [
            d.animate.shift(RIGHT * float(rng.uniform(0.3, 0.9)) +
                            UP    * float(rng.uniform(-0.25, 0.25)))
            for d in particle_dots
        ]
        note1b = Text("Apply a force — they start to flow together",
                      font_size=20, color=C_YELLOW)
        note1b.to_edge(DOWN, buff=0.5)
        self.add_fixed_in_frame_mobjects(note1b)
        self.play(FadeOut(note1a), FadeIn(note1b),
                  *drift_anims, run_time=2.2)
        self.remove(note1a)
        self.wait(1.5)

        self.play(FadeOut(particle_dots), FadeOut(note1b),
                  FadeOut(lbl1), run_time=0.7)
        self.remove(particle_dots, note1b, lbl1)

        # ══════════════════════════════════════════════════════════════════
        # PART 2 — VELOCITY FIELD
        # ══════════════════════════════════════════════════════════════════
        lbl2 = Text("The Velocity Field", font_size=28, color=C_CYAN, weight=BOLD)
        lbl2.to_edge(UP, buff=0.45)
        self.add_fixed_in_frame_mobjects(lbl2)
        self.play(FadeIn(lbl2), run_time=0.5)

        def vel(x, y):
            u = 1.0 + 0.5 * np.sin(y * PI / 2.5)
            v = 0.4 * np.sin(x * PI / 2.5)
            return np.array([u, v])

        grid_x = np.linspace(-4.5, 4.5, 14)
        grid_y = np.linspace(-2.8, 2.8, 9)
        arrows = VGroup()
        for gx in grid_x:
            for gy in grid_y:
                uv    = vel(gx, gy)
                speed = float(np.linalg.norm(uv))
                uv_n  = uv / (speed + 1e-6) * min(speed * 0.38, 0.55)
                col   = interpolate_color(
                    BLUE_C, RED_C, float(np.clip(speed / 1.8, 0, 1))
                )
                arr = Arrow(
                    start=np.array([gx, gy, 0]),
                    end=np.array([gx + uv_n[0], gy + uv_n[1], 0]),
                    buff=0, stroke_width=2.2,
                    max_tip_length_to_length_ratio=0.38,
                    color=col,
                )
                arrows.add(arr)

        self.add_fixed_in_frame_mobjects(arrows)
        self.play(LaggedStart(*[GrowArrow(a) for a in arrows],
                              lag_ratio=0.012, run_time=2.5))

        note2a = Text(
            "Each arrow shows where the fluid is going and how fast  (colour = speed)",
            font_size=19, color=C_GREY)
        note2a.to_edge(DOWN, buff=0.5)

        legend_slow = Text("Slow", font_size=16, color=BLUE_C)
        legend_fast = Text("Fast", font_size=16, color=RED_C)
        legend_bar  = Rectangle(width=2.2, height=0.18,
                                 fill_opacity=1, stroke_width=0)
        legend_bar.set_color_by_gradient(BLUE_C, RED_C)
        # Place bar in UR corner then nudge left enough so "Fast" label fits
        legend_bar.to_corner(UR, buff=0.5)
        legend_bar.shift(LEFT * 0.85)
        legend_slow.next_to(legend_bar, LEFT,  buff=0.1)
        legend_fast.next_to(legend_bar, RIGHT, buff=0.1)

        # Register each piece individually — prevents pre-flash
        self.add_fixed_in_frame_mobjects(note2a)
        self.add_fixed_in_frame_mobjects(legend_bar)
        self.add_fixed_in_frame_mobjects(legend_slow)
        self.add_fixed_in_frame_mobjects(legend_fast)
        self.play(FadeIn(note2a), FadeIn(legend_bar),
                  FadeIn(legend_slow), FadeIn(legend_fast), run_time=0.6)
        self.wait(2.5)

        tracer_path = ParametricFunction(
            lambda t: np.array([
                -4.0 + t * 0.85,
                0.9 * np.sin(t * 0.9),
                0,
            ]),
            t_range=[0, 9.8], color=C_YELLOW, stroke_width=3.5,
        )
        tracer_dot = Dot([-4.0, 0, 0], color=C_YELLOW, radius=0.10)
        note2b = Text(
            "A tracer particle follows the velocity field — this is a streamline",
            font_size=19, color=C_YELLOW)
        note2b.to_edge(DOWN, buff=0.5)

        self.add_fixed_in_frame_mobjects(note2b)
        self.play(FadeOut(note2a), FadeIn(note2b), run_time=0.4)
        self.remove(note2a)
        # Add path & dot only NOW so they don't flash during the note swap
        tracer_path.set_opacity(0)
        self.add_fixed_in_frame_mobjects(tracer_path, tracer_dot)
        tracer_path.set_opacity(1)
        self.play(
            Create(tracer_path, run_time=3.5),
            MoveAlongPath(tracer_dot, tracer_path.copy(),
                          run_time=3.5, rate_func=linear),
        )
        self.wait(1.5)

        self.play(*[FadeOut(m) for m in [
            arrows, tracer_path, tracer_dot,
            note2b, legend_bar, legend_slow, legend_fast, lbl2,
        ]], run_time=0.7)
        self.remove(arrows, tracer_path, tracer_dot,
                    note2b, legend_bar, legend_slow, legend_fast, lbl2)

        # ══════════════════════════════════════════════════════════════════
        # PART 3 — THREE FORCES
        # ══════════════════════════════════════════════════════════════════
        lbl3 = Text("Three Forces Drive Every Fluid",
                    font_size=28, color=C_CYAN, weight=BOLD)
        lbl3.to_edge(UP, buff=0.45)
        self.add_fixed_in_frame_mobjects(lbl3)
        self.play(FadeIn(lbl3), run_time=0.5)

        def pill(title_str, body_str, col, pos):
            bg = RoundedRectangle(corner_radius=0.22, width=3.6, height=2.0,
                                  fill_color=col, fill_opacity=0.13,
                                  stroke_color=col, stroke_width=1.8)
            t  = Text(title_str, font_size=22, color=col, weight=BOLD)
            b  = Text(body_str,  font_size=17, color=C_GREY)
            b.next_to(t, DOWN, buff=0.22)
            grp = VGroup(bg, t, b)
            grp.move_to(pos)
            bg.move_to(grp.get_center())
            return grp

        pill_p = pill("Pressure  ∇p",
                      "Pushes fluid from\nhigh → low pressure",
                      C_CYAN,   LEFT * 3.8)
        pill_v = pill("Viscosity  μ∇²u",
                      "Internal friction —\nresists deformation",
                      C_ORANGE, ORIGIN)
        pill_e = pill("External Forces  f",
                      "Gravity, wind, pumps\nacting on the fluid",
                      C_GREEN,  RIGHT * 3.8)

        for p in [pill_p, pill_v, pill_e]:
            self.add_fixed_in_frame_mobjects(p)
        self.play(
            LaggedStart(FadeIn(pill_p, shift=UP * 0.3),
                        FadeIn(pill_v, shift=UP * 0.3),
                        FadeIn(pill_e, shift=UP * 0.3),
                        lag_ratio=0.3, run_time=1.8),
        )

        balance = Text(
            "Navier-Stokes balances ALL three — simultaneously, at every point",
            font_size=19, color=C_YELLOW)
        balance.to_edge(DOWN, buff=0.5)
        self.add_fixed_in_frame_mobjects(balance)
        self.play(FadeIn(balance), run_time=0.6)
        self.wait(3.0)

        self.play(*[FadeOut(m) for m in
                    [pill_p, pill_v, pill_e, balance, lbl3]], run_time=0.7)
        self.remove(pill_p, pill_v, pill_e, balance, lbl3)

        # ══════════════════════════════════════════════════════════════════
        # PART 4 — 3D PRESSURE LANDSCAPE
        # ══════════════════════════════════════════════════════════════════
        self.set_camera_orientation(phi=72 * DEGREES, theta=-35 * DEGREES)

        lbl4 = Text("Pressure Field — the 'altitude' of the fluid",
                    font_size=24, color=C_CYAN, weight=BOLD)
        lbl4.to_edge(UP, buff=0.55)
        self.add_fixed_in_frame_mobjects(lbl4)
        self.play(FadeIn(lbl4), run_time=0.5)

        def pressure(x, y):
            return (
                1.4 * np.exp(-((x - 1.2)**2 + (y - 0.8)**2) / 1.0)
                - 1.0 * np.exp(-((x + 1.5)**2 + (y + 0.6)**2) / 0.7)
                + 0.7 * np.exp(-((x - 0.3)**2 + (y + 1.8)**2) / 0.8)
            )

        psurf = Surface(
            lambda u, v: np.array([u, v, pressure(u, v) * 1.6]),
            u_range=[-3.2, 3.2], v_range=[-3.2, 3.2],
            resolution=(38, 38), fill_opacity=0.72,
        )
        psurf.set_color_by_gradient(BLUE_D, TEAL_C, GREEN_C,
                                    YELLOW_C, ORANGE, RED_C)

        self.play(Create(psurf, run_time=3.0))

        note4a = Text("High peaks = high pressure  |  Valleys = low pressure",
                      font_size=19, color=C_GREY)
        note4a.to_edge(DOWN, buff=0.5)
        self.add_fixed_in_frame_mobjects(note4a)
        self.play(FadeIn(note4a), run_time=0.5)

        self.begin_ambient_camera_rotation(rate=0.16)
        self.wait(2.5)
        self.move_camera(phi=88 * DEGREES, theta=-35 * DEGREES,
                         zoom=1.2, run_time=2.0, rate_func=smooth)
        self.move_camera(phi=88 * DEGREES, theta=145 * DEGREES,
                         zoom=1.2, run_time=3.0, rate_func=smooth)
        self.move_camera(phi=55 * DEGREES, theta=260 * DEGREES,
                         zoom=1.0, run_time=2.0, rate_func=smooth)

        note4b = Text("Fluid always flows from peaks → valleys (high → low pressure)",
                      font_size=20, color=C_YELLOW, weight=BOLD)
        note4b.to_edge(DOWN, buff=0.5)
        self.add_fixed_in_frame_mobjects(note4b)
        self.play(FadeOut(note4a), FadeIn(note4b), run_time=0.5)
        self.remove(note4a)
        self.wait(2.5)
        self.stop_ambient_camera_rotation()

        self.play(FadeOut(psurf), FadeOut(lbl4), FadeOut(note4b), run_time=0.7)
        self.remove(lbl4, note4b)

        # ══════════════════════════════════════════════════════════════════
        # PART 5 — VORTEX / ROTATION
        # ══════════════════════════════════════════════════════════════════
        self.set_camera_orientation(phi=0, theta=-PI / 2)

        lbl5 = Text("Rotation & Vortices", font_size=28, color=C_PURPLE, weight=BOLD)
        lbl5.to_edge(UP, buff=0.45)
        self.add_fixed_in_frame_mobjects(lbl5)
        self.play(FadeIn(lbl5), run_time=0.5)

        def vortex_vel(x, y):
            dx1, dy1 = x + 1.8, y
            r1 = dx1**2 + dy1**2 + 0.4
            u1, v1 = -dy1 / r1, dx1 / r1
            dx2, dy2 = x - 1.8, y
            r2 = dx2**2 + dy2**2 + 0.4
            u2, v2 = dy2 / r2, -dx2 / r2
            return np.array([u1 + u2, v1 + v2])

        vgrid_x = np.linspace(-4.8, 4.8, 16)
        vgrid_y = np.linspace(-2.8, 2.8, 10)
        v_arrows = VGroup()
        for gx in vgrid_x:
            for gy in vgrid_y:
                uv    = vortex_vel(gx, gy)
                speed = float(np.linalg.norm(uv))
                uv_n  = uv / (speed + 1e-6) * min(speed * 0.45, 0.5)
                col   = interpolate_color(
                    C_PURPLE, C_PINK, float(np.clip(speed / 2.0, 0, 1))
                )
                arr = Arrow(
                    start=np.array([gx, gy, 0]),
                    end=np.array([gx + uv_n[0], gy + uv_n[1], 0]),
                    buff=0, stroke_width=2.0,
                    max_tip_length_to_length_ratio=0.4,
                    color=col,
                )
                v_arrows.add(arr)

        self.add_fixed_in_frame_mobjects(v_arrows)
        self.play(LaggedStart(*[GrowArrow(a) for a in v_arrows],
                              lag_ratio=0.01, run_time=2.5))

        v_left  = Circle(radius=0.22, color=C_PURPLE,
                         stroke_width=2.5, fill_opacity=0.2)
        v_right = Circle(radius=0.22, color=C_PINK,
                         stroke_width=2.5, fill_opacity=0.2)
        v_left.move_to([-1.8, 0, 0])
        v_right.move_to([1.8, 0, 0])
        lv_l = Text("↺", font_size=28, color=C_PURPLE).move_to([-1.8, 0, 0])
        lv_r = Text("↻", font_size=28, color=C_PINK).move_to([1.8, 0, 0])

        self.add_fixed_in_frame_mobjects(v_left, v_right, lv_l, lv_r)
        self.play(FadeIn(v_left), FadeIn(v_right),
                  FadeIn(lv_l),  FadeIn(lv_r), run_time=0.7)

        note5 = Text(
            "Vortices are spinning pockets of fluid — tornadoes, whirlpools, turbulence",
            font_size=19, color=C_GREY)
        note5.to_edge(DOWN, buff=0.5)
        self.add_fixed_in_frame_mobjects(note5)
        self.play(FadeIn(note5), run_time=0.6)
        self.wait(3.0)

        orbit = ParametricFunction(
            lambda t: np.array([-1.8 + 1.1 * np.cos(t),
                                  1.1 * np.sin(t), 0]),
            t_range=[0, TAU], color=C_YELLOW, stroke_width=2.5,
        )
        orb_dot = Dot([-1.8 + 1.1, 0, 0], color=C_YELLOW, radius=0.10)
        self.add_fixed_in_frame_mobjects(orbit, orb_dot)
        self.play(Create(orbit), FadeIn(orb_dot, scale=1.8), run_time=0.8)
        self.play(MoveAlongPath(orb_dot, orbit.copy()),
                  run_time=2.8, rate_func=linear)
        self.play(FadeOut(orb_dot, scale=0.3), run_time=0.3)
        self.wait(1.5)

        self.play(*[FadeOut(m) for m in [
            v_arrows, v_left, v_right, lv_l, lv_r,
            note5, orbit, lbl5,
        ]], run_time=0.7)
        self.remove(v_arrows, v_left, v_right, lv_l, lv_r,
                    note5, orbit, lbl5)

        # ══════════════════════════════════════════════════════════════════
        # PART 6 — LAMINAR vs TURBULENT
        # ══════════════════════════════════════════════════════════════════
        self.set_camera_orientation(phi=68 * DEGREES, theta=-30 * DEGREES)

        lbl6 = Text("Laminar  vs  Turbulent Flow",
                    font_size=26, color=C_CYAN, weight=BOLD)
        lbl6.to_edge(UP, buff=0.55)
        self.add_fixed_in_frame_mobjects(lbl6)
        self.play(FadeIn(lbl6), run_time=0.5)

        pipe = Surface(
            lambda u, v: np.array([v * 5.0 - 2.5,
                                    1.4 * np.cos(u),
                                    1.4 * np.sin(u)]),
            u_range=[0, TAU], v_range=[0, 1],
            resolution=(20, 4), fill_opacity=0.10,
            checkerboard_colors=[ManimColor("#112233"), ManimColor("#112233")],
        )
        pipe_edge1 = ParametricFunction(
            lambda t: np.array([t * 5 - 2.5,  1.4, 0]),
            t_range=[0, 1], color=ManimColor("#334455"), stroke_width=1.5)
        pipe_edge2 = ParametricFunction(
            lambda t: np.array([t * 5 - 2.5, -1.4, 0]),
            t_range=[0, 1], color=ManimColor("#334455"), stroke_width=1.5)

        self.play(Create(pipe, run_time=1.5),
                  Create(pipe_edge1), Create(pipe_edge2))

        lam_lines = VGroup(*[
            ParametricFunction(
                lambda t, r=r: np.array([t * 5 - 2.5, r, 0]),
                t_range=[0, 1],
                color=interpolate_color(
                    BLUE_C, TEAL_C, float((r + 1.2) / 2.4)
                ),
                stroke_width=2.5,
            )
            for r in np.linspace(-1.15, 1.15, 7)
        ])

        note6a = Text("Laminar — smooth, orderly parallel layers",
                      font_size=20, color=TEAL_C)
        note6a.to_edge(DOWN, buff=0.5)
        self.add_fixed_in_frame_mobjects(note6a)
        self.play(LaggedStart(*[Create(l) for l in lam_lines],
                              lag_ratio=0.12, run_time=2.0))
        self.play(FadeIn(note6a), run_time=0.5)
        self.move_camera(phi=55 * DEGREES, theta=60 * DEGREES,
                         run_time=2.2, rate_func=smooth)
        self.move_camera(phi=68 * DEGREES, theta=-30 * DEGREES,
                         run_time=2.0, rate_func=smooth)
        self.wait(1.0)

        rng2 = np.random.default_rng(7)
        turb_offsets = [float(x) for x in rng2.uniform(0, 10, 9)]
        turb_colors  = [float(x) for x in rng2.random(9)]
        turb_lines = VGroup(*[
            ParametricFunction(
                lambda t, r=r, seed=seed: np.array([
                    t * 5 - 2.5,
                    r + 0.55 * np.sin(t * 14 + seed) +
                        0.25 * np.sin(t * 23 + seed * 2),
                    0.2 * np.sin(t * 11 + seed * 1.5),
                ]),
                t_range=[0, 1],
                color=interpolate_color(C_ORANGE, C_RED, tc),
                stroke_width=2.0,
            )
            for r, seed, tc in zip(
                np.linspace(-1.1, 1.1, 9),
                turb_offsets,
                turb_colors,
            )
        ])

        note6b = Text("Turbulent — chaotic, mixing, unpredictable",
                      font_size=20, color=C_ORANGE)
        note6b.to_edge(DOWN, buff=0.5)
        self.add_fixed_in_frame_mobjects(note6b)

        self.play(FadeOut(lam_lines), run_time=0.6)
        self.play(FadeOut(note6a), FadeIn(note6b), run_time=0.4)
        self.remove(note6a)
        self.play(LaggedStart(*[Create(l) for l in turb_lines],
                              lag_ratio=0.08, run_time=2.5))

        self.begin_ambient_camera_rotation(rate=0.20)
        self.wait(3.5)
        self.stop_ambient_camera_rotation()

        re_note = Text(
            "Reynolds Number Re determines which regime you're in",
            font_size=18, color=C_YELLOW)
        re_note.to_edge(DOWN, buff=0.5)
        self.add_fixed_in_frame_mobjects(re_note)
        self.play(FadeOut(note6b), FadeIn(re_note), run_time=0.5)
        self.remove(note6b)
        self.wait(2.5)

        self.play(*[FadeOut(m) for m in [
            pipe, pipe_edge1, pipe_edge2, turb_lines, re_note, lbl6,
        ]], run_time=0.7)
        self.remove(pipe, pipe_edge1, pipe_edge2, turb_lines, re_note, lbl6)

        # ══════════════════════════════════════════════════════════════════
        # PART 7 — NAVIER-STOKES EQUATION  (reworked annotation layout)
        # ══════════════════════════════════════════════════════════════════
        self.set_camera_orientation(phi=0, theta=-PI / 2)

        eq_head = Text("The Navier-Stokes Equation",
                       font_size=34, color=C_CYAN, weight=BOLD)
        eq_head.to_edge(UP, buff=0.35)
        self.add_fixed_in_frame_mobjects(eq_head)
        self.play(FadeIn(eq_head), run_time=0.8)

        # ── equation sits near the top ──────────────────────────────────
        ns_eq = MathTex(
            r"\rho",                                     # [0] density
            r"\!\left(\frac{\partial \mathbf{u}}{\partial t}",   # [1] time deriv
            r"+ (\mathbf{u} \cdot \nabla)\mathbf{u}\right)",     # [2] convection
            r"= -\nabla p",                              # [3] pressure
            r"+ \mu \nabla^2 \mathbf{u}",               # [4] viscosity
            r"+ \mathbf{f}",                             # [5] external
            font_size=44,
        )
        ns_eq.next_to(eq_head, DOWN, buff=0.42)
        colors = [C_GREY, C_CYAN, TEAL_C, C_RED, C_ORANGE, C_GREEN]
        for i, c in enumerate(colors):
            ns_eq[i].set_color(ManimColor(c))

        self.add_fixed_in_frame_mobjects(ns_eq)
        self.play(Write(ns_eq), run_time=3.2)
        self.wait(0.6)

        # ── helper: build a pill card ────────────────────────────────────
        def ann_card(symbol_str, meaning_str, col):
            sym  = Text(symbol_str,  font_size=19, color=ManimColor(col), weight=BOLD)
            mean = Text(meaning_str, font_size=16, color=C_GREY)
            inner = VGroup(sym, mean).arrange(DOWN, buff=0.08, aligned_edge=LEFT)
            bg = RoundedRectangle(
                corner_radius=0.14,
                width=inner.width + 0.40,
                height=inner.height + 0.28,
                fill_color=ManimColor(col), fill_opacity=0.12,
                stroke_color=ManimColor(col), stroke_width=1.4,
            )
            bg.move_to(inner)
            return VGroup(bg, inner)

        # ── 6 cards: left column (3) and right column (3) ───────────────
        data = [
            ("ρ  — density",          "mass per unit volume\nof the fluid",    C_GREY),
            ("∂u/∂t  — acceleration", "how velocity changes\nover time",       C_CYAN),
            ("(u·∇)u  — convection",  "fluid carrying\nits own momentum",      TEAL_C),
            ("−∇p  — pressure",       "flow from high\nto low pressure",       C_RED),
            ("μ∇²u  — viscosity",     "internal friction\nthat smooths flow",  C_ORANGE),
            ("f  — body forces",      "gravity, pumps, wind\nacting on fluid",  C_GREEN),
        ]

        left_cards  = VGroup(*[ann_card(*d) for d in data[:3]])
        right_cards = VGroup(*[ann_card(*d) for d in data[3:]])

        left_cards.arrange(DOWN,  buff=0.18, aligned_edge=LEFT)
        right_cards.arrange(DOWN, buff=0.18, aligned_edge=LEFT)

        cols = VGroup(left_cards, right_cards).arrange(RIGHT, buff=0.55)
        # Push cards to the BOTTOM of the screen so the dashed connectors
        # span a large gap from the equation — making them read as pointers
        cols.to_edge(DOWN, buff=0.18)
        cols.center()

        cols.to_edge(DOWN, buff=0.30)
        cols.center()

        # Reveal each card one by one — no pointers, no separator
        all_cards = [left_cards[0], left_cards[1], left_cards[2],
                     right_cards[0], right_cards[1], right_cards[2]]

        for card in all_cards:
            self.add_fixed_in_frame_mobjects(card)
            self.play(FadeIn(card, shift=UP * 0.12), run_time=0.42)

        self.wait(4.2)

        self.play(
            FadeOut(ns_eq), FadeOut(cols), FadeOut(eq_head),
            run_time=0.9,
        )
        self.remove(ns_eq, cols, eq_head)

        # ══════════════════════════════════════════════════════════════════
        # PART 8 — CLOSING CARD
        # ══════════════════════════════════════════════════════════════════
        finale = Text("Why does it matter?",
                      font_size=38, color=C_CYAN, weight=BOLD)
        finale.to_edge(UP, buff=0.7)
        self.add_fixed_in_frame_mobjects(finale)
        self.play(FadeIn(finale, shift=DOWN * 0.2), run_time=0.8)

        facts = VGroup(
            Text("  Aircraft wing design — lift and drag",        font_size=21, color=C_GREY),
            Text("  Ocean current modelling — climate science",   font_size=21, color=C_GREY),
            Text("  Blood flow through arteries — medical devices", font_size=21, color=C_GREY),
            Text("  Weather forecasting — every storm prediction", font_size=21, color=C_GREY),
            Text("  Real-time fluid simulations in games & VFX",  font_size=21, color=C_GREY),
        )
        facts.arrange(DOWN, buff=0.38, aligned_edge=LEFT)
        facts.next_to(finale, DOWN, buff=0.55)
        facts.center()

        divider = Line(LEFT * 3.5, RIGHT * 3.5,
                       color=ManimColor("#222244"), stroke_width=1)
        divider.next_to(facts, DOWN, buff=0.38)

        unsolved = Text(
            "Proving smooth solutions always exist is a\n"
            "Millennium Prize Problem — worth $1,000,000 — still unsolved.",
            font_size=19, color=C_YELLOW, weight=BOLD,
        )
        unsolved.next_to(divider, DOWN, buff=0.32)

        for f_mob in facts:
            self.add_fixed_in_frame_mobjects(f_mob)
            self.play(FadeIn(f_mob, shift=RIGHT * 0.15), run_time=0.42)

        self.add_fixed_in_frame_mobjects(divider)
        self.play(FadeIn(divider), run_time=0.4)
        self.add_fixed_in_frame_mobjects(unsolved)
        self.play(FadeIn(unsolved, shift=UP * 0.12), run_time=0.9)
        self.wait(6.0)

        self.play(
            FadeOut(finale), FadeOut(facts),
            FadeOut(divider), FadeOut(unsolved),
            run_time=1.2,
        )