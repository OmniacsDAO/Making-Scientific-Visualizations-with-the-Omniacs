from manim import *
import numpy as np
from scipy.stats import norm

class ComprehensiveNormalDistribution3D(ThreeDScene):
    def construct(self):
        # Initial camera setup
        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)
        
        # Create 3D axes with larger lengths to occupy more screen space
        axes = ThreeDAxes(
            x_range=[-6, 6, 1],
            y_range=[-6, 6, 1],
            z_range=[0, 0.2, 0.1],
            x_length=10,  # Increased length
            y_length=10,  # Increased length
            z_length=3.3   # Increased length
        )
        # Labels for the axes
        x_label = axes.get_x_axis_label("x")
        y_label = axes.get_y_axis_label("y")
        z_label = Text("P(x,y)", font_size=20, color=GRAY_A).next_to(axes.z_axis, UP)
        labels = VGroup(x_label, y_label, z_label)

        # Title that stays fixed on screen
        title = Text("Normal Distribution Animation", font_size=24, color=BLUE).to_edge(UP*0.5)
        self.play(Write(title))
        self.add_fixed_in_frame_mobjects(title)
        self.wait(1)

        # Static normal distribution function text on the top left of the screen
        normal_dist_text = Text(
            "Normal Distribution Function:\n P(x,y) = e^(-((x^2+y^2)/2))/(2π)",
            font_size=12, color=WHITE
        )
        normal_dist_text.to_corner(DL)
        self.add_fixed_in_frame_mobjects(normal_dist_text)

        # Define the 3D normal distribution function
        def normal_dist_3d(x, y):
            return np.exp(-(x**2 + y**2)/2) / (2*np.pi)
        
        # Define a color map function based on the z-value
        def color_map(z):
            return interpolate_color(GREEN, GREY, z / 0.5)

        # Create the surface representing the normal distribution
        surface = Surface(
            lambda u, v: axes.c2p(
                u, v, 
                normal_dist_3d(u, v)
            ),
            u_range=[-6, 6],
            v_range=[-6, 6],
            resolution=(35, 35),
            checkerboard_colors=[GREEN, GREY],
            fill_opacity=0.8
        )

        # Create contour curves
        contours = VGroup()
        heights = [0.02, 0.05, 0.1, 0.15]
        colors = [DARK_BLUE, YELLOW_A, YELLOW_B, YELLOW_D]
        
        for height, color in zip(heights, colors):
            radius = np.sqrt(-2 * np.log(height * 2 * np.pi))
            circle = ParametricFunction(
                lambda t: axes.c2p(
                    radius * np.cos(t),
                    radius * np.sin(t),
                    height
                ),
                t_range=[0, TAU],
                color=color
            )
            contours.add(circle)

        # Begin animation sequence
        self.play( Write(labels), Create(axes), run_time=5)
        self.wait()

        # Create and rotate surface
        self.begin_ambient_camera_rotation(rate=0.2)
        self.play(Create(surface), run_time=30)
        self.wait(2)

        # Add explanation text
        explanation = Text(
            "The bivariate normal distribution\nforms a bell-shaped surface",
            font_size=15, color=WHITE
        ).to_corner(UR)
        self.add_fixed_in_frame_mobjects(explanation)
        self.play(Write(explanation))
        self.wait(2)

        # Show contour curves
        self.play(Create(contours), run_time=4) 
        new_explanation = Text(
            "Contour curves show points\nof equal probability",
            font_size=15, color=WHITE
        ).to_corner(UR)
        self.add_fixed_in_frame_mobjects(new_explanation)
        self.play(ReplacementTransform(explanation, new_explanation))
        self.wait(2)

        # Create cross sections
        cross_sections = VGroup()
        for y_pos in [-2, -1, 0, 1, 2]:
            curve = ParametricFunction(
                lambda t: axes.c2p(t, y_pos, normal_dist_3d(t, y_pos)),
                t_range=[-4, 4],
                color=RED_A
            )
            cross_sections.add(curve)

        # Show cross sections
        cross_section_text = Text(
            "Cross sections are also\nnormal distributions",
            font_size=15, color=WHITE
        ).to_corner(UR)
        self.add_fixed_in_frame_mobjects(cross_section_text)
        self.play(
            ReplacementTransform(new_explanation, cross_section_text),
            Create(cross_sections),  run_time=6
        )
        self.wait(2)

        # Final rotation with all elements
        self.move_camera(phi=65 * DEGREES, theta=60 * DEGREES)
        self.wait(2)
        
        self.move_camera(phi=85 * DEGREES, theta=90 * DEGREES)
        self.wait(2)
        
        # Stop camera rotation
        self.stop_ambient_camera_rotation()
        self.wait()
        
    
        # Fade out all elements in the scene
        self.play(
            *[FadeOut(mob) for mob in self.mobjects],
            run_time=4,
            rate_func=rate_functions.smooth
        )