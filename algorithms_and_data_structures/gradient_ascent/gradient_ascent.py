from manim import *
import numpy as np


class GradientAscent(ThreeDScene):
    def construct(self):
        self.camera.background_color = "#0a0a0f"

        # ── helpers ────────────────────────────────────────────────────────
        def f(x, y):
            return (
                1.5 * np.exp(-((x - 1) ** 2 + (y - 1) ** 2) / 0.8)
                + np.exp(-((x + 1.5) ** 2 + (y + 0.5) ** 2) / 0.5)
                + 0.8 * np.exp(-((x - 0.5) ** 2 + (y + 1.5) ** 2) / 0.6)
            )

        def grad_f(x, y):
            eps = 1e-4
            gx = (f(x + eps, y) - f(x - eps, y)) / (2 * eps)
            gy = (f(x, y + eps) - f(x, y - eps)) / (2 * eps)
            return np.array([gx, gy])

        def ascent_path(x0, y0, lr=0.15, steps=40):
            path = [(x0, y0)]
            x, y = x0, y0
            for _ in range(steps):
                g = grad_f(x, y)
                norm = np.linalg.norm(g)
                if norm < 1e-6:
                    break
                x += lr * g[0]
                y += lr * g[1]
                x = np.clip(x, -2.8, 2.8)
                y = np.clip(y, -2.8, 2.8)
                path.append((x, y))
            return path

        # ── PART 1: Title ──────────────────────────────────────────────────
        title = Text("Gradient Ascent", font_size=52, color="#00e5ff", weight=BOLD)
        rule = Line(title.get_left(), title.get_right(), color="#ffdd00", stroke_width=2)
        rule.next_to(title, DOWN, buff=0.18)

        # Show title + rule, let them breathe, then fade out cleanly
        self.play(Write(title), run_time=1.8)
        self.play(Create(rule), run_time=0.6)
        self.wait(1.2)
        self.play(FadeOut(title), FadeOut(rule), run_time=0.7)
        self.wait(0.3)

        # Plain-English explanation lines revealed one at a time on clear screen
        line_a = Text(
            "Imagine you are blindfolded on a hilly landscape.",
            font_size=22, color="#aaaacc",
        )
        line_b = Text(
            "You can't see the peaks — but you can feel which way the ground rises.",
            font_size=22, color="#aaaacc",
        )
        line_c = Text(
            "Gradient Ascent: always step uphill until you reach a peak.",
            font_size=22, color="#ffdd00", weight=BOLD,
        )
        line_d = Text(
            "Used in machine learning, optimisation, and physics simulations.",
            font_size=19, color="#666688",
        )
        explanation = VGroup(line_a, line_b, line_c, line_d)
        explanation.arrange(DOWN, buff=0.38, aligned_edge=LEFT)
        explanation.center()
        explanation.shift(DOWN * 0.3)

        for line in explanation:
            self.play(FadeIn(line, shift=UP * 0.15), run_time=0.75)
        self.wait(2.0)
        self.play(*[FadeOut(ln) for ln in explanation])

        # ── PART 2: The math ───────────────────────────────────────────────
        eq_title = Text("The Idea", font_size=34, color="#00e5ff", weight=BOLD)
        eq_title.to_edge(UP, buff=0.6)

        eq1 = MathTex(
            r"\nabla f(x,y) = \left(\frac{\partial f}{\partial x},\, \frac{\partial f}{\partial y}\right)",
            font_size=38,
            color="#ffdd00",
        )
        eq2 = MathTex(
            r"\mathbf{x}_{n+1} = \mathbf{x}_n + \alpha \,\nabla f(\mathbf{x}_n)",
            font_size=38,
            color="#ff9944",
        )
        note = Text(
            "alpha is the learning rate — controls how big each step is",
            font_size=20,
            color="#aaaacc",
        )

        eq1.move_to(UP * 0.8)
        eq2.next_to(eq1, DOWN, buff=0.7)
        note.next_to(eq2, DOWN, buff=0.5)

        self.play(FadeIn(eq_title))
        self.play(Write(eq1), run_time=2)
        self.play(Write(eq2), run_time=2)
        self.play(FadeIn(note), run_time=0.8)
        self.wait(2)
        self.play(FadeOut(eq_title), FadeOut(eq1), FadeOut(eq2), FadeOut(note))

        # ── PART 3: 3D Surface ─────────────────────────────────────────────
        self.set_camera_orientation(phi=55 * DEGREES, theta=-50 * DEGREES)

        surf_label = Text("Our landscape  f(x, y)", font_size=26, color="#00e5ff")
        surf_label.to_edge(UP, buff=0.7)
        self.add_fixed_in_frame_mobjects(surf_label)
        self.play(FadeIn(surf_label))

        surface = Surface(
            lambda u, v: np.array([u, v, f(u, v) * 1.8]),
            u_range=[-3, 3],
            v_range=[-3, 3],
            resolution=(40, 40),
            fill_opacity=0.75,
        )
        surface.set_color_by_gradient(BLUE, TEAL, GREEN, YELLOW, ORANGE, RED)

        self.play(Create(surface), run_time=3)
        self.begin_ambient_camera_rotation(rate=0.18)
        self.wait(3)
        self.stop_ambient_camera_rotation()

        note2 = Text(
            "Multiple peaks — gradient ascent finds the nearest one",
            font_size=20, color="#aaaacc",
        )
        note2.to_edge(DOWN, buff=0.5)
        self.add_fixed_in_frame_mobjects(note2)
        self.play(FadeIn(note2))
        self.wait(2)
        self.play(FadeOut(surf_label), FadeOut(note2), FadeOut(surface))

        # ── PART 4: Contour map ────────────────────────────────────────────
        self.set_camera_orientation(phi=0, theta=-PI / 2)

        contour_title = Text("Top-down view: contour map", font_size=26, color="#00e5ff")
        contour_title.to_edge(UP, buff=0.7)
        self.add_fixed_in_frame_mobjects(contour_title)
        self.play(FadeIn(contour_title))

        grid = NumberPlane(
            x_range=[-3, 3, 1],
            y_range=[-3, 3, 1],
            background_line_style={"stroke_color": "#222244", "stroke_width": 1},
        ).scale(0.85)
        self.add_fixed_in_frame_mobjects(grid)
        self.play(Create(grid), run_time=1.5)

        levels = [0.3, 0.6, 0.9, 1.2, 1.45]
        colors = ["#003366", "#005599", "#0088cc", "#00bbee", "#00e5ff"]
        contours = VGroup()
        for level, col in zip(levels, colors):
            pts = []
            for angle in np.linspace(0, TAU, 120):
                for r in np.linspace(0.05, 2.5, 60):
                    x = r * np.cos(angle)
                    y = r * np.sin(angle)
                    if abs(f(x, y) - level) < 0.06:
                        pts.append(grid.c2p(x, y, 0))
            if pts:
                dots = VGroup(*[Dot(p, radius=0.012, color=col) for p in pts])
                contours.add(dots)

        self.add_fixed_in_frame_mobjects(contours)
        self.play(FadeIn(contours), run_time=2)

        dot_a = Dot(grid.c2p(-2, -2, 0), color="#ff4488", radius=0.13)
        dot_b = Dot(grid.c2p(2, -1.5, 0), color="#44ff88", radius=0.13)
        label_a = Text("Start A", font_size=16, color="#ff4488").next_to(dot_a, UP, buff=0.1)
        label_b = Text("Start B", font_size=16, color="#44ff88").next_to(dot_b, UP, buff=0.1)

        self.add_fixed_in_frame_mobjects(dot_a, dot_b, label_a, label_b)
        self.play(FadeIn(dot_a), FadeIn(dot_b), FadeIn(label_a), FadeIn(label_b))
        self.wait(1)
        self.play(
            FadeOut(contour_title), FadeOut(grid), FadeOut(contours),
            FadeOut(dot_a), FadeOut(dot_b), FadeOut(label_a), FadeOut(label_b),
        )

        # ── PART 5: Animated ascent on 3D surface ──────────────────────────
        self.set_camera_orientation(phi=55 * DEGREES, theta=-50 * DEGREES)

        surface2 = Surface(
            lambda u, v: np.array([u, v, f(u, v) * 1.8]),
            u_range=[-3, 3],
            v_range=[-3, 3],
            resolution=(40, 40),
            fill_opacity=0.6,
        )
        surface2.set_color_by_gradient(BLUE, TEAL, GREEN, YELLOW, ORANGE, RED)
        self.play(Create(surface2), run_time=2)

        ascent_label = Text("Climbing the surface...", font_size=24, color="#00e5ff")
        ascent_label.to_edge(UP, buff=0.7)
        self.add_fixed_in_frame_mobjects(ascent_label)
        self.play(FadeIn(ascent_label))

        path_a = ascent_path(-2, -2, lr=0.2, steps=35)
        path_b = ascent_path(2, -1.5, lr=0.2, steps=35)

        def make_3d_dot(x, y, color):
            return Dot3D(
                point=np.array([x, y, f(x, y) * 1.8 + 0.05]),
                color=color,
                radius=0.1,
            )

        dot3a = make_3d_dot(*path_a[0], "#ff4488")
        dot3b = make_3d_dot(*path_b[0], "#44ff88")
        self.play(FadeIn(dot3a), FadeIn(dot3b))

        self.begin_ambient_camera_rotation(rate=0.12)

        trail_a   = VGroup()
        trail_b   = VGroup()
        arrows_all = VGroup()   # ← collects every gradient arrow

        max_steps = max(len(path_a), len(path_b))
        for i in range(1, max_steps):
            anims = []

            if i < len(path_a):
                x0a, y0a = path_a[i - 1]
                x1a, y1a = path_a[i]
                seg_a = Line3D(
                    start=np.array([x0a, y0a, f(x0a, y0a) * 1.8 + 0.05]),
                    end=np.array([x1a, y1a, f(x1a, y1a) * 1.8 + 0.05]),
                    color="#ff4488",
                    thickness=0.025,
                )
                trail_a.add(seg_a)
                new_dot_a = make_3d_dot(x1a, y1a, "#ff4488")
                anims += [Create(seg_a), Transform(dot3a, new_dot_a)]

                g  = grad_f(x0a, y0a)
                gn = g / (np.linalg.norm(g) + 1e-8) * 0.4
                arrow_a = Arrow3D(
                    start=np.array([x0a, y0a, f(x0a, y0a) * 1.8 + 0.08]),
                    end=np.array([x0a + gn[0], y0a + gn[1], f(x0a, y0a) * 1.8 + 0.08]),
                    color="#ffdd00",
                    thickness=0.018,
                )
                arrows_all.add(arrow_a)          # ← track it
                anims.append(FadeIn(arrow_a))

            if i < len(path_b):
                x0b, y0b = path_b[i - 1]
                x1b, y1b = path_b[i]
                seg_b = Line3D(
                    start=np.array([x0b, y0b, f(x0b, y0b) * 1.8 + 0.05]),
                    end=np.array([x1b, y1b, f(x1b, y1b) * 1.8 + 0.05]),
                    color="#44ff88",
                    thickness=0.025,
                )
                trail_b.add(seg_b)
                new_dot_b = make_3d_dot(x1b, y1b, "#44ff88")
                anims += [Create(seg_b), Transform(dot3b, new_dot_b)]

                g  = grad_f(x0b, y0b)
                gn = g / (np.linalg.norm(g) + 1e-8) * 0.4
                arrow_b = Arrow3D(
                    start=np.array([x0b, y0b, f(x0b, y0b) * 1.8 + 0.08]),
                    end=np.array([x0b + gn[0], y0b + gn[1], f(x0b, y0b) * 1.8 + 0.08]),
                    color="#ffdd00",
                    thickness=0.018,
                )
                arrows_all.add(arrow_b)          # ← track it
                anims.append(FadeIn(arrow_b))

            if anims:
                self.play(*anims, run_time=0.18)

        self.wait(2)
        self.stop_ambient_camera_rotation()

        converged = Text(
            "Both paths converged to a local maximum!",
            font_size=22, color="#ffdd00",
        )
        converged.to_edge(DOWN, buff=0.5)
        self.add_fixed_in_frame_mobjects(converged)
        self.play(FadeIn(converged))
        self.wait(2)

        # ← FadeOut everything including ALL arrows via arrows_all
        self.play(
            FadeOut(surface2),
            FadeOut(trail_a),
            FadeOut(trail_b),
            FadeOut(dot3a),
            FadeOut(dot3b),
            FadeOut(ascent_label),
            FadeOut(converged),
            FadeOut(arrows_all),
        )

        # ── PART 6: Closing — learning rate effects ────────────────────────
        self.set_camera_orientation(phi=0, theta=-PI / 2)

        close_title = Text(
            "Learning Rate Matters",
            font_size=34, color="#00e5ff", weight=BOLD,
        )
        close_title.to_edge(UP, buff=0.7)

        row1 = Text("Too small   →  tiny steps, very slow to converge",   font_size=22, color="#aaaacc")
        row2 = Text("Too large   →  overshoots, may diverge or oscillate", font_size=22, color="#ff6666")
        row3 = Text("Just right  →  smooth, confident climb to the peak",  font_size=22, color="#44ff88")

        rows = VGroup(row1, row2, row3)
        rows.arrange(DOWN, buff=0.5, aligned_edge=LEFT)
        rows.move_to(ORIGIN + DOWN * 0.3)

        closing = Text(
            "Gradient ascent: follow the slope, reach the top.",
            font_size=20, color="#ffdd00",
        )
        closing.next_to(rows, DOWN, buff=0.7)

        # Register and reveal title first — nothing else added yet
        self.add_fixed_in_frame_mobjects(close_title)
        self.play(FadeIn(close_title))

        # Register and reveal each row individually — no pre-flash
        self.add_fixed_in_frame_mobjects(row1)
        self.play(FadeIn(row1, shift=RIGHT * 0.2), run_time=0.7)

        self.add_fixed_in_frame_mobjects(row2)
        self.play(FadeIn(row2, shift=RIGHT * 0.2), run_time=0.7)

        self.add_fixed_in_frame_mobjects(row3)
        self.play(FadeIn(row3, shift=RIGHT * 0.2), run_time=0.7)

        self.add_fixed_in_frame_mobjects(closing)
        self.play(FadeIn(closing), run_time=1)

        self.wait(3)
        self.play(
            FadeOut(close_title),
            FadeOut(row1), FadeOut(row2), FadeOut(row3),
            FadeOut(closing),
        )
