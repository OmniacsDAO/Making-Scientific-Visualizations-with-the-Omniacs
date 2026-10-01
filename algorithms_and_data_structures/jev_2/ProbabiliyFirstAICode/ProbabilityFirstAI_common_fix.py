from manim import *
import json
Text.set_default(font="Montserrat")
SAFE_X, SAFE_Y = 6.85, 3.9

def fit(m, w=None, h=None):
    if w and m.width > w: m.scale_to_fit_width(w)
    if h and m.height > h: m.scale_to_fit_height(h)
    return m

class FixMixin:
    LOG = "/tmp/fix.log"
    def _init_fix(self):
        if not hasattr(self, "_tl"):
            self._tl = []; self._cur_title = "start"; open(self.LOG, "w").close()
    def _mark(self, title):
        self._init_fix(); self._cur_title = title
        self._tl.append(dict(title=title, t=self.renderer.time))
        json.dump(self._tl, open(self.LOG.replace(".log", "_timeline.json"), "w"), indent=0)
    def play(self, *a, **k):
        self._init_fix()
        super().play(*a, **k)
        for m in self.mobjects:
            if m.width > 15.5 or m.height > 9: continue   # full-frame backgrounds/grids
            l, r, tp, bt = m.get_left()[0], m.get_right()[0], m.get_top()[1], m.get_bottom()[1]
            if l < -SAFE_X - 0.02 or r > SAFE_X + 0.02 or tp > SAFE_Y + 0.02 or bt < -SAFE_Y - 0.02:
                with open(self.LOG, "a") as f:
                    f.write(f"{self.renderer.time:7.2f} [{self._cur_title}] {type(m).__name__} x[{l:.2f},{r:.2f}] y[{bt:.2f},{tp:.2f}] {self._txt(m)}\n")
    def _txt(self, m):
        for s in m.get_family():
            if isinstance(s, Text): return repr(s.original_text[:40])
        return ""
