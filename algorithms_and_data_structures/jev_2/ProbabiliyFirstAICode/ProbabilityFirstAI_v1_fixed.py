import sys; sys.path.insert(0, "/home/claude/jev/fix"); sys.path.insert(0, "/home/claude/jev/JEV_Probability_First_AI_bundle")
from common_fix import *
from JEV_Probability_First_AI import *
from JEV_Probability_First_AI import ProbabilityFirstAI as Base

class ProbabilityFirstAIFixed(FixMixin, Base):
    LOG = "/tmp/fix_v1.log"
    def header(self, title, subtitle=None, color=CYAN):
        self._mark(title)
        h = fit(Text(title, font_size=34, color=color, weight=BOLD), 12.3).to_edge(UP, buff=0.32)
        if subtitle:
            s = fit(Text(subtitle, font_size=18, color=GREY_B), 12.0).next_to(h, DOWN, buff=0.10)
            return VGroup(h, s)
        return VGroup(h)
    def panel(self, title, body=None, color=CYAN, width=3.5, height=2.0, title_size=23, body_size=16, fill_opacity=0.38):
        g = super().panel(title, body, color, width, height, title_size, body_size, fill_opacity)
        fit(g[1], width - 0.36, height - 0.3); g[1].move_to(g[0]); return g
    def pill(self, text, color=CYAN, width=None, font_size=18):
        g = super().pill(text, color, width, font_size)
        fit(g[1], g[0].width - 0.3); g[1].move_to(g[0]); return g
    def chat_bubble(self, text, color, width=3.8, height=0.82, font_size=16):
        g = super().chat_bubble(text, color, width, height, font_size)
        fit(g[1], width - 0.3, height - 0.16); g[1].move_to(g[0]); return g
    def caption(self, text, color=YELLOW2, size=22):
        return fit(Text(text, font_size=size, color=color, weight=BOLD), 12.2).to_edge(DOWN, buff=0.35)
    def source_tag(self, text):
        return fit(Text(text, font_size=13, color=GREY2), 6.5).to_corner(DR, buff=0.22)
