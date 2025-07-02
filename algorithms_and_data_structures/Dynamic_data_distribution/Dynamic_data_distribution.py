from manim import *

class Cityscape3D(ThreeDScene):
    def construct(self):
         # Create title
        title = Text("Dynamic Data Distribution", font_size=26,weight=BOLD, color=BLUE)
        title.to_edge(UP*0.4)
        self.add_fixed_in_frame_mobjects(title)# Add title to the scene and fix it
        self.play(FadeIn(title, run_time=2))
        
        # Set the initial camera orientation
        self.set_camera_orientation(phi=75 * DEGREES, theta=-45 * DEGREES,rate_func=rate_functions.linear, run_time=6)
        
        # Create a NumberPlane to represent the base with hidden x and y axes
        base_plane = NumberPlane(
            x_range=[-7, 7, 1], y_range=[-7, 7, 1], 
            axis_config={"stroke_opacity": 0},  # Hide the x and y axes lines
            background_line_style={
                "stroke_color": GREY,
                "stroke_width": 0.5,
                "stroke_opacity": 0.7
            }
        )
        self.add(base_plane)
        
        #Create histograms
        histograms = VGroup()
        colors = [RED, GREEN, BLUE, YELLOW, ORANGE, PURPLE, TEAL, PINK]
        num_histograms = 50  # Number of histograms to create
        min_height = 0.1  # Minimal starting height for the histograms
        


        for i in range(num_histograms):
            height = min_height 
            color = colors[i % len(colors)]
            bar = Prism(dimensions=[0.5, 0.5, height], fill_color=color, fill_opacity=10)

            # Increase the range of random positions to spread out the histograms more
            x_pos = np.random.uniform(-5, 5)  # Increased range for x position
            y_pos = np.random.uniform(-3, 3)  # Increased range for y position
            z_pos = height / 2                # Set z position to half the height to ensure it touches the base
            bar.move_to([x_pos, y_pos, z_pos])

            histograms.add(bar)

        # Add histograms to the scene with animations
        for bar in histograms:
            self.play(FadeIn(bar, run_time=0.3))  # Adjust run_time to control the speed of each bar appearing

        self.wait(1)  # Wait for a moment before ending the scene
        # Animate the histograms to increase their heights upwards only
        animations = []
        for bar in histograms:
            new_height = np.random.uniform(1, 3)  # Random height increase
            scale_factor = new_height / min_height
            # Scale only the height and move the bar upwards to keep the base fixed
            animations.append(bar.animate.scale([1, 1, scale_factor]).shift([0, 0, (new_height - min_height) / 2]))

        # Play animations sequentially
        for anim in animations:
            self.play(anim, run_time=1)
            self.wait(0.5)

        # Add camera movements to show the histograms from all sides
        self.move_camera(phi=75 * DEGREES, theta=135 * DEGREES, run_time=3) 
        self.wait(1)
        self.move_camera(phi=45 * DEGREES, theta=(360+45) * DEGREES, rate_func=rate_functions.linear, run_time=5)
        self.wait()
        self.move_camera(phi=75 * DEGREES, theta=45 * DEGREES, run_time=4) 
        self.wait()
        self.move_camera(phi=0 * DEGREES, theta=(360+45) * DEGREES, rate_func=rate_functions.linear, run_time=6)
        self.wait()
        self.move_camera(phi=0 * DEGREES, theta=(360 + 405) * DEGREES, rate_func=rate_functions.linear, run_time=6)       


        # Fade out all elements in the scene
        self.play(
            *[FadeOut(mob) for mob in self.mobjects],  # Fade out all objects in the scene
            run_time=5,
            rate_func=rate_functions.smooth  # Make the fade-out smooth
        )