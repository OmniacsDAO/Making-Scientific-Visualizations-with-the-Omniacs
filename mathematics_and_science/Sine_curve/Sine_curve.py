from manim import *

class FollowingGraphCamera(MovingCameraScene):
    def construct(self):
        self.camera.frame.save_state()

        # Create the title text with specific font size and color
        title = Tex(r"Sine Curve Animation", font_size=48, color=BLUE)
        
        # Position the title at the center of the screen initially
        title.move_to(ORIGIN)
        
        # Play the animation: Write the title
        self.play(Write(title))
        self.wait(1)
        
        # Animate the title moving up and fading out
        self.play(
            title.animate.to_edge(UP).set_opacity(0),
            run_time=3
        )
        self.wait(0.8)
        
        # Create a number plane (grid) with custom colors for the lines
        grid = NumberPlane(
            axis_config={
                "stroke_color": WHITE,
                "stroke_opacity": 0,  # Set the opacity to 0 to remove white lines
            },
            background_line_style={
                "stroke_color": GREY,
                "stroke_width": 1,
                "stroke_opacity": 1
            }
        )
        
        # Add the number plane to the scene
        self.add(grid)
        
        # Animate the creation of the grid with a runtime of 4 seconds and some lag ratio
        self.play(Create(grid, run_time=4, lag_ratio=0.1))
        self.wait()

        # Now start the sine curve animation
        self.show_axis()
        self.show_circle()
        self.move_dot_and_draw_curve()
        self.wait()

    def show_axis(self):
        x_start = np.array([-7, 0, 0])
        x_end = np.array([7, 0, 0])

        y_start = np.array([-6, -3.5, 0])
        y_end = np.array([-6, 3.5, 0])

        x_axis = Line(x_start, x_end)
        y_axis = Line(y_start, y_end)

        # Animate the axes with a run_time of 2 seconds each
        self.play(Create(x_axis, run_time=2))
        self.play(Create(y_axis, run_time=2))

        self.add_x_labels()

        self.origin_point = np.array([-6, 0, 0])
        self.curve_start = np.array([-5, 0, 0])
        self.wait()

    def add_x_labels(self):
        x_labels = [
            MathTex(r"\pi"), MathTex(r"2 \pi"),
            MathTex(r"3 \pi"), MathTex(r"4 \pi"),
            MathTex(r"5 \pi"), MathTex(r"6 \pi"),
            MathTex(r"7 \pi"), MathTex(r"8 \pi"), 
            MathTex(r"9 \pi"),
            MathTex(r"10 \pi"), MathTex(r"11 \pi"),
        ]

        # Adjust the labels to start from the origin and move rightward
        for i, label in enumerate(x_labels):
            label.next_to(np.array([-4 + (i), 0, 0]), DOWN)
            label.set_font_size(14)
            self.add(label)

    def show_circle(self):
        circle = Circle(radius=1)
        circle.move_to(self.origin_point)

        # Animate the drawing of the circle with a run_time of 3 seconds
        self.play(Create(circle, run_time=3))

        self.circle = circle
        self.wait(1)

    def move_dot_and_draw_curve(self):
        orbit = self.circle
        origin_point = self.origin_point

        dot = Dot(radius=0.08, color=GREEN)
        dot.move_to(orbit.point_from_proportion(0))
        self.t_offset = 0
        rate = 0.25

        def go_around_circle(mob, dt):
            self.t_offset += (dt * rate)
            mob.move_to(orbit.point_from_proportion(self.t_offset % 1))

        # Create a second dot for the drawer
        drawer_dot = Dot(radius=0.08, color=RED)
        drawer_dot.move_to(self.curve_start)

        def move_drawer_dot(mob, dt):
            x = self.curve_start[0] + self.t_offset * 2
            y = orbit.point_from_proportion(self.t_offset % 1)[1]
            mob.move_to(np.array([x, y, 0]))

        def get_line_to_circle():
            return Line(origin_point, dot.get_center(), color=BLUE)

        def get_line_to_curve():
            x = self.curve_start[0] + self.t_offset * 2
            y = dot.get_center()[1]
            return Line(dot.get_center(), np.array([x, y, 0]), color=YELLOW_A, stroke_width=2)

        self.curve = VGroup()
        self.curve.add(Line(self.curve_start, self.curve_start))

        def get_curve():
            last_line = self.curve[-1]
            x = self.curve_start[0] + self.t_offset * 2
            y = dot.get_center()[1]
            new_line = Line(last_line.get_end(), np.array([x, y, 0]), color=YELLOW_D)
            self.curve.add(new_line)
            return self.curve

        dot.add_updater(go_around_circle)
        drawer_dot.add_updater(move_drawer_dot)

        origin_to_circle_line = always_redraw(get_line_to_circle)
        dot_to_curve_line = always_redraw(get_line_to_curve)
        sine_curve_line = always_redraw(get_curve)

        self.add(dot, drawer_dot)
        self.add(orbit, origin_to_circle_line, dot_to_curve_line, sine_curve_line)
        self.wait(0.5)

        # Add camera movement to follow the moving dot with smooth transition
        self.play(self.camera.frame.animate.scale(0.5).move_to(drawer_dot), rate_func=rate_functions.smooth)

        def update_camera(mob):
            mob.move_to(drawer_dot.get_center())

        self.camera.frame.add_updater(update_camera)
        self.wait(18.5)
        self.camera.frame.remove_updater(update_camera)
        self.play(Restore(self.camera.frame), run_time=4)

        dot.remove_updater(go_around_circle)
        drawer_dot.remove_updater(move_drawer_dot)
        
        # Fade out all elements in the scene
        self.play(
            *[FadeOut(mob) for mob in self.mobjects],  # Fade out all objects in the scene
            run_time=4,
            rate_func=rate_functions.smooth  # Make the fade-out smooth
        )
        
        # Create the title text with specific font size and color
        title = Tex(r"Sine Curve Animation", font_size=48, color=BLUE)
        
        # Position the title at the center of the screen initially
        title.move_to(ORIGIN)
        
        # Play the animation: Write the title
        self.play(Write(title))
        self.wait(1)
        
        # Animate the title moving up and fading out
        self.play(
            title.animate.to_edge(DOWN).set_opacity(0),
            run_time=3
        )
        self.wait(1)