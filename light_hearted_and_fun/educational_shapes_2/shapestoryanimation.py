!sudo apt update
!sudo apt install -y ffmpeg libcairo2-dev libpango1.0-dev texlive texlive-latex-extra texlive-fonts-recommended texlive-xetex

!pip install manim
print("✅ Installation complete!")

from manim import *
import numpy as np
from IPython.display import Video, display
import os
import numpy as np

class ShapeStoryAnimation(Scene):
    def construct(self):

        circle = Circle(radius=1.5, color=YELLOW, fill_opacity=0.8, stroke_width=3)
        circle_label = Text("Circle", font_size=24, color=YELLOW).next_to(circle, DOWN, buff=0.8)

        circle_code = Text(
            "circle = Circle(radius=1.5, color=YELLOW, fill_opacity=0.8)",
            font_size=18,
            color=WHITE,
            font="monospace"
        ).to_corner(UL, buff=0.3)

        code_bg = Rectangle(
            width=circle_code.width + 0.4,
            height=circle_code.height + 0.2,
            color=BLACK,
            fill_opacity=0.8,
            stroke_color=WHITE,
            stroke_width=1
        ).move_to(circle_code.get_center())

        self.play(Create(circle), Write(circle_label))
        self.play(Create(code_bg), Write(circle_code), run_time=1.5)
        self.wait(0.8)

        sun_rays = VGroup()
        for i in range(12):
            angle = i * PI / 6
            start_point = circle.get_center() + 1.8 * np.array([np.cos(angle), np.sin(angle), 0])
            end_point = circle.get_center() + 2.4 * np.array([np.cos(angle), np.sin(angle), 0])
            ray = Line(start_point, end_point, color=YELLOW, stroke_width=4)
            sun_rays.add(ray)

        sun_label = Text("Sun", font_size=24, color=YELLOW).next_to(circle, DOWN, buff=1.0)

        sun_code = Text(
            "# Create sun rays with loop\nfor i in range(12):\n    ray = Line(..., color=YELLOW)\n    sun_rays.add(ray)",
            font_size=14,
            color=WHITE,
            font="monospace",
            line_spacing=1.2
        ).to_corner(UR, buff=0.3)

        sun_code_bg = Rectangle(
            width=sun_code.width + 0.4,
            height=sun_code.height + 0.2,
            color=BLACK,
            fill_opacity=0.8,
            stroke_color=WHITE,
            stroke_width=1
        ).move_to(sun_code.get_center())

        self.play(FadeOut(circle_code), FadeOut(code_bg))
        self.play(Create(sun_code_bg), Write(sun_code), run_time=1.5)
        self.play(
            Create(sun_rays),
            Transform(circle_label, sun_label),
            run_time=2
        )
        self.wait(1)


        oval = Ellipse(width=3, height=1.8, color=WHITE, fill_opacity=0.9, stroke_width=3, stroke_color=BLACK)
        oval_label = Text("Oval", font_size=24, color=BLACK).next_to(oval, DOWN, buff=0.8)

        oval_code = Text(
            "oval = Ellipse(width=3, height=1.8, color=WHITE)",
            font_size=18,
            color=WHITE,
            font="monospace"
        ).to_corner(UL, buff=0.3)

        oval_code_bg = Rectangle(
            width=oval_code.width + 0.4,
            height=oval_code.height + 0.2,
            color=BLACK,
            fill_opacity=0.8,
            stroke_color=WHITE,
            stroke_width=1
        ).move_to(oval_code.get_center())

        self.play(FadeOut(sun_code), FadeOut(sun_code_bg))
        self.play(Create(oval_code_bg), Write(oval_code), run_time=1.5)
        self.play(
            Transform(circle, oval),
            Transform(circle_label, oval_label),
            FadeOut(sun_rays),
            run_time=2
        )
        self.wait(0.8)

        iris = Circle(radius=0.6, color=BLUE, fill_opacity=1).move_to(oval.get_center())
        pupil = Circle(radius=0.25, color=BLACK, fill_opacity=1).move_to(oval.get_center())
        eye_shine = Circle(radius=0.08, color=WHITE, fill_opacity=1).move_to(oval.get_center() + 0.1*UP + 0.1*LEFT)

        eye_label = Text("Eye", font_size=24, color=BLUE).next_to(oval, DOWN, buff=0.5)

        eye_code = Text(
            "# Create eye parts\niris = Circle(radius=0.6, color=BLUE)\npupil = Circle(radius=0.25, color=BLACK)",
            font_size=14,
            color=WHITE,
            font="monospace",
            line_spacing=1.2
        ).to_corner(UR, buff=0.3)

        eye_code_bg = Rectangle(
            width=eye_code.width + 0.4,
            height=eye_code.height + 0.2,
            color=BLACK,
            fill_opacity=0.8,
            stroke_color=WHITE,
            stroke_width=1
        ).move_to(eye_code.get_center())

        self.play(FadeOut(oval_code), FadeOut(oval_code_bg))
        self.play(Create(eye_code_bg), Write(eye_code), run_time=1.5)
        self.play(
            Create(iris),
            Create(pupil),
            Create(eye_shine),
            Transform(circle_label, eye_label),
            run_time=2
        )
        self.wait(1)

        square = Square(side_length=2.5, color="#8B4513", fill_opacity=0.3, stroke_width=4)
        square_label = Text("Square", font_size=24, color="#8B4513").next_to(square, DOWN, buff=0.5)

        square_code = Text(
            'square = Square(side_length=2.5, color="#8B4513")',
            font_size=18,
            color=WHITE,
            font="monospace"
        ).to_corner(UL, buff=0.3)

        square_code_bg = Rectangle(
            width=square_code.width + 0.4,
            height=square_code.height + 0.2,
            color=BLACK,
            fill_opacity=0.8,
            stroke_color=WHITE,
            stroke_width=1
        ).move_to(square_code.get_center())

        self.play(FadeOut(eye_code), FadeOut(eye_code_bg))
        self.play(Create(square_code_bg), Write(square_code), run_time=1.5)
        self.play(
            Transform(circle, square),
            Transform(circle_label, square_label),
            FadeOut(iris),
            FadeOut(pupil),
            FadeOut(eye_shine),
            run_time=2
        )
        self.wait(0.8)

        clock_face = Circle(radius=1.1, color=WHITE, fill_opacity=0.9, stroke_width=3, stroke_color=BLACK).move_to(square.get_center())

        hour_hand = Line(clock_face.get_center(), clock_face.get_center() + 0.6*UP, color=BLACK, stroke_width=6)
        minute_hand = Line(clock_face.get_center(), clock_face.get_center() + 0.8*RIGHT, color=BLACK, stroke_width=4)
        center_dot = Circle(radius=0.05, color=BLACK, fill_opacity=1).move_to(clock_face.get_center())

        twelve = Text("12", font_size=16, color=BLACK).move_to(clock_face.get_center() + 0.8*UP)
        three = Text("3", font_size=16, color=BLACK).move_to(clock_face.get_center() + 0.8*RIGHT)
        six = Text("6", font_size=16, color=BLACK).move_to(clock_face.get_center() + 0.8*DOWN)
        nine = Text("9", font_size=16, color=BLACK).move_to(clock_face.get_center() + 0.8*LEFT)

        clock_label = Text("Clock", font_size=24, color="#8B4513").next_to(square, DOWN, buff=0.5)

        clock_code = Text(
            "# Create clock components\nclock_face = Circle(radius=1.1, color=WHITE)\nhour_hand = Line(center, center + 0.6*UP)",
            font_size=14,
            color=WHITE,
            font="monospace",
            line_spacing=1.2
        ).to_corner(UR, buff=0.3)

        clock_code_bg = Rectangle(
            width=clock_code.width + 0.4,
            height=clock_code.height + 0.2,
            color=BLACK,
            fill_opacity=0.8,
            stroke_color=WHITE,
            stroke_width=1
        ).move_to(clock_code.get_center())

        self.play(FadeOut(square_code), FadeOut(square_code_bg))
        self.play(Create(clock_code_bg), Write(clock_code), run_time=1.5)
        self.play(
            Create(clock_face),
            Create(hour_hand),
            Create(minute_hand),
            Create(center_dot),
            Write(twelve),
            Write(three),
            Write(six),
            Write(nine),
            Transform(circle_label, clock_label),
            run_time=2.5
        )
        self.wait(1)

        triangle = RegularPolygon(3, radius=1.8, color=RED, fill_opacity=0.4, stroke_width=4)
        triangle_label = Text("Triangle", font_size=24, color=RED).next_to(triangle, DOWN, buff=0.5)

        triangle_code = Text(
            "triangle = RegularPolygon(3, radius=1.8, color=RED)",
            font_size=18,
            color=WHITE,
            font="monospace"
        ).to_corner(UL, buff=0.3)

        triangle_code_bg = Rectangle(
            width=triangle_code.width + 0.4,
            height=triangle_code.height + 0.2,
            color=BLACK,
            fill_opacity=0.8,
            stroke_color=WHITE,
            stroke_width=1
        ).move_to(triangle_code.get_center())

        self.play(FadeOut(clock_code), FadeOut(clock_code_bg))
        self.play(Create(triangle_code_bg), Write(triangle_code), run_time=1.5)
        self.play(
            Transform(circle, triangle),
            Transform(circle_label, triangle_label),
            FadeOut(clock_face),
            FadeOut(hour_hand),
            FadeOut(minute_hand),
            FadeOut(center_dot),
            FadeOut(twelve),
            FadeOut(three),
            FadeOut(six),
            FadeOut(nine),
            run_time=2
        )
        self.wait(0.8)

        # Hat top
        hat_top = triangle.copy()

        # Hat brim
        hat_brim = Ellipse(width=4, height=1, color=RED, fill_opacity=0.7, stroke_width=3)
        hat_brim.next_to(triangle, DOWN, buff=-0.1)
        # Hat band
        hat_band = Rectangle(width=3, height=0.25, color="#FFD700", fill_opacity=1, stroke_width=2)
        hat_band.move_to(triangle.get_bottom() + UP * 0.1)

        # Small hat decoration
        hat_decoration = Circle(radius=0.15, color="#FFD700", fill_opacity=1)
        hat_decoration.move_to(triangle.get_center() + LEFT * 0.8)

        hat_label = Text("Hat", font_size=24, color=RED).next_to(hat_brim, DOWN, buff=0.5)

        # Code annotation for hat
        hat_code = Text(
            "# Build hat from shapes\nhat_brim = Ellipse(width=4, height=1, color=RED)\nhat_band = Rectangle(width=3, height=0.25)",
            font_size=14,
            color=WHITE,
            font="monospace",
            line_spacing=1.2
        ).to_corner(UR, buff=0.3)

        hat_code_bg = Rectangle(
            width=hat_code.width + 0.4,
            height=hat_code.height + 0.2,
            color=BLACK,
            fill_opacity=0.8,
            stroke_color=WHITE,
            stroke_width=1
        ).move_to(hat_code.get_center())

        self.play(FadeOut(triangle_code), FadeOut(triangle_code_bg))
        self.play(Create(hat_code_bg), Write(hat_code), run_time=1.5)
        self.play(
            Create(hat_brim),
            Create(hat_band),
            Create(hat_decoration),
            Transform(circle_label, hat_label),
            run_time=2
        )
        self.wait(1.5)

        self.play(
            FadeOut(circle),
            FadeOut(circle_label),
            FadeOut(hat_brim),
            FadeOut(hat_band),
            FadeOut(hat_decoration),
            FadeOut(hat_code),
            FadeOut(hat_code_bg),
            run_time=1
        )
        self.wait(0.5)

        house_title = Text("Building a House with Shapes!", font_size=28, color=WHITE)
        self.play(Write(house_title))
        self.wait(1)
        self.play(house_title.animate.to_edge(UP))

        house_code = Text(
            "# Building house step by step\nroof = RegularPolygon(3,\n  radius=1.8, color=RED)\nroof.shift(RIGHT * 1.5 +\n  DOWN * 0.5)\nwalls = Rectangle(\n  width=3, height=2,\n  color=YELLOW)\nwalls.move_to(\n  roof.get_bottom() +\n  DOWN * walls.height/2)\ndoor = Rectangle(\n  width=0.5, height=1,\n  color='#654321')\nwindow1 = Square(\n  side_length=0.6,\n  color='#87CEEB')\nwindow2 = Square(\n  side_length=0.6,\n  color='#87CEEB')\nclouds = Ellipse(\n  width=1.2, height=0.7,\n  color=WHITE)",
            font_size=10,
            color=WHITE,
            font="monospace",
            line_spacing=1.1
        ).to_corner(DL, buff=0.3)

        house_code_bg = Rectangle(
            width=house_code.width + 0.4,
            height=house_code.height + 0.2,
            color=BLACK,
            fill_opacity=0.9,
            stroke_color=WHITE,
            stroke_width=1
        ).move_to(house_code.get_center())

        self.play(Create(house_code_bg), Write(house_code), run_time=2)


        roof = RegularPolygon(3, radius=1.8, color=RED, fill_opacity=0.8, stroke_width=4)
        roof.shift(RIGHT * 1.5 + DOWN * 0.5)  # Move house to the right and down
        roof_label = Text("Triangle Roof", font_size=18, color=RED).next_to(roof, RIGHT, buff=0.5)

        self.play(Create(roof), Write(roof_label), run_time=1.5)
        self.wait(0.8)

        walls = Rectangle(width=3, height=2, color=YELLOW, fill_opacity=0.7, stroke_width=4)
        roof_bottom = roof.get_bottom()
        walls.move_to(roof_bottom + DOWN * walls.height/2)
        wall_label = Text("Rectangle Walls", font_size=18, color=YELLOW).move_to(walls.get_center() + RIGHT * 2.5 + DOWN * 1.2)

        self.play(Create(walls), Write(wall_label), run_time=1.5)
        self.wait(0.8)

        door = Rectangle(width=0.5, height=1, color="#654321", fill_opacity=0.9, stroke_width=3)
        door.move_to(walls.get_center() + DOWN * 0.3)
        doorknob = Circle(radius=0.04, color="#FFD700", fill_opacity=1, stroke_width=1)
        doorknob.move_to(door.get_center() + LEFT * 0.15 + UP * 0.05)
        door_label = Text("Rectangle Door", font_size=18, color="#654321").next_to(door, DOWN, buff=0.4)

        self.play(Create(door), Create(doorknob), Write(door_label), run_time=1.5)
        self.wait(0.8)

        window1 = Square(side_length=0.6, color="#87CEEB", fill_opacity=0.8, stroke_width=3)
        window1.move_to(walls.get_center() + UP * 0.3 + LEFT * 1.0)
        window2 = Square(side_length=0.6, color="#87CEEB", fill_opacity=0.8, stroke_width=3)
        window2.move_to(walls.get_center() + UP * 0.3 + RIGHT * 1.0)

        pane1_v = Line(window1.get_top(), window1.get_bottom(), color=WHITE, stroke_width=3)
        pane1_h = Line(window1.get_left(), window1.get_right(), color=WHITE, stroke_width=3)
        pane2_v = Line(window2.get_top(), window2.get_bottom(), color=WHITE, stroke_width=3)
        pane2_h = Line(window2.get_left(), window2.get_right(), color=WHITE, stroke_width=3)

        window_label = Text("Square Windows", font_size=18, color="#87CEEB").next_to(window2, RIGHT, buff=0.4)

        self.play(
            Create(window1), Create(window2),
            Create(pane1_v), Create(pane1_h), Create(pane2_v), Create(pane2_h),
            Write(window_label),
            run_time=2
        )
        self.wait(0.8)

        cloud1 = Ellipse(width=1.2, height=0.7, color=WHITE, fill_opacity=0.9, stroke_width=2)
        cloud1.move_to(roof.get_center() + UP * 1.8 + LEFT * 2.5)
        cloud2 = Ellipse(width=1, height=0.6, color=WHITE, fill_opacity=0.9, stroke_width=2)
        cloud2.move_to(roof.get_center() + UP * 2 + RIGHT * 2.8)
        cloud3 = Ellipse(width=0.8, height=0.5, color=WHITE, fill_opacity=0.9, stroke_width=2)
        cloud3.move_to(roof.get_center() + UP * 1.5 + LEFT * 4)

        sun_in_sky.move_to(roof.get_center() + UP * 2.2 + LEFT * 1)
        sun_rays_sky = VGroup()
        for i in range(8):
            angle = i * PI / 4
            start_point = sun_in_sky.get_center() + 0.6 * np.array([np.cos(angle), np.sin(angle), 0])
            end_point = sun_in_sky.get_center() + 0.8 * np.array([np.cos(angle), np.sin(angle), 0])
            ray = Line(start_point, end_point, color=YELLOW, stroke_width=2)
            sun_rays_sky.add(ray)

        self.play(
            Create(cloud1), Create(cloud2), Create(cloud3),
            Create(sun_in_sky), Create(sun_rays_sky),
            run_time=2
        )
        self.wait(1)

        house_parts = VGroup(roof, walls, door, doorknob, window1, window2, pane1_v, pane1_h, pane2_v, pane2_h)
        self.play(
            house_parts.animate.scale(1.05),
            run_time=1
        )
        self.play(
            house_parts.animate.scale(1/1.05),
            run_time=1
        )

        self.wait(2)
        self.play(FadeOut(Group(*self.mobjects)), run_time=1.5)

        credits_title = Text("Sources Used", font_size=42, color=BLUE, weight=BOLD)
        credits_title.to_edge(UP, buff=1)
        self.play(Write(credits_title))
        self.wait(1)

        # Create credit entries
        credit_entries = VGroup()

        # Pixabay Icon
        pixabay_icon = VGroup(
            Circle(radius=0.3, fill_color=GREEN, fill_opacity=0.8, stroke_color=WHITE),
            Text("P", font_size=20, color=WHITE, weight=BOLD)
        )
        pixabay_text = Text("Pixabay - Music", font_size=24, color=WHITE)
        pixabay_entry = VGroup(pixabay_icon, pixabay_text)
        pixabay_entry.arrange(RIGHT, buff=0.5)

        # Canva Icon
        canva_icon = VGroup(
            RoundedRectangle(width=0.6, height=0.6, corner_radius=0.3,
                           fill_color=PURPLE, fill_opacity=0.8, stroke_color=WHITE),
            Text("C", font_size=20, color=WHITE, weight=BOLD)
        )
        canva_text = Text("Canva - Video Editing", font_size=24, color=WHITE)
        canva_entry = VGroup(canva_icon, canva_text)
        canva_entry.arrange(RIGHT, buff=0.5)

        # Arrange all credits
        credit_entries.add(pixabay_entry, canva_entry)
        credit_entries.arrange(DOWN, buff=0.8, aligned_edge=LEFT)
        credit_entries.move_to(ORIGIN + DOWN * 0.5)

        # Animate each credit entry
        for entry in credit_entries:
            self.play(
                FadeIn(entry[0], shift=RIGHT*0.5),
                Write(entry[1], run_time=1.5)
            )
            self.wait(0.5)

        self.wait(2)
        self.play(FadeOut(Group(*self.mobjects)), run_time=1)

# %%manim -qh ShapeStoryAnimation
