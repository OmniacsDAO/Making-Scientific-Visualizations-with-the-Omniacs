from manim import *
import string
import numpy as np

class EnhancedCaesarAnimation(Scene):
    def create_background_grid(self):
        grid = VGroup()
        for i in range(-8, 9):
            h_line = Line(
                start=LEFT * 8 + UP * i,
                end=RIGHT * 8 + UP * i,
                stroke_width=0.5,
                stroke_opacity=0.3,
                color=BLUE_D
            )
            v_line = Line(
                start=LEFT * i + UP * 4,
                end=LEFT * i + DOWN * 4,
                stroke_width=0.5,
                stroke_opacity=0.3,
                color=BLUE_D
            )
            grid.add(h_line, v_line)
        return grid

    def create_frequency_histogram(self, text):
        freq_dict = {char: text.lower().count(char) for char in string.ascii_lowercase}
        max_freq = max(freq_dict.values())
        
        histogram = VGroup()
        colors = [BLUE, RED, GREEN, YELLOW, PURPLE, ORANGE]
        
        for i, (char, freq) in enumerate(freq_dict.items()):
            height = (freq / max_freq) * 2.5
            color = colors[i % len(colors)]
            bar = Rectangle(
                height=height,
                width=0.3,
                fill_opacity=0.8,
                color=color
            ).move_to(RIGHT * (i * 0.4 - 3) + UP * (height/2 - 3))
            
            label = Text(char, font_size=16).next_to(bar, DOWN, buff=0.1)
            histogram.add(VGroup(bar, label))
        
        return histogram

    def create_particle_effect(self, point):
        particles = VGroup()
        colors = [YELLOW_A, YELLOW_B, YELLOW_C, YELLOW_D]

        for _ in range(8):
            angle = np.random.uniform(0, TAU)
            radius = np.random.uniform(0.3, 0.6)
            color = np.random.choice(colors)
            particle = Circle(radius=0.02, fill_opacity=1, color=color)
            particle.move_to(point)
            particles.add(particle)

            target_point = point + radius * np.array([np.cos(angle), np.sin(angle), 0])
            particle.add_updater(lambda m, dt, target=target_point: m.shift(
                (target - m.get_center()) * dt * 2
            ).set_fill(opacity=m.get_fill_opacity() - dt))

        return particles

    def construct(self):
        title = Text("Caesar Cipher Encryption Visualization", font_size=24, color=BLUE)
        title.to_edge(UP*0.5)
        self.play(Write(title))
        
        grid = self.create_background_grid()
        self.play(FadeIn(grid, run_time=2))

        alphabet = string.ascii_lowercase
        radius = 3
        num_letters = len(alphabet)
        
        letter_circles = VGroup()
        colors = [BLUE_A, BLUE_B, BLUE_C, BLUE_D, BLUE_E]
        
        for i, letter in enumerate(alphabet):
            angle = i * TAU / num_letters
            position = radius * np.array([np.cos(angle), np.sin(angle), 0])
            color = colors[i % len(colors)]
            
            circle = Circle(radius=0.3, color=color, stroke_width=4)
            text = Text(letter).scale(0.5)
            text.move_to(circle.get_center())
            combined = VGroup(circle, text)
            combined.move_to(position)
            letter_circles.add(combined)
            
        # Shift the entire letter circle group to the left
        letter_circles.move_to(LEFT * 2.3)

        self.play(Create(letter_circles), rate_func=smooth, run_time=5)
        self.wait(4)

        input_text = "Omnianalytics"
        key = 3
        
        input_display = Text(f"Input: {input_text}", font_size=18, color=WHITE)
        input_display.to_edge(RIGHT, buff=2.0).shift(UP * 3)
        key_display = Text(f"Key: {key}", font_size=18, color=RED)
        key_display.next_to(input_display, DOWN, buff=0.5)
        encrypted_text_display = Text(f"Encrypted: ", font_size=18, color=WHITE)
        encrypted_text_display.next_to(key_display, DOWN, buff=0.5)

        initial_histogram = self.create_frequency_histogram(input_text)
        initial_histogram_title = Text("Frequency Analysis", font_size=24)
        initial_histogram_title.next_to(initial_histogram, UP)
        histogram_group = VGroup(initial_histogram, initial_histogram_title)
        histogram_group.scale(0.7).move_to(RIGHT * 4.5 + DOWN * 2.2) 
        
        self.play(Write(input_display))
        self.wait(2)
        self.play(Write(key_display))
        self.wait(2)
        self.play(Write(encrypted_text_display))
        self.wait(2)
        self.play(Create(histogram_group))
        self.wait(2)


        encrypted_text = ""
        for i, char in enumerate(input_text):
            if char.isalpha():
                current_pos = alphabet.index(char.lower())
                new_pos = (current_pos + key) % 26

                particles = self.create_particle_effect(letter_circles[current_pos].get_center())
                self.add(particles)

                self.play(
                    letter_circles[current_pos][0].animate.set_color(YELLOW),
                    run_time=1.0
                )

                encrypted_char = alphabet[new_pos]
                encrypted_text += encrypted_char

                arrow = Arrow(
                    letter_circles[current_pos].get_center(),
                    letter_circles[new_pos].get_center(),
                    color=RED
                )

                # Add grow effect for target circle with a smoke-like glow
                glow_effect = Circle(
                    radius=0.5,  # Adjust radius to control glow size
                    color=GREEN,  
                    fill_opacity=0.4,
                    stroke_opacity=0.2
                ).move_to(letter_circles[new_pos].get_center())

                glow_effect.scale(0.5)
                self.add(glow_effect)

                # Animate the glow effect to expand and fade out
                self.play(
                    glow_effect.animate.scale(2).set_opacity(0),  # Expands and fades out
                    letter_circles[new_pos].animate.scale(1.2).set_color(GREEN),  # Scale the circle slightly
                    run_time=1.0
                )

                self.play(
                    letter_circles[new_pos].animate.scale(1 / 1.2),  # Return to original scale
                    run_time=0.3
                )

                self.remove(glow_effect)  # Clean up the glow effect

                new_char = Text(encrypted_char, font_size=14, color=WHITE)
                new_char.next_to(encrypted_text_display, RIGHT, buff=0.1 * (i + 1))

                self.play(
                    Create(arrow),
                    Write(new_char),
                    run_time=1
                )

                self.play(FadeOut(particles), run_time=0.5)
                self.wait(0.3)
                self.play(FadeOut(arrow))

                original_color = colors[current_pos % len(colors)]
                new_color = colors[new_pos % len(colors)]
                self.play(
                    letter_circles[current_pos][0].animate.set_color(original_color),
                    letter_circles[new_pos][0].animate.set_color(new_color)
                )

        self.wait(2)
        
         # Group all scene elements
        all_elements = VGroup(
            title,  # The title of the scene
            grid,  # The background grid
            letter_circles,  # The letter circles
            input_display,  # Input text display
            key_display,  # Key display
            encrypted_text_display,  # Encrypted text display
            histogram_group  # The histogram group
        )

        # Apply fade-out to all elements
        self.play(FadeOut(all_elements, run_time=5))  # Adjust run_time for slower fade-out
        self.wait(2)
