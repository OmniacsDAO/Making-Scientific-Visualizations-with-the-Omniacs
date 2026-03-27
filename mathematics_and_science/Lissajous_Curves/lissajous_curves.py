"""
Lissajous Curves -- Complete Manim Visualization
================================================
Structure:
  1. Title card
  2. Concept introduction
  3. Formula reveal with parameter annotations
  4. Parameter exploration (a:b ratio, phase shift)
  5. Full 3x3 frequency ratio grid
  6. Animated curve demo with tracer dot
  7. Use cases showcase
  8. Hilbert-style rotating finale + outro

Run:
    manim -qh lissajous_curves.py LissajousCurves
"""

from manim import *
import numpy as np


# ---------------------------------------------------------------------------
# Global Style
# ---------------------------------------------------------------------------
BACKGROUND_COLOR = "#000000"
TITLE_COLOR      = "#00BFFF"   # Deep Sky Blue
FORMULA_COLOR    = "#FFD700"   # Gold
CAPTION_COLOR    = "#FFFFFF"   # White
ACCENT_COLOR     = "#FF4500"   # Orange Red
SUBTITLE_COLOR   = "#AAAAAA"   # Soft grey

CURVE_PALETTE = [
    "#FF4500",  # Red-Orange
    "#00BFFF",  # Sky Blue
    "#7CFC00",  # Lawn Green
    "#FFD700",  # Gold
    "#FF69B4",  # Hot Pink
    "#DA70D6",  # Orchid
    "#00CED1",  # Dark Turquoise
    "#FF8C00",  # Dark Orange
    "#ADFF2F",  # Green-Yellow
]


# ---------------------------------------------------------------------------
# Helper functions
# ---------------------------------------------------------------------------
def lissajous_points(a, b, delta, num_points=2000, cycles=2):
    """Generate (x, y) arrays for a Lissajous curve."""
    t = np.linspace(0, cycles * np.pi, num_points)
    x = np.sin(a * t + delta)
    y = np.sin(b * t)
    return x, y


def make_lissajous_vmobject(a, b, delta, color, stroke_width=3, cycles=2, scale=2.5):
    """Return a smooth VMobject tracing the Lissajous curve."""
    x, y = lissajous_points(a, b, delta, num_points=2000, cycles=cycles)
    points = [np.array([xi * scale, yi * scale, 0]) for xi, yi in zip(x, y)]
    curve = VMobject(color=color, stroke_width=stroke_width)
    curve.set_points_smoothly(points)
    return curve


