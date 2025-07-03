from manim import *
import numpy as np
from scipy.integrate import solve_ivp

def lorenz_equations(t, state):
    """Compute the Lorenz system derivatives."""
    x, y, z = state
    sigma, rho, beta = 10, 28, 2.667
    dx = sigma * (y - x)
    dy = x * (rho - z) - y
    dz = x * y - beta * z
    return [dx, dy, dz]

class LorenzAttractorAnimation(ThreeDScene):
    def construct(self):
        # Configure the 3D scene
        self.set_camera_orientation(phi=75 * DEGREES, theta=-45 * DEGREES)
        
        # Instead of frame updater, we'll use begin_ambient_camera_rotation
        self.begin_ambient_camera_rotation(rate=0.2)

        # Create and style the axes - shifted down and scaled
        axes = ThreeDAxes(
            x_range=(-30, 30),
            y_range=(-30, 32),
            z_range=(0, 50),
            x_length=6,
            y_length=7,
            z_length=6,
        ).set_opacity(0.5)
        axes.move_to(ORIGIN)
        self.play(Create(axes, run_time=4))  # Adjust run_time for smoothness



        # Title - moved down slightly
        title = Text("Exploring Chaos: The Lorenz Attractor in Motion", font_size=24, color=BLUE).to_edge(UP * 0.5)
        self.add_fixed_in_frame_mobjects(title)
        self.play(Write(title, run_time=2))

        # Solve the Lorenz system for two slightly different initial conditions
        t_span = [0, 50]
        t_eval = np.linspace(0, 50, 5000)
        initial_conditions = [
            [0, 1, 1.05],  # First trajectory
            [0, 1, 1.06]   # Second trajectory (slightly different)
        ]
        
        # Create curves with different colors
        colors = [GREEN, RED]
        curves = VGroup()
        
        for initial, color in zip(initial_conditions, colors):
            # Solve the system
            solution = solve_ivp(
                lorenz_equations,
                t_span,
                initial,
                t_eval=t_eval,
                method='RK45'
            )
            
            # Convert solution points to 3D coordinates and shift them with the axes
            points = [
                axes.c2p(x, y, z) 
                for x, y, z in zip(solution.y[0], solution.y[1], solution.y[2])
            ]
            
            # Create and style the curve
            curve = VMobject(stroke_width=3)
            curve.set_points_smoothly(points)
            curve.set_color(color)
            curves.add(curve)

        # Animation sequence
        #self.play(Create(axes), Write(title))
        self.play(
            *[Create(curve, run_time=80, rate_func=linear) for curve in curves]
        )
        
        # Add explanatory text - moved up slightly from bottom
        explanation = Text(
            "Two trajectories with slightly different initial conditions",
            font_size=18, color=WHITE
        ).to_edge(DOWN)
        self.add_fixed_in_frame_mobjects(explanation)
        self.play(FadeIn(explanation), run_time=3)
        
        # Let the scene run a bit longer to show the rotation
        self.wait(5)
        
        # Cleanup
        self.play(
            *[FadeOut(mob) for mob in [curves, axes, title, explanation]], run_time=5)
