from manim import *
import numpy as np

# -----------------------------------------------------------------------------
# OPEN-SOURCE JEV ALTERNATIVES
# Omniacs.DAO / Making Scientific Visualizations with the Omniacs
#
# Target runtime: 5:55 (355 seconds) at PACING = 1.0
# Preview quickly by setting PACING = 0.12–0.20.
#
# Render:
#   manim -pql Open_Source_JEV_Alternatives.py OpenSourceJevAlternatives
#   manim -pqh Open_Source_JEV_Alternatives.py OpenSourceJevAlternatives
# -----------------------------------------------------------------------------

PACING = 1.0
BG = "#07111A"
PANEL = "#0B1824"
PANEL2 = "#102331"
CYAN = "#20D5E8"
BLUE2 = "#4C8DFF"
TEAL = "#25C7A5"
YELLOW = "#FFD166"
ORANGE = "#FF9F43"
RED = "#FF5C6C"
PURPLE = "#B388FF"
GREEN = "#7BE495"
GREY = "#93A4B7"
GREY_DARK = "#33485C"
WHITE2 = "#F2F7FA"

config.background_color = BG


class OpenSourceJevAlternatives(Scene):
    """A ~5:55 explainer of open-source Jev-like decision models.

    Editorial rule:
        API similarity is not architecture identity.
        Official Jev internals remain undisclosed beyond TypeSafe's public claims.
    """

    # ------------------------------------------------------------------
    # Timing helpers
    # ------------------------------------------------------------------
    def setup(self):
        self.nominal_elapsed = 0.0

    def rt(self, seconds):
        return max(0.03, seconds * PACING)

    def play_t(self, *animations, t=1.0, **kwargs):
        self.play(*animations, run_time=self.rt(t), **kwargs)
        self.nominal_elapsed += t

    def hold(self, seconds):
        self.wait(self.rt(seconds))
        self.nominal_elapsed += seconds

    def pad_to(self, target_seconds):
        remaining = target_seconds - self.nominal_elapsed
        if remaining > 0.01:
            self.hold(remaining)

    def clear_scene(self, t=1.0):
        if self.mobjects:
            self.play_t(
                *[FadeOut(m) for m in list(self.mobjects)],
                t=t,
                rate_func=smooth,
            )

    # ------------------------------------------------------------------
    # Styling helpers
    # ------------------------------------------------------------------
    def grid(self):
        g = VGroup()
        for x in np.arange(-8, 9, 1):
            g.add(Line(UP * 4.5 + RIGHT * x, DOWN * 4.5 + RIGHT * x,
                       stroke_width=0.45, stroke_opacity=0.14, color=BLUE_D))
        for y in np.arange(-5, 6, 1):
            g.add(Line(LEFT * 8 + UP * y, RIGHT * 8 + UP * y,
                       stroke_width=0.45, stroke_opacity=0.14, color=BLUE_D))
        return g

    def section_header(self, title, subtitle=None, color=CYAN):
        h = Text(title, font_size=36, color=color, weight=BOLD)
        if h.width > 13.15:
            h.scale_to_fit_width(13.15)
        h.to_edge(UP, buff=0.30)
        if subtitle:
            s = Text(subtitle, font_size=18, color=GREY)
            if s.width > 12.8:
                s.scale_to_fit_width(12.8)
            s.next_to(h, DOWN, buff=0.10)
            return VGroup(h, s)
        return VGroup(h)

    def panel(self, title, lines=None, color=CYAN, width=3.3, height=2.0,
              title_size=22, body_size=16, fill=PANEL, opacity=0.44):
        box = RoundedRectangle(
            corner_radius=0.18,
            width=width,
            height=height,
            color=color,
            stroke_width=2.4,
            fill_color=fill,
            fill_opacity=opacity,
        )
        title_m = Text(title, font_size=title_size, color=color, weight=BOLD)
        mobs = [title_m]
        if lines:
            body = VGroup(*[Text(line, font_size=body_size, color=WHITE2) for line in lines])
            body.arrange(DOWN, aligned_edge=LEFT, buff=0.10)
            mobs.append(body)
        labels = VGroup(*mobs).arrange(DOWN, buff=0.18)
        if labels.width > width - 0.28:
            labels.scale_to_fit_width(width - 0.28)
        if labels.height > height - 0.22:
            labels.scale_to_fit_height(height - 0.22)
        labels.move_to(box)
        return VGroup(box, labels)

    def chip(self, text, color=CYAN, font_size=17, pad=0.42):
        label = Text(text, font_size=font_size, color=WHITE2, weight=BOLD)
        box = RoundedRectangle(
            corner_radius=0.15,
            width=label.width + pad,
            height=0.52,
            color=color,
            stroke_width=1.8,
            fill_color=color,
            fill_opacity=0.12,
        )
        label.move_to(box)
        return VGroup(box, label)

    def source(self, text):
        t = Text(text, font_size=12, color=GREY)
        if t.width > 7.2:
            t.scale_to_fit_width(7.2)
        t.to_corner(DR, buff=0.18)
        return t

    def probability_bar(self, label, value, color=TEAL, width=3.5, label_size=18):
        value = float(np.clip(value, 0, 1))
        lab = Text(label, font_size=label_size, color=WHITE2)
        track = RoundedRectangle(
            corner_radius=0.07, width=width, height=0.38,
            color=GREY_DARK, stroke_width=1.2,
            fill_color=GREY_DARK, fill_opacity=0.35,
        )
        fw = max(0.03, width * value)
        fill = RoundedRectangle(
            corner_radius=0.06, width=fw, height=0.31,
            stroke_width=0, fill_color=color, fill_opacity=0.95,
        )
        fill.align_to(track, LEFT).shift(RIGHT * 0.03)
        num = Text(f"{value:.0%}", font_size=18, color=color, weight=BOLD)
        lab.next_to(track, LEFT, buff=0.18)
        num.next_to(track, RIGHT, buff=0.18)
        return VGroup(lab, track, fill, num)

    def flow_arrow(self, a, b, color=YELLOW, buff=0.15):
        return Arrow(a.get_right(), b.get_left(), buff=buff,
                     color=color, stroke_width=4.5, tip_length=0.17)

    def down_arrow(self, a, b, color=YELLOW, buff=0.12):
        return Arrow(a.get_bottom(), b.get_top(), buff=buff,
                     color=color, stroke_width=4.5, tip_length=0.17)

    def caption(self, text, color=YELLOW, size=22):
        t = Text(text, font_size=size, color=color, weight=BOLD)
        if t.width > 13.1:
            t.scale_to_fit_width(13.1)
        t.to_edge(DOWN, buff=0.32)
        return t

    def tiny_model_cards(self, names, y=-2.4, colors=None):
        cards = VGroup()
        colors = colors or [CYAN] * len(names)
        for name, c in zip(names, colors):
            cards.add(self.chip(name, c, 15))
        cards.arrange(RIGHT, buff=0.14)
        cards.move_to(UP * y)
        return cards

    # ------------------------------------------------------------------
    # 0:00–0:30 — Hook
    # ------------------------------------------------------------------
    def section_hook(self):
        grid = self.grid()
        self.play_t(FadeIn(grid), t=1.0)

        title = Text("ONE API. MANY MACHINES.", font_size=47, color=CYAN, weight=BOLD)
        sub = Text("Open-source alternatives to TypeSafe JEV", font_size=23, color=WHITE2)
        VGroup(title, sub).arrange(DOWN, buff=0.14).move_to(UP * 2.55)
        self.play_t(Write(title), FadeIn(sub, shift=UP * 0.15), t=1.6)

        state = self.panel("STATE", ["ticket / JSON / game", "policy / context"], BLUE2,
                           width=2.65, height=1.5, body_size=14)
        api = self.panel("SYSTEM ONE API", ["typed questions"], CYAN,
                         width=2.85, height=1.5, body_size=14)
        probs = self.panel("PROBABILITIES", ["choice  •  score  •  noul"], TEAL,
                           width=3.05, height=1.5, body_size=14)
        chain = VGroup(state, api, probs).arrange(RIGHT, buff=1.0).move_to(UP * 0.65)
        a1 = self.flow_arrow(state, api)
        a2 = self.flow_arrow(api, probs)
        self.play_t(FadeIn(state, shift=UP * 0.2), t=0.9)
        self.play_t(GrowArrow(a1), FadeIn(api, shift=UP * 0.2), t=0.9)
        self.play_t(GrowArrow(a2), FadeIn(probs, shift=UP * 0.2), t=0.9)

        family_names = [
            ("ENCODER", BLUE2),
            ("FROZEN LLM", YELLOW),
            ("LoRA + LOGITS", PURPLE),
            ("CUSTOM HEAD", ORANGE),
            ("CONTRASTIVE", TEAL),
            ("DIFFUSION", GREEN),
        ]
        families = VGroup(*[self.chip(n, c, 15) for n, c in family_names])
        families.arrange_in_grid(rows=2, cols=3, buff=(0.25, 0.20)).move_to(DOWN * 1.62)

        reveal = Text("Same contract ≠ same architecture", font_size=25, color=YELLOW, weight=BOLD)
        reveal.to_edge(DOWN, buff=0.28)
        self.play_t(LaggedStart(*[FadeIn(x, scale=0.92) for x in families], lag_ratio=0.12), t=2.3)
        self.play_t(Write(reveal), t=1.1)

        self.pad_to(33.0)
        self.clear_scene(t=1.0)
        self.pad_to(34.0)

    # ------------------------------------------------------------------
    # 0:30–1:00 — Official Jev: public claims and unknowns
    # ------------------------------------------------------------------
    def section_official_jev(self):
        grid = self.grid()
        hdr = self.section_header("WHAT DO WE ACTUALLY KNOW ABOUT JEV?",
                                  "Public claims are clear. Internal implementation is not.")
        self.play_t(FadeIn(grid), Write(hdr), t=1.4)

        jev = RoundedRectangle(corner_radius=0.24, width=2.45, height=2.45,
                               color=CYAN, stroke_width=3.2,
                               fill_color=PANEL2, fill_opacity=0.9)
        jev_lab = Text("JEV", font_size=42, color=CYAN, weight=BOLD).move_to(jev)
        black_box = VGroup(jev, jev_lab).move_to(ORIGIN)
        self.play_t(FadeIn(black_box, scale=0.88), t=1.0)

        known = self.panel("PUBLICLY DISCLOSED", [
            "new architecture",
            "parallel sampler",
            "RLCD training",
            "typed probabilities",
        ], GREEN, width=3.8, height=2.7, body_size=17)
        unknown = self.panel("NOT PUBLIC", [
            "model weights",
            "architecture spec",
            "training corpus",
            "exact RLCD recipe",
        ], ORANGE, width=3.8, height=2.7, body_size=17)
        known.move_to(LEFT * 4.65 + DOWN * 0.15)
        unknown.move_to(RIGHT * 4.65 + DOWN * 0.15)
        self.play_t(FadeIn(known, shift=RIGHT * 0.25), FadeIn(unknown, shift=LEFT * 0.25), t=1.5)

        left_arrow = Arrow(black_box.get_left(), known.get_right(), buff=0.22,
                           color=GREEN, stroke_width=4, tip_length=0.16)
        right_arrow = Arrow(black_box.get_right(), unknown.get_left(), buff=0.22,
                            color=ORANGE, stroke_width=4, tip_length=0.16)
        self.play_t(GrowArrow(left_arrow), GrowArrow(right_arrow), t=1.0)

        contract = self.caption("An open model can reproduce the behavioral contract without reproducing JEV.", YELLOW, 20)
        self.play_t(Write(contract), t=1.3)
        src = self.source("Source: TypeSafe, “Introducing System One Models & Jev”, Sep 15 2026")
        self.play_t(FadeIn(src), t=0.6)

        self.pad_to(63.0)
        self.clear_scene(t=1.0)
        self.pad_to(64.0)

    # ------------------------------------------------------------------
    # 1:00–1:52 — Dedicated decision encoders + calibration/RL aside
    # ------------------------------------------------------------------
    def section_encoders(self):
        grid = self.grid()
        hdr = self.section_header("FAMILY 1 — BUILD A REAL DECISION MODEL",
                                  "Small encoders trained to score supplied answers directly", BLUE2)
        self.play_t(FadeIn(grid), Write(hdr), t=1.4)

        mmbert = self.panel("mmBERT-small", ["multilingual encoder"], BLUE2, width=2.65, height=1.35, body_size=14)
        julia = self.panel("JULIA-1", ["decision components", "144.3M params"], TEAL, width=2.75, height=1.55, body_size=14)
        cpu = self.panel("CPU", ["~550 MiB weights"], GREEN, width=2.2, height=1.35, body_size=14)
        chain = VGroup(mmbert, julia, cpu).arrange(RIGHT, buff=0.9).move_to(UP * 1.25)
        a1 = self.flow_arrow(mmbert, julia)
        a2 = self.flow_arrow(julia, cpu)
        self.play_t(FadeIn(mmbert), GrowArrow(a1), FadeIn(julia), GrowArrow(a2), FadeIn(cpu), t=2.2)
        julia_note = Text("Training pipeline not public", font_size=15, color=ORANGE).next_to(julia, DOWN, buff=0.16)
        self.play_t(FadeIn(julia_note), t=0.6)

        self.play_t(FadeOut(VGroup(mmbert, julia, cpu, a1, a2, julia_note)), t=0.8)

        laya = self.panel("LAYA POLICY", ["probability distribution"], PURPLE, width=2.75, height=1.45, body_size=14)
        noise = self.panel("EXPLORE", ["Gaussian logit noise"], ORANGE, width=2.5, height=1.45, body_size=14)
        reward = self.panel("PROPER SCORE", ["reward honest beliefs"], GREEN, width=2.7, height=1.45, body_size=14)
        trio = VGroup(laya, noise, reward).arrange(RIGHT, buff=0.75).move_to(UP * 1.05)
        ar1 = self.flow_arrow(laya, noise, ORANGE)
        ar2 = self.flow_arrow(noise, reward, GREEN)
        loop = CurvedArrow(reward.get_bottom(), laya.get_bottom(), angle=-1.8,
                           color=PURPLE, stroke_width=4.2, tip_length=0.16)
        loop_lab = Text("REINFORCE / group-mean baseline", font_size=15, color=PURPLE)
        loop_lab.move_to(DOWN * 0.18)
        self.play_t(FadeIn(laya), GrowArrow(ar1), FadeIn(noise), GrowArrow(ar2), FadeIn(reward), t=2.2)
        self.play_t(Create(loop), FadeIn(loop_lab), t=1.1)

        bars = VGroup(
            self.probability_bar("refund", 0.72, TEAL, width=2.45, label_size=15),
            self.probability_bar("escalate", 0.18, YELLOW, width=2.45, label_size=15),
            self.probability_bar("deny", 0.10, RED, width=2.45, label_size=15),
        ).arrange(DOWN, buff=0.20).scale(0.9).move_to(DOWN * 1.55)
        honest = Text("Reward targets the distribution — not just the argmax.", font_size=19, color=YELLOW, weight=BOLD)
        honest.to_edge(DOWN, buff=0.25)
        self.play_t(LaggedStart(*[FadeIn(b, shift=RIGHT * 0.15) for b in bars], lag_ratio=0.18), t=1.7)
        self.play_t(Write(honest), t=1.0)

        self.play_t(FadeOut(VGroup(laya, noise, reward, ar1, ar2, loop, loop_lab, bars, honest)), t=0.9)

        rl = self.panel("POLICY-GRADIENT RL", ["Laya", "outcome / reward loop"], PURPLE,
                        width=3.7, height=2.0, body_size=16)
        loss = self.panel("CALIBRATION-AWARE LOSS", ["Von / Verdict", "cross-entropy + Brier"], BLUE2,
                          width=3.7, height=2.0, body_size=16)
        VGroup(rl, loss).arrange(RIGHT, buff=1.0).move_to(UP * 0.45)
        neq = Text("≠", font_size=56, color=YELLOW, weight=BOLD).move_to(ORIGIN + UP * 0.45)
        caveat = self.caption("Training for calibration is not automatically reinforcement learning.", ORANGE, 21)
        self.play_t(FadeIn(rl, shift=RIGHT * 0.15), FadeIn(loss, shift=LEFT * 0.15), Write(neq), t=1.4)
        self.play_t(Write(caveat), t=1.1)

        tags = self.tiny_model_cards(["Julia", "Laya", "Von", "Verdict"], y=-2.4,
                                     colors=[TEAL, PURPLE, BLUE2, BLUE2])
        self.play_t(FadeIn(tags), t=0.7)
        src = self.source("Sources: Julia model card; Laya README; Von / Verdict READMEs")
        self.play_t(FadeIn(src), t=0.5)

        self.pad_to(115.0)
        self.clear_scene(t=1.0)
        self.pad_to(116.0)

    # ------------------------------------------------------------------
    # 1:52–2:42 — Frozen logits
    # ------------------------------------------------------------------
    def section_frozen_logits(self):
        grid = self.grid()
        hdr = self.section_header("FAMILY 2 — MAYBE THE DECISION MODEL WAS ALREADY INSIDE",
                                  "Freeze the LLM. Read the logits instead of generating text.", YELLOW)
        self.play_t(FadeIn(grid), Write(hdr), t=1.4)

        qwen = self.panel("QWEN / GEMMA", ["ordinary causal LLM"], BLUE2, width=3.0, height=1.45, body_size=15)
        qwen.move_to(LEFT * 4.6 + UP * 0.65)
        vocab = RoundedRectangle(corner_radius=0.18, width=4.6, height=3.3,
                                 color=GREY, stroke_width=2,
                                 fill_color=PANEL, fill_opacity=0.45)
        vocab.move_to(RIGHT * 1.0 + UP * 0.95)
        vocab_title = Text("VOCABULARY LOGITS", font_size=21, color=GREY, weight=BOLD)
        vocab_title.next_to(vocab.get_top(), DOWN, buff=0.23)

        rng = np.random.default_rng(7)
        bars = VGroup()
        for i in range(18):
            h = 0.25 + float(rng.random()) * 1.55
            bar = RoundedRectangle(corner_radius=0.025, width=0.14, height=h,
                                   stroke_width=0, fill_color=GREY_DARK, fill_opacity=0.82)
            bars.add(bar)
        bars.arrange(RIGHT, buff=0.055, aligned_edge=DOWN)
        bars.move_to(vocab.get_center() + DOWN * 0.42)
        # Make three target logits visible
        target_idx = [3, 9, 14]
        target_colors = [TEAL, YELLOW, ORANGE]
        for idx, c in zip(target_idx, target_colors):
            bars[idx].set_fill(c, opacity=0.98)
        arr = self.flow_arrow(qwen, vocab, YELLOW)
        self.play_t(FadeIn(qwen), GrowArrow(arr), FadeIn(vocab), Write(vocab_title), FadeIn(bars), t=2.1)

        labels = VGroup(
            Text("A", font_size=18, color=TEAL, weight=BOLD).next_to(bars[3], DOWN, buff=0.08),
            Text("B", font_size=18, color=YELLOW, weight=BOLD).next_to(bars[9], DOWN, buff=0.08),
            Text("C", font_size=18, color=ORANGE, weight=BOLD).next_to(bars[14], DOWN, buff=0.08),
        )
        self.play_t(FadeIn(labels), t=0.7)

        # Fade non-target logits
        non_targets = VGroup(*[bars[i] for i in range(len(bars)) if i not in target_idx])
        self.play_t(non_targets.animate.set_opacity(0.10), t=1.0)

        softmax = self.panel("RESTRICT + SOFTMAX", ["A / B / C only"], PURPLE,
                             width=2.85, height=1.35, body_size=14)
        softmax.move_to(RIGHT * 4.75 + UP * 0.65)
        ar2 = Arrow(vocab.get_right(), softmax.get_left(), buff=0.18, color=PURPLE,
                    stroke_width=4.5, tip_length=0.17)
        self.play_t(GrowArrow(ar2), FadeIn(softmax), t=1.0)

        probs = VGroup(
            self.probability_bar("A billing", 0.06, TEAL, width=2.8, label_size=15),
            self.probability_bar("B support", 0.92, YELLOW, width=2.8, label_size=15),
            self.probability_bar("C sales", 0.02, ORANGE, width=2.8, label_size=15),
        ).arrange(DOWN, buff=0.16).scale(0.82).move_to(DOWN * 1.45 + RIGHT * 1.15)
        self.play_t(LaggedStart(*[FadeIn(x, shift=RIGHT * 0.2) for x in probs], lag_ratio=0.18), t=1.8)

        zero_weights = self.chip("0 NEW MODEL WEIGHTS", GREEN, 19, pad=0.7)
        zero_weights.move_to(LEFT * 4.5 + DOWN * 1.35)
        self.play_t(FadeIn(zero_weights, scale=1.08), t=0.9)

        chips = VGroup(
            self.chip("SemIf", YELLOW, 16),
            self.chip("Reflex", TEAL, 16),
            self.chip("Cygnet", GREEN, 16),
        ).arrange(RIGHT, buff=0.18).move_to(DOWN * 2.55)
        self.play_t(FadeIn(chips), t=0.8)

        wrench = Text("FINE-TUNE", font_size=22, color=PURPLE, weight=BOLD).move_to(LEFT * 3.7 + DOWN * 0.25)
        cross1 = Line(wrench.get_corner(UL) + LEFT * 0.12, wrench.get_corner(DR) + RIGHT * 0.12, color=RED, stroke_width=5)
        cross2 = Line(wrench.get_corner(DL) + LEFT * 0.12, wrench.get_corner(UR) + RIGHT * 0.12, color=RED, stroke_width=5)
        reflex_note = Text("Reflex: released path stays frozen", font_size=16, color=ORANGE)
        reflex_note.next_to(wrench, DOWN, buff=0.22)
        self.play_t(FadeIn(wrench), Create(cross1), Create(cross2), FadeIn(reflex_note), t=1.2)

        takeaway = self.caption("Generation may be only one way of reading what the model already knows.", YELLOW, 20)
        self.play_t(Write(takeaway), t=1.1)
        src = self.source("Sources: SemIf method; Reflex README; Cygnet recipe")
        self.play_t(FadeIn(src), t=0.5)

        self.pad_to(165.0)
        self.clear_scene(t=1.0)
        self.pad_to(166.0)

    # ------------------------------------------------------------------
    # 2:42–3:32 — Fine-tuned logits and real outcome RL
    # ------------------------------------------------------------------
    def section_trained_readout(self):
        grid = self.grid()
        hdr = self.section_header("FAMILY 3 — TRAIN THE READOUT",
                                  "Same option-logit inference. Very different developmental histories.", PURPLE)
        self.play_t(FadeIn(grid), Write(hdr), t=1.4)

        base = self.panel("BASE LLM", ["Qwen3.5"], BLUE2, width=2.3, height=1.35, body_size=14)
        lora = self.panel("LoRA", ["adapt decision behavior"], PURPLE, width=2.4, height=1.35, body_size=14)
        logits = self.panel("A / B / C LOGITS", ["restricted softmax"], YELLOW, width=2.8, height=1.35, body_size=14)
        temp = self.panel("TEMPERATURE", ["calibrate confidence"], TEAL, width=2.55, height=1.35, body_size=14)
        pipeline = VGroup(base, lora, logits, temp).arrange(RIGHT, buff=0.62).move_to(UP * 1.6)
        arrows = VGroup(self.flow_arrow(base, lora), self.flow_arrow(lora, logits), self.flow_arrow(logits, temp))
        self.play_t(FadeIn(base), GrowArrow(arrows[0]), FadeIn(lora), GrowArrow(arrows[1]),
                    FadeIn(logits), GrowArrow(arrows[2]), FadeIn(temp), t=2.4)

        hopper = self.panel("HOPPER", ["rank-16 LoRA", "letter logits"], PURPLE,
                            width=2.55, height=1.55, body_size=14)
        nimble = self.panel("NIMBLE", ["hard labels", "cross-entropy"], BLUE2,
                            width=2.55, height=1.55, body_size=14)
        jevk5 = self.panel("JEVK5", ["teacher + replay", "soft targets when known"], TEAL,
                           width=2.65, height=1.55, body_size=13)
        row = VGroup(hopper, nimble, jevk5).arrange(RIGHT, buff=0.42).move_to(DOWN * 0.15)
        self.play_t(LaggedStart(*[FadeIn(x, shift=UP * 0.18) for x in row], lag_ratio=0.16), t=1.6)

        plumb = self.panel("PLUMB", ["fine-tune JevK5", "upweight hard cases"], ORANGE,
                           width=2.65, height=1.55, body_size=13)
        plumb.move_to(RIGHT * 4.65 + DOWN * 0.15)
        jp = Arrow(jevk5.get_right(), plumb.get_left(), buff=0.16, color=ORANGE,
                   stroke_width=4.2, tip_length=0.16)
        self.play_t(GrowArrow(jp), FadeIn(plumb), t=1.0)

        self.play_t(FadeOut(VGroup(row, plumb, jp, pipeline, arrows)), t=0.9)

        sup = self.panel("SUPERVISED DECIDER", ["~95 datasets", "teacher + agent data"], BLUE2,
                         width=3.4, height=1.8, body_size=15)
        rl = self.panel("OUTCOME RL", ["live browser", "games with exact laws"], PURPLE,
                        width=3.25, height=1.8, body_size=15)
        result = self.panel("CALIBRATED BELIEFS", ["reward what happens"], GREEN,
                            width=3.2, height=1.8, body_size=15)
        group = VGroup(sup, rl, result).arrange(RIGHT, buff=0.72).move_to(UP * 0.55)
        da1 = self.flow_arrow(sup, rl, PURPLE)
        da2 = self.flow_arrow(rl, result, GREEN)
        self.play_t(FadeIn(sup), GrowArrow(da1), FadeIn(rl), GrowArrow(da2), FadeIn(result), t=2.2)

        badge = self.chip("DECIDER-2B v10: 384 outcome-RL updates", YELLOW, 17, pad=0.65)
        badge.move_to(DOWN * 1.35)
        self.play_t(FadeIn(badge), t=0.8)

        eikos = self.chip("Eikos: richer multi-loss training recipe", ORANGE, 16, pad=0.55)
        eikos.move_to(DOWN * 2.05)
        self.play_t(FadeIn(eikos), t=0.7)

        aside = self.caption("Identical inference can hide radically different training histories.", YELLOW, 20)
        self.play_t(Write(aside), t=1.0)
        src = self.source("Sources: Hopper, Nimble, JevK5, Plumb, Decider model cards")
        self.play_t(FadeIn(src), t=0.5)

        self.pad_to(215.0)
        self.clear_scene(t=1.0)
        self.pad_to(216.0)

    # ------------------------------------------------------------------
    # 3:32–4:15 — Custom decision heads
    # ------------------------------------------------------------------
    def section_custom_heads(self):
        grid = self.grid()
        hdr = self.section_header("FAMILY 4 — REMOVE THE LANGUAGE HEAD",
                                  "Reuse the backbone knowledge, replace how decisions are read.", ORANGE)
        self.play_t(FadeIn(grid), Write(hdr), t=1.4)

        backbone = RoundedRectangle(corner_radius=0.22, width=4.4, height=2.15,
                                    color=BLUE2, stroke_width=3,
                                    fill_color=BLUE_E, fill_opacity=0.22)
        back_lab = Text("QWEN BACKBONE", font_size=29, color=BLUE2, weight=BOLD).move_to(backbone)
        back = VGroup(backbone, back_lab).move_to(LEFT * 3.6 + UP * 0.6)
        vocab = self.panel("VOCAB HEAD", ["50k+ tokens"], GREY, width=2.55, height=1.45, body_size=14)
        vocab.move_to(RIGHT * 2.2 + UP * 0.6)
        av = Arrow(back.get_right(), vocab.get_left(), buff=0.18, color=GREY,
                   stroke_width=4.2, tip_length=0.16)
        self.play_t(FadeIn(back), GrowArrow(av), FadeIn(vocab), t=1.5)

        cross1 = Line(vocab.get_corner(UL) + LEFT * 0.08, vocab.get_corner(DR) + RIGHT * 0.08,
                      color=RED, stroke_width=6)
        cross2 = Line(vocab.get_corner(DL) + LEFT * 0.08, vocab.get_corner(UR) + RIGHT * 0.08,
                      color=RED, stroke_width=6)
        self.play_t(Create(cross1), Create(cross2), t=0.7)
        self.play_t(FadeOut(VGroup(vocab, av, cross1, cross2)), t=0.7)

        kev = self.panel("KEV", ["pointer head", "<decide> ↔ option states"], PURPLE,
                         width=3.0, height=1.65, body_size=13)
        oj = self.panel("OPEN-JEV", ["scalar candidate head", "Yes − No initialization"], TEAL,
                        width=3.0, height=1.65, body_size=13)
        nano = self.panel("NANOJEV", ["set attention", "Boolean + ordinal heads"], ORANGE,
                          width=3.0, height=1.65, body_size=13)
        heads = VGroup(kev, oj, nano).arrange(DOWN, buff=0.30).move_to(RIGHT * 3.65 + DOWN * 0.05)
        head_arrows = VGroup(*[
            Arrow(back.get_right(), h.get_left(), buff=0.18, color=h[0].get_color(),
                  stroke_width=3.8, tip_length=0.15)
            for h in heads
        ])
        self.play_t(LaggedStart(*[FadeIn(h, shift=LEFT * 0.15) for h in heads], lag_ratio=0.18),
                    LaggedStart(*[GrowArrow(a) for a in head_arrows], lag_ratio=0.18), t=2.2)

        pointer = VGroup()
        d = Dot(LEFT * 4.2 + DOWN * 1.4, radius=0.08, color=PURPLE)
        dl = Text("<decide>", font_size=15, color=PURPLE).next_to(d, LEFT, buff=0.12)
        for yy, name in zip([-0.9, -1.4, -1.9], ["option A", "option B", "option C"]):
            o = Dot(LEFT * 2.15 + UP * yy, radius=0.07, color=YELLOW)
            lab = Text(name, font_size=14, color=WHITE2).next_to(o, RIGHT, buff=0.10)
            ln = Line(d.get_center(), o.get_center(), color=PURPLE, stroke_width=2.5)
            pointer.add(o, lab, ln)
        pointer.add(d, dl)
        self.play_t(FadeIn(pointer), t=1.0)

        takeaway = self.caption("Same backbone knowledge. Different readout machinery.", YELLOW, 21)
        self.play_t(Write(takeaway), t=1.0)
        src = self.source("Sources: Kev README; Zefan-Cai Open-Jev provenance; NanoJev README")
        self.play_t(FadeIn(src), t=0.5)

        self.pad_to(258.0)
        self.clear_scene(t=1.0)
        self.pad_to(259.0)

    # ------------------------------------------------------------------
    # 4:15–4:42 — CLM contrastive geometry
    # ------------------------------------------------------------------
    def section_clm(self):
        grid = self.grid()
        hdr = self.section_header("FAMILY 5 — DECISIONS AS GEOMETRY",
                                  "CLM: contrastive state/action embeddings", TEAL)
        self.play_t(FadeIn(grid), Write(hdr), t=1.3)

        state_box = self.panel("STATE ENCODER", ["frozen LLM + projection"], BLUE2,
                               width=3.15, height=1.5, body_size=14)
        action_box = self.panel("ACTION ENCODER", ["frozen LLM + projection"], PURPLE,
                                width=3.15, height=1.5, body_size=14)
        VGroup(state_box, action_box).arrange(RIGHT, buff=2.2).move_to(UP * 1.35)
        self.play_t(FadeIn(state_box), FadeIn(action_box), t=1.0)

        s = Dot(LEFT * 1.1 + DOWN * 0.45, radius=0.12, color=BLUE2)
        s_lab = Text("state", font_size=17, color=BLUE2).next_to(s, DOWN, buff=0.14)
        a_good = Dot(RIGHT * 1.1 + DOWN * 0.10, radius=0.11, color=GREEN)
        a_bad1 = Dot(RIGHT * 3.3 + DOWN * 1.35, radius=0.11, color=RED)
        a_bad2 = Dot(RIGHT * 3.7 + UP * 0.20, radius=0.11, color=RED)
        good_lab = Text("correct action", font_size=15, color=GREEN).next_to(a_good, RIGHT, buff=0.12)
        bad_lab1 = Text("negative", font_size=14, color=RED).next_to(a_bad1, RIGHT, buff=0.10)
        bad_lab2 = Text("negative", font_size=14, color=RED).next_to(a_bad2, RIGHT, buff=0.10)
        self.play_t(FadeIn(VGroup(s, s_lab, a_good, a_bad1, a_bad2, good_lab, bad_lab1, bad_lab2)), t=1.0)

        good_line = Line(s.get_center(), a_good.get_center(), color=GREEN, stroke_width=5)
        bad_line1 = DashedLine(s.get_center(), a_bad1.get_center(), color=RED, dash_length=0.08, stroke_width=2.5)
        bad_line2 = DashedLine(s.get_center(), a_bad2.get_center(), color=RED, dash_length=0.08, stroke_width=2.5)
        self.play_t(Create(good_line), Create(bad_line1), Create(bad_line2), t=1.0)

        infonce = self.chip("InfoNCE: pull positive close, push negatives away", YELLOW, 17, pad=0.65)
        infonce.move_to(DOWN * 2.0)
        self.play_t(FadeIn(infonce), t=0.8)

        score = Text("score(action) = state · action", font_size=24, color=TEAL, weight=BOLD)
        score.to_edge(DOWN, buff=0.35)
        self.play_t(Write(score), t=0.9)
        src = self.source("Source: Contrastive-LM / CLM README")
        self.play_t(FadeIn(src), t=0.4)

        self.pad_to(285.0)
        self.clear_scene(t=1.0)
        self.pad_to(286.0)

    # ------------------------------------------------------------------
    # 4:42–5:05 — DiffusionGemma
    # ------------------------------------------------------------------
    def section_diffusion(self):
        grid = self.grid()
        hdr = self.section_header("AND THEN DIFFUSIONGEMMA BREAKS THE PATTERN",
                                  "A full token canvas instead of left-to-right decoding", GREEN)
        self.play_t(FadeIn(grid), Write(hdr), t=1.3)

        causal_title = Text("CAUSAL LLM", font_size=23, color=BLUE2, weight=BOLD).move_to(LEFT * 3.6 + UP * 1.65)
        tokens = VGroup(*[self.chip(x, BLUE2 if i < 3 else GREY, 14, pad=0.28)
                          for i, x in enumerate(["STATE", "Q", "A", "→", "→", "→"])])
        tokens.arrange(RIGHT, buff=0.10).move_to(LEFT * 3.6 + UP * 0.55)
        arrows = VGroup()
        for i in range(len(tokens) - 1):
            arrows.add(Arrow(tokens[i].get_right(), tokens[i+1].get_left(), buff=0.04,
                             color=GREY, stroke_width=2.3, tip_length=0.10))
        self.play_t(Write(causal_title), FadeIn(tokens), LaggedStart(*[GrowArrow(a) for a in arrows], lag_ratio=0.1), t=1.5)

        divider = Line(UP * 2.2, DOWN * 2.35, color=GREY_DARK, stroke_width=2).move_to(ORIGIN)
        self.play_t(Create(divider), t=0.5)

        diff_title = Text("DIFFUSION CANVAS", font_size=23, color=GREEN, weight=BOLD).move_to(RIGHT * 3.55 + UP * 1.65)
        canvas = RoundedRectangle(corner_radius=0.18, width=5.4, height=2.2,
                                  color=GREEN, stroke_width=2.5,
                                  fill_color=PANEL, fill_opacity=0.5).move_to(RIGHT * 3.55 + UP * 0.35)
        q1 = self.chip("Q1: [MASK]", YELLOW, 15, pad=0.36).move_to(RIGHT * 2.15 + UP * 0.55)
        q2 = self.chip("Q2: [MASK]", YELLOW, 15, pad=0.36).move_to(RIGHT * 3.55 + UP * 0.55)
        q3 = self.chip("Q3: [MASK]", YELLOW, 15, pad=0.36).move_to(RIGHT * 4.95 + UP * 0.55)
        qs = VGroup(q1, q2, q3).arrange(RIGHT, buff=0.16)
        if qs.width > 4.9: qs.scale_to_fit_width(4.9)
        qs.move_to(RIGHT * 3.55 + UP * 0.55)
        state = Text("STATE / IMAGE / CONTEXT", font_size=15, color=WHITE2).move_to(RIGHT * 3.55 + DOWN * 0.32)
        self.play_t(Write(diff_title), FadeIn(canvas), FadeIn(VGroup(q1, q2, q3, state)), t=1.4)
        self.play_t(Indicate(q1, color=GREEN), Indicate(q2, color=GREEN), Indicate(q3, color=GREEN), t=1.2)

        note = self.caption("Parallel-looking readout does not prove it matches TypeSafe's sampler.", ORANGE, 19)
        self.play_t(Write(note), t=0.9)
        src = self.source("Source: razorback16/openjev — DiffusionGemma canvas readout")
        self.play_t(FadeIn(src), t=0.4)

        self.pad_to(308.0)
        self.clear_scene(t=1.0)
        self.pad_to(309.0)

    # ------------------------------------------------------------------
    # 5:05–5:35 — Calibration trap
    # ------------------------------------------------------------------
    def section_calibration(self):
        grid = self.grid()
        hdr = self.section_header("THE CALIBRATION TRAP",
                                  "Softmax confidence is not automatically empirical probability.", RED)
        self.play_t(FadeIn(grid), Write(hdr), t=1.3)

        ninety = Text("90%", font_size=88, color=YELLOW, weight=BOLD).move_to(LEFT * 4.2 + UP * 0.65)
        says = Text("model confidence", font_size=18, color=GREY).next_to(ninety, DOWN, buff=0.15)
        self.play_t(FadeIn(ninety, scale=1.2), FadeIn(says), t=1.0)

        bucket = RoundedRectangle(corner_radius=0.20, width=5.4, height=3.0,
                                  color=GREY, stroke_width=2,
                                  fill_color=PANEL, fill_opacity=0.45).move_to(RIGHT * 2.5 + UP * 0.25)
        dots = VGroup()
        positions = []
        for r in range(2):
            for c in range(5):
                positions.append(RIGHT * (1.0 + c * 0.75) + UP * (0.75 - r * 0.85))
        for i, pos in enumerate(positions):
            col = GREEN if i < 6 else RED
            symbol = "✓" if i < 6 else "×"
            circ = Circle(radius=0.25, color=col, stroke_width=2.5, fill_color=col, fill_opacity=0.14)
            txt = Text(symbol, font_size=22, color=col, weight=BOLD).move_to(circ)
            dots.add(VGroup(circ, txt).move_to(pos))
        btitle = Text("10 predictions near 90% confidence", font_size=18, color=WHITE2)
        btitle.next_to(bucket.get_top(), DOWN, buff=0.18)
        self.play_t(FadeIn(bucket), Write(btitle), LaggedStart(*[FadeIn(d) for d in dots], lag_ratio=0.08), t=1.8)

        empirical = Text("EMPIRICAL ACCURACY: 60%", font_size=28, color=RED, weight=BOLD)
        empirical.move_to(DOWN * 1.72 + RIGHT * 2.5)
        self.play_t(Write(empirical), t=1.0)

        neq = Text("90%  ≠  calibrated 90%", font_size=29, color=ORANGE, weight=BOLD)
        neq.move_to(LEFT * 3.65 + DOWN * 1.45)
        self.play_t(Write(neq), t=0.9)

        self.play_t(FadeOut(VGroup(ninety, says, bucket, dots, btitle, empirical, neq)), t=0.8)

        temp = self.panel("TEMPERATURE SCALING", ["reshape confidence", "argmax unchanged"], TEAL,
                          width=3.45, height=1.8, body_size=15)
        proper = self.panel("PROPER SCORING", ["Brier / log score", "reward honest distributions"], PURPLE,
                            width=3.45, height=1.8, body_size=15)
        outcomes = self.panel("OUTCOME RL", ["reward beliefs against", "what actually happens"], GREEN,
                              width=3.45, height=1.8, body_size=15)
        VGroup(temp, proper, outcomes).arrange(RIGHT, buff=0.5).move_to(UP * 0.45)
        self.play_t(LaggedStart(FadeIn(temp), FadeIn(proper), FadeIn(outcomes), lag_ratio=0.22), t=1.6)

        lesson1 = Text("Softmax score  ≠  calibrated belief", font_size=25, color=YELLOW, weight=BOLD)
        lesson2 = Text("Calibration asks whether confidence matches frequency.", font_size=20, color=WHITE2)
        lessons = VGroup(lesson1, lesson2).arrange(DOWN, buff=0.16).move_to(DOWN * 1.45)
        self.play_t(Write(lessons), t=1.2)

        self.pad_to(345.0)
        self.clear_scene(t=1.0)
        self.pad_to(346.0)

    # ------------------------------------------------------------------
    # 5:35–5:55 — Synthesis / closing
    # ------------------------------------------------------------------
    def section_closing(self):
        grid = self.grid()
        self.play_t(FadeIn(grid), t=0.8)

        title = Text("ONE INTERFACE. AN EXPANDING DESIGN SPACE.", font_size=39, color=CYAN, weight=BOLD)
        title.scale_to_fit_width(min(title.width, 12.3)); title.to_edge(UP, buff=0.35)
        self.play_t(Write(title), t=1.2)

        names = [
            ("Dedicated\nencoder", BLUE2),
            ("Frozen\nlogits", YELLOW),
            ("Fine-tuned\nlogits", PURPLE),
            ("Custom\nheads", ORANGE),
            ("Contrastive\nembeddings", TEAL),
            ("Diffusion\ncanvas", GREEN),
        ]
        cards = VGroup()
        for text, color in names:
            box = RoundedRectangle(corner_radius=0.16, width=1.78, height=1.55,
                                   color=color, stroke_width=2,
                                   fill_color=color, fill_opacity=0.10)
            lab = Text(text, font_size=16, color=WHITE2, line_spacing=0.85, weight=BOLD).move_to(box)
            cards.add(VGroup(box, lab))
        cards.arrange(RIGHT, buff=0.22).move_to(UP * 0.62)
        self.play_t(LaggedStart(*[FadeIn(c, shift=UP * 0.16) for c in cards], lag_ratio=0.12), t=2.0)

        bracket = Line(cards.get_left() + DOWN * 1.15, cards.get_right() + DOWN * 1.15,
                       color=CYAN, stroke_width=4)
        left_tick = Line(bracket.get_start(), bracket.get_start() + UP * 0.20, color=CYAN, stroke_width=4)
        right_tick = Line(bracket.get_end(), bracket.get_end() + UP * 0.20, color=CYAN, stroke_width=4)
        contract = Text("STATE IN  →  TYPED PROBABILITIES OUT", font_size=25, color=CYAN, weight=BOLD)
        contract.next_to(bracket, DOWN, buff=0.18)
        self.play_t(Create(bracket), Create(left_tick), Create(right_tick), Write(contract), t=1.4)

        final = Text("DECISION MODELS ARE BECOMING A CATEGORY,\nNOT A SINGLE ARCHITECTURE.",
                     font_size=31, color=YELLOW, weight=BOLD, line_spacing=0.9)
        final.move_to(DOWN * 2.15)
        self.play_t(Write(final), t=1.5)

        brand = Text("Omniacs.DAO  •  Making Scientific Visualizations with the Omniacs",
                     font_size=14, color=GREY)
        brand.to_edge(DOWN, buff=0.18)
        self.play_t(FadeIn(brand), t=0.5)

        self.pad_to(368.0)
        self.clear_scene(t=1.0)
        self.pad_to(369.0)

    # ------------------------------------------------------------------
    # Main
    # ------------------------------------------------------------------
    def construct(self):
        self.section_hook()            # 0:00–0:30
        self.section_official_jev()    # 0:30–1:00
        self.section_encoders()        # 1:00–1:52
        self.section_frozen_logits()   # 1:52–2:42
        self.section_trained_readout() # 2:42–3:32
        self.section_custom_heads()    # 3:32–4:15
        self.section_clm()             # 4:15–4:42
        self.section_diffusion()       # 4:42–5:05
        self.section_calibration()     # 5:05–5:35
        self.section_closing()         # 5:35–5:55
        print(f"[OpenSourceJevAlternatives] nominal runtime: {self.nominal_elapsed:.1f}s")
