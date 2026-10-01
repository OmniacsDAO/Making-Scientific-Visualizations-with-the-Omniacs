from manim import *
import numpy as np

# -----------------------------------------------------------------------------
# Probability-First AI: The Open Research That Resembles JEV
# Omniacs.DAO / Making Scientific Visualizations with the Omniacs
#
# Target runtime: ~3 minutes at PACING = 1.0
# Quick preview: set PACING = 0.18
# Render:
#   manim -pql JEV_Probability_First_AI.py ProbabilityFirstAI
#   manim -pqh JEV_Probability_First_AI.py ProbabilityFirstAI
# -----------------------------------------------------------------------------

PACING = 1.0
BG = "#07111A"
PANEL = "#0B1824"
CYAN = "#20D5E8"
BLUE2 = "#4C8DFF"
TEAL2 = "#25C7A5"
YELLOW2 = "#FFD166"
ORANGE2 = "#FF8C42"
RED2 = "#FF5C6C"
PURPLE2 = "#B388FF"
GREEN2 = "#7BE495"
GREY2 = "#93A4B7"

config.background_color = BG


class ProbabilityFirstAI(Scene):
    """A ~3-minute explainer of open 2025 research that resembles JEV's
    publicly described probability-first / confidence-aware design pattern.

    Important framing:
      * SalesRLAgent and Confidence-Aware Routing are open 2025 preprints.
      * TypeSafe publicly introduced Jev in September 2026.
      * Architectural resemblance is observable from public descriptions.
      * Shared code, direct lineage, or copying is NOT established here.
    """

    # ------------------------- pacing / scene utilities ----------------------
    def rt(self, seconds):
        return max(0.05, seconds * PACING)

    def hold(self, seconds):
        self.wait(self.rt(seconds))

    def clear_scene(self, seconds=1.25):
        if self.mobjects:
            self.play(
                *[FadeOut(mob) for mob in list(self.mobjects)],
                run_time=self.rt(seconds),
                rate_func=smooth,
            )

    def create_background_grid(self):
        grid = VGroup()
        for i in np.arange(-8, 9, 1):
            grid.add(
                Line(
                    LEFT * 8 + UP * i,
                    RIGHT * 8 + UP * i,
                    stroke_width=0.5,
                    stroke_opacity=0.16,
                    color=BLUE_D,
                ),
                Line(
                    LEFT * i + UP * 4.5,
                    LEFT * i + DOWN * 4.5,
                    stroke_width=0.5,
                    stroke_opacity=0.16,
                    color=BLUE_D,
                ),
            )
        return grid

    def source_tag(self, text):
        tag = Text(text, font_size=13, color=GREY2)
        tag.to_corner(DR, buff=0.22)
        return tag

    def header(self, title, subtitle=None, color=CYAN):
        h = Text(title, font_size=34, color=color, weight=BOLD)
        h.to_edge(UP, buff=0.32)
        if subtitle:
            s = Text(subtitle, font_size=18, color=GREY_B)
            s.next_to(h, DOWN, buff=0.10)
            return VGroup(h, s)
        return VGroup(h)

    def panel(self, title, body=None, color=CYAN, width=3.5, height=2.0,
              title_size=23, body_size=16, fill_opacity=0.38):
        box = RoundedRectangle(
            corner_radius=0.18,
            width=width,
            height=height,
            color=color,
            stroke_width=2.5,
            fill_color=PANEL,
            fill_opacity=fill_opacity,
        )
        title_mob = Text(title, font_size=title_size, color=color, weight=BOLD)
        if body:
            body_mob = Text(body, font_size=body_size, color=WHITE, line_spacing=0.9)
            labels = VGroup(title_mob, body_mob).arrange(DOWN, buff=0.18)
        else:
            labels = VGroup(title_mob)
        labels.move_to(box.get_center())
        return VGroup(box, labels)

    def pill(self, text, color=CYAN, width=None, font_size=18):
        label = Text(text, font_size=font_size, color=WHITE, weight=BOLD)
        w = width or max(1.35, label.width + 0.55)
        rect = RoundedRectangle(
            corner_radius=0.16,
            width=w,
            height=0.58,
            stroke_width=2,
            color=color,
            fill_color=color,
            fill_opacity=0.16,
        )
        label.move_to(rect)
        return VGroup(rect, label)

    def chat_bubble(self, text, color, width=3.8, height=0.82, font_size=16):
        box = RoundedRectangle(
            corner_radius=0.16,
            width=width,
            height=height,
            color=color,
            stroke_width=2,
            fill_color=color,
            fill_opacity=0.13,
        )
        label = Text(text, font_size=font_size, color=WHITE)
        label.move_to(box)
        return VGroup(box, label)

    def probability_bar(self, label, value, color=TEAL2, width=4.1):
        value = float(np.clip(value, 0, 1))
        label_mob = Text(label, font_size=18, color=WHITE)
        track = RoundedRectangle(
            corner_radius=0.08,
            width=width,
            height=0.42,
            stroke_width=1.5,
            color=GREY_D,
            fill_color=GREY_E,
            fill_opacity=0.45,
        )
        fill_width = max(0.02, width * value)
        fill = RoundedRectangle(
            corner_radius=0.07,
            width=fill_width,
            height=0.35,
            stroke_width=0,
            fill_color=color,
            fill_opacity=0.95,
        )
        fill.align_to(track, LEFT).shift(RIGHT * 0.035)
        number = Text(f"{value:.0%}", font_size=20, color=color, weight=BOLD)
        number.next_to(track, RIGHT, buff=0.18)
        label_mob.next_to(track, LEFT, buff=0.18)
        return VGroup(label_mob, track, fill, number)

    def arrow_between(self, left_mob, right_mob, color=YELLOW2, buff=0.18):
        return Arrow(
            left_mob.get_right(),
            right_mob.get_left(),
            buff=buff,
            stroke_width=5,
            color=color,
            tip_length=0.18,
        )

    def mini_embedding(self, count=24, color=BLUE2):
        bars = VGroup()
        heights = [0.18 + 0.52 * (0.5 + 0.5 * np.sin(i * 1.9)) for i in range(count)]
        for h in heights:
            bars.add(
                RoundedRectangle(
                    corner_radius=0.03,
                    width=0.085,
                    height=h,
                    stroke_width=0,
                    fill_color=color,
                    fill_opacity=0.9,
                )
            )
        bars.arrange(RIGHT, buff=0.035, aligned_edge=DOWN)
        return bars

    def caption(self, text, color=YELLOW2, size=22):
        cap = Text(text, font_size=size, color=color, weight=BOLD)
        cap.to_edge(DOWN, buff=0.35)
        return cap

    # ------------------------------- video -----------------------------------
    def construct(self):
        # ------------------------------------------------------------------
        # 0:00-0:18 — Hook
        # Narration: Most language models make decisions by first writing an
        # answer, one token at a time. Automation often needs probabilities,
        # scores, choices, and uncertainty instead.
        # ------------------------------------------------------------------
        grid = self.create_background_grid()
        self.play(FadeIn(grid), run_time=self.rt(1.4))

        title = Text("PROBABILITY-FIRST AI", font_size=48, color=CYAN, weight=BOLD)
        subtitle = Text(
            "The open research that resembles JEV",
            font_size=25,
            color=WHITE,
        )
        qualifier = Text(
            "Architectural resemblance  !=  proven provenance",
            font_size=18,
            color=YELLOW2,
        )
        title_group = VGroup(title, subtitle, qualifier).arrange(DOWN, buff=0.24)
        title_group.move_to(UP * 0.55)

        token_stream = VGroup(*[
            self.pill(t, color=BLUE2, font_size=16)
            for t in ["The", "answer", "is", "..."]
        ]).arrange(RIGHT, buff=0.12)
        token_stream.scale(0.78).move_to(DOWN * 1.55)

        self.play(Write(title), run_time=self.rt(1.3))
        self.play(FadeIn(subtitle, shift=UP * 0.15), run_time=self.rt(0.9))
        self.play(FadeIn(qualifier), run_time=self.rt(0.7))
        for token in token_stream:
            self.play(FadeIn(token, shift=RIGHT * 0.18), run_time=self.rt(0.45))
        self.hold(12.15)
        self.clear_scene(1.1)

        # ------------------------------------------------------------------
        # 0:18-0:38 — Token generation vs direct decisions
        # ------------------------------------------------------------------
        grid = self.create_background_grid()
        hdr = self.header("Two different primitives", "Generate language ... or estimate decisions")
        self.add(grid)
        self.play(FadeIn(hdr, shift=DOWN * 0.15), run_time=self.rt(1.0))

        llm = self.panel(
            "AUTOREGRESSIVE LLM",
            "state -> next token -> next token -> ...",
            BLUE2, width=5.6, height=2.25,
        ).move_to(LEFT * 3.4 + UP * 0.7)
        decision = self.panel(
            "DECISION MODEL",
            "state -> probabilities + confidence",
            TEAL2, width=5.6, height=2.25,
        ).move_to(RIGHT * 3.4 + UP * 0.7)

        self.play(FadeIn(llm, shift=UP * 0.2), FadeIn(decision, shift=UP * 0.2), run_time=self.rt(1.2))

        tokens = VGroup(*[
            self.pill(t, BLUE2, font_size=15)
            for t in ["yes", ",", "because", "..."]
        ]).arrange(RIGHT, buff=0.08).scale(0.78)
        tokens.move_to(LEFT * 3.4 + DOWN * 1.25)

        probs = VGroup(
            self.probability_bar("approve", 0.82, TEAL2, width=2.3),
            self.probability_bar("escalate", 0.18, PURPLE2, width=2.3),
        ).arrange(DOWN, buff=0.20).scale(0.78)
        probs.move_to(RIGHT * 3.3 + DOWN * 1.2)

        for token in tokens:
            self.play(FadeIn(token, shift=RIGHT * 0.1), run_time=self.rt(0.48))
        self.play(LaggedStart(*[FadeIn(p, shift=RIGHT * 0.15) for p in probs], lag_ratio=0.12), run_time=self.rt(1.0))

        shift_text = Text(
            "The shift: from generating what to say -> estimating what to do",
            font_size=23,
            color=YELLOW2,
            weight=BOLD,
        ).to_edge(DOWN, buff=0.42)
        self.play(Write(shift_text), run_time=self.rt(1.1))
        self.hold(14.12)
        self.clear_scene(1.1)

        # ------------------------------------------------------------------
        # 0:38-1:04 — March 2025 SalesRLAgent architecture
        # ------------------------------------------------------------------
        grid = self.create_background_grid()
        hdr = self.header(
            "MARCH 2025: SalesRLAgent",
            "A conversation becomes state; the policy outputs a probability",
            color=TEAL2,
        )
        source = self.source_tag("Nandakishor M. - arXiv:2503.23303")
        self.add(grid)
        self.play(FadeIn(hdr), FadeIn(source), run_time=self.rt(1.0))

        bubbles = VGroup(
            self.chat_bubble("Customer: What does it cost?", BLUE2),
            self.chat_bubble("Rep: $1,000/month - want a demo?", TEAL2),
            self.chat_bubble("Customer: That could work.", BLUE2),
        ).arrange(DOWN, buff=0.13)
        bubbles.scale(0.86).move_to(LEFT * 5.0 + UP * 0.1)

        emb_box = self.panel("EMBEDDING", "semantic vector\n3072 dimensions", BLUE2, width=2.7, height=2.0)
        emb_box.move_to(LEFT * 1.9 + UP * 0.2)
        emb_viz = self.mini_embedding(22, BLUE2).scale(0.75)
        emb_viz.next_to(emb_box, DOWN, buff=0.25)

        state_box = self.panel("STATE", "embedding +\nconversation features", YELLOW2, width=2.6, height=2.0)
        state_box.move_to(RIGHT * 1.15 + UP * 0.2)

        policy_box = self.panel("POLICY", "P(convert)", TEAL2, width=2.3, height=1.35)
        value_box = self.panel("VALUE", "future reward", PURPLE2, width=2.3, height=1.35)
        conf_box = self.panel("CONFIDENCE", "know uncertainty", ORANGE2, width=2.3, height=1.35)
        heads = VGroup(policy_box, value_box, conf_box).arrange(DOWN, buff=0.18)
        heads.scale(0.84).move_to(RIGHT * 4.85 + DOWN * 0.05)

        self.play(LaggedStart(*[FadeIn(b, shift=UP * 0.13) for b in bubbles], lag_ratio=0.18), run_time=self.rt(1.8))
        self.play(FadeIn(emb_box), FadeIn(emb_viz), run_time=self.rt(1.0))
        a1 = self.arrow_between(bubbles, emb_box, YELLOW2)
        self.play(Create(a1), run_time=self.rt(0.7))
        self.play(FadeIn(state_box), run_time=self.rt(0.8))
        a2 = self.arrow_between(emb_box, state_box, YELLOW2)
        self.play(Create(a2), run_time=self.rt(0.7))

        self.play(LaggedStart(*[FadeIn(h, shift=RIGHT * 0.15) for h in heads], lag_ratio=0.15), run_time=self.rt(1.4))
        branch_lines = VGroup(*[
            Arrow(state_box.get_right(), h.get_left(), buff=0.14, stroke_width=3.5, tip_length=0.13, color=h[0].get_color())
            for h in heads
        ])
        self.play(LaggedStart(*[Create(a) for a in branch_lines], lag_ratio=0.10), run_time=self.rt(1.2))

        output = self.probability_bar("conversion", 0.74, TEAL2, width=3.2)
        output.scale(0.88).to_edge(DOWN, buff=0.48)
        self.play(FadeIn(output, shift=UP * 0.15), run_time=self.rt(1.0))
        self.hold(15.30)
        self.clear_scene(1.1)

        # ------------------------------------------------------------------
        # 1:04-1:27 — Probability trajectory + PPO/RL abstraction
        # ------------------------------------------------------------------
        grid = self.create_background_grid()
        hdr = self.header(
            "THE ACTION IS A PROBABILITY",
            "The open implementation is described by its author as PPO over conversation-state embeddings",
            color=YELLOW2,
        )
        source = self.source_tag("Paper + author's open-source Reddit explanation (2025)")
        self.add(grid)
        self.play(FadeIn(hdr), FadeIn(source), run_time=self.rt(1.0))

        # A turn-by-turn probability trajectory.
        axes = Axes(
            x_range=[0, 6, 1],
            y_range=[0, 1.01, 0.25],
            x_length=7.2,
            y_length=3.7,
            axis_config={"color": GREY_B, "stroke_width": 2},
            tips=False,
        ).move_to(LEFT * 2.4 + DOWN * 0.1)
        xlab = Text("conversation turn", font_size=16, color=GREY_B).next_to(axes, DOWN, buff=0.18)
        ylab = Text("P(convert)", font_size=16, color=GREY_B).rotate(PI / 2).next_to(axes, LEFT, buff=0.18)
        probs_data = [0.31, 0.38, 0.52, 0.47, 0.67, 0.79]
        pts = [axes.c2p(i + 0.5, p) for i, p in enumerate(probs_data)]
        path = VMobject(color=TEAL2, stroke_width=5).set_points_as_corners(pts)
        dots = VGroup(*[Dot(p, radius=0.075, color=TEAL2) for p in pts])

        self.play(Create(axes), FadeIn(xlab), FadeIn(ylab), run_time=self.rt(1.2))
        self.play(Create(path), LaggedStart(*[GrowFromCenter(d) for d in dots], lag_ratio=0.12), run_time=self.rt(1.8))

        rl = self.panel(
            "RL LOOP",
            "state  ->  policy\nprobability = action\noutcome = reward",
            ORANGE2,
            width=4.0,
            height=2.55,
            title_size=26,
            body_size=18,
        ).move_to(RIGHT * 4.5 + UP * 0.15)
        ppo = self.pill("PPO", ORANGE2, width=1.55, font_size=19)
        ppo.next_to(rl, DOWN, buff=0.25)
        self.play(FadeIn(rl, shift=LEFT * 0.15), FadeIn(ppo, shift=UP * 0.1), run_time=self.rt(1.1))

        thesis = Text(
            "Optimize the decision directly - not the sentence around it.",
            font_size=23,
            color=YELLOW2,
            weight=BOLD,
        ).to_edge(DOWN, buff=0.35)
        self.play(Write(thesis), run_time=self.rt(1.0))
        self.hold(15.80)
        self.clear_scene(1.1)

        # ------------------------------------------------------------------
        # 1:27-1:52 — September 2025 confidence-aware routing
        # ------------------------------------------------------------------
        grid = self.create_background_grid()
        hdr = self.header(
            "SEPTEMBER 2025: CONFIDENCE BECOMES A ROUTER",
            "Estimate uncertainty BEFORE deciding which system should act",
            color=PURPLE2,
        )
        source = self.source_tag("Nandakishor M. - arXiv:2510.01237")
        self.add(grid)
        self.play(FadeIn(hdr), FadeIn(source), run_time=self.rt(1.0))

        signals = VGroup(
            self.panel("SEMANTIC", "alignment", BLUE2, width=2.4, height=1.35),
            self.panel("CONVERGENCE", "internal stability", PURPLE2, width=2.4, height=1.35),
            self.panel("LEARNED", "confidence head", ORANGE2, width=2.4, height=1.35),
        ).arrange(DOWN, buff=0.20).scale(0.9)
        signals.move_to(LEFT * 5.1 + DOWN * 0.05)

        combine = Circle(radius=0.88, color=YELLOW2, stroke_width=3, fill_color=YELLOW2, fill_opacity=0.12)
        combine_label = Text("C", font_size=36, color=YELLOW2, weight=BOLD).move_to(combine)
        combine_group = VGroup(combine, combine_label).move_to(LEFT * 1.8 + DOWN * 0.05)
        combine_sub = Text("overall\nconfidence", font_size=15, color=GREY_B, line_spacing=0.8).next_to(combine_group, DOWN, buff=0.15)

        routes = VGroup(
            self.pill("HIGH -> LOCAL", GREEN2, width=3.1, font_size=16),
            self.pill("MEDIUM -> RAG", TEAL2, width=3.1, font_size=16),
            self.pill("LOW -> LARGER MODEL", ORANGE2, width=3.1, font_size=16),
            self.pill("VERY LOW -> HUMAN", RED2, width=3.1, font_size=16),
        ).arrange(DOWN, buff=0.23)
        routes.move_to(RIGHT * 4.2 + DOWN * 0.05)

        self.play(LaggedStart(*[FadeIn(s, shift=RIGHT * 0.15) for s in signals], lag_ratio=0.16), run_time=self.rt(1.5))
        for s in signals:
            arr = Arrow(s.get_right(), combine_group.get_left(), buff=0.12, color=GREY_B, stroke_width=3, tip_length=0.13)
            self.play(Create(arr), run_time=self.rt(0.42))
        self.play(GrowFromCenter(combine_group), FadeIn(combine_sub), run_time=self.rt(0.9))
        self.play(LaggedStart(*[FadeIn(r, shift=LEFT * 0.15) for r in routes], lag_ratio=0.14), run_time=self.rt(1.4))

        router_arrow = Arrow(combine_group.get_right(), routes.get_left(), buff=0.18, color=YELLOW2, stroke_width=5, tip_length=0.17)
        self.play(Create(router_arrow), run_time=self.rt(0.8))

        caption = self.caption("Confidence becomes control flow.", PURPLE2, 24)
        self.play(Write(caption), run_time=self.rt(0.9))
        self.hold(16.98)
        self.clear_scene(1.1)

        # ------------------------------------------------------------------
        # 1:52-2:28 — Compare with Jev's PUBLIC description
        # ------------------------------------------------------------------
        grid = self.create_background_grid()
        hdr = self.header(
            "NOW COMPARE THAT WITH JEV",
            "TypeSafe's public description - September 2026",
            color=CYAN,
        )
        source = self.source_tag("TypeSafe: Introducing System One Models & Jev (Sep 15, 2026)")
        self.add(grid)
        self.play(FadeIn(hdr), FadeIn(source), run_time=self.rt(1.0))

        state = self.panel("UNSTRUCTURED STATE", "text / program state", BLUE2, width=3.1, height=1.65)
        state.move_to(LEFT * 4.95 + UP * 0.55)
        core = self.panel(
            "JEV",
            "new architecture\nparallel sampler\nRLCD training",
            CYAN,
            width=3.0,
            height=2.4,
            title_size=30,
            body_size=17,
        ).move_to(LEFT * 1.1 + UP * 0.55)

        out1 = self.pill("choice: A   72%", TEAL2, width=3.15, font_size=16)
        out2 = self.pill("risk: HIGH   64%", ORANGE2, width=3.15, font_size=16)
        out3 = self.pill("escalate: YES   18%", PURPLE2, width=3.15, font_size=16)
        outputs = VGroup(out1, out2, out3).arrange(DOWN, buff=0.28)
        outputs.move_to(RIGHT * 4.2 + UP * 0.55)

        self.play(FadeIn(state, shift=RIGHT * 0.15), run_time=self.rt(0.8))
        self.play(Create(self.arrow_between(state, core, YELLOW2)), FadeIn(core), run_time=self.rt(1.1))
        # Parallel fan-out: all outputs appear together.
        fan = VGroup(*[
            Arrow(core.get_right(), out.get_left(), buff=0.12, stroke_width=3.5, tip_length=0.13, color=out[0].get_color())
            for out in outputs
        ])
        self.play(
            LaggedStart(*[Create(a) for a in fan], lag_ratio=0.06),
            AnimationGroup(*[FadeIn(out, shift=RIGHT * 0.12) for out in outputs], lag_ratio=0.0),
            run_time=self.rt(1.5),
        )

        public_claim = Text(
            "unstructured state in  ->  typed probabilistic decisions out",
            font_size=23,
            color=CYAN,
            weight=BOLD,
        ).move_to(DOWN * 1.65)
        self.play(Write(public_claim), run_time=self.rt(1.0))

        # Reveal the recurring design pattern under the Jev diagram.
        pattern = VGroup(
            self.pill("1  REPRESENT STATE", BLUE2, width=2.65, font_size=15),
            self.pill("2  PREDICT PROBABILITIES", TEAL2, width=3.25, font_size=15),
            self.pill("3  QUANTIFY UNCERTAINTY", PURPLE2, width=3.25, font_size=15),
            self.pill("4  BRANCH IN SOFTWARE", YELLOW2, width=2.85, font_size=15),
        ).arrange(RIGHT, buff=0.16).scale(0.88)
        pattern.to_edge(DOWN, buff=0.37)
        self.play(LaggedStart(*[FadeIn(p, shift=UP * 0.12) for p in pattern], lag_ratio=0.12), run_time=self.rt(1.6))
        self.hold(27.90)
        self.clear_scene(1.1)

        # ------------------------------------------------------------------
        # 2:28-2:51 — What is actually established?
        # ------------------------------------------------------------------
        grid = self.create_background_grid()
        hdr = self.header("WHAT THE PUBLIC EVIDENCE DOES - AND DOESN'T - SHOW", color=YELLOW2)
        self.add(grid)
        self.play(FadeIn(hdr), run_time=self.rt(1.0))

        verified = self.panel(
            "VERIFIABLE",
            "March 2025:\nRL state -> probability + confidence\n\nSeptember 2025:\nconfidence -> routing\n\nSeptember 2026:\nJev publicly described with\nprobabilities, confidence, parallel sampling",
            GREEN2,
            width=6.1,
            height=4.7,
            title_size=25,
            body_size=17,
        ).move_to(LEFT * 3.35 + DOWN * 0.15)

        not_proven = self.panel(
            "NOT ESTABLISHED",
            "shared code\n\nshared weights or dataset\n\ndirect technical lineage\n\ncopying",
            RED2,
            width=5.25,
            height=4.7,
            title_size=25,
            body_size=18,
        ).move_to(RIGHT * 3.6 + DOWN * 0.15)

        self.play(FadeIn(verified, shift=RIGHT * 0.2), FadeIn(not_proven, shift=LEFT * 0.2), run_time=self.rt(1.5))

        author_claim = Text(
            "The open-research author argues the systems are architecturally similar.",
            font_size=20,
            color=YELLOW2,
            weight=BOLD,
        ).to_edge(DOWN, buff=0.36)
        self.play(Write(author_claim), run_time=self.rt(1.0))
        self.hold(18.40)
        self.clear_scene(1.1)

        # ------------------------------------------------------------------
        # 2:51-3:00 — Closing thesis
        # ------------------------------------------------------------------
        grid = self.create_background_grid()
        self.add(grid)
        line1 = Text("FROM AI THAT WRITES A DECISION", font_size=37, color=GREY_B, weight=BOLD)
        line2 = Text("TO AI THAT ESTIMATES A DECISION", font_size=39, color=CYAN, weight=BOLD)
        line3 = Text("...and tells you how sure it is.", font_size=25, color=YELLOW2)
        close = VGroup(line1, line2, line3).arrange(DOWN, buff=0.28)
        close.move_to(UP * 0.35)

        brand = Text(
            "OMNIACS.DAO  |  Making Scientific Visualizations with the Omniacs",
            font_size=17,
            color=GREY2,
        ).to_edge(DOWN, buff=0.42)

        self.play(Write(line1), run_time=self.rt(0.8))
        self.play(TransformFromCopy(line1, line2), run_time=self.rt(1.0))
        self.play(FadeIn(line3, shift=UP * 0.12), FadeIn(brand), run_time=self.rt(0.8))
        self.hold(4.80)
        self.play(*[FadeOut(m) for m in self.mobjects], run_time=self.rt(1.6))
