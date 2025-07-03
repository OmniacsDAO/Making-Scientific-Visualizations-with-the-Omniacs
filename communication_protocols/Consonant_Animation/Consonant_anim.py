from manim import *
from collections import defaultdict

class ConsonantHistogram(Scene):
    def construct(self):

        # Insert your text here
        phrase = ("Omni Analytics Group, found at omnianalytics.org, is a consulting firm specializing "
                  "in data science, statistical analysis, and algorithm development. They work with businesses "
                  "across various industries, including startups, small businesses, and large enterprises. "
                  "Their services range from data strategy and algorithm design to advanced statistical analysis "
                  "and analytics training.")
        
        # Define consonants (I included both UPPER Case consonants so they can be captured das unique characters.)
        consonants = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
        
        # Count consonants progressively
        consonant_counts = defaultdict(int)
        consonant_progression = []
        
        for i, char in enumerate(phrase):
            if char in consonants:
                consonant_counts[char] += 1
            
            # Create a snapshot of current counts at certain intervals
            if i % 10 == 0 or i == len(phrase) - 1:
                consonant_progression.append(dict(consonant_counts))
        
        # Prepare the histogram
        def create_histogram(counts):
            bars = []
            max_count = max(counts.values()) if counts else 1

            x_offset = -6
            bar_width = 0.8  # Width of each bar
            colors = [BLUE, GREEN, YELLOW, PURPLE, ORANGE, TEAL]  # List of colors to cycle through

            for idx, (letter, count) in enumerate(sorted(counts.items())):
                bar_height = count / max_count * 4  # Normalize height
                color = colors[idx % len(colors)]  # Cycle through colors
                bar = Rectangle(
                    width=bar_width, 
                    height=bar_height, 
                    fill_color=color, 
                    fill_opacity=0.7,
                    stroke_width=1
                ).set_x(x_offset).set_y(-2 + bar_height / 2)
                
                # Add letter label
                letter_text = Text(letter, font_size=20).next_to(bar, DOWN)
                
                # Add count label
                count_text = Text(str(count), font_size=20).next_to(bar, UP)
                
                bar_group = VGroup(bar, letter_text, count_text)
                bars.append((bar_group, bar, letter, count))  # Include bar group for easy sorting
                
                # Increment x_offset
                x_offset += 0.5

            return bars
             
                # Animation
        title = Text("Consonant Frequency Progression", font_size=30, color=BLUE).to_edge(UP)
        self.play(Write(title))

        progress_text = None  # Initialize the progress text variable
        for i, counts in enumerate(consonant_progression):
            # Clear previous histogram
            if i > 0:
                self.play(FadeOut(current_histogram))
            
            # Create and animate new histogram
            bars = create_histogram(counts)
            current_histogram = VGroup(*[bar_group[0] for bar_group in bars])
            self.play(Create(current_histogram))
            
            # Progress text
            progress_text = Text(f"Progress: {i+1}/{len(consonant_progression)}", 
                                 font_size=20).to_edge(DOWN)
            if i > 0:
                self.play(ReplacementTransform(prev_progress, progress_text))
            else:
                self.play(Write(progress_text))
            
            prev_progress = progress_text
            
            # Pause briefly
            self.wait(0.2)

        # Fade out the progress text when bubble sort starts
        self.play(FadeOut(progress_text))

        # Fade out the initial title before showing the sorting title
        self.play(FadeOut(title))
                
                # Change title to "Sorting Consonants"
        title_sorting = Text("Sorting Consonants", font_size=30, color=BLUE).to_edge(UP)
        self.play(Write(title_sorting))  # Replace with new title

        
        # Bubble sort animation
        for i in range(len(bars)):
            for j in range(len(bars) - 1 - i):
                bar1, bar2 = bars[j], bars[j + 1]
                
                if bar1[3] > bar2[3]:  # Compare the counts
                    # Highlight bars being compared
                    self.play(
                        bar1[1].animate.set_fill(RED, opacity=0.9),
                        bar2[1].animate.set_fill(RED, opacity=0.9),
                        run_time=0.2
                    )
                    
                    # Swap the bars' positions and groups
                    self.play(
                        bar1[0].animate.shift(0.5 * RIGHT),
                        bar2[0].animate.shift(-0.5 * RIGHT),
                        run_time=0.2
                    )
                    
                    # Swap the elements in the list
                    bars[j], bars[j + 1] = bars[j + 1], bars[j]
                    
                    # Reset colors
                    self.play(
                        bar1[1].animate.set_fill(bar1[1].fill_color, opacity=0.7),
                        bar2[1].animate.set_fill(bar2[1].fill_color, opacity=0.7),
                        run_time=0.2
                    )
        
        self.wait(0.3)  # Final pause after sorting
