from manim import *

class HilbertCurve(Scene):
    def construct(self):
        # Configure animation settings
        self.camera.background_color = BLACK
        
        
        # Create and animate title
        title = Text("Hilbert Curve Visualization", font_size=26, color=BLUE).to_edge(UP * 0.5)
        # Animate the title
        self.play(Write(title))  # Animate the title
        self.wait(1)
        self.play(FadeOut(title), run_time=2)
        self.wait(0.5)
        
        # Define colors and stroke widths for each level
        CURVE_COLORS = [
            "#FF0000",  # Red
            "#00FF00",  # Green
            "#0000FF",  # Blue
            "#FFD700",  # Gold
            "#FF00FF",  # Magenta
            "#00FFFF",  # Cyan
        ]
        
        # Stroke widths decrease as levels increase
        STROKE_WIDTHS = [6, 5, 4, 3, 2, 1]
        
        def get_hilbert_points(level, offset=np.array([0, 0, 0]), size=4):
            if level == 0:
                return [offset]
                
            points = []
            quadrant_size = size / 2
            
            # Define the relative positions and rotations for each quadrant
            quadrants = [
                lambda p: np.array([p[1], p[0], 0]),           # Bottom left
                lambda p: np.array([p[0], p[1], 0]),           # Top left
                lambda p: np.array([p[0], p[1], 0]),           # Top right
                lambda p: np.array([-p[1], -p[0], 0]),         # Bottom right
            ]
            
            offsets = [
                np.array([-quadrant_size, -quadrant_size, 0]),  # Bottom left
                np.array([-quadrant_size, quadrant_size, 0]),   # Top left
                np.array([quadrant_size, quadrant_size, 0]),    # Top right
                np.array([quadrant_size, -quadrant_size, 0]),   # Bottom right
            ]
            
            # Recursively get points for each quadrant
            for i in range(4):
                sub_points = get_hilbert_points(level - 1, 
                                              offset + offsets[i], 
                                              quadrant_size)
                points.extend([quadrants[i](p - offset) + offset for p in sub_points])
            
            return points

        # Create curves for different levels
        max_level = 5
        curves = []
        final_curves = []  # Store the final state of curves
        
        for level in range(1, max_level + 1):
            points = get_hilbert_points(level)
            curve = VMobject(stroke_color=CURVE_COLORS[level-1], 
                           stroke_width=STROKE_WIDTHS[level-1])
            curve.set_points_smoothly(points)
            curves.append(curve)
            # Create a separate copy for the final state
            final_curve = curve.copy()
            final_curves.append(final_curve)

        # Animation sequence
        # Start with level 1
        self.play(Create(curves[0]), run_time=5)
        self.wait()
        
        # Transform through each level
        for i in range(len(curves)-1):
            self.play(Transform(curves[i], curves[i+1]), 
                     run_time=4)
            self.wait()
        
        # Clear the scene and add final curves
        self.clear()
        for curve in final_curves:
            self.add(curve)
        
        # Create different rotation animations for each curve
        rotations_out = []
        rotations_back = []
        
        for i, curve in enumerate(final_curves):
            angle = PI if i % 2 == 0 else -PI
            speed_factor = 1 + (i * 0.2)
            
            rotation_out = Rotate(
                curve,
                angle=angle,
                rate_func=smooth,
                run_time=6 / speed_factor
            )
            rotations_out.append(rotation_out)
            
            rotation_back = Rotate(
                curve,
                angle=-angle,
                rate_func=smooth,
                run_time=6 / speed_factor
            )
            rotations_back.append(rotation_back)
        
        # Play rotations
        self.play(*rotations_out)
        self.wait(0.5)
        self.play(*rotations_back)
        self.wait(0.5)
        
        # Create a slow dissolve effect for all curves
        fade_animations = []
        for curve in final_curves:
            fade = FadeOut(curve, run_time=2)
            fade_animations.append(fade)
        
        # Play all fade animations simultaneously with a slower rate
        self.play(
            *fade_animations,
            rate_func=lambda t: smooth(t),
            run_time=3
        )
        
        # Final pause
        self.wait(1)