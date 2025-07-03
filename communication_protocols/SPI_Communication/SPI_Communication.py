from manim import *

CPOL = 0
CPHA = 0

class Main(Scene):
    def plot_step_function(
        self, data_bits, axe, color, initial_y, CPHA=0, dy=0, disabled=True
    ):
        initial_x = 1.5 if CPHA else 0 if disabled else 0.5
        start_x = initial_x
        start_y = initial_y
        stroke_width_data = 8
        stroke_width_empty = 2

        # Adjusting the initial line to extend from the start of the x-axis
        if not disabled:
            additional_line = Line(
                axe.c2p(axe.x_range[0], start_y),
                axe.c2p(initial_x, start_y),
                color=color,
                stroke_width=stroke_width_empty,
            )
            self.play(Create(additional_line), run_time=0.25)

        for i, bit in enumerate(data_bits):
            end_x = initial_x + i + 1
            line = Line(
                axe.c2p(start_x, start_y),
                axe.c2p(end_x, start_y),
                color=color,
                stroke_width=stroke_width_data if bit == 1 else stroke_width_empty,
            )

            if CPHA and i == len(data_bits) - 1:
                pass
            else:
                self.play(Create(line), run_time=0.25)

            if i < len(data_bits) - 1 and data_bits[i + 1] != bit:
                transition_line = Line(
                    axe.c2p(end_x, start_y),
                    axe.c2p(end_x, initial_y - dy + data_bits[i + 1]),
                    color=color,
                    stroke_width=stroke_width_empty,
                )
                self.play(Create(transition_line), run_time=0.1)

            start_x = end_x
            start_y = (
                initial_y - dy + data_bits[i + 1]
                if i < len(data_bits) - 1
                else initial_y - dy
            )

        # Adjusting the final line to extend to the end of the x-axis
        if not disabled:
            additional_line = Line(
                axe.c2p(initial_x + len(data_bits), start_y),
                axe.c2p(axe.x_range[1], start_y),
                color=color,
                stroke_width=stroke_width_empty,
            )
            self.play(Create(additional_line), run_time=0.25)

    def generate_clock_signal(self, length, axe, color, initial_y, CPOL=0):
        start_x = 1
        start_y = initial_y + 1 if CPOL else initial_y
        stroke_width_data = 6
        stroke_width_empty = 2

        # Adjusting the initial line to extend from the start of the x-axis
        no_clock_line_1 = Line(
            axe.c2p(axe.x_range[0], start_y),
            axe.c2p(start_x, start_y),
            color=color,
            stroke_width=stroke_width_empty,
        )
        self.play(Create(no_clock_line_1), run_time=0.25)

        for i in range(start_x, length + 1):
            end_x = i + 0.25

            low_state_start = Line(
                axe.c2p(start_x, start_y),
                axe.c2p(end_x, start_y),
                color=color,
                stroke_width=stroke_width_empty,
            )

            rising_edge = Line(
                axe.c2p(end_x, start_y),
                axe.c2p(end_x, start_y - 1 if CPOL else start_y + 1),
                color=color,
                stroke_width=stroke_width_data,
            )

            high_state = Line(
                axe.c2p(end_x, start_y - 1 if CPOL else start_y + 1),
                axe.c2p(end_x + 0.5, start_y - 1 if CPOL else start_y + 1),
                color=color,
                stroke_width=stroke_width_empty,
            )

            falling_edge = Line(
                axe.c2p(end_x + 0.5, start_y - 1 if CPOL else start_y + 1),
                axe.c2p(end_x + 0.5, start_y),
                color=color,
                stroke_width=stroke_width_data,
            )

            low_state_end = Line(
                axe.c2p(end_x + 0.5, start_y),
                axe.c2p(end_x + 0.75, start_y),
                color=color,
                stroke_width=stroke_width_empty,
            )

            self.play(Create(low_state_start), run_time=0.1)
            self.play(Create(rising_edge), run_time=0.25)
            self.play(Create(high_state), run_time=0.1)
            self.play(Create(falling_edge), run_time=0.25)
            self.play(Create(low_state_end), run_time=0.1)

            start_x = start_x + 1

        # Adjusting the final line to extend to the end of the x-axis
        no_clock_line_2 = Line(
            axe.c2p(length + 1, start_y),
            axe.c2p(axe.x_range[1], start_y),
            color=color,
            stroke_width=stroke_width_empty,
        )
        self.play(Create(no_clock_line_2), run_time=0.25)

    def create_dotted_lines(self, axe, length, run_time=0.2):
        animations = []
        for i in range(1, length + 1):
            dotted_line = DashedLine(
                axe.c2p(i, 0),
                axe.c2p(i, 7.25),
                dash_length=0.05,
                dashed_ratio=0.3,
                color="GREY",
            )
            animations.append(Create(dotted_line))
        return AnimationGroup(*animations, run_time=run_time)
    
    def construct(self):
        cs_line_data =   [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0]
        mosi_line_data = [0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0]
        miso_line_data = [0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0]

        axe = (
            Axes(
                x_range=[0, 18, 1],
                y_range=[0, 7.25, 1],
                x_length=28,
                y_length=14,
                axis_config={"tip_shape": StealthTip, "tip_length": 0.1},
                x_axis_config={
                    "include_numbers": True,
                    "include_tip": False,
                    "numbers_to_exclude": [0, 18],
                },
            )
            .scale(0.35)
            .shift(RIGHT * 0.5, DOWN * 0.25)
        )
        extra_y_axis = (
            axe.get_y_axis()
            .copy()
            .next_to(axe, RIGHT, buff=0)
            .align_to(DOWN)
            .shift(LEFT * 0.08, UP * 0.1)
        )

        cs_line_label = (
            Text("CS", font="Cascadia Code", color="BLUE")
            .scale(0.5)
            .next_to(axe, LEFT, buff=0.1)
            .align_to(axe, DOWN)
            .shift(UP * 4.25)
        )

        cs_transition_line = Line(
            axe.c2p(13, 6),
            axe.c2p(13, 7),
            color="BLUE",
        )
        cs_disable_line = Line(
            axe.c2p(13, 7),
            axe.c2p(14, 7),
            color="BLUE",
        )

        sclk_line_label = (
            Text("SCLK", font="Cascadia Code", color="YELLOW")
            .scale(0.5)
            .next_to(axe, LEFT, buff=0.1)
            .align_to(axe, DOWN)
            .shift(UP * 2.9)
        )

        mosi_line_label = (
            Text("MOSI", font="Cascadia Code", color="GREY")
            .scale(0.5)
            .next_to(axe, LEFT, buff=0.1)
            .align_to(axe, DOWN)
            .shift(UP * 1.55)
        )

        miso_line_label = (
            Text("MISO", font="Cascadia Code", color="GREEN")
            .scale(0.5)
            .next_to(axe, LEFT, buff=0.1)
            .align_to(axe, DOWN)
            .shift(UP * 0.25)
        )

        borders = SurroundingRectangle(
            axe,
            color="BLACK",
            fill_color="PURPLE",
            fill_opacity=0,
            buff=0.25,
        )

        # title
        title = Text("SPI Communication Protocol Animation", font="Cascadia Code", font_size=24, color="BLUE").to_edge(UP*0.5)
        self.play(Create(title), run_time=1)  # Use Manim's Create method for title animation

        self.wait(2)

        # Adding axes and labels
        self.play(Create(axe), Create(extra_y_axis), run_time=1.5)
        self.wait(0.25)

        # Create dotted lines animation
        dotted_lines_animation = self.create_dotted_lines(axe, 17, run_time=3)
        self.play(dotted_lines_animation)
        
        self.wait(0.5)

        # CS/SS Line
        self.play(Write(cs_line_label))
        self.wait(0.25)
        self.plot_step_function(cs_line_data, axe, "BLUE", initial_y=7, dy=1)
        self.wait(0.25)

        # SCLK Line
        self.play(Write(sclk_line_label))
        self.wait(0.25)
        self.generate_clock_signal(12, axe, "RED", initial_y=4, CPOL=CPOL)
        self.wait(0.25)

        # MOSI Line
        self.play(Write(mosi_line_label))
        self.wait(0.25)
        self.plot_step_function(
            mosi_line_data, axe, "PURPLE", CPHA=CPHA, initial_y=2, disabled=False
        )
        self.wait(0.25)

        # MISO Line
        self.play(Write(miso_line_label))
        self.wait(0.25)
        self.plot_step_function(
            miso_line_data, axe, "GREEN", CPHA=CPHA, initial_y=0, disabled=False
        )
        self.wait(0.25)

        # End CS/SS Line
        self.play(Create(cs_transition_line), run_time=0.1)
        self.wait(0.25)
        self.play(Create(cs_disable_line), run_time=0.25)
        self.wait(0.5)

        # Title at the end
        self.play(Write(title))
        self.wait(2)
        
        # Fade out all elements in the scene
        self.play(
            *[FadeOut(mob) for mob in self.mobjects],  # Fade out all objects in the scene
            run_time=4,
            rate_func=rate_functions.smooth  # Make the fade-out smooth
        )