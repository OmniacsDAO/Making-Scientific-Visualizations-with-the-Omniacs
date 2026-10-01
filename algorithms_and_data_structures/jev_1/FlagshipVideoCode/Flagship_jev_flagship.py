from manim import *
import json, numpy as np

config.background_color = "#0A0F1E"
META = json.load(open("/home/claude/jev/flag/vo_meta.json"))
SEG = {m["id"]: m for m in META}
GAP = 0.45

CY, VI, AM, GR, RD, PK = "#22D3EE", "#A78BFA", "#FBBF24", "#34D399", "#F87171", "#F472B6"
WH, MU, PANEL, BG = "#F1F5F9", "#94A3B8", "#111A2E", "#0A0F1E"
HF, MF = "Montserrat", "Space Mono"
CONTENT_TOP, CONTENT_BOT = 2.35, -2.8


def T(s, size=28, color=WH, font=HF, weight=NORMAL, max_w=None, max_h=None):
    t = Text(s, font=font, font_size=size, color=color, weight=weight)
    if max_w and t.width > max_w: t.scale_to_fit_width(max_w)
    if max_h and t.height > max_h: t.scale_to_fit_height(max_h)
    return t


def card(title, body=None, color=CY, w=3.2, h=1.6, ts=26, bs=20, fill=PANEL):
    box = RoundedRectangle(corner_radius=0.18, width=w, height=h, stroke_color=color, stroke_width=3,
                           fill_color=fill, fill_opacity=0.96)
    pad = 0.24
    items = [T(title, ts, color, weight=BOLD, max_w=w - 2 * pad)]
    if body:
        items.append(VGroup(*[T(l, bs, WH, max_w=w - 2 * pad) for l in body.split("\n")]).arrange(DOWN, buff=0.08))
    c = VGroup(*items).arrange(DOWN, buff=0.14)
    if c.height > h - 2 * pad: c.scale_to_fit_height(h - 2 * pad)
    if c.width > w - 2 * pad: c.scale_to_fit_width(w - 2 * pad)
    c.move_to(box)
    return VGroup(box, c)


def chip(s, color=CY, size=20, solid=False, font=MF):
    t = T(s, size, BG if solid else color, font=font, weight=BOLD)
    r = RoundedRectangle(corner_radius=0.12, width=t.width + 0.36, height=t.height + 0.26, stroke_color=color,
                         stroke_width=2, fill_color=color if solid else PANEL, fill_opacity=1)
    t.move_to(r)
    return VGroup(r, t)


def header(title, sub=None, color=CY):
    h = T(title, 42, color, weight=BOLD, max_w=12.6).move_to(UP * 3.3)
    g = VGroup(h)
    if sub:
        g.add(T(sub, 20, MU, font=MF, max_w=12.6).next_to(h, DOWN, buff=0.14))
    return g


def prob_rows(labels, vals, colors, track_w=3.0, size=22, label_w=1.9):
    rows = VGroup()
    for lab, v, col in zip(labels, vals, colors):
        slot = Rectangle(width=label_w, height=0.42, stroke_width=0, fill_opacity=0)
        lg = VGroup(slot)
        if lab:
            lt = T(lab, size, col, font=MF, weight=BOLD, max_w=label_w).move_to(slot, aligned_edge=LEFT)
            lg.add(lt)
        track = RoundedRectangle(corner_radius=0.08, width=track_w, height=0.32, stroke_width=0, fill_color="#1E293B", fill_opacity=1).next_to(slot, RIGHT, buff=0.25)
        fillr = RoundedRectangle(corner_radius=0.08, width=max(0.06, track_w * v), height=0.32, stroke_width=0, fill_color=col, fill_opacity=1).move_to(track, aligned_edge=LEFT)
        pct = T(f"{int(round(v * 100))}%", size, WH, font=MF, weight=BOLD).next_to(track, RIGHT, buff=0.2)
        rows.add(VGroup(lg, track, fillr, pct))
    rows.arrange(DOWN, buff=0.28, aligned_edge=LEFT)
    return rows


def grow_rows(rows, rt=1.2):
    return AnimationGroup(*[AnimationGroup(FadeIn(r[0]), FadeIn(r[1]), GrowFromEdge(r[2], LEFT), FadeIn(r[3])) for r in rows], lag_ratio=0, run_time=rt)


def lock_icon(color=MU, s=0.22):
    body = RoundedRectangle(corner_radius=0.04, width=s * 1.4, height=s, fill_color=color, fill_opacity=1, stroke_width=0)
    arc = Arc(radius=s * 0.45, start_angle=0, angle=PI, stroke_color=color, stroke_width=4).next_to(body, UP, buff=-0.02)
    return VGroup(body, arc)


class JevExplained(Scene):
    # ---------- infrastructure ----------
    def setup_captions(self):
        self.cap_band = Rectangle(width=14.4, height=1.05, fill_color=BLACK, fill_opacity=0.6, stroke_width=0).to_edge(DOWN, buff=0)
        self.cap = VGroup()
        self.cur = None
        def upd(m):
            if self.cur is None: return
            t = self.renderer.time - self.cur["t0"]
            idx = None
            for i, (a, b) in enumerate(self.cur["times"]):
                if a <= t < b + 0.25: idx = i
            if idx != self.cur["idx"]:
                self.cur["idx"] = idx
                m.submobjects = [self.cur["mobs"][idx]] if idx is not None else []
        self.cap.add_updater(upd)
        self.add(self.cap_band, self.cap)

    def cap_mob(self, s):
        t = T(s, 26, WH, max_w=99)
        if t.width > 12.8:
            words = s.split(); best = None
            for i in range(1, len(words)):
                a, b = " ".join(words[:i]), " ".join(words[i:])
                d = abs(len(a) - len(b))
                if best is None or d < best[0]: best = (d, a, b)
            t = VGroup(T(best[1], 24, WH, max_w=12.8), T(best[2], 24, WH, max_w=12.8)).arrange(DOWN, buff=0.08)
        return t.move_to(DOWN * 3.47)

    def begin(self, sid):
        m = SEG[sid]
        self.add_sound(f"/home/claude/jev/flag/vo_{sid}.wav")
        t0 = self.renderer.time
        self.tlog.append(dict(id=sid, t0=t0))
        json.dump(self.tlog, open("/home/claude/jev/flag/timeline.json", "w"))
        tot = sum(len(c) for c in m["captions"]); acc = 0; times = []
        for c in m["captions"]:
            s = acc / tot * m["dur"]; acc += len(c); times.append((s, acc / tot * m["dur"]))
        
        self.seg_end = t0 + m["dur"] + GAP
        self.sid = sid

    def fill(self):
        rem = self.seg_end - self.renderer.time
        if rem > 0.02: self.wait(rem)

    def chk(self, mob):
        l, r = mob.get_left()[0], mob.get_right()[0]; tp, bt = mob.get_top()[1], mob.get_bottom()[1]
        bad = []
        if l < -6.95 or r > 6.95: bad.append(f"x[{l:.2f},{r:.2f}]")
        if bt < CONTENT_BOT: bad.append(f"bottom {bt:.2f}")
        if tp > 3.95: bad.append(f"top {tp:.2f}")
        if bad:
            with open("/home/claude/jev/flag/overflow.log", "a") as f: f.write(f"{self.sid}: {' '.join(bad)}\n")
        return mob

    def clear(self, rt=0.45):
        mobs = [m for m in self.mobjects if m not in (self.cap_band, self.cap)]
        if mobs: self.play(*[FadeOut(m) for m in mobs], run_time=rt)

    # ---------- the film ----------
    def construct(self):
        open("/home/claude/jev/flag/overflow.log", "w").close()
        self.tlog = []
        self.cap_band = VMobject(); self.cap = VMobject()
        self.sid = "intro"
        self.intro()
        for s in ["hook", "pitch", "public", "vocab", "options", "calib", "roots", "sales1", "sales2", "route1", "route2",
                  "caution", "wave", "fam1", "fam2", "fam3", "fam4", "fam5", "same", "close"]:
            getattr(self, "s_" + s)()
        self.outro()

    def intro(self):
        bars = VGroup(*[Rectangle(width=0.5, height=h, fill_color=c, fill_opacity=0.18, stroke_width=0)
                        for h, c in zip([3.2, 1.2, 0.5, 2.2, 0.8], [GR, AM, RD, CY, VI])]).arrange(RIGHT, buff=0.35, aligned_edge=DOWN).move_to(DOWN * 0.6)
        title = T("JEV, EXPLAINED", 88, CY, weight=BOLD, max_w=12.4).move_to(UP * 0.55)
        sub = T("The AI that decides instead of talks", 34, WH, max_w=12).next_to(title, DOWN, buff=0.3)
        tag = T("state in  ·  probabilities out", 22, MU, font=MF).next_to(sub, DOWN, buff=0.3)
        self.play(LaggedStart(*[GrowFromEdge(b, DOWN) for b in bars], lag_ratio=0.12), run_time=1.2)
        self.play(Write(title), run_time=1.1)
        self.play(FadeIn(sub, shift=UP * 0.2), FadeIn(tag), run_time=0.8)
        self.wait(1.3)

    def s_hook(self):
        self.begin("hook"); self.clear()
        hd = header("Two ways to make a decision")
        lp = card("LANGUAGE MODEL", None, VI, w=6.1, h=4.3).move_to(LEFT * 3.35 + DOWN * 0.3)
        rp = card("DECISION MODEL", None, GR, w=6.1, h=4.3).move_to(RIGHT * 3.35 + DOWN * 0.3)
        for p in (lp, rp): p[1].move_to(p[0].get_top() + DOWN * 0.42)
        q1 = chip("Approve this loan?", WH, 20).next_to(lp[1], DOWN, buff=0.25)
        q2 = chip("Approve this loan?", WH, 20).next_to(rp[1], DOWN, buff=0.25)
        toks = ["Based", "on", "the", "applicant's", "income", "history,", "it", "appears", "that", "the", "overall",
                "risk", "profile", "is", "moderate,", "and", "therefore..."]
        tchips = VGroup(*[chip(w, VI, 17, font=HF) for w in toks])
        rows, row, wsum = VGroup(), VGroup(), 0
        for c in tchips:
            if wsum + c.width > 5.4 and len(row):
                rows.add(row.arrange(RIGHT, buff=0.08)); row = VGroup(); wsum = 0
            row.add(c); wsum += c.width + 0.08
        rows.add(row.arrange(RIGHT, buff=0.08))
        rows.arrange(DOWN, buff=0.12, aligned_edge=LEFT).next_to(q1, DOWN, buff=0.3)
        if rows.width > 5.6: rows.scale_to_fit_width(5.6)
        if rows.height > 2.05: rows.scale_to_fit_height(2.05); rows.next_to(q1, DOWN, buff=0.3)
        rows.set_x(lp.get_x())
        cnt = T("one token at a time...", 20, MU, font=MF).move_to(lp[0].get_bottom() + UP * 0.28)
        pr = prob_rows(["APPROVE", "REVIEW", "DENY"], [0.82, 0.13, 0.05], [GR, AM, RD], track_w=2.6).next_to(q2, DOWN, buff=0.4).set_x(rp.get_x())
        conf = T("confidence  0.91", 22, CY, font=MF, weight=BOLD).next_to(pr, DOWN, buff=0.35).set_x(rp.get_x())
        self.chk(VGroup(hd, lp, rp, rows, pr, conf))
        self.play(FadeIn(hd), FadeIn(lp), FadeIn(rp), run_time=0.8)
        self.play(FadeIn(q1), FadeIn(q2), run_time=0.4)
        self.play(LaggedStart(*[FadeIn(c, shift=RIGHT * 0.1) for c in tchips], lag_ratio=1.0), FadeIn(cnt), run_time=4.6, rate_func=linear)
        self.play(grow_rows(pr, 1.0), run_time=1.0)
        self.play(FadeIn(conf, shift=UP * 0.1), Circumscribe(rp[0], color=GR), run_time=1.2)
        self.fill()

    def s_pitch(self):
        self.begin("pitch"); self.clear()
        hd = header("What TypeSafe says Jev does", "public launch description · Sept 2026")
        a = card("UNSTRUCTURED STATE", "emails · chats\nJSON · logs", CY, w=3.6, h=2.0).move_to(LEFT * 4.55)
        j = card("JEV", "System One model", AM, w=2.7, h=2.0, ts=44).move_to(ORIGIN)
        outs = VGroup(chip("choice: approve  0.82", GR, 18), chip("risk: high  0.64", AM, 18), chip("escalate: no  0.18", VI, 18)).arrange(DOWN, buff=0.18)
        b = card("TYPED DECISIONS", None, GR, w=3.8, h=2.6).move_to(RIGHT * 4.55)
        b[1].move_to(b[0].get_top() + DOWN * 0.35); outs.next_to(b[1], DOWN, buff=0.2)
        if outs.width > 3.5: outs.scale_to_fit_width(3.5)
        outs.set_x(b.get_x())
        a1 = Arrow(a.get_right(), j.get_left(), buff=0.12, color=MU); a2 = Arrow(j.get_right(), b.get_left(), buff=0.12, color=MU)
        g = VGroup(a, j, b, outs).shift(DOWN * 0.2); a1.shift(DOWN * 0.2); a2.shift(DOWN * 0.2)
        self.chk(VGroup(hd, g))
        self.play(FadeIn(hd), run_time=0.5)
        self.play(FadeIn(a, shift=RIGHT * 0.3), run_time=0.7)
        self.play(GrowArrow(a1), FadeIn(j, scale=0.8), run_time=0.8)
        dots = VGroup(*[Dot(a.get_right() + DOWN * 0.2, radius=0.06, color=CY) for _ in range(4)])
        self.play(LaggedStart(*[MoveAlongPath(d, Line(a.get_right() + DOWN * 0.2, j.get_left() + DOWN * 0.2)) for d in dots], lag_ratio=0.25), run_time=1.2)
        self.remove(dots)
        self.play(GrowArrow(a2), FadeIn(b), run_time=0.7)
        self.play(LaggedStart(*[FadeIn(o, shift=LEFT * 0.2) for o in outs], lag_ratio=0.3), run_time=1.1)
        self.play(Indicate(j[1][0], color=AM, scale_factor=1.15), run_time=0.8)
        self.fill()

    def s_public(self):
        self.begin("public"); self.clear()
        hd = header("What's public, and what isn't")
        cards = VGroup(card("NEW", "architecture", CY, w=3.8, h=1.7, ts=30),
                       card("PARALLEL", "sampler", VI, w=3.8, h=1.7, ts=30),
                       card("RLCD", "Reinforcement Learning\nfor Calibrated Decisions", AM, w=3.8, h=1.7, ts=30)).arrange(RIGHT, buff=0.35).move_to(UP * 0.95)
        lab = T("NOT PUBLISHED", 24, RD, font=MF, weight=BOLD).move_to(DOWN * 0.75)
        locks = VGroup()
        for s in ["model weights", "architecture spec", "training corpus", "RLCD recipe"]:
            c = chip(s, MU, 19); li = lock_icon().next_to(c, LEFT, buff=0.12); locks.add(VGroup(li, c))
        locks.arrange(RIGHT, buff=0.35).next_to(lab, DOWN, buff=0.35)
        if locks.width > 12.4: locks.scale_to_fit_width(12.4)
        self.chk(VGroup(hd, cards, lab, locks))
        self.play(FadeIn(hd), run_time=0.5)
        self.play(LaggedStart(*[FadeIn(c, shift=UP * 0.3) for c in cards], lag_ratio=0.45), run_time=4.5)
        self.wait(2.2)
        self.play(FadeIn(lab), run_time=0.5)
        self.play(LaggedStart(*[FadeIn(l, shift=UP * 0.2) for l in locks], lag_ratio=0.35), run_time=2.5)
        self.play(*[l[1][0].animate.set_stroke(RD) for l in locks], run_time=0.6)
        self.fill()

    def s_vocab(self):
        self.begin("vocab"); self.clear()
        hd = header("The decision is buried in the vocabulary")
        words = ["the", "Based", "I", "It", "We", "This", "However", "In", "yes", "Sure", "Paris", "banana", "maybe",
                 "loan", "no", "risk", "cat", "=", "{", "therefore", "42", "quantum", "hello", "apply"]
        strip = VGroup(*[chip(w, CY if w == "yes" else MU, 18, font=HF) for w in words * 2]).arrange(RIGHT, buff=0.12).move_to(UP * 1.65).align_to(LEFT * 6.8, LEFT)
        ax = Axes(x_range=[0, 60, 10], y_range=[0, 0.3, 0.1], x_length=9.0, y_length=2.6,
                  axis_config={"color": MU, "include_ticks": False}).move_to(DOWN * 0.95 + LEFT * 1.3)
        vals = [0.26 * np.exp(-i / 7) + 0.004 for i in range(60)]
        bars = VGroup(*[Rectangle(width=0.1, height=max(0.02, v / 0.3 * 2.6), fill_color=(CY if i == 23 else VI), fill_opacity=0.9 if i == 23 else 0.55, stroke_width=0)
                        .move_to(ax.c2p(i + 0.5, 0), aligned_edge=DOWN) for i, v in enumerate(vals)])
        ylab = T("next-token probability", 18, MU, font=MF).next_to(ax, UP, buff=0.05).align_to(ax, LEFT)
        note = card("\"yes\"", "≈ 1 of 150,000\ntokens", CY, w=2.9, h=1.6).move_to(RIGHT * 4.9 + DOWN * 0.8)
        arr = Arrow(note.get_left(), bars[23].get_top() + UP * 0.05, buff=0.1, color=CY)
        clip = Rectangle(width=14.2, height=0.8).move_to(UP * 1.65)
        self.chk(VGroup(hd, ax, note, ylab))
        self.play(FadeIn(hd), FadeIn(strip), run_time=0.6)
        self.play(strip.animate.shift(LEFT * 7), run_time=4.0, rate_func=linear)
        self.play(Create(ax), FadeIn(ylab), LaggedStart(*[GrowFromEdge(b, DOWN) for b in bars], lag_ratio=0.03), strip.animate.shift(LEFT * 2.5), run_time=2.5)
        self.play(FadeIn(note, shift=LEFT * 0.2), GrowArrow(arr), Flash(bars[23].get_top(), color=CY), run_time=1.2)
        self.fill()

    def s_options(self):
        self.begin("options"); self.clear()
        hd = header("A decision model scores only the options", color=GR)
        st = card("STATE", "loan application\n+ history", CY, w=3.2, h=1.9).move_to(LEFT * 4.7 + DOWN * 0.25)
        pr = prob_rows(["APPROVE", "REVIEW", "DENY"], [0.82, 0.13, 0.05], [GR, AM, RD], track_w=3.6, size=26, label_w=2.2).move_to(RIGHT * 1.9 + DOWN * 0.25)
        arrs = VGroup(*[Arrow(st.get_right(), r[0].get_left(), buff=0.15, color=MU, stroke_width=4) for r in pr])
        tag = T("one pass  ·  all options  ·  one distribution", 22, GR, font=MF, weight=BOLD, max_w=12).move_to(DOWN * 2.35)
        self.chk(VGroup(hd, st, pr, tag))
        self.play(FadeIn(hd), FadeIn(st, shift=RIGHT * 0.2), run_time=0.8)
        self.play(*[GrowArrow(a) for a in arrs], *[FadeIn(r[0]) for r in pr], *[FadeIn(r[1]) for r in pr], run_time=1.0)
        self.play(grow_rows(pr, 1.3))
        self.play(FadeIn(tag, shift=UP * 0.2), run_time=0.7)
        self.fill()

    def s_calib(self):
        self.begin("calib"); self.clear()
        hd = header("Calibration: 70% should mean 70%", color=AM)
        ax = Axes(x_range=[0, 1, 0.5], y_range=[0, 1, 0.5], x_length=4.2, y_length=4.2, axis_config={"color": MU},
                  tips=False).move_to(LEFT * 3.2 + DOWN * 0.1)
        xl = T("model says", 18, MU, font=MF).next_to(ax, DOWN, buff=0.12)
        yl = T("actually right", 18, MU, font=MF).rotate(PI / 2).next_to(ax, LEFT, buff=0.12)
        diag = DashedLine(ax.c2p(0, 0), ax.c2p(1, 1), color=MU)
        over = ax.plot(lambda x: x ** 2.3, color=RD, stroke_width=5)
        cal = ax.plot(lambda x: x + 0.03 * np.sin(x * 9), color=GR, stroke_width=5)
        dot = Dot(ax.c2p(0.7, 0.7 + 0.03 * np.sin(6.3)), color=WH, radius=0.09)
        g1 = DashedLine(ax.c2p(0.7, 0), dot.get_center(), color=WH, stroke_width=2); g2 = DashedLine(ax.c2p(0, 0.7), dot.get_center(), color=WH, stroke_width=2)
        c1 = card("OVERCONFIDENT", "says 90%\nright ~60%", RD, w=3.9, h=1.7).move_to(RIGHT * 3.6 + UP * 0.75)
        c2 = card("CALIBRATED", "says 70%\nright 70%", GR, w=3.9, h=1.7).move_to(RIGHT * 3.6 + DOWN * 1.25)
        self.chk(VGroup(hd, ax, xl, yl, c1, c2))
        self.play(FadeIn(hd), Create(ax), FadeIn(xl), FadeIn(yl), run_time=1.0)
        self.play(Create(diag), run_time=0.7)
        self.play(Create(over), FadeIn(c1, shift=LEFT * 0.2), run_time=1.4)
        self.play(Create(cal), FadeIn(c2, shift=LEFT * 0.2), run_time=1.4)
        self.play(FadeIn(dot, scale=2), Create(g1), Create(g2), run_time=1.0)
        self.play(Indicate(c2, color=GR, scale_factor=1.04), run_time=1.0)
        self.fill()

    def s_roots(self):
        self.begin("roots"); self.clear()
        hd = header("The open research trail", color=VI)
        line = Line(LEFT * 5.6, RIGHT * 5.6, color=MU, stroke_width=4).move_to(DOWN * 0.1)
        pts = [(-4.0, "MAR 2025", "SalesRLAgent", CY), (0.0, "SEP 2025", "confidence routing", VI), (4.0, "SEP 2026", "Jev launches", AM)]
        marks = VGroup()
        for x, d, n, c in pts:
            dt = Dot(RIGHT * x + DOWN * 0.1, radius=0.14, color=c)
            a = T(d, 24, c, font=MF, weight=BOLD).next_to(dt, UP, buff=0.3)
            b = T(n, 24, WH, max_w=3.6).next_to(dt, DOWN, buff=0.3)
            marks.add(VGroup(dt, a, b))
        self.chk(VGroup(hd, line, marks))
        self.play(FadeIn(hd), Create(line), run_time=0.9)
        self.play(LaggedStart(*[FadeIn(m, shift=UP * 0.2) for m in marks], lag_ratio=0.5), run_time=2.4)
        self.fill()

    def s_sales1(self):
        self.begin("sales1"); self.clear()
        hd = header("March 2025: a conversation becomes a state", "SalesRLAgent · arXiv 2503.23303", CY)
        msgs = ["How much does it cost?", "Budget is about $1k a month.", "Could we book a demo?"]
        bub = VGroup(*[card(m, None, CY if i % 2 == 0 else VI, w=4.0, h=0.78, ts=20) for i, m in enumerate(msgs)]).arrange(DOWN, buff=0.22).move_to(LEFT * 4.55 + DOWN * 0.35)
        r = np.random.default_rng(3)
        vec = VGroup(*[Rectangle(width=0.1, height=r.uniform(0.15, 1.4), fill_color=CY, fill_opacity=0.85, stroke_width=0) for _ in range(26)]).arrange(RIGHT, buff=0.05, aligned_edge=DOWN).move_to(UP * 0.35)
        vl = T("embedding · 3,072 dims", 18, CY, font=MF).next_to(vec, DOWN, buff=0.15)
        feats = VGroup(chip("stage", AM, 17), chip("sentiment", AM, 17), chip("objections", AM, 17)).arrange(RIGHT, buff=0.12).next_to(vl, DOWN, buff=0.35)
        fl = T("+ conversation features", 18, AM, font=MF).next_to(feats, DOWN, buff=0.12)
        mid = VGroup(vec, vl, feats, fl).move_to(DOWN * 0.35)
        st = card("STATE", "what the conversation\nis right now", AM, w=3.3, h=1.9).move_to(RIGHT * 4.75 + DOWN * 0.35)
        a1 = Arrow(bub.get_right(), mid.get_left(), buff=0.15, color=MU); a2 = Arrow(mid.get_right(), st.get_left(), buff=0.15, color=MU)
        self.chk(VGroup(hd, bub, mid, st))
        self.play(FadeIn(hd), run_time=0.5)
        self.play(LaggedStart(*[FadeIn(b, shift=RIGHT * 0.3) for b in bub], lag_ratio=0.5), run_time=2.2)
        self.play(GrowArrow(a1), LaggedStart(*[GrowFromEdge(v, DOWN) for v in vec], lag_ratio=0.05), FadeIn(vl), run_time=2.0)
        self.play(LaggedStart(*[FadeIn(f, scale=0.8) for f in feats], lag_ratio=0.3), FadeIn(fl), run_time=1.4)
        self.play(GrowArrow(a2), FadeIn(st, shift=LEFT * 0.2), run_time=1.0)
        self.fill()

    def s_sales2(self):
        self.begin("sales2"); self.clear()
        hd = header("The action is a probability", "PPO policy · reward = the sale converts", GR)
        flow = VGroup(card("STATE", None, AM, w=2.6, h=0.95, ts=24), card("POLICY (PPO)", None, VI, w=3.0, h=0.95, ts=24),
                      card("p(convert)", None, GR, w=2.8, h=0.95, ts=24)).arrange(RIGHT, buff=0.8).move_to(UP * 1.55)
        fa = VGroup(*[Arrow(flow[i].get_right(), flow[i + 1].get_left(), buff=0.1, color=MU) for i in range(2)])
        ax = Axes(x_range=[1, 8, 1], y_range=[0, 1, 0.5], x_length=9.2, y_length=2.7, axis_config={"color": MU},
                  tips=False).move_to(DOWN * 1.05)
        xl = T("conversation turn", 18, MU, font=MF).next_to(ax, DOWN, buff=0.08).align_to(ax, RIGHT)
        vals = [0.22, 0.31, 0.27, 0.45, 0.52, 0.46, 0.66, 0.74]
        pts = [ax.c2p(i + 1, v) for i, v in enumerate(vals)]
        path = VMobject(color=GR, stroke_width=5).set_points_as_corners(pts)
        dots = VGroup(*[Dot(p, radius=0.07, color=GR) for p in pts])
        end = T("74%", 30, GR, font=MF, weight=BOLD).next_to(pts[-1], UP, buff=0.18)
        rew = chip("reward +1 if it converts", AM, 18).move_to(ax.c2p(2.6, 0.9))
        self.chk(VGroup(hd, flow, ax, xl, end, rew))
        self.play(FadeIn(hd), run_time=0.5)
        self.play(LaggedStart(FadeIn(flow[0]), GrowArrow(fa[0]), FadeIn(flow[1]), GrowArrow(fa[1]), FadeIn(flow[2]), lag_ratio=0.4), run_time=2.6)
        self.play(Create(ax), FadeIn(xl), run_time=0.9)
        self.play(Create(path), LaggedStart(*[FadeIn(d, scale=2) for d in dots], lag_ratio=0.2), run_time=4.5, rate_func=linear)
        self.play(FadeIn(end, shift=UP * 0.2), Flash(pts[-1], color=GR), run_time=0.9)
        self.play(FadeIn(rew, shift=DOWN * 0.2), run_time=0.8)
        self.fill()

    def s_route1(self):
        self.begin("route1"); self.clear()
        hd = header("September 2025: confidence becomes control flow", "confidence-aware routing · arXiv 2510.01237", VI)
        ins = VGroup(card("SEMANTIC ALIGNMENT", None, CY, w=3.9, h=0.95, ts=21), card("INTERNAL CONVERGENCE", None, VI, w=3.9, h=0.95, ts=21),
                     card("LEARNED CONFIDENCE", None, AM, w=3.9, h=0.95, ts=21)).arrange(DOWN, buff=0.35).move_to(LEFT * 4.5 + DOWN * 0.35)
        c = VGroup(Circle(radius=0.95, color=AM, stroke_width=5, fill_color=PANEL, fill_opacity=1), T("C", 54, AM, weight=BOLD)).move_to(LEFT * 0.6 + DOWN * 0.35)
        cl = T("one score", 20, MU, font=MF).next_to(c, DOWN, buff=0.15)
        arr = VGroup(*[Arrow(i.get_right(), c.get_left(), buff=0.1, color=MU) for i in ins])
        self.route_c = VGroup(c, cl)
        self.chk(VGroup(hd, ins, c, cl))
        self.play(FadeIn(hd), run_time=0.5)
        self.play(LaggedStart(*[FadeIn(i, shift=RIGHT * 0.3) for i in ins], lag_ratio=0.5), run_time=4.0)
        self.play(*[GrowArrow(a) for a in arr], run_time=0.9)
        self.play(DrawBorderThenFill(c), FadeIn(cl), run_time=1.3)
        self.fill()

    def s_route2(self):
        self.begin("route2")
        lanes = [("HIGH → small local model", GR), ("MEDIUM → add retrieval", CY), ("LOW → larger model", AM), ("VERY LOW → a human", RD)]
        cards = VGroup(*[card(s, None, col, w=4.6, h=0.78, ts=21) for s, col in lanes]).arrange(DOWN, buff=0.22).move_to(RIGHT * 4.25 + DOWN * 0.35)
        c = self.route_c[0]
        arrs = VGroup(*[Arrow(c.get_right(), k.get_left(), buff=0.1, color=MU, stroke_width=3) for k in cards])
        self.chk(cards)
        self.play(LaggedStart(*[AnimationGroup(GrowArrow(a), FadeIn(k)) for a, k in zip(arrs, cards)], lag_ratio=0.2), run_time=1.4)
        for a, k, (_, col) in zip(arrs, cards, lanes):
            d = Dot(c.get_right(), radius=0.1, color=col)
            self.play(MoveAlongPath(d, Line(a.get_start(), a.get_end())), run_time=0.9)
            self.play(Indicate(k, color=col, scale_factor=1.05), FadeOut(d), run_time=0.9)
        self.fill()

    def s_caution(self):
        self.begin("caution"); self.clear()
        hd = header("Similar shape. Unproven lineage.", color=AM)
        l = card("WHAT WE CAN SAY", "open 2025 papers describe\na probability-first\ndecision pattern", GR, w=5.4, h=2.4, bs=22).move_to(LEFT * 3.1 + UP * 0.35)
        r = card("WHAT WE CAN'T", "shared code\ndirect lineage\ncopying", RD, w=5.4, h=2.4, bs=22).move_to(RIGHT * 3.1 + UP * 0.35)
        big = T("RESEMBLANCE ≠ PROVENANCE", 46, AM, weight=BOLD, max_w=12).move_to(DOWN * 1.9)
        self.chk(VGroup(hd, l, r, big))
        self.play(FadeIn(hd), run_time=0.5)
        self.play(FadeIn(l, shift=RIGHT * 0.3), run_time=1.0)
        self.wait(2.2)
        self.play(FadeIn(r, shift=LEFT * 0.3), run_time=1.0)
        self.wait(2.8)
        self.play(Write(big), run_time=1.4)
        self.fill()

    FAMS = [("Julia", CY), ("Laya", CY), ("Von", CY), ("Verdict", CY), ("SemIf", AM), ("Reflex", AM), ("Cygnet", AM), ("Hopper", VI),
            ("Nimble", VI), ("JevK5", VI), ("Plumb", VI), ("Decider", VI), ("Kev", GR), ("Open-Jev", GR), ("NanoJev", GR), ("CLM", PK)]

    def s_wave(self):
        self.begin("wave"); self.clear()
        hd = header("The open-source wave", "same interface · very different machines", CY)
        box = card("state  →  probabilities", None, CY, w=6.2, h=1.1, ts=32).move_to(UP * 1.2)
        chips = VGroup(*[chip(n, MU, 19) for n, _ in self.FAMS])
        rows = VGroup(VGroup(*chips[:8]).arrange(RIGHT, buff=0.18), VGroup(*chips[8:]).arrange(RIGHT, buff=0.18)).arrange(DOWN, buff=0.3).move_to(DOWN * 1.15)
        if rows.width > 12.4: rows.scale_to_fit_width(12.4)
        self.chk(VGroup(hd, box, rows))
        self.play(FadeIn(hd), FadeIn(box, scale=0.9), run_time=0.8)
        self.play(LaggedStart(*[FadeIn(c, shift=DOWN * 0.6) for c in chips], lag_ratio=0.12), run_time=3.6)
        self.wait(1.5)
        self.play(*[c[0].animate.set_stroke(col, 3) for c, (_, col) in zip(chips, self.FAMS)],
                  *[c[1].animate.set_color(col) for c, (_, col) in zip(chips, self.FAMS)], run_time=1.2)
        leg = T("5 families", 26, WH, weight=BOLD).next_to(rows, DOWN, buff=0.25)
        if leg.get_bottom()[1] < CONTENT_BOT: leg.next_to(rows, RIGHT, buff=0.3)
        self.play(FadeIn(leg), run_time=0.6)
        self.fill()

    def names_row(self, names, color):
        return VGroup(*[chip(n, color, 20) for n in names]).arrange(RIGHT, buff=0.2).move_to(DOWN * 2.3)

    def s_fam1(self):
        self.begin("fam1"); self.clear()
        hd = header("Family 1 · Build a real decision model", "small encoders trained to score options", CY)
        enc = card("ENCODER", "ModernBERT /\nmmBERT", CY, w=2.7, h=2.0).move_to(LEFT * 5.0 + UP * 0.2)
        opts = VGroup(*[chip(f"[MASK] {o}", WH, 18) for o in ("approve", "review", "deny")]).arrange(DOWN, buff=0.28, aligned_edge=LEFT).move_to(LEFT * 1.75 + UP * 0.2)
        pr = prob_rows(["", "", ""], [0.7, 0.22, 0.08], [GR, AM, RD], track_w=1.5, size=18, label_w=0.1)
        for row, o in zip(pr, opts):
            row[0].set_opacity(0); row[1].next_to(o, RIGHT, buff=0.25); row[2].move_to(row[1], aligned_edge=LEFT); row[3].next_to(row[1], RIGHT, buff=0.15)
        arr = VGroup(*[Arrow(enc.get_right(), o.get_left(), buff=0.1, color=MU, stroke_width=3) for o in opts])
        loop_c = RIGHT * 4.75 + UP * 0.2
        nodes = VGroup(card("explore", "noise", VI, w=1.9, h=0.9, ts=19, bs=15).move_to(loop_c + UP * 1.05),
                       card("score", "proper rule", AM, w=1.9, h=0.9, ts=19, bs=15).move_to(loop_c + RIGHT * 1.0 + DOWN * 0.75),
                       card("update", "REINFORCE", GR, w=1.9, h=0.9, ts=19, bs=15).move_to(loop_c + LEFT * 1.0 + DOWN * 0.75))
        la = VGroup(*[CurvedArrow(nodes[i].get_center() + (nodes[(i + 1) % 3].get_center() - nodes[i].get_center()) * 0.38,
                                  nodes[(i + 1) % 3].get_center() - (nodes[(i + 1) % 3].get_center() - nodes[i].get_center()) * 0.38, angle=-PI / 3, color=MU) for i in range(3)])
        ll = T("Laya's RL loop", 18, MU, font=MF).next_to(nodes, UP, buff=0.12)
        names = self.names_row(["Julia", "Laya", "Von", "Verdict"], CY)
        self.chk(VGroup(hd, enc, opts, pr, nodes, ll, names))
        self.play(FadeIn(hd), FadeIn(enc, shift=RIGHT * 0.2), run_time=0.8)
        self.play(*[GrowArrow(a) for a in arr], LaggedStart(*[FadeIn(o) for o in opts], lag_ratio=0.2), *[FadeIn(r[1]) for r in pr], run_time=1.4)
        self.play(grow_rows(pr, 1.0))
        self.play(LaggedStart(*[FadeIn(n, scale=0.9) for n in names], lag_ratio=0.25), run_time=1.6)
        self.wait(1.6)
        self.play(FadeIn(ll), LaggedStart(*[FadeIn(n) for n in nodes], lag_ratio=0.3), run_time=1.5)
        self.play(*[Create(a) for a in la], run_time=1.0)
        self.play(Rotate(la, angle=2 * PI, about_point=nodes.get_center()), run_time=2.0)
        self.fill()

    def s_fam2(self):
        self.begin("fam2"); self.clear()
        hd = header("Family 2 · The decision model was already inside", "freeze the LLM, read the logits", AM)
        llm = card("FROZEN LLM", "Qwen · Gemma", AM, w=3.0, h=1.9).move_to(LEFT * 4.9 + UP * 0.25)
        fz = chip("0 new weights", AM, 17).next_to(llm, DOWN, buff=0.2)
        r = np.random.default_rng(7)
        hs = r.uniform(0.1, 1.6, 40); idx = {9: "A", 21: "B", 30: "C"}; hs[9], hs[21], hs[30] = 1.5, 0.9, 0.45
        bars = VGroup(*[Rectangle(width=0.09, height=h, fill_color=(AM if i in idx else MU), fill_opacity=0.9, stroke_width=0) for i, h in enumerate(hs)]).arrange(RIGHT, buff=0.04, aligned_edge=DOWN).move_to(LEFT * 0.4 + UP * 0.25)
        labs = VGroup(*[T(l, 20, AM, font=MF, weight=BOLD).next_to(bars[i], DOWN, buff=0.08) for i, l in idx.items()])
        bl = T("all vocabulary logits", 18, MU, font=MF).next_to(bars, UP, buff=0.15)
        pr = prob_rows(["A", "B", "C"], [0.71, 0.22, 0.07], [GR, AM, RD], track_w=1.9, size=22, label_w=0.5).move_to(RIGHT * 4.5 + UP * 0.25)
        sm = T("softmax over A, B, C", 18, GR, font=MF).next_to(pr, UP, buff=0.2)
        a1 = Arrow(llm.get_right(), bars.get_left(), buff=0.15, color=MU); a2 = Arrow(bars.get_right(), pr.get_left(), buff=0.2, color=MU)
        names = self.names_row(["SemIf", "Reflex", "Cygnet"], AM)
        self.chk(VGroup(hd, llm, fz, bars, labs, bl, pr, sm, names))
        self.play(FadeIn(hd), FadeIn(llm), run_time=0.8)
        self.play(FadeIn(fz, scale=0.8), run_time=0.6)
        self.play(GrowArrow(a1), LaggedStart(*[GrowFromEdge(b, DOWN) for b in bars], lag_ratio=0.02), FadeIn(bl), run_time=1.8)
        self.play(*[bars[i].animate.set_opacity(0.12) for i in range(40) if i not in idx], FadeIn(labs), run_time=1.2)
        self.play(GrowArrow(a2), FadeIn(sm), *[FadeIn(rw[0]) for rw in pr], *[FadeIn(rw[1]) for rw in pr], run_time=0.9)
        self.play(grow_rows(pr, 1.1))
        self.play(LaggedStart(*[FadeIn(n) for n in names], lag_ratio=0.3), run_time=1.3)
        self.fill()

    def s_fam3(self):
        self.begin("fam3"); self.clear()
        hd = header("Family 3 · Fine-tune the readout", "a small LoRA adapter makes the logits better probabilities", VI)
        base = card("BASE LLM", "billions of frozen\nparameters", MU, w=3.6, h=2.4).move_to(LEFT * 4.2 + UP * 0.2)
        lora = card("LoRA", "rank 16", VI, w=1.9, h=1.1, ts=26, bs=18).move_to(LEFT * 0.4 + UP * 1.6)
        before = prob_rows(["A", "B"], [0.99, 0.01], [RD, RD], track_w=2.2, size=22, label_w=0.5)
        after = prob_rows(["A", "B"], [0.74, 0.26], [GR, GR], track_w=2.2, size=22, label_w=0.5)
        bt = T("before: overconfident", 20, RD, font=MF, weight=BOLD); at = T("after: calibrated", 20, GR, font=MF, weight=BOLD)
        bg = VGroup(bt, before).arrange(DOWN, buff=0.2, aligned_edge=LEFT).move_to(RIGHT * 3.9 + UP * 0.25)
        ag = VGroup(at, after).arrange(DOWN, buff=0.2, aligned_edge=LEFT).move_to(bg)
        names = self.names_row(["Hopper", "Nimble", "JevK5", "Decider"], VI)
        self.chk(VGroup(hd, base, lora, bg, ag, names))
        self.play(FadeIn(hd), FadeIn(base), run_time=0.8)
        self.play(FadeIn(bt), *[FadeIn(r) for r in before], run_time=0.8)
        self.wait(1.2)
        self.play(lora.animate.next_to(base, RIGHT, buff=-0.05).shift(UP * 0.5), run_time=1.3, rate_func=rate_functions.ease_out_back)
        self.play(Flash(lora.get_left(), color=VI), run_time=0.6)
        self.play(ReplacementTransform(bt, at), *[ReplacementTransform(b, a) for b, a in zip(before, after)], run_time=1.4)
        self.play(LaggedStart(*[FadeIn(n) for n in names], lag_ratio=0.3), run_time=1.5)
        self.fill()

    def s_fam4(self):
        self.begin("fam4"); self.clear()
        hd = header("Family 4 · Replace the language head", "the backbone stays, the readout changes", GR)
        bb = card("QWEN BACKBONE", None, CY, w=3.4, h=3.2).move_to(LEFT * 4.7 + DOWN * 0.1)
        lm = chip("LM head", MU, 18).next_to(bb, UP, buff=0.1).shift(RIGHT * 0.9)
        crs = Cross(lm, stroke_color=RD, stroke_width=5)
        q = VGroup(Dot(radius=0.13, color=GR), T("<decide>", 18, GR, font=MF)).arrange(RIGHT, buff=0.12).move_to(LEFT * 1.3 + DOWN * 0.1)
        keys = VGroup(*[VGroup(Dot(radius=0.11, color=WH), T(f"option {l}", 18, WH, font=MF)).arrange(RIGHT, buff=0.12) for l in "ABC"]).arrange(DOWN, buff=0.55).move_to(RIGHT * 1.6 + DOWN * 0.1)
        ptr = VGroup(*[Arrow(q[0].get_center(), k[0].get_center(), buff=0.14, color=GR if i == 1 else MU, stroke_width=6 if i == 1 else 2) for i, k in enumerate(keys)])
        kv = T("Kev: pointer head", 20, GR, font=MF, weight=BOLD).next_to(keys, UP, buff=0.35).align_to(q, LEFT)
        oj = card("Open-Jev", "scalar head\n= Yes − No", AM, w=2.6, h=1.6, ts=22, bs=18).move_to(RIGHT * 5.1 + DOWN * 0.1)
        names = self.names_row(["Kev", "Open-Jev", "NanoJev"], GR)
        self.chk(VGroup(hd, bb, lm, q, keys, kv, oj, names))
        self.play(FadeIn(hd), FadeIn(bb), FadeIn(lm), run_time=0.9)
        self.play(Create(crs), run_time=0.7)
        self.play(FadeIn(q), LaggedStart(*[FadeIn(k) for k in keys], lag_ratio=0.2), FadeIn(kv), run_time=1.3)
        self.play(LaggedStart(*[GrowArrow(p) for p in ptr], lag_ratio=0.25), run_time=1.3)
        self.play(Indicate(keys[1], color=GR), run_time=0.9)
        self.wait(1.3)
        self.play(FadeIn(oj, shift=LEFT * 0.3), run_time=0.9)
        self.play(LaggedStart(*[FadeIn(n) for n in names], lag_ratio=0.3), run_time=1.2)
        self.fill()

    def s_fam5(self):
        self.begin("fam5"); self.clear()
        hd = header("Family 5 · Decisions as geometry", "contrastive state and action embeddings", PK)
        pl = NumberPlane(x_range=[-4, 4, 1], y_range=[-2.2, 2.2, 1], x_length=7.2, y_length=3.96,
                         background_line_style={"stroke_color": "#1E293B", "stroke_width": 1}, axis_config={"stroke_color": MU}).move_to(LEFT * 1.6 + DOWN * 0.3)
        o = pl.c2p(0, 0)
        sv = Arrow(o, pl.c2p(2.6, 1.3), buff=0, color=CY, stroke_width=7); sl = T("state", 20, CY, font=MF, weight=BOLD).next_to(sv.get_end(), UP, buff=0.1)
        acts = [(2.2, 1.6, GR, "approve"), (-1.8, 1.2, MU, "deny"), (1.2, -1.8, MU, "review")]
        av = VGroup(*[Arrow(o, pl.c2p(x, y), buff=0, color=c, stroke_width=5) for x, y, c, _ in acts])
        al = VGroup(*[T(n, 18, c, font=MF).next_to(pl.c2p(x, y), DOWN if y < 0 else UP, buff=0.1) for x, y, c, n in acts])
        form = card("score = state · action", "closest action wins", PK, w=4.1, h=1.6, ts=22, bs=18).move_to(RIGHT * 4.55 + DOWN * 0.3)
        self.chk(VGroup(hd, pl, sl, al, form))
        self.play(FadeIn(hd), Create(pl), run_time=1.0)
        self.play(GrowArrow(sv), FadeIn(sl), run_time=0.8)
        self.play(LaggedStart(*[GrowArrow(a) for a in av], lag_ratio=0.3), FadeIn(al), run_time=1.3)
        self.play(FadeIn(form, shift=LEFT * 0.2), Indicate(av[0], color=GR), run_time=1.2)
        self.fill()

    def s_same(self):
        self.begin("same"); self.clear()
        hd = header("Same contract. Five different machines.", color=CY)
        top = card("state  →  probabilities", None, CY, w=6.0, h=1.0, ts=30).move_to(UP * 1.45)
        fams = VGroup(*[card(n, None, c, w=2.3, h=1.15, ts=19) for n, c in
                        [("ENCODER", CY), ("FROZEN LOGITS", AM), ("TUNED READOUT", VI), ("CUSTOM HEAD", GR), ("GEOMETRY", PK)]]).arrange(RIGHT, buff=0.22).move_to(DOWN * 0.55)
        arr = VGroup(*[Arrow(f.get_top(), top.get_bottom(), buff=0.1, color=MU, stroke_width=3) for f in fams])
        stamp = chip("NONE OF THEM IS JEV", AM, 24).move_to(DOWN * 2.1)
        self.chk(VGroup(hd, top, fams, stamp))
        self.play(FadeIn(hd), FadeIn(top), run_time=0.7)
        self.play(LaggedStart(*[FadeIn(f, shift=UP * 0.3) for f in fams], lag_ratio=0.2), run_time=1.6)
        self.play(*[GrowArrow(a) for a in arr], run_time=0.8)
        self.play(FadeIn(stamp, scale=1.3), run_time=0.7)
        self.fill()

    def s_close(self):
        self.begin("close"); self.clear()
        a = T("AI that writes what to say", 44, MU, weight=BOLD, max_w=12).move_to(UP * 1.4)
        strike = Line(a.get_left(), a.get_right(), color=RD, stroke_width=6)
        b = T("AI that estimates what to do", 50, CY, weight=BOLD, max_w=12).move_to(UP * 0.1)
        c = T("...and how sure it is.", 42, AM, weight=BOLD, max_w=12).move_to(DOWN * 1.2)
        self.chk(VGroup(a, b, c))
        self.play(FadeIn(a), run_time=0.8)
        self.play(Create(strike), run_time=0.6)
        self.wait(1.2)
        self.play(FadeIn(b, shift=UP * 0.3), run_time=0.9)
        self.wait(1.6)
        self.play(Write(c), run_time=1.1)
        self.fill()

    def outro(self):
        self.tlog.append(dict(id="end", t0=self.renderer.time)); json.dump(self.tlog, open("/home/claude/jev/flag/timeline.json", "w"))
        self.play(*[FadeOut(m) for m in self.mobjects], run_time=0.8)
        t = T("JEV, EXPLAINED", 70, CY, weight=BOLD).move_to(UP * 0.4)
        s = T("sources and papers in the description", 26, MU, font=MF).next_to(t, DOWN, buff=0.35)
        self.play(FadeIn(t, scale=0.9), FadeIn(s), run_time=1.0)
        self.wait(2.6)
        self.play(FadeOut(t), FadeOut(s), run_time=1.0)