# ---------------------------------------------------------------------------
# Main Scene
# ---------------------------------------------------------------------------
class LissajousCurves(Scene):

    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR
        self._title_card()
        self._concept_intro()
        self._formula_reveal()
        self._parameter_exploration()
        self._full_grid()
        self._animated_curve_demo()
        self._use_cases()
        self._outro()

    # -----------------------------------------------------------------------
    # 1. Title Card
    # -----------------------------------------------------------------------
    def _title_card(self):
        title = Text("Lissajous Curves", font_size=64, color=TITLE_COLOR, weight=BOLD)
        subtitle = Text("Two oscillations. Infinite beauty.", font_size=28, color=SUBTITLE_COLOR)
        subtitle.next_to(title, DOWN, buff=0.4)
        self.play(Write(title), run_time=2)
        self.play(FadeIn(subtitle, shift=UP * 0.3), run_time=1)
        self.wait(1.5)
        self.play(FadeOut(title), FadeOut(subtitle), run_time=1)

    # -----------------------------------------------------------------------
    # 2. Concept Introduction
    # -----------------------------------------------------------------------
    def _concept_intro(self):
        heading = Text("What are Lissajous Curves?", font_size=40, color=TITLE_COLOR)
        heading.to_edge(UP, buff=0.5)

        lines = [
            "Named after Jules Antoine Lissajous (1857)",
            "Formed by combining two perpendicular oscillations",
            "The shape encodes the ratio of their frequencies",
            "Simple rules -- endlessly complex patterns",
        ]
        line_objects = VGroup(*[
            Text(l, font_size=26, color=CAPTION_COLOR) for l in lines
        ]).arrange(DOWN, aligned_edge=LEFT, buff=0.45)
        line_objects.next_to(heading, DOWN, buff=0.6)
        line_objects.to_edge(LEFT, buff=1.0)

        preview = make_lissajous_vmobject(3, 2, np.pi / 4, color=CURVE_PALETTE[3], stroke_width=4)
        preview.scale(0.65).to_edge(RIGHT, buff=1.0)

        self.play(Write(heading), run_time=1.2)
        self.play(Create(preview), run_time=3)
        for line in line_objects:
            self.play(FadeIn(line, shift=RIGHT * 0.2), run_time=0.6)
        self.wait(1.5)
        self.play(FadeOut(VGroup(heading, line_objects, preview)), run_time=1)

    # -----------------------------------------------------------------------
    # 3. Formula Reveal
    # -----------------------------------------------------------------------
    def _formula_reveal(self):
        heading = Text("The Parametric Formula", font_size=40, color=TITLE_COLOR)
        heading.to_edge(UP, buff=0.5)
        self.play(Write(heading), run_time=1)

        formula = MathTex(
            r"x(t) = A \sin(at + \delta)",
            r"\qquad",
            r"y(t) = B \sin(bt)",
            font_size=46, color=FORMULA_COLOR
        )
        formula.move_to(ORIGIN + UP * 1.5)
        self.play(Write(formula), run_time=2.5)
        self.wait(0.5)

        param_data = [
            (r"A,\, B", "Amplitudes  --  set width and height of the figure"),
            (r"a,\, b", "Frequencies  --  control the number of loops"),
            (r"\delta", "Phase shift  --  rotates and tilts the curve"),
            (r"t",      "Time, ranging from 0 to 2 pi"),
        ]

        param_group = VGroup()
        for i, (sym, desc) in enumerate(param_data):
            sym_tex  = MathTex(sym, font_size=34, color=ACCENT_COLOR)
            dash     = Text("  --  ", font_size=26, color=SUBTITLE_COLOR)
            desc_tex = Text(desc, font_size=24, color=CAPTION_COLOR)
            row = VGroup(sym_tex, dash, desc_tex).arrange(RIGHT, buff=0.15)
            row.to_edge(LEFT, buff=1.2)
            row.shift(DOWN * (0.5 + i * 0.7))
            param_group.add(row)

        for row in param_group:
            self.play(FadeIn(row, shift=RIGHT * 0.15), run_time=0.55)
        self.wait(2)
        self.play(FadeOut(VGroup(heading, formula, param_group)), run_time=1)

    # -----------------------------------------------------------------------
    # 4. Parameter Exploration
    # -----------------------------------------------------------------------
    def _parameter_exploration(self):
        heading = Text("How Parameters Shape the Curve", font_size=40, color=TITLE_COLOR)
        heading.to_edge(UP, buff=0.5)
        self.play(Write(heading), run_time=1)

        configs = [
            (1, 1, 0,           CURVE_PALETTE[0], "a:b = 1:1   delta = 0     diagonal line"),
            (1, 1, np.pi / 2,   CURVE_PALETTE[1], "a:b = 1:1   delta = pi/2  circle"),
            (1, 2, np.pi / 2,   CURVE_PALETTE[2], "a:b = 1:2   delta = pi/2  figure-8"),
            (3, 2, np.pi / 4,   CURVE_PALETTE[3], "a:b = 3:2   delta = pi/4  pretzel"),
            (5, 4, np.pi / 4,   CURVE_PALETTE[4], "a:b = 5:4   delta = pi/4  intricate web"),
        ]

        axes = Axes(
            x_range=[-1.2, 1.2, 0.5], y_range=[-1.2, 1.2, 0.5],
            x_length=5, y_length=5,
            axis_config={"color": SUBTITLE_COLOR, "stroke_width": 1, "include_tip": False},
        ).move_to(ORIGIN + RIGHT * 1.8)
        self.play(Create(axes), run_time=0.8)

        current_curve = None
        current_cap   = None
        current_lbl   = None
        fit = axes.x_length / 2 / 2.5

        for a, b, delta, color, cap_text in configs:
            curve = make_lissajous_vmobject(a, b, delta, color, stroke_width=3.5, cycles=2)
            curve.scale(fit)
            curve.move_to(axes.get_center())

            cap = Text(cap_text, font_size=24, color=CAPTION_COLOR)
            cap.to_edge(LEFT, buff=0.6).shift(DOWN * 0.3)

            lbl = MathTex(r"a=" + str(a) + r",\; b=" + str(b), font_size=30, color=FORMULA_COLOR)
            lbl.next_to(axes, DOWN, buff=0.4)

            fade_outs = []
            if current_curve:
                fade_outs.append(FadeOut(current_curve))
            if current_cap:
                fade_outs.append(FadeOut(current_cap))
            if current_lbl:
                fade_outs.append(FadeOut(current_lbl))
            if fade_outs:
                self.play(*fade_outs, run_time=0.4)

            self.play(Create(curve), run_time=2)
            self.play(FadeIn(cap, shift=UP * 0.1), Write(lbl), run_time=0.7)
            self.wait(1.2)

            current_curve = curve
            current_cap   = cap
            current_lbl   = lbl

        self.play(FadeOut(VGroup(heading, axes, current_curve, current_cap, current_lbl)), run_time=1)

    # -----------------------------------------------------------------------
    # 5. Full 3x3 Frequency Ratio Grid
    # -----------------------------------------------------------------------
    def _full_grid(self):
        heading = Text("Frequency Ratio Matrix", font_size=40, color=TITLE_COLOR)
        heading.to_edge(UP, buff=0.4)
        self.play(Write(heading), run_time=1)

        ratios = [
            (1, 1, 0),          (1, 2, np.pi / 2),  (1, 3, np.pi / 4),
            (2, 1, 0),          (2, 3, np.pi / 4),  (2, 5, np.pi / 4),
            (3, 1, 0),          (3, 2, np.pi / 4),  (3, 4, np.pi / 4),
        ]

        grid = VGroup()
        for idx, (a, b, delta) in enumerate(ratios):
            color = CURVE_PALETTE[idx % len(CURVE_PALETTE)]
            c = make_lissajous_vmobject(a, b, delta, color, stroke_width=2.5, cycles=4)
            c.scale(0.36)
            label = MathTex(str(a) + ":" + str(b), font_size=20, color=SUBTITLE_COLOR)
            label.next_to(c, DOWN, buff=0.08)
            cell = VGroup(c, label)
            grid.add(cell)

        grid.arrange_in_grid(rows=3, cols=3, buff=0.5)
        grid.next_to(heading, DOWN, buff=0.45)

        self.play(
            LaggedStart(*[Create(grid[i][0]) for i in range(9)], lag_ratio=0.15, run_time=6),
            LaggedStart(*[FadeIn(grid[i][1]) for i in range(9)], lag_ratio=0.15, run_time=3),
        )
        self.wait(2)

        caption = Text("Rational ratios a:b always produce closed, repeating curves",
                       font_size=23, color=CAPTION_COLOR)
        caption.to_edge(DOWN, buff=0.4)
        self.play(FadeIn(caption, shift=UP * 0.2), run_time=0.8)
        self.wait(2)
        self.play(FadeOut(VGroup(heading, grid, caption)), run_time=1)

    # -----------------------------------------------------------------------
    # 6. Animated Curve Demo with Tracer Dot
    # -----------------------------------------------------------------------
    def _animated_curve_demo(self):
        heading = Text("Watch It Trace", font_size=40, color=TITLE_COLOR)
        heading.to_edge(UP, buff=0.5)
        self.play(Write(heading), run_time=1)

        caption = Text(
            "Two sine waves  --  one horizontal, one vertical  --  draw the curve in real time",
            font_size=23, color=CAPTION_COLOR
        )
        caption.to_edge(DOWN, buff=0.5)
        self.play(FadeIn(caption, shift=UP * 0.15), run_time=0.7)

        a, b, delta = 3, 2, np.pi / 4
        color = CURVE_PALETTE[3]

        axes = Axes(
            x_range=[-1.2, 1.2, 0.5], y_range=[-1.2, 1.2, 0.5],
            x_length=5.5, y_length=5.5,
            axis_config={"color": SUBTITLE_COLOR, "stroke_width": 1, "include_tip": False},
        ).move_to(ORIGIN + DOWN * 0.3)

        param_label = MathTex(r"a=3,\; b=2,\; \delta=\tfrac{\pi}{4}",
                               font_size=30, color=FORMULA_COLOR)
        param_label.next_to(axes, RIGHT, buff=0.4).shift(UP * 1.5)

        self.play(Create(axes), Write(param_label), run_time=1)

        fit = axes.x_length / 2 / 2.5
        full_curve = make_lissajous_vmobject(a, b, delta, color, stroke_width=3.5, cycles=2)
        full_curve.scale(fit)
        full_curve.move_to(axes.get_center())

        self.play(Create(full_curve), run_time=4, rate_func=linear)
        self.wait(1)

        tracer = Dot(color=WHITE, radius=0.1)
        tracer.move_to(full_curve.get_start())
        self.play(FadeIn(tracer), run_time=0.3)
        self.play(MoveAlongPath(tracer, full_curve), run_time=3, rate_func=linear)
        self.play(FadeOut(tracer), run_time=0.3)
        self.wait(1)

        self.play(FadeOut(VGroup(heading, caption, axes, param_label, full_curve)), run_time=1)

    # -----------------------------------------------------------------------
    # 7. Use Cases
    # -----------------------------------------------------------------------
    def _use_cases(self):
        heading = Text("Real-World Applications", font_size=40, color=TITLE_COLOR)
        heading.to_edge(UP, buff=0.5)
        self.play(Write(heading), run_time=1)

        use_cases = [
            ("Oscilloscopes",     "Measure frequency ratios and phase differences in signals"),
            ("Music & Acoustics", "Visually tune instruments by comparing signal frequencies"),
            ("Power Grids",       "Detect voltage sags, swells, and harmonics in microgrids"),
            ("Drone Search",      "Irrational ratios create optimal area-coverage flight paths"),
            ("Space Orbits",      "Spacecraft follow Lissajous paths near Lagrange points"),
            ("Art & Design",      "Harmonographs draw Lissajous art with coupled pendulums"),
        ]
        mini_configs = [
            (1, 1, np.pi / 2),
            (1, 2, np.pi / 2),
            (2, 3, np.pi / 4),
            (3, 4, np.pi / 4),
            (4, 5, np.pi / 4),
            (5, 4, np.pi / 3),
        ]

        rows = VGroup()
        for i, ((title, desc), (a, b, d)) in enumerate(zip(use_cases, mini_configs)):
            mini = make_lissajous_vmobject(a, b, d, CURVE_PALETTE[i], stroke_width=2.0, cycles=2)
            mini.scale(0.22)
            title_t = Text(title, font_size=24, color=ACCENT_COLOR, weight=BOLD)
            desc_t  = Text(desc,  font_size=20, color=CAPTION_COLOR)
            text_col = VGroup(title_t, desc_t).arrange(DOWN, aligned_edge=LEFT, buff=0.05)
            row = VGroup(mini, text_col).arrange(RIGHT, buff=0.3, aligned_edge=UP)
            rows.add(row)

        rows.arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        rows.next_to(heading, DOWN, buff=0.45)
        rows.to_edge(LEFT, buff=0.8)

        for row in rows:
            self.play(Create(row[0]), FadeIn(row[1], shift=RIGHT * 0.15), run_time=0.7)
        self.wait(2.5)
        self.play(FadeOut(VGroup(heading, rows)), run_time=1)

    # -----------------------------------------------------------------------
    # 8. Hilbert-Style Finale + Outro
    # -----------------------------------------------------------------------
    def _outro(self):
        finale_configs = [
            (1, 2, 0),
            (2, 3, np.pi / 4),
            (3, 4, np.pi / 4),
            (4, 5, np.pi / 4),
            (5, 6, np.pi / 4),
        ]
        curves = VGroup()
        for i, (a, b, d) in enumerate(finale_configs):
            c = make_lissajous_vmobject(
                a, b, d, CURVE_PALETTE[i],
                stroke_width=max(2.5 - i * 0.3, 1.0),
                cycles=4
            )
            c.scale(0.9 - i * 0.07)
            c.move_to(ORIGIN)
            curves.add(c)

        self.play(LaggedStart(*[Create(c) for c in curves], lag_ratio=0.3, run_time=4))
        self.wait(0.5)

        self.play(*[
            Rotate(
                curves[i],
                angle=(1 if i % 2 == 0 else -1) * TAU,
                rate_func=smooth,
                run_time=4 + i * 0.5
            )
            for i in range(len(curves))
        ])
        self.wait(0.5)

        outro_text = Text("Lissajous Curves", font_size=52, color=TITLE_COLOR, weight=BOLD)
        tag = Text("OmniacsDAO  |  $IACS  |  Base Chain", font_size=22, color=SUBTITLE_COLOR)
        tag.next_to(outro_text, DOWN, buff=0.4)

        self.play(FadeOut(curves, run_time=1.5), Write(outro_text, run_time=1.5))
        self.play(FadeIn(tag, shift=UP * 0.2), run_time=1)
        self.wait(2)
        self.play(FadeOut(VGroup(outro_text, tag)), run_time=1.5)
