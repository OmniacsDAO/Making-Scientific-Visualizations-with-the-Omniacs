import sys; sys.path.insert(0, "/home/claude/jev/fix"); sys.path.insert(0, "/home/claude/jev/Open_Source_JEV_Alternatives_bundle/open_source_jev_video")
from common_fix import *
from Open_Source_JEV_Alternatives import *
from Open_Source_JEV_Alternatives import OpenSourceJevAlternatives as Base

class OpenSourceJevAlternativesFixed(FixMixin, Base):
    LOG = "/tmp/fix_v2.log"
    def section_header(self, title, subtitle=None, color=CYAN):
        self._mark(title)
        h = fit(Text(title, font_size=36, color=color, weight=BOLD), 12.3).to_edge(UP, buff=0.30)
        if subtitle:
            s = fit(Text(subtitle, font_size=18, color=GREY), 12.0).next_to(h, DOWN, buff=0.10)
            return VGroup(h, s)
        return VGroup(h)
    def panel(self, title, lines=None, color=CYAN, width=3.3, height=2.0, title_size=22, body_size=16, fill=PANEL, opacity=0.44):
        g = super().panel(title, lines, color, width, height, title_size, body_size, fill, opacity)
        fit(g[1], width - 0.4, height - 0.32); g[1].move_to(g[0]); return g
    def caption(self, text, color=YELLOW, size=22):
        return fit(Text(text, font_size=size, color=color, weight=BOLD), 12.2).to_edge(DOWN, buff=0.32)
    def source(self, text):
        return fit(Text(text, font_size=12, color=GREY), 6.4).to_corner(DR, buff=0.18)
