class EducationalShapeEvolution(Scene):
    def construct(self):
        self.camera.background_color = "#0f0f23"

        def display_text(text):
            label = Text(text, font_size=24, color=WHITE)
            label.to_edge(DOWN, buff=0.5)
            return label

        def show_code_line(code_lines, duration=2):
            if isinstance(code_lines, str):
                code_lines = [code_lines]

            code_lines = code_lines[:5]

            code_texts = []
            max_width = 0

            for line in code_lines:
                if len(line) > 50:
                    line = line[:60] + "..."

                code_text = Text(
                    line,
                    font_size=12,
                    color="#cdd6f4",
                    font="Consolas"
                )

                if any(keyword in line for keyword in ["Triangle", "Polygon", "Star", "Circle", "RegularPolygon"]):
                    code_text.set_color("#89b4fa")
                elif any(color in line for color in ["BLUE", "YELLOW", "ORANGE", "GREEN", "RED"]):
                    code_text.set_color("#a6e3a1")
                elif "VGroup" in line or "Line" in line:
                    code_text.set_color("#f9e2af")
                else:
                    code_text.set_color("#cdd6f4")

                code_texts.append(code_text)
                max_width = max(max_width, code_text.width)

            box_height = 0.6 + len(code_texts) * 0.30
            box_width = min(max_width + 1, 10)

            code_bg = Rectangle(
                width=box_width,
                height=box_height,
                color="#1e1e2e",
                fill_opacity=1,
                stroke_color="#89b4fa",
                stroke_width=1
            )
            code_bg.to_corner(UL, buff=0.3)

            code_group = VGroup(code_bg)
            for i, code_text in enumerate(code_texts):
                y_offset = (len(code_texts) - 1) * 0.175 - i * 0.35
                code_text.move_to(code_bg.get_center() + UP * y_offset)
                code_group.add(code_text)

            self.play(FadeIn(code_group), run_time=0.5)
            self.wait(duration)
            self.play(FadeOut(code_group), run_time=0.5)

            return code_group

        main_title = Text("Educational Shape Evolution",
                         font_size=40, color="#89b4fa", weight=BOLD)
        subtitle = Text("Learn Manim while watching shapes transform!",
                       font_size=20, color="#cdd6f4")
        subtitle.next_to(main_title, DOWN, buff=0.3)

        self.play(Write(main_title), run_time=2)
        self.play(Write(subtitle), run_time=1.5)
        self.wait(1)
        self.play(FadeOut(main_title), FadeOut(subtitle))

        # 1. Triangle → Mountain Scene
        triangle = Triangle(color=BLUE, fill_opacity=0.7)
        triangle.scale(2)

        self.play(DrawBorderThenFill(triangle), run_time=2)
        label_triangle = display_text("Step 1: Triangle → Mountain Scene")
        self.play(Write(label_triangle))

        show_code_line([
            "triangle = Triangle(color=BLUE)",
            "triangle.set_fill(opacity=0.7)"
        ])

        # Create snow caps and trees
        snow_cap1 = Polygon(
            LEFT * 0.5 + UP * 1.2, ORIGIN + UP * 2, RIGHT * 0.5 + UP * 1.2,
            color=WHITE, fill_opacity=1
        )
        snow_cap2 = Polygon(
            LEFT * 1.2 + UP * 1, LEFT * 1 + UP * 1.5, LEFT * 0.8 + UP * 1,
            color=WHITE, fill_opacity=1
        )

        # Create stamens
        stamens = VGroup()
        for i in range(18):
            angle = i * PI / 9
            stamen_pos = 0.25 * np.array([np.cos(angle), np.sin(angle), 0])
            stamen = Circle(radius=0.03, color="#ffa500", fill_opacity=1)
            stamen.move_to(stamen_pos)
            stamens.add(stamen)

        # Create leaves
        leaves = VGroup()
        for i in range(3):
            angle = i * 2 * PI / 3 + PI / 6
            leaf = Ellipse(width=0.4, height=1.2, color="#228b22", fill_opacity=0.8)
            leaf.rotate(angle + PI / 2)
            leaf.shift(1.8 * np.array([np.cos(angle), np.sin(angle), 0]))
            leaves.add(leaf)

        # Pine trees
        trees = VGroup()
        for x in [-2.5, -1.8, 1.5, 2.2]:
            tree_trunk = Rectangle(width=0.1, height=0.3, color="#3d2914", fill_opacity=1)
            tree_trunk.move_to(DOWN * 1.85 + RIGHT * x)

            tree_layers = VGroup()
            for i in range(3):
                layer = Triangle(color="#0d5016", fill_opacity=1)
                layer.scale(0.3 - i * 0.05)
                layer.move_to(DOWN * (1.7 - i * 0.15) + RIGHT * x)
                tree_layers.add(layer)

            trees.add(VGroup(tree_trunk, tree_layers))

        # Transform triangle into mountain landscape
        mountain_back = Polygon(
            LEFT * 3 + DOWN * 2, LEFT * 1 + UP * 1.5, RIGHT * 1 + DOWN * 2,
            color="#4a4a6b", fill_opacity=1
        )
        mountain_front = Polygon(
            LEFT * 2 + DOWN * 2, ORIGIN + UP * 2, RIGHT * 2 + DOWN * 2,
            color="#5d5d7a", fill_opacity=1
        )

        mountain_scene = VGroup(mountain_back, mountain_front, snow_cap1, snow_cap2, trees)
        self.play(Transform(triangle, mountain_scene), run_time=4)

        show_code_line([
            "mountain = Polygon(...)",
            "trees = VGroup(*tree_objects)",
            "scene = VGroup(mountain, trees)"
        ])

        self.play(FadeOut(label_triangle))

        # 2. Hexagon → Flower
        hexagon = RegularPolygon(n=6, radius=2, color=YELLOW, fill_opacity=0.7)
        self.play(Transform(triangle, hexagon), run_time=2)
        label_hexagon = display_text("Step 2: Hexagon → Flower")
        self.play(Write(label_hexagon))

        show_code_line([
            "hexagon = RegularPolygon(n=6)",
            "hexagon.set_color(YELLOW)"
        ])

        # Transform hexagon into detailed flower
        flower_center = Circle(radius=0.4, color="#ffd700", fill_opacity=1)
        flower_center.set_fill("#ff8c00")

        # Create petals using hexagon structure
        petals = VGroup()
        for i in range(6):
            angle = i * PI / 3
            petal = Ellipse(width=1.2, height=0.6, color="#ff69b4")
            petal.set_fill("#ffb6c1", opacity=0.9)
            petal.rotate(angle)
            petal.shift(1.2 * np.array([np.cos(angle), np.sin(angle), 0]))

            texture_lines = VGroup()
            for j in range(3):
                line_start = 0.8 * np.array([np.cos(angle), np.sin(angle), 0])
                line_end = 1.4 * np.array([np.cos(angle), np.sin(angle), 0])
                line_offset = (j - 1) * 0.15 * np.array([-np.sin(angle), np.cos(angle), 0])
                texture_line = Line(line_start + line_offset, line_end + line_offset,
                                  color="#ff1493", stroke_width=1.5)
                texture_lines.add(texture_line)

            petals.add(VGroup(petal, texture_lines))

        realistic_flower = VGroup(leaves, petals, flower_center, stamens)

        self.play(Transform(triangle, realistic_flower), run_time=4)

        show_code_line([
            "petal = Ellipse(width=1.2, height=0.6)",
            "petal.rotate(angle)",
            "petals = VGroup(*all_petals)"
        ])

        self.play(FadeOut(label_hexagon))

        # 3. Star → Starfish
        star = Star(n=5, outer_radius=2, inner_radius=0.8, color=ORANGE, fill_opacity=0.7)
        self.play(Transform(triangle, star), run_time=2)
        label_star = display_text("Step 3: Star → Starfish")
        self.play(Write(label_star))

        show_code_line([
            "star = Star(n=5, outer_radius=2)",
            "star.set_color(ORANGE)"
        ])

        # Transform star into starfish
        starfish_body = Star(n=5, outer_radius=1.5, inner_radius=0.6,
                            color="#ff6347", fill_opacity=1)
        starfish_body.set_fill("#ff7f50")

        texture_dots = VGroup()
        for i in range(25):
            dot = Circle(radius=0.03, color="#ff4500", fill_opacity=0.8)
            angle = np.random.random() * 2 * PI
            radius = np.random.random() * 1.2
            pos = radius * np.array([np.cos(angle), np.sin(angle), 0])
            dot.move_to(pos)
            texture_dots.add(dot)

        arm_details = VGroup()
        for i in range(5):
            angle = i * 2 * PI / 5
            ridge_start = 0.3 * np.array([np.cos(angle), np.sin(angle), 0])
            ridge_end = 1.3 * np.array([np.cos(angle), np.sin(angle), 0])
            ridge = Line(ridge_start, ridge_end, color="#ff4500", stroke_width=3)
            arm_details.add(ridge)

            for j in range(3):
                spine_pos = (0.5 + j * 0.3) * np.array([np.cos(angle), np.sin(angle), 0])
                spine_angle1 = angle + PI/6
                spine_angle2 = angle - PI/6
                spine1 = Line(spine_pos, spine_pos + 0.2 * np.array([np.cos(spine_angle1), np.sin(spine_angle1), 0]),
                             color="#ff6347", stroke_width=2)
                spine2 = Line(spine_pos, spine_pos + 0.2 * np.array([np.cos(spine_angle2), np.sin(spine_angle2), 0]),
                             color="#ff6347", stroke_width=2)
                arm_details.add(spine1, spine2)

        mouth = Circle(radius=0.15, color="#8b0000", fill_opacity=1)

        realistic_starfish = VGroup(starfish_body, texture_dots, arm_details, mouth)
        self.play(Transform(triangle, realistic_starfish), run_time=4)

        show_code_line([
            "dots = [Circle(radius=0.03) for _ in range(25)]",
            "for dot in dots: dot.move_to(random_pos)",
            "texture = VGroup(*dots)"
        ])

        self.play(FadeOut(label_star))

        # 4. Pentagon → Shield
        pentagon = RegularPolygon(n=5, radius=2.5, color=GREEN, fill_opacity=0.7)
        self.play(Transform(triangle, pentagon), run_time=2)
        label_pentagon = display_text("Step 4: Pentagon → Medieval Shield")
        self.play(Write(label_pentagon))

        show_code_line([
            "pentagon = RegularPolygon(n=5)",
            "pentagon.set_color(GREEN)"
        ])

        # Transform pentagon into medieval shield
        shield_base = RegularPolygon(n=5, radius=1.8, color="#c0c0c0", fill_opacity=1)
        shield_base.set_fill("#e6e6e6")

        shield_border = RegularPolygon(n=5, radius=1.8, color="#8b7355", fill_opacity=0)
        shield_border.set_stroke("#8b7355", width=10)

        inner_border = RegularPolygon(n=5, radius=1.6, color="#daa520", fill_opacity=0)
        inner_border.set_stroke("#daa520", width=4)

        # Heraldic cross in center
        cross_vertical = Rectangle(width=0.4, height=2.2, color="#dc143c", fill_opacity=1)
        cross_horizontal = Rectangle(width=2.2, height=0.4, color="#dc143c", fill_opacity=1)

        cross_v_outline = Rectangle(width=0.5, height=2.3, color="#8b0000", fill_opacity=0)
        cross_v_outline.set_stroke("#8b0000", width=2)
        cross_h_outline = Rectangle(width=2.3, height=0.5, color="#8b0000", fill_opacity=0)
        cross_h_outline.set_stroke("#8b0000", width=2)

        shield_studs = VGroup()
        for i in range(5):
            angle = i * 2 * PI / 5 - PI/2
            stud_pos = 1.4 * np.array([np.cos(angle), np.sin(angle), 0])
            stud = Circle(radius=0.1, color="#ffd700", fill_opacity=1)
            stud_highlight = Circle(radius=0.06, color="#ffff00", fill_opacity=1)
            stud.move_to(stud_pos)
            stud_highlight.move_to(stud_pos + 0.03 * np.array([-0.5, 0.5, 0]))
            shield_studs.add(VGroup(stud, stud_highlight))

        handle_mount1 = Rectangle(width=0.3, height=0.15, color="#654321", fill_opacity=1)
        handle_mount1.move_to(LEFT * 0.8)
        handle_mount2 = Rectangle(width=0.3, height=0.15, color="#654321", fill_opacity=1)
        handle_mount2.move_to(RIGHT * 0.8)

        damage_marks = VGroup()
        dent1 = Arc(radius=0.2, angle=PI/3, color="#999999", stroke_width=3)
        dent1.move_to(LEFT * 0.5 + UP * 0.8)
        dent2 = Arc(radius=0.15, angle=PI/4, color="#999999", stroke_width=2)
        dent2.move_to(RIGHT * 0.7 + DOWN * 0.6)
        damage_marks.add(dent1, dent2)

        banner = Ellipse(width=2, height=0.4, color="#4169e1", fill_opacity=1)
        banner.move_to(DOWN * 1.3)
        banner_text = Text("HONOR", font_size=16, color=WHITE, weight=BOLD)
        banner_text.move_to(DOWN * 1.3)

        realistic_shield = VGroup(
            shield_base, inner_border, shield_border,
            cross_v_outline, cross_h_outline, cross_vertical, cross_horizontal,
            shield_studs, handle_mount1, handle_mount2, damage_marks,
            banner, banner_text
        )

        self.play(Transform(triangle, realistic_shield), run_time=4)

        show_code_line([
            "shield_base = RegularPolygon(n=5, radius=1.8, color='#c0c0c0')",
            "shield_border = RegularPolygon(n=5, radius=1.8, stroke_width=10)",
            "cross_vertical = Rectangle(width=0.4, height=2.2)",
            "banner_text = Text(\"HONOR\", font_size=16, color=WHITE, weight=BOLD)",
         ])

        self.play(FadeOut(label_pentagon))

        self.play(FadeOut(triangle), run_time=1)

        # Create bicycle
        bicycle = VGroup()

        # Wheels first - foundation of the bike
        wheel1 = Circle(radius=1, color="#2f2f2f", fill_opacity=0)
        wheel1.set_stroke("#2f2f2f", width=8)
        wheel1.move_to(LEFT * 2.5 + DOWN * 1.5)

        wheel2 = Circle(radius=1, color="#2f2f2f", fill_opacity=0)
        wheel2.set_stroke("#2f2f2f", width=8)
        wheel2.move_to(RIGHT * 2.5 + DOWN * 1.5)

        # Wheel details
        rim1 = Circle(radius=0.95, color="#c0c0c0", fill_opacity=0)
        rim1.set_stroke("#c0c0c0", width=2)
        rim1.move_to(wheel1.get_center())

        rim2 = Circle(radius=0.95, color="#c0c0c0", fill_opacity=0)
        rim2.set_stroke("#c0c0c0", width=2)
        rim2.move_to(wheel2.get_center())

        # Spokes
        spokes1 = VGroup()
        for i in range(16):
            angle = i * PI / 8
            spoke = Line(
                wheel1.get_center(),
                wheel1.get_center() + 0.9 * np.array([np.cos(angle), np.sin(angle), 0]),
                color="#c0c0c0", stroke_width=1.5
            )
            spokes1.add(spoke)

        spokes2 = VGroup()
        for i in range(16):
            angle = i * PI / 8
            spoke = Line(
                wheel2.get_center(),
                wheel2.get_center() + 0.9 * np.array([np.cos(angle), np.sin(angle), 0]),
                color="#c0c0c0", stroke_width=1.5
            )
            spokes2.add(spoke)

        # Main frame triangle
        frame_joint = LEFT * 1 + UP * 0.3  # Main junction point
        seat_post_top = RIGHT * 1 + UP * 0.3
        bottom_bracket = RIGHT * 1 + DOWN * 0.2  # Where pedals attach

        # Main triangle
        top_tube = Line(frame_joint, seat_post_top, color="#ff0000", stroke_width=6)
        down_tube = Line(frame_joint, bottom_bracket, color="#ff0000", stroke_width=6)
        seat_tube = Line(seat_post_top, bottom_bracket, color="#ff0000", stroke_width=6)

        # Rear triangle
        chain_stay = Line(bottom_bracket, wheel2.get_center(), color="#ff0000", stroke_width=5)
        seat_stay = Line(seat_post_top, wheel2.get_center(), color="#ff0000", stroke_width=5)

        # Front fork
        head_tube_top = frame_joint + UP * 0.5
        fork_crown = LEFT * 1.5 + UP * 0.3  # Crown of the fork

        head_tube = Line(frame_joint, head_tube_top, color="#ff0000", stroke_width=6)
        fork_steerer = Line(head_tube_top, fork_crown, color="#2f2f2f", stroke_width=4)

        # Fork blades
        fork_left = Line(fork_crown, wheel1.get_center() + LEFT * 0.2, color="#2f2f2f", stroke_width=5)
        fork_right = Line(fork_crown, wheel1.get_center() + RIGHT * 0.2, color="#2f2f2f", stroke_width=5)

        # handlebars
        handlebar_stem = Line(head_tube_top, head_tube_top + UP * 0.4, color="#2f2f2f", stroke_width=4)
        handlebar_center = head_tube_top + UP * 0.4
        handlebar = Line(handlebar_center + LEFT * 0.8, handlebar_center + RIGHT * 0.8,
                        color="#2f2f2f", stroke_width=5)

        # Brake levers
        brake_left = Line(handlebar_center + LEFT * 0.5,
                         handlebar_center + LEFT * 0.5 + DOWN * 0.2 + LEFT * 0.1,
                         color="#333333", stroke_width=3)
        brake_right = Line(handlebar_center + RIGHT * 0.5,
                          handlebar_center + RIGHT * 0.5 + DOWN * 0.2 + RIGHT * 0.1,
                          color="#333333", stroke_width=3)

        # Seat assembly
        seat_post = Line(seat_post_top, seat_post_top + UP * 0.5, color="#2f2f2f", stroke_width=4)
        seat = Ellipse(width=1, height=0.3, color="#654321", fill_opacity=1)
        seat.move_to(seat_post_top + UP * 0.5)

        # Pedal assembly
        crank_arm1 = Line(bottom_bracket, bottom_bracket + DOWN * 0.6, color="#2f2f2f", stroke_width=5)
        crank_arm2 = Line(bottom_bracket, bottom_bracket + UP * 0.6, color="#2f2f2f", stroke_width=5)

        pedal1 = Rectangle(width=0.25, height=0.08, color="#333333", fill_opacity=1)
        pedal1.move_to(bottom_bracket + DOWN * 0.6)
        pedal2 = Rectangle(width=0.25, height=0.08, color="#333333", fill_opacity=1)
        pedal2.move_to(bottom_bracket + UP * 0.6)

        # chain
        chain = Line(bottom_bracket, wheel2.get_center(), color="#333333", stroke_width=2)

        # Hub details
        hub1 = Circle(radius=0.08, color="#ffd700", fill_opacity=1)
        hub1.move_to(wheel1.get_center())
        hub2 = Circle(radius=0.08, color="#ffd700", fill_opacity=1)
        hub2.move_to(wheel2.get_center())

        # Tire treads
        tread1 = Circle(radius=1.02, color="#1a1a1a", fill_opacity=0)
        tread1.set_stroke("#1a1a1a", width=3)
        tread1.move_to(wheel1.get_center())
        tread2 = Circle(radius=1.02, color="#1a1a1a", fill_opacity=0)
        tread2.set_stroke("#1a1a1a", width=3)
        tread2.move_to(wheel2.get_center())

        # Water bottle
        bottle = Rectangle(width=0.12, height=0.5, color="#4169e1", fill_opacity=1)
        bottle.move_to(frame_joint + DOWN * 0.3)

        # Assemble bicycle in logical groups
        wheels_group = VGroup(wheel1, wheel2, tread1, tread2, rim1, rim2, hub1, hub2)
        spokes_group = VGroup(spokes1, spokes2)
        frame_group = VGroup(top_tube, down_tube, seat_tube, chain_stay, seat_stay, head_tube)
        fork_group = VGroup(fork_steerer, fork_left, fork_right)
        handlebar_group = VGroup(handlebar_stem, handlebar, brake_left, brake_right)
        seat_group = VGroup(seat_post, seat)
        drivetrain_group = VGroup(crank_arm1, crank_arm2, pedal1, pedal2, chain)
        details_group = VGroup(bottle)

        bicycle.add(wheels_group, spokes_group, frame_group, fork_group,
                   handlebar_group, seat_group, drivetrain_group, details_group)

        # Scale and position the bicycle
        bicycle.scale(0.8)
        bicycle.move_to(DOWN * 0.3)

        # Animate bicycle creation with  code annotations and sectioning
        label_bike = display_text("Step 5: Creating a Bicycle")
        self.play(Write(label_bike))

        # 1. Wheels first
        self.play(*[DrawBorderThenFill(part) for part in wheels_group], run_time=1)
        show_code_line([
            "wheel = Circle(radius=1, stroke_width=8)",
            "rim = Circle(radius=0.95, stroke_width=2)",
            "hub = Circle(radius=0.08, fill_color=GOLD)"
        ])

        # 2. Spokes
        self.play(*[Create(part) for part in spokes_group], run_time=1)
        show_code_line([
            "spokes = VGroup()",
            "for i in range(16):",
            "  spokes.add(Line(center, rim_edge))"
        ])

        # 3. Main frame
        self.play(*[Create(part) for part in frame_group], run_time=1)
        show_code_line([
            "# Main triangle frame",
            "top_tube = Line(head, seat_post)",
            "down_tube = Line(head, bottom_bracket)"
        ])

        # 4 steering
        self.play(*[Create(part) for part in fork_group], run_time=1)
        show_code_line([
            "fork_left = Line(crown, wheel_left)",
            "fork_right = Line(crown, wheel_right)",
            "# Fork holds front wheel"
        ])

        # 5. Handlebars
        self.play(*[Create(part) for part in handlebar_group], run_time=1)
        show_code_line([
            "stem = Line(head_top, handlebar_center)",
            "handlebar = Line(left_grip, right_grip)",
            "brakes = Line(lever_pos, brake_pos)"
        ])

        # 6. Seat
        self.play(*[DrawBorderThenFill(part) for part in seat_group], run_time=1)
        show_code_line([
            "seat_post = Line(frame, seat_height)",
            "seat = Ellipse(width=1, height=0.3)",
            "# Rider comfort component"
        ])

        # 7. Drivetrain
        self.play(*[Create(part) for part in drivetrain_group], run_time=1)
        show_code_line([
            "crank_arms = VGroup(arm1, arm2)",
            "pedals = Rectangle(width=0.25, height=0.08)",
            "chain = Line(pedals, rear_wheel)"
        ])

        # 8. Final details
        self.play(*[DrawBorderThenFill(part) for part in details_group], run_time=1)
        show_code_line([
            "bottle = Rectangle(width=0.12, height=0.5)",
            "# Additional realistic details",
            "complete_bike = VGroup(*all_parts)"
        ])

        self.play(FadeOut(label_bike))

        # Final wheel rotation
        show_code_line([
            "self.play(Rotate(wheel_assembly, 2*PI))",
            "# Animate realistic wheel spinning",
            "# Makes the bicycle come alive!"
        ])

        self.play(
            Rotate(VGroup(spokes1, hub1), PI, run_time=1),
            Rotate(VGroup(spokes2, hub2), PI, run_time=1),
        )

        # Final educational message
        final_title = Text("Shape Evolution Complete!",
                          font_size=36, color="#89b4fa", weight=BOLD)
        final_title.to_edge(UP, buff=0.5)

        educational_msg = Text("You've learned: Polygons, Transformations, Grouping, and Animation!",
                              font_size=20, color="#a6e3a1")
        educational_msg.to_edge(DOWN, buff=0.5)

        self.play(
            Write(final_title),
            Write(educational_msg),
            run_time=3
        )

        # Final rotation
        self.play(
            Rotate(VGroup(spokes1, hub1), 2*PI, run_time=4),
            Rotate(VGroup(spokes2, hub2), 2*PI, run_time=4),
        )
        self.wait(2)
        self.play(FadeOut(Group(*self.mobjects)), run_time=1)

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
            Text("P", font_size=20, color=WHITE, weight=BOLD)
        )
        pixabay_text = Text("Pixabay - Music", font_size=24, color=WHITE)
        pixabay_entry = VGroup(pixabay_icon, pixabay_text)
        pixabay_entry.arrange(RIGHT, buff=0.5)
        pixabay_entry.shift(UP*0.5)


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
        self.play(FadeOut(Group(*self.mobjects)), run_time=1.5)
