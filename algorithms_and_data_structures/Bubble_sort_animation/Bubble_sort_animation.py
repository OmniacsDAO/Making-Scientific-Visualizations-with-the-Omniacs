from manim import *

class BubbleSortBarGraph(Scene):
    def construct(self):
        # Display a title
        title = Text("Bubble Sort Algorithm", font_size=48)
        title.to_edge(UP)
        self.play(Write(title))

        # Display code on the left side
        code = Code(
            code="""
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
            """,
            language="python",
            font_size=18,
            background="window",
            background_stroke_width=1,
            background_stroke_color=WHITE,
            line_spacing=1.1
        )
        code.to_edge(LEFT, buff=0.5)
        self.play(Create(code))

        # Create a bar chart for the array to be sorted
        array_values = [4, 3, 1, 5, 2]
        bars = VGroup(*[
            Rectangle(height=value, width=0.5).set_fill(TEAL, opacity=0.7).set_stroke(WHITE)
            for value in array_values
        ])
        bars.arrange(RIGHT, buff=0.2).to_edge(RIGHT, buff=1)

        # Add text labels on top of the bars
        labels = VGroup(*[
            Text(str(value), font_size=24).next_to(bar, UP)
            for value, bar in zip(array_values, bars)
        ])

        for bar, label in zip(bars, labels):
            self.add(bar, label)

        self.wait(1)

        # Bubble sort logic with animation
        n = len(array_values)
        for i in range(n):
            for j in range(n - i - 1):
                # Highlight the bars being compared
                self.play(
                    bars[j].animate.set_fill(RED, opacity=0.9),
                    bars[j + 1].animate.set_fill(RED, opacity=0.9)
                )
                self.wait(0.5)

                # Swap if needed
                if array_values[j] > array_values[j + 1]:
                    array_values[j], array_values[j + 1] = array_values[j + 1], array_values[j]
                    self.play(
                        Swap(bars[j], bars[j + 1]),
                        Swap(labels[j], labels[j + 1])
                    )
                    bars[j], bars[j + 1] = bars[j + 1], bars[j]
                    labels[j], labels[j + 1] = labels[j + 1], labels[j]

                # Reset color after comparison
                self.play(
                    bars[j].animate.set_fill(TEAL, opacity=0.7),
                    bars[j + 1].animate.set_fill(TEAL, opacity=0.7)
                )
                self.wait(0.2)

        self.wait(1)
        self.play(FadeOut(bars), FadeOut(labels), FadeOut(code), FadeOut(title))
