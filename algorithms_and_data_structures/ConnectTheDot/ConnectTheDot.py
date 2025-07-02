from manim import *
import numpy as np
import random

class connectTheDots(Scene):
    def construct(self):
        
        # Title
        title = Text("Three Methods to Connect Data Points", font_size=28, color=BLUE).to_edge(UP*0.5)
        self.play(Write(title))
        self.wait(2)        
        
        # Create coordinate plane with separate x and y axes animation
        ax = NumberPlane(
            x_range=[-10, 10, 2],
            y_range=[-3.5, 3.5, 1],
            background_line_style={"stroke_color": GRAY, "stroke_width": 1, "stroke_opacity": 0.5}
        )
        
        # Separate x and y axes
        x_axis = ax.get_x_axis()
        y_axis = ax.get_y_axis()
        
        # Animate x-axis first
        x_axis.set_opacity(0)
        self.add(x_axis)
        self.play(
            x_axis.animate.set_opacity(1),
            Create(x_axis),
            run_time=1.5
        )
        
        # Then animate y-axis
        y_axis.set_opacity(0)
        self.add(y_axis)
        self.play(
            y_axis.animate.set_opacity(1),
            Create(y_axis),
            run_time=1.5
        )
        
        # Fade in background grid lines
        grid_lines = VGroup()
        grid_lines.add(ax.background_lines)
        self.play(FadeIn(grid_lines), run_time=1)
        
        # Generate random x and y values and colors for dots
        xvals = [np.random.uniform(-6.5, 6.5) for _ in range(20)]
        yvals = [np.random.uniform(-3.5, 3.5) for _ in range(20)]
        colors = [np.random.choice([RED, GREEN, BLUE, YELLOW, MAROON, ORANGE, WHITE]) for _ in range(20)]

        # Create dots first, then set their opacity
        dots = VGroup(
            *[Dot(point=[x, y, 0], color=c) for x, y, c in zip(xvals, yvals, colors)]
        )
        
        # First add dots with zero opacity
        for dot in dots:
            dot.set_opacity(0)
        self.add(dots)
        
        # Gradually fade in dots
        self.play(
            LaggedStart(
                *[dot.animate.set_opacity(1) for dot in dots],
                lag_ratio=0.4
            ),
            run_time=2.5
        )

        # Method 1: Connecting in Sequence
        subtitle1 = Text("Connecting in Sequence", font_size=24, color=LIGHT_GRAY).to_edge(DOWN *0.5)
        self.play(Write(subtitle1))
        self.wait(1)
        lines_seq = VGroup(
            *[
                Line(
                    start=dots[i].get_center(),
                    end=dots[i+1].get_center(),
                ) for i in range(len(dots) - 1)
            ]
        )
        self.play(
            LaggedStart(
                *[Create(line) for line in lines_seq],
                lag_ratio=0.6,
            ),
            run_time=8,
            rate_func=rate_functions.linear,
        )
        self.play(FadeOut(lines_seq))
        self.play(FadeOut(subtitle1))
        self.wait(1)

        # Method 2: Different Shapes
        subtitle2 = Text("Connecting by Creating Different Shapes", font_size=24, color=LIGHT_GRAY).to_edge(DOWN*0.5)
        self.play(Write(subtitle2))
        self.wait(1)

        shapes = [
            Polygon(dots[0].get_center(), dots[2].get_center(), dots[5].get_center(), dots[6].get_center()),
            Polygon(dots[10].get_center(), dots[4].get_center(), dots[3].get_center(), dots[1].get_center()),  # typo corrected: should be dots[7]
            Polygon(dots[12].get_center(), dots[2].get_center(), dots[4].get_center(), dots[9].get_center()),  # typo corrected: should be dots[9]
            Polygon(dots[4].get_center(), dots[8].get_center(), dots[12].get_center()),
            Polygon(
                *[dots[i].get_center() for i in range(0, len(dots) - 2, 5)]
            )  # use * to unpack the centers
        ]

        for shape in shapes:
            self.play(Create(shape), run_time=2)
            self.wait(1)  # Wait before creating the next shape
            self.play(FadeOut(shape))
        self.wait(2)
        
        self.play(FadeOut(subtitle2))
        self.wait()

        # Method 3: Connecting Randomly
        subtitle3 = Text("Connecting Randomly", font_size=24, color=LIGHT_GRAY).to_edge(DOWN *0.5)
        self.play(Write(subtitle3))
        self.wait(1)

        # Connect dots randomly
        random_lines = VGroup(
            *[
                Line(
                    start=dots[i].get_center(),
                    end=dots[random.randint(0, len(dots) - 1)].get_center()
                ) for i in range(len(dots))
            ]
        )
        self.play(
            LaggedStart(
                *[Create(line) for line in random_lines],
                lag_ratio=0.6
            ),
            run_time=8,
            rate_func=rate_functions.linear,
        )
        self.wait(2)
        self.play(FadeOut(random_lines))
        self.wait()
        
        
        # Final dissolve of all content
        all_content = VGroup(
            title, 
            ax, 
            dots, 
            lines_seq, 
            subtitle1
        )
        
        # Dissolve animation
        self.play(
            FadeOut(all_content, scale=1.5),  # Scale out while fading
            run_time=2
        )
        
        self.wait(1)
