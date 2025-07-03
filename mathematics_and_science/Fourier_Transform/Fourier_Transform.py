from manim import *
import numpy as np

class FourierTransformVisualization(Scene):
    def construct(self):
        # Title and subtitle
        title = Text("Fourier Transform in Motion", font_size=28, color=BLUE).to_edge(UP, buff=0.1)
        subtitle = Text("Breaking Signals into Frequencies", font_size=20, color=GREY).next_to(title, DOWN, buff=0.1)
        self.play(Write(title), FadeIn(subtitle))
        self.wait(1)

        # Create two coordinate planes, one for the left and one for the right
        left_plane = NumberPlane(
            x_range=[-4, 4, 2],
            y_range=[-3.5, 3.5, 1],
            background_line_style={"stroke_color": GRAY, "stroke_width": 1, "stroke_opacity": 0.5}
        ).shift(LEFT * 5)

        right_plane = NumberPlane(
            x_range=[-5, 5, 2],
            y_range=[-3.5, 3.5, 1],
            background_line_style={"stroke_color": GRAY, "stroke_width": 1, "stroke_opacity": 0.5}
        ).shift(RIGHT * 5)

        right_plane.y_axis.shift(LEFT * 1.5)

        self.play(Create(left_plane, run_time=1.5), Create(right_plane, run_time=1.5))
        self.wait(0.5)

        # Define frequencies, amplitudes, and colors
        frequencies = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,11,12]
        amplitudes = [1.0, 0.5, 0.3, 0.2, 0.15, 0.1, 0.08,0.07,0.05, 0.04, 0.03, 0.02]
        colors = [RED, GREEN, BLUE, ORANGE, PURPLE, TEAL, PINK, YELLOW, GOLD, MAROON]

        # Create group to hold all individual waves on the right side
        wave_components = VGroup()

        # Initialize the composite wave (starting at 0) for the left plane
        composite_wave = left_plane.plot(lambda x: 0, color=YELLOW, x_range=[-4, 4], stroke_width=4)
        composite_label = Text("Building Composite Wave", font_size=20, color=YELLOW).to_edge(DOWN)
        self.wait(0.5)

        current_composite = lambda x: 0  # Initialize composite function
        for freq, amp, color in zip(frequencies, amplitudes, colors):
            # Plot the current wave on the right plane
            wave = right_plane.plot(
                lambda x, f=freq, a=amp: a * np.sin(f * x),
                color=color,
                x_range=[-4, 4],
                stroke_width=4
            )
            wave_components.add(wave)

            # Update the composite wave on the left plane
            new_composite = lambda x, c=current_composite, f=freq, a=amp: c(x) + a * np.sin(f * x)
            updated_wave_left = left_plane.plot(
                new_composite,
                color=YELLOW,
                x_range=[-4, 4],
                stroke_width=6
            )

            # Animate the addition of the current wave and update both composite waves
            self.play(
                Create(wave),  # Show the current wave on the right
                Transform(composite_wave, updated_wave_left),  # Update the composite wave on the left
                run_time=1.5
            )
            current_composite = new_composite
            self.wait(0.5)

        # Ensure all waves stay visible
        self.play(FadeIn(wave_components), run_time=1)

        # Reverse the composite wave buildup
        reverse_label = Text("Breaking Down Composite Wave", font_size=20, color=RED).to_edge(DOWN)
        self.play(Transform(composite_label, reverse_label))
        self.wait(0.5)

        for wave, freq, amp, color in reversed(list(zip(wave_components, frequencies, amplitudes, colors))):
            # Update composite wave by removing the contribution of the current wave
            new_composite = lambda x, c=current_composite, f=freq, a=amp: c(x) - a * np.sin(f * x)
            updated_wave_left = left_plane.plot(
                new_composite,
                color=YELLOW,
                x_range=[-4, 4],
                stroke_width=6
            )

            # Animate the removal of the current wave on the right and update the composite wave on the left
            self.play(
                Transform(composite_wave, updated_wave_left),  # Update the composite wave on the left
                FadeOut(wave),  # Fade out the current wave on the right
                run_time=1.5
            )
            current_composite = new_composite
            self.wait(0.5)



        # Transition to histograms
        new_title = Text("Frequency Spectrum", font_size=28, color=TEAL).to_edge(UP, buff=0.1)
        self.play(
            FadeOut(composite_wave),  # Remove composite wave on the right
            FadeOut(composite_label),  # Fade out the composite label
            FadeOut(subtitle),         # Fade out the subtitle
            Transform(title, new_title)  # Transition title
        )
        self.wait(1)

        # Create histograms on the right plane
        for freq, amp, color in zip(frequencies, amplitudes, colors):
            bar = Rectangle(
                height=amp * 4,  # Scale the amplitude for visibility
                width=0.4,
                fill_color=color,
                fill_opacity=0.8,
                stroke_width=0.6,
            ).shift(RIGHT * ((freq - 0.3) * 0.6) + UP * (amp - 0))  # Adjust positions

            freq_label = Text(f"{freq} Hz", font_size=16, color=color).next_to(bar, DOWN)
            
            # Update the composite wave on the left as the histogram is created
            new_composite = lambda x, c=current_composite, f=freq, a=amp: c(x) + a * np.sin(f * x)
            updated_wave_left = left_plane.plot(
                new_composite,
                color=YELLOW,
                x_range=[-4, 4],
                stroke_width=6
            )

            # Animate the creation of the histogram and the update of the composite wave
            self.play(
                Create(bar),  # Show the current histogram on the right plane
                FadeIn(freq_label),  # Label the histogram
                Transform(composite_wave, updated_wave_left),  # Update the composite wave on the left
                run_time=1.5
            )

            current_composite = new_composite
            self.wait(0.3)

        # Fade out all elements except the title and subtitle
        self.play(
            *[FadeOut(mob) for mob in self.mobjects ],
            run_time=2
        )
        self.wait(0.5)

        # Display the final text at the center
        final_text = Text(
            "Fourier Transform converts time-domain signals\ninto frequency-domain for better analysis.",
            font_size=24,
            color=WHITE,
            line_spacing=1,
        ).move_to(ORIGIN)
        self.play(FadeOut(subtitle), Write(final_text), run_time=2)
        self.wait(3)
