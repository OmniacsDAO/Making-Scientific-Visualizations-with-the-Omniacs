from manim import *

class OmniacsLogoEducational(Scene):
    def construct(self):
        # Colors
        blue = "#4EC3F7"
        dark_gray = "#5B5B66"
        bg_color = "#F5F5F5"
        self.camera.background_color = bg_color


        def create_logo_components(shift_amount=ORIGIN):
            # Create main body
            body_outer = RoundedRectangle(
                corner_radius=0.5, height=4.2, width=3.1,
                color=dark_gray, fill_color=dark_gray, fill_opacity=1, stroke_width=0
            ).shift(shift_amount + DOWN*0.2)

            body_inner = RoundedRectangle(
                corner_radius=0.38, height=3.6, width=2.5,
                color=blue, fill_color=blue, fill_opacity=1, stroke_width=0
            ).move_to(body_outer.get_center())

            # Eyes
            eye_y = body_outer.get_corner(UL)[1] - 0.65
            eye_x1 = body_outer.get_corner(UL)[0] + 0.65
            eye_x2 = body_outer.get_corner(UL)[0] + 1.05
            eye_radius = 0.13
            eye = Dot(point=[eye_x1, eye_y, 0], radius=eye_radius, color=dark_gray)
            eye2 = Dot(point=[eye_x2, eye_y, 0], radius=eye_radius, color=dark_gray)

            # Antenna
            frame_top_y = body_outer.get_top()[1]
            antenna1_start = [eye_x1, frame_top_y, 0]
            antenna1_control1 = [eye_x1, frame_top_y + 0.25, 0]
            antenna1_control2 = [eye_x1 + 0.08, frame_top_y + 0.35, 0]
            antenna1_end = [eye_x1 + 0.2, frame_top_y + 0.3, 0]

            antenna1 = CubicBezier(
                antenna1_start, antenna1_control1, antenna1_control2, antenna1_end
            ).set_stroke(color=dark_gray, width=8)

            antenna2_x_start = eye_x1 + 0.25
            antenna2_start = [antenna2_x_start, frame_top_y, 0]
            antenna2_control1 = [antenna2_x_start, frame_top_y + 0.25, 0]
            antenna2_control2 = [antenna2_x_start + 0.08, frame_top_y + 0.35, 0]
            antenna2_end = [antenna2_x_start + 0.2, frame_top_y + 0.3, 0]

            antenna2 = CubicBezier(
                antenna2_start, antenna2_control1, antenna2_control2, antenna2_end
            ).set_stroke(color=dark_gray, width=8)

            # Mouth
            mouth_y = body_outer.get_corner(UL)[1] - 1.05
            mouth_start = [body_outer.get_corner(UL)[0] + 0.18, mouth_y, 0]
            mouth_mid = [body_outer.get_corner(UL)[0] + 1.5, mouth_y, 0]
            mouth_end = [body_outer.get_corner(UL)[0] + 2.5, mouth_y + 0.06, 0]

            mouth = VMobject()
            mouth.set_points_as_corners([mouth_start, mouth_mid])
            mouth.append_points(CubicBezier(
                mouth_mid,
                [mouth_mid[0] + 0.2, mouth_mid[1], 0],
                [mouth_end[0] - 0.2, mouth_end[1] - 0.1, 0],
                mouth_end
            ).get_points())
            mouth.set_stroke(color=dark_gray, width=10)

            # Fangs
            fang1_length = 0.32
            fang2_length = 0.44
            fang1_x = eye_x1
            fang1_y = mouth_y - 0.05
            fang1 = Polygon(
                [0, 0, 0], [0.13, -fang1_length, 0], [0.26, 0, 0],
                color=dark_gray, fill_color=dark_gray, fill_opacity=1
            ).scale(0.55).move_to([fang1_x, fang1_y - fang1_length*0.3, 0])

            fang2_x = eye_x2
            fang2_y = mouth_y - 0.05
            fang2 = Polygon(
                [0, 0, 0], [0.18, -fang2_length, 0], [0.36, 0, 0],
                color=dark_gray, fill_color=dark_gray, fill_opacity=1
            ).scale(0.55).move_to([fang2_x, fang2_y - fang2_length*0.3, 0])

            return {
                'body_outer': body_outer,
                'body_inner': body_inner,
                'eye': eye,
                'eye2': eye2,
                'antenna1': antenna1,
                'antenna2': antenna2,
                'antenna1_start': antenna1_start,
                'antenna2_start': antenna2_start,
                'mouth': mouth,
                'fang1': fang1,
                'fang2': fang2,
                'eye_x1': eye_x1,
                'eye_x2': eye_x2,
                'eye_y': eye_y,
                'eye_radius': eye_radius
            }

        def animate_logo(components):
            # Build animation
            self.play(DrawBorderThenFill(components['body_outer']), run_time=1)
            self.play(DrawBorderThenFill(components['body_inner']), run_time=0.8)
            self.play(
                GrowFromCenter(components['eye']),
                GrowFromCenter(components['eye2']),
                run_time=0.6
            )
            self.play(Create(components['antenna1']), Create(components['antenna2']), run_time=1.2)
            self.play(Create(components['mouth']), run_time=0.8)

            #fangs drop
            self.play(
                components['fang1'].animate.shift(UP * 0.2),
                components['fang2'].animate.shift(UP * 0.2),
                run_time=0.01
            )
            self.play(
                components['fang1'].animate.shift(DOWN * 0.2),
                components['fang2'].animate.shift(DOWN * 0.2),
                run_time=0.3
            )

            # blink animation
            for _ in range(2):
                blink1 = Line(
                    start=[components['eye_x1'] - components['eye_radius'], components['eye_y'], 0],
                    end=[components['eye_x1'] + components['eye_radius'], components['eye_y'], 0],
                    stroke_width=8, color=dark_gray
                )
                blink2 = Line(
                    start=[components['eye_x2'] - components['eye_radius'], components['eye_y'], 0],
                    end=[components['eye_x2'] + components['eye_radius'], components['eye_y'], 0],
                    stroke_width=8, color=dark_gray
                )

                self.play(Transform(components['eye'], blink1), Transform(components['eye2'], blink2), run_time=0.1)
                self.play(
                    Transform(components['eye'], Dot(point=[components['eye_x1'], components['eye_y'], 0], radius=components['eye_radius'], color=dark_gray)),
                    Transform(components['eye2'], Dot(point=[components['eye_x2'], components['eye_y'], 0], radius=components['eye_radius'], color=dark_gray)),
                    run_time=0.15
                )
                self.wait(0.8)

            # Antenna wiggle
            self.play(
                Rotate(components['antenna1'], angle=PI/6, about_point=components['antenna1_start']),
                Rotate(components['antenna2'], angle=-PI/6, about_point=components['antenna2_start']),
                run_time=0.4
            )
            self.play(
                Rotate(components['antenna1'], angle=-PI/6, about_point=components['antenna1_start']),
                Rotate(components['antenna2'], angle=PI/6, about_point=components['antenna2_start']),
                run_time=0.4
            )

            # Color pulse
            self.play(components['body_inner'].animate.set_fill(color="#FFD700", opacity=1), run_time=0.5)
            self.play(components['body_inner'].animate.set_fill(color=blue, opacity=1), run_time=0.5)

            # Final bounce
            logo_group = VGroup(
                components['body_outer'], components['body_inner'], components['eye'], components['eye2'],
                components['antenna1'], components['antenna2'], components['mouth'],
                components['fang1'], components['fang2']
            )
            self.play(logo_group.animate.shift(UP * 0.3), run_time=0.4)
            self.play(logo_group.animate.shift(DOWN * 0.3), run_time=0.4)

            return logo_group

        # Create and animate centered logo
        centered_components = create_logo_components(ORIGIN)
        centered_logo = animate_logo(centered_components)
        self.wait(2)

        self.play(FadeOut(centered_logo), run_time=1)
        self.wait(0.5)


        # Create code annotation area on the right side
        code_bg = Rectangle(
            width=5.5, height=7.5,
            fill_color=BLACK, fill_opacity=1.0,
            stroke_color=WHITE, stroke_width=2
        ).to_edge(RIGHT, buff=0.3)

        code_title = Text("Code Walkthrough", color=WHITE, font_size=28, weight=BOLD)
        code_title.move_to(code_bg.get_top() + DOWN*0.5)

        self.play(DrawBorderThenFill(code_bg), Write(code_title), run_time=1)
        current_annotations = VGroup()

        def show_code(code_txt, step_title="", highlight_color="#00FF88"):
            nonlocal current_annotations

            if current_annotations:
                self.remove(current_annotations)
            current_annotations = VGroup()

            step_text = Text(step_title, color=highlight_color, font_size=22, weight=BOLD)
            step_text.move_to(code_bg.get_top() + DOWN*1.0)
            current_annotations.add(step_text)

            code_lines = code_text.strip().split('\n')
            code_group = VGroup()
            max_width = code_bg.get_width() - 0.6

            for i, line in enumerate(code_lines):
                if line.strip():
                    if line.strip().startswith('#'):
                        color = "#AAAAAA"
                    elif any(keyword in line for keyword in ['RoundedRectangle', 'Dot', 'CubicBezier', 'Polygon', 'VMobject', 'Line']):
                        color = "#00FFFF"
                    elif 'self.play' in line:
                        color = "#FF6B6B"
                    elif '=' in line and not line.strip().startswith('#'):
                        color = "#FFD700"
                    else:
                        color = WHITE

                    line_text = Text(
                        line,
                        color=color,
                        font_size=12,
                        font="Arial"
                    )

                    if line_text.get_width() > max_width:
                        scale_factor = max_width / line_text.get_width()
                        line_text.scale(scale_factor)

                    code_group.add(line_text)

            if len(code_group) > 0:
                start_y = code_bg.get_top()[1] - 1.6
                line_height = 0.22

                for i, line in enumerate(code_group):
                    line.move_to([code_bg.get_left()[0] + 0.3, start_y - i * line_height, 0])
                    line.align_to(code_bg.get_left(), LEFT)
                    line.shift(RIGHT * 0.3)

                total_height = len(code_group) * line_height
                available_height = code_bg.get_height() - 2.2

                if total_height > available_height:
                    scale_factor = max(0.7, available_height / total_height)
                    code_group.scale(scale_factor, about_point=code_group.get_top())
                    code_group.move_to([code_bg.get_center()[0], code_bg.get_center()[1] - 0.4, 0])
                    code_group.align_to(code_bg.get_left(), LEFT)
                    code_group.shift(RIGHT * 0.3)

            current_annotations.add(code_group)
            self.add(current_annotations)
            return current_annotations

        # Now recreate the logo on the left side for educational walkthrough
        left_shift = LEFT * 2
        edu_components = create_logo_components(left_shift)

        show_code("""# Setup colors and background
blue = "#4EC3F7"
dark_gray = "#5B5B66"
bg_color = "#F5F5F5"
self.camera.background_color = bg_color""", "Step 1: Environment Setup")
        self.wait(2)

        show_code("""# Create the main body with rounded rectangles
body_outer = RoundedRectangle(
    corner_radius=0.5, height=4.2, width=3.1,
    color=dark_gray, fill_color=dark_gray,
    fill_opacity=1, stroke_width=0
).shift(LEFT*2 + DOWN*0.2)

body_inner = RoundedRectangle(
    corner_radius=0.38, height=3.6, width=2.5,
    color=blue, fill_color=blue,
    fill_opacity=1, stroke_width=0
).move_to(body_outer.get_center())""", "Step 2: Creating Main Body")

        self.play(DrawBorderThenFill(edu_components['body_outer']), run_time=1)
        self.play(DrawBorderThenFill(edu_components['body_inner']), run_time=0.8)
        self.wait(1)

        show_code("""# Create the eyes using Dot objects
eye_y = body_outer.get_corner(UL)[1] - 0.65
eye_x1 = body_outer.get_corner(UL)[0] + 0.65
eye_x2 = body_outer.get_corner(UL)[0] + 1.05
eye_radius = 0.13

eye = Dot(point=[eye_x1, eye_y, 0],
         radius=eye_radius, color=dark_gray)
eye2 = Dot(point=[eye_x2, eye_y, 0],
          radius=eye_radius, color=dark_gray)""", "Step 3: Adding Eyes")

        self.play(
            GrowFromCenter(edu_components['eye']),
            GrowFromCenter(edu_components['eye2']),
            run_time=0.6
        )
        self.wait(1)

        show_code("""# Create curved antennae with CubicBezier
frame_top_y = body_outer.get_top()[1]
antenna1_start = [eye_x1, frame_top_y, 0]
antenna1_control1 = [eye_x1, frame_top_y + 0.25, 0]
antenna1_control2 = [eye_x1 + 0.08, frame_top_y + 0.35, 0]
antenna1_end = [eye_x1 + 0.2, frame_top_y + 0.3, 0]

antenna1 = CubicBezier(
    antenna1_start, antenna1_control1,
    antenna1_control2, antenna1_end
).set_stroke(color=dark_gray, width=8)""", "Step 4: Curved Antennae")

        self.play(Create(edu_components['antenna1']), Create(edu_components['antenna2']), run_time=1.2)
        self.wait(1)

        show_code("""# Create curved mouth using VMobject
mouth_y = body_outer.get_corner(UL)[1] - 1.05
mouth_start = [body_outer.get_corner(UL)[0] + 0.18, mouth_y, 0]
mouth_mid = [body_outer.get_corner(UL)[0] + 1.5, mouth_y, 0]
mouth_end = [body_outer.get_corner(UL)[0] + 2.5, mouth_y + 0.06, 0]

mouth = VMobject()
mouth.set_points_as_corners([mouth_start, mouth_mid])
mouth.append_points(CubicBezier(...).get_points())
mouth.set_stroke(color=dark_gray, width=10)""", "Step 5: Creating Mouth")

        self.play(Create(edu_components['mouth']), run_time=0.8)
        self.wait(1)

        show_code("""# Create triangular fangs using Polygon
fang1_length = 0.32
fang2_length = 0.44
fang1_x = eye_x1
fang1_y = mouth_y - 0.05

fang1 = Polygon(
    [0, 0, 0], [0.13, -fang1_length, 0], [0.26, 0, 0],
    color=dark_gray, fill_color=dark_gray,
    fill_opacity=1
).scale(0.55).move_to([fang1_x, fang1_y - fang1_length*0.3, 0])""", "Step 6: Adding Fangs")

        self.play(
            edu_components['fang1'].animate.shift(UP * 0.2),
            edu_components['fang2'].animate.shift(UP * 0.2),
            run_time=0.01
        )
        self.play(
            edu_components['fang1'].animate.shift(DOWN * 0.2),
            edu_components['fang2'].animate.shift(DOWN * 0.2),
            run_time=0.3
        )
        self.wait(1)

        show_code("""# Create blinking animation with Line objects
for _ in range(2):
    # Create blink shapes (horizontal lines)
    blink1 = Line(
        start=[eye_x1 - eye_radius, eye_y, 0],
        end=[eye_x1 + eye_radius, eye_y, 0],
        stroke_width=8, color=dark_gray
    )

    # Quick blink transformation
    self.play(Transform(eye, blink1), run_time=0.1)
    self.play(Transform(eye, original_dot), run_time=0.15)""", "Step 7: Blinking Animation")

        for _ in range(2):
            blink1 = Line(
                start=[edu_components['eye_x1'] - edu_components['eye_radius'], edu_components['eye_y'], 0],
                end=[edu_components['eye_x1'] + edu_components['eye_radius'], edu_components['eye_y'], 0],
                stroke_width=8, color=dark_gray
            )
            blink2 = Line(
                start=[edu_components['eye_x2'] - edu_components['eye_radius'], edu_components['eye_y'], 0],
                end=[edu_components['eye_x2'] + edu_components['eye_radius'], edu_components['eye_y'], 0],
                stroke_width=8, color=dark_gray
            )

            self.play(Transform(edu_components['eye'], blink1), Transform(edu_components['eye2'], blink2), run_time=0.1)
            self.play(
                Transform(edu_components['eye'], Dot(point=[edu_components['eye_x1'], edu_components['eye_y'], 0], radius=edu_components['eye_radius'], color=dark_gray)),
                Transform(edu_components['eye2'], Dot(point=[edu_components['eye_x2'], edu_components['eye_y'], 0], radius=edu_components['eye_radius'], color=dark_gray)),
                run_time=0.15
            )
            self.wait(0.8)

        show_code("""# Antenna wiggle animation using Rotate
self.play(
    Rotate(antenna1, angle=PI/6, about_point=antenna1_start),
    Rotate(antenna2, angle=-PI/6, about_point=antenna2_start),
    run_time=0.4
)
self.play(
    Rotate(antenna1, angle=-PI/6, about_point=antenna1_start),
    Rotate(antenna2, angle=PI/6, about_point=antenna2_start),
    run_time=0.4
)""", "Step 8: Antenna Wiggle")

        self.play(
            Rotate(edu_components['antenna1'], angle=PI/6, about_point=edu_components['antenna1_start']),
            Rotate(edu_components['antenna2'], angle=-PI/6, about_point=edu_components['antenna2_start']),
            run_time=0.4
        )
        self.play(
            Rotate(edu_components['antenna1'], angle=-PI/6, about_point=edu_components['antenna1_start']),
            Rotate(edu_components['antenna2'], angle=PI/6, about_point=edu_components['antenna2_start']),
            run_time=0.4
        )
        self.wait(1)

        show_code("""# Color pulse effect using animate.set_fill
self.play(
    body_inner.animate.set_fill(color="#FFD700", opacity=1),
    run_time=0.5
)
self.play(
    body_inner.animate.set_fill(color=blue, opacity=1),
    run_time=0.5
)""", "Step 9: Color Pulse")

        self.play(edu_components['body_inner'].animate.set_fill(color="#FFD700", opacity=1), run_time=0.5)
        self.play(edu_components['body_inner'].animate.set_fill(color=blue, opacity=1), run_time=0.5)
        self.wait(1)

        show_code("""# Group animation - bounce effect
logo_group = VGroup(
    body_outer, body_inner, eye, eye2,
    antenna1, antenna2, mouth, fang1, fang2
)

self.play(logo_group.animate.shift(UP * 0.3), run_time=0.4)
self.play(logo_group.animate.shift(DOWN * 0.3), run_time=0.4)""", "Step 10: Group Animation")

        edu_logo_group = VGroup(
            edu_components['body_outer'], edu_components['body_inner'], edu_components['eye'], edu_components['eye2'],
            edu_components['antenna1'], edu_components['antenna2'], edu_components['mouth'],
            edu_components['fang1'], edu_components['fang2']
        )
        self.play(edu_logo_group.animate.shift(UP * 0.3), run_time=0.4)
        self.play(edu_logo_group.animate.shift(DOWN * 0.3), run_time=0.4)

        show_code("""# Complete! Key Manim concepts covered:
# • RoundedRectangle, Dot, Polygon for shapes
# • CubicBezier for smooth curves
# • VMobject for custom paths
# • Transform, Create, DrawBorderThenFill
# • VGroup for grouping objects
# • Rotate, GrowFromCenter for effects
# • Color changes with animate.set_fill()

# To render in colab:%%manim -ql OmniacsLogoEducational""", "Tutorial Complete!")

        self.wait(3)
        self.play(FadeOut(Group(*self.mobjects)), run_time=1.5)

        # Credits
        credits_title = Text("Sources Used", font_size=42, color=BLUE, weight=BOLD)
        credits_title.to_edge(UP, buff=1)
        self.play(Write(credits_title))
        self.wait(1)

        # Create credit entries
        credit_entries = VGroup()

        # Pixabay Icon
        pixabay_icon = VGroup(
            Circle(radius=0.3, fill_color=GREEN, fill_opacity=0.8, stroke_color=WHITE),
            Text("P", font_size=20, color=BLACK, weight=BOLD)
        )
        pixabay_text = Text("Pixabay - Music", font_size=24, color=BLACK)
        pixabay_entry = VGroup(pixabay_icon, pixabay_text)
        pixabay_entry.arrange(RIGHT, buff=0.5)
        pixabay_entry.shift(UP*0.5)

        # Canva Icon
        canva_icon = VGroup(
            RoundedRectangle(width=0.6, height=0.6, corner_radius=0.3,
                           fill_color=PURPLE, fill_opacity=0.8, stroke_color=WHITE),
            Text("C", font_size=20, color=BLACK, weight=BOLD)
        )
        canva_text = Text("Canva - Video Editing", font_size=24, color=BLACK)
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
        self.play(FadeOut(Group(*self.mobjects)), run_time=1.5)
