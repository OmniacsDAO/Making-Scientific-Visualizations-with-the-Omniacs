from manim import *

class axesIn3D(ThreeDScene):
    def construct(self):
        # Setup constants
        radius = 4 * 7/10
        
        # Create title
        title = Text("Coordinate System Animation", font_size=24, color=BLUE)
        title.to_edge(UP*0.4)
        self.add_fixed_in_frame_mobjects(title)# Add title to the scene and fix it
        # Create and show axes
        axes = ThreeDAxes(
            x_range=[-5, 5, 1],
            y_range=[-5, 5, 1],
            z_range=[-5, 5, 1],
            x_length=7,
            y_length=7,
            z_length=7,
            axis_config={"color": WHITE},
            x_axis_config={"color": PURPLE_E},
            y_axis_config={"color": GREEN_E},
            z_axis_config={"color": BLUE},
        )
        lbls = axes.get_axis_labels()
        self.play(Create(axes), Create(lbls), run_time=3)
        self.move_camera(phi=45 * DEGREES, theta=45 * DEGREES, run_time=4)
        self.wait()
        
        # Create and animate phi circles one by one
        for phi in range(15, 180, 15):
            circle = Circle(radius=radius * np.sin(phi * DEGREES), color=DARK_GREY)
            circle.shift(radius * np.cos(phi * DEGREES) * OUT)
            label = MathTex(r"\varphi={:.0f}^o".format(phi), color=RED_B).scale(0.5)
            label.rotate(angle=90 * DEGREES, axis=RIGHT)
            label.shift([0, -radius * np.sin(phi * DEGREES), 0.2 + radius * np.cos(phi * DEGREES)])
            label.rotate(135 * DEGREES, axis=OUT, about_point=ORIGIN)
            
            # Animate each circle and label individually
            self.play(
                Create(circle, run_time=1),
                Write(label, run_time=0.5)
            )

        # Create and animate theta arcs one by one
        for theta in range(0, 360, 30):
            arc = Arc(
                radius=radius,
                start_angle=10 * DEGREES,
                angle=160 * DEGREES,
                color=GREEN
            )
            arc.rotate(90 * DEGREES, axis=RIGHT, about_point=ORIGIN)
            arc.rotate(90 * DEGREES, axis=UP, about_point=ORIGIN)
            arc.rotate(theta * DEGREES, axis=OUT, about_point=ORIGIN)
            
            label = MathTex(r"\theta={:.0f}^o".format(theta), color=GREY).scale(0.5)
            label.shift((1.1 * radius - label.get_left()[0]) * RIGHT)
            label.rotate(theta * DEGREES, axis=OUT, about_point=ORIGIN)
            
            # Animate each arc and label individually
            self.play(
                Create(arc, run_time=1),
                Write(label, run_time=0.5)
            )

        # Camera movements
        self.move_camera(phi=45 * DEGREES, theta=45 * DEGREES, run_time=4)
        self.wait()
        self.move_camera(phi=45 * DEGREES, theta=(360+45) * DEGREES, rate_func=rate_functions.linear, run_time=6)
        self.wait()
        self.move_camera(phi=0 * DEGREES, theta=(360+45) * DEGREES, rate_func=rate_functions.linear, run_time=3)
        self.wait()
        self.move_camera(phi=0 * DEGREES, theta=(360 + 405) * DEGREES, rate_func=rate_functions.linear, run_time=6)
        self.wait(2)
        self.move_camera(phi=180 * DEGREES, theta=(360+45) * DEGREES, rate_func=rate_functions.linear, run_time=6)
        self.wait()
        self.move_camera(phi=180 * DEGREES, theta=(360 + 405) * DEGREES, rate_func=rate_functions.linear, run_time=6)
        self.wait(2)


        # Return to the initial camera view before fading out
        self.move_camera(phi=0 * DEGREES, theta=45 * DEGREES, run_time=6)
        

        # Fade out all elements in the scene
        self.play(
            *[FadeOut(mob) for mob in self.mobjects],  # Fade out all objects in the scene
            run_time=5,
            rate_func=rate_functions.smooth  # Make the fade-out smooth
        )
        
        