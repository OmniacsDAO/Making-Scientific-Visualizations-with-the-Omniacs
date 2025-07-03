from manim import *
config.frame_rate=60
class compass2(Scene):
    def construct(self):
        l = 2
        n = np.sqrt(4.0)  # speed multiplier on second arm
        θ = ValueTracker(0)
        def Zfunc(x):
            return np.exp(x * 1j)
        def splitZ(Z):
            return [Z.real,Z.imag]
        Z1 = always_redraw(lambda:
            Line(
                ORIGIN,
                l*np.array([
                    *splitZ(Zfunc(θ.get_value())),
                    0
                ]),
                color=YELLOW,
            )
        )
        Z2 = always_redraw(lambda:
            Line(
                ORIGIN,
                l*np.array([
                    np.real(Zfunc(n*θ.get_value())),
                    np.imag(Zfunc(n*θ.get_value())),
                    0
                ]),
                color=RED,
            )
            .shift(Z1.get_end())
        )

        self.add(Z1,Z2)
        tpath = TracedPath(Z2.get_end, stroke_color=BLUE)
        self.add(tpath)
        self.play(
            θ.animate.set_value(60*PI),
            run_time=60,
            rate_func=rate_functions.linear
        )
        self.wait()