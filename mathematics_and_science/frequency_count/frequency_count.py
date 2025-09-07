from manim import *
import numpy as np

class MathematicalFrequencyCount(Scene):
    def construct(self):
        self.camera.background_color = "#1a1a1a"
        self.colors = [RED, ORANGE, BLUE, GREEN, PURPLE]
        self.data = [3, 1, 2, 1, 3, 2, 1, 3, 2, 1, 4, 2, 3, 1, 4, 2, 5, 3, 1, 2, 4, 3, 5, 1, 2]

        self.introduction()
        self.show_data()
        self.setup_counters()
        self.counting_process()
        self.show_results()
        self.final_summary()

    def introduction(self):
        title = Text("Frequency Count Algorithm", font_size=44, color=BLUE)
        title.to_edge(UP, buff=0.5)

        subtitle = Text("Counting occurrences of each value in a dataset",
                       font_size=24, color=GRAY)
        subtitle.next_to(title, DOWN, buff=0.3)

        self.play(Write(title), run_time=1.5)
        self.play(Write(subtitle), run_time=1)
        self.wait(1.5)

        self.play(FadeOut(title), FadeOut(subtitle), run_time=0.5)

    def show_data(self):
        title = Text("Step 1: Our Dataset", font_size=32, color=GREEN)
        title.to_edge(UP, buff=0.8)

        description = Text(f"Dataset with {len(self.data)} numbers:",
                          font_size=20, color=WHITE)
        description.move_to(UP * 2.5)

        self.data_elements = VGroup()
        for i, value in enumerate(self.data):
            element = Text(str(value), font_size=28, color=YELLOW)
            row, col = divmod(i, 10)
            element.move_to(LEFT * 4.5 + RIGHT * col * 0.9 + UP * (1.5 - row * 0.6))
            self.data_elements.add(element)

        self.play(Write(title), FadeIn(description), run_time=1)
        self.play(
            LaggedStart(
                *[FadeIn(element, shift=DOWN*0.2) for element in self.data_elements],
                lag_ratio=0.04
            ),
            run_time=2
        )
        self.wait(1.5)

        self.current_title = title
        self.current_description = description

    def setup_counters(self):
        self.play(
            FadeOut(self.current_title),
            FadeOut(self.current_description),
            FadeOut(self.data_elements),
            run_time=0.8
        )

        title = Text("Step 2: Initialize Counters", font_size=32, color=GREEN)
        title.to_edge(UP, buff=0.8)

        description = Text("Create counters for each unique value:",
                          font_size=20, color=WHITE)
        description.move_to(UP * 2.5)

        self.play(Write(title), FadeIn(description), run_time=0.8)

        self.data_elements = VGroup()
        for i, value in enumerate(self.data):
            element = Text(str(value), font_size=20, color=YELLOW)
            row, col = divmod(i, 15)
            element.move_to(LEFT * 5 + RIGHT * col * 0.67 + UP * (2 - row * 0.4))
            self.data_elements.add(element)

        unique_values = sorted(set(self.data))
        self.counters = {}
        self.counter_groups = VGroup()

        for i, value in enumerate(unique_values):
            color = self.colors[i]
            x_pos = LEFT * 4 + RIGHT * i * 2.2

            value_label = Text(f"Value {value}", font_size=20, color=WHITE)
            value_label.move_to(x_pos + DOWN * 1)

            counter_box = Rectangle(width=1.6, height=0.8, color=color,
                                  fill_opacity=0.2, stroke_width=2)
            counter_box.next_to(value_label, DOWN, buff=0.3)

            counter_text = Text("0", font_size=26, color=color, weight=BOLD)
            counter_text.move_to(counter_box.get_center())

            self.counters[value] = {
                'count': 0,
                'text': counter_text,
                'box': counter_box,
                'color': color
            }

            counter_group = VGroup(value_label, counter_box, counter_text)
            self.counter_groups.add(counter_group)

        self.play(FadeIn(self.data_elements), run_time=0.8)
        self.play(FadeIn(self.counter_groups), run_time=1.5)
        self.wait(1)

        self.current_title = title
        self.current_description = description

    def counting_process(self):
        new_title = Text("Step 3: Count Each Value", font_size=32, color=GREEN)
        new_title.to_edge(UP, buff=0.8)

        new_description = Text("Processing each number in the dataset:",
                              font_size=20, color=WHITE)
        new_description.move_to(UP * 2.5)

        self.play(
            Transform(self.current_title, new_title),
            Transform(self.current_description, new_description),
            run_time=0.8
        )

        progress_text = Text("Progress: 0%", font_size=18, color=YELLOW)
        progress_text.move_to(DOWN * 3.2)
        self.play(FadeIn(progress_text))

        total_items = len(self.data)

        for i, value in enumerate(self.data):
            highlight = Circle(radius=0.2, color=WHITE, stroke_width=2)
            highlight.move_to(self.data_elements[i].get_center())

            self.counters[value]['count'] += 1
            new_count = self.counters[value]['count']

            new_counter_text = Text(str(new_count), font_size=26,
                                  color=self.counters[value]['color'], weight=BOLD)
            new_counter_text.move_to(self.counters[value]['text'].get_center())

            progress = int((i + 1) / total_items * 100)
            new_progress = Text(f"Progress: {progress}%", font_size=18, color=YELLOW)
            new_progress.move_to(DOWN * 3.2)

            animations = [
                Create(highlight),
                self.data_elements[i].animate.scale(1.15),
                Transform(self.counters[value]['text'], new_counter_text)
            ]

            if i % 5 == 0:
                animations.append(Transform(progress_text, new_progress))

            self.play(*animations, run_time=0.08)
            self.play(
                FadeOut(highlight),
                self.data_elements[i].animate.scale(1/1.15),
                run_time=0.05
            )

        self.play(FadeOut(progress_text), run_time=0.3)
        self.wait(0.5)

        self.final_progress = progress_text

    def show_results(self):
        self.play(
            FadeOut(self.current_title),
            FadeOut(self.current_description),
            FadeOut(self.data_elements),
            FadeOut(self.counter_groups),
            run_time=1
        )

        title = Text("Step 4: Results & Visualization", font_size=32, color=GREEN)
        title.move_to(UP * 3.5)

        self.play(Write(title), run_time=1)

        sorted_values = sorted(self.counters.keys())
        max_count = max(c['count'] for c in self.counters.values())

        chart_title = Text("📊 Frequency Distribution BarChart", font_size=26, color=BLUE, weight=BOLD)
        chart_title.move_to(UP * 2.6)

        x_axis = Line(LEFT * 3.5, RIGHT * 1.5, color=WHITE, stroke_width=2)
        x_axis.move_to(DOWN * 2.5)

        y_axis = Line(DOWN * 2.5, UP * 0.8, color=WHITE, stroke_width=2)
        y_axis.move_to(LEFT * 3.5)

        y_axis_label = Text("Frequency (Count)", font_size=18, color=YELLOW, weight=BOLD)
        y_axis_label.move_to(LEFT * 5 + DOWN * 0.5).rotate(PI/2)

        x_axis_label = Text("Dataset Values", font_size=18, color=YELLOW, weight=BOLD)
        x_axis_label.move_to(DOWN * 3.2)

        grid_lines = VGroup()
        total_chart_height = 3.3

        for i in range(0, max_count + 1):
            y_pos = DOWN * 2.5 + UP * (i / max_count * total_chart_height)
            grid_line = DashedLine(LEFT * 3.5, RIGHT * 1.5, color=GRAY, stroke_opacity=0.3)
            grid_line.move_to(y_pos)
            grid_lines.add(grid_line)

            tick_label = Text(str(i), font_size=14, color=GRAY)
            tick_label.move_to(LEFT * 3.8 + y_pos[1] * UP)
            grid_lines.add(tick_label)

        self.play(FadeIn(chart_title), run_time=0.8)
        self.play(Create(x_axis), Create(y_axis), run_time=1)
        self.play(FadeIn(grid_lines), run_time=0.5)
        self.play(FadeIn(y_axis_label), FadeIn(x_axis_label), run_time=0.8)

        bars = VGroup()

        for i, value in enumerate(sorted_values):
            count = self.counters[value]['count']
            color = self.counters[value]['color']

            bar_height = count / max_count * total_chart_height

            bar = RoundedRectangle(
                height=bar_height,
                width=1.0,
                corner_radius=0.1,
                color=color,
                fill_opacity=0.8,
                stroke_width=3,
                stroke_color=WHITE
            )

            x_pos = LEFT * 2.5 + RIGHT * i * 1.0
            bar.move_to(x_pos + DOWN * 2.5 + UP * (bar_height/2))


            value_label = Text(str(value), font_size=22, color=WHITE, weight=BOLD)
            value_label.move_to(x_pos + DOWN * 2.8)

            count_circle = Circle(radius=0.25, color=color, fill_opacity=0.9, stroke_width=2, stroke_color=WHITE)
            count_circle.move_to(x_pos + DOWN * 2.5 + UP * bar_height + UP * 0.4)

            count_label = Text(str(count), font_size=18, color=WHITE, weight=BOLD)
            count_label.move_to(count_circle.get_center())

            percentage = round((count / len(self.data)) * 100, 1)
            percent_label = Text(f"{percentage}%", font_size=14, color=color, weight=BOLD)
            percent_label.next_to(count_circle, UP, buff=0.1)

            bar_group = VGroup(bar, value_label, count_circle, count_label, percent_label)
            bars.add(bar_group)

        for i, bar_group in enumerate(bars):
            bar, value_label, count_circle, count_label, percent_label = bar_group

            self.play(FadeIn(value_label), run_time=0.3)

            self.play(FadeIn(bar), run_time=0.6)

            self.play(
                FadeIn(count_circle),
                FadeIn(count_label),
                FadeIn(percent_label),
                run_time=0.4
            )

            self.wait(0.2)

        total_items = len(self.data)
        unique_items = len(sorted_values)

        stats_title = Text("📈 Summary Statistics", font_size=20, color=ORANGE, weight=BOLD)
        stats_title.move_to(RIGHT * 4.5 + UP * 1.5)

        stats_group = VGroup()
        stats_info = [
            f"Total Items: {total_items}",
            f"Unique Values: {unique_items}",
            f"Most Frequent: Value {max(self.counters.keys(), key=lambda x: self.counters[x]['count'])}",
            f"Max Frequency: {max_count}"
        ]

        for stat in stats_info:
            stat_text = Text(stat, font_size=16, color=WHITE)
            stats_group.add(stat_text)

        stats_group.arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        stats_group.next_to(stats_title, DOWN, buff=0.3)

        self.play(FadeIn(stats_title), run_time=0.5)
        self.play(
            LaggedStart(
                *[FadeIn(stat, shift=RIGHT*0.2) for stat in stats_group],
                lag_ratio=0.2
            ),
            run_time=1.5
        )

        self.wait(3)

        self.play(
            FadeOut(VGroup(title, chart_title, x_axis, y_axis, grid_lines,
                          y_axis_label, x_axis_label, bars, stats_title, stats_group)),
            run_time=1.2
        )

    def final_summary(self):
        title = Text("Algorithm Summary", font_size=40, color=BLUE)
        title.move_to(UP * 3)

        steps = [
            "1. Initialize counters for each unique value",
            "2. Iterate through the dataset once",
            "3. Increment counter for each value encountered",
            "4. Output the frequency distribution"
        ]

        step_group = VGroup()
        for step in steps:
            step_text = Text(step, font_size=24, color=WHITE)
            step_group.add(step_text)

        step_group.arrange(DOWN, buff=0.5, aligned_edge=LEFT)
        step_group.move_to(UP * 0.8)

        complexity_title = Text("Complexity Analysis:", font_size=22, color=YELLOW)
        complexity_title.move_to(DOWN * 1.2)

        time_complexity = Text("• Time Complexity: O(n)", font_size=20, color=WHITE)
        time_complexity.move_to(DOWN * 1.7)

        space_complexity = Text("• Space Complexity: O(k) where k = unique values", font_size=20, color=WHITE)
        space_complexity.move_to(DOWN * 2.1)

        applications = Text("Applications: Statistics, Data Analysis, Histograms, Survey Data",
                           font_size=18, color=GRAY)
        applications.move_to(DOWN * 2.8)

        self.play(Write(title), run_time=1.2)
        self.play(
            LaggedStart(
                *[FadeIn(step, shift=RIGHT*0.3) for step in step_group],
                lag_ratio=0.3
            ),
            run_time=2.5
        )
        self.play(FadeIn(complexity_title), run_time=0.8)
        self.play(FadeIn(time_complexity), FadeIn(space_complexity), run_time=1)
        self.play(FadeIn(applications), run_time=0.8)

        self.wait(3)

        self.play(FadeOut(Group(*self.mobjects)), run_time=1)
        credits_title = Text("Sources Used", font_size=42, color=BLUE, weight=BOLD)
        credits_title.to_edge(UP, buff=1)
        self.play(Write(credits_title))
        self.wait(1)

        credit_entries = VGroup()



        pixabay_icon = VGroup(
            Circle(radius=0.3, fill_color=GREEN, fill_opacity=0.8, stroke_color=WHITE),
            Text("P", font_size=20, color=WHITE, weight=BOLD)
        )
        pixabay_text = Text("Pixabay - Music", font_size=24, color=WHITE)
        pixabay_entry = VGroup(pixabay_icon, pixabay_text)
        pixabay_entry.arrange(RIGHT, buff=0.5)

        canva_icon = VGroup(
            RoundedRectangle(width=0.6, height=0.6, corner_radius=0.3,
                           fill_color=PURPLE, fill_opacity=0.8, stroke_color=WHITE),
            Text("C", font_size=20, color=WHITE, weight=BOLD)
        )
        canva_text = Text("Canva - Video Editing", font_size=24, color=WHITE)
        canva_entry = VGroup(canva_icon, canva_text)
        canva_entry.arrange(RIGHT, buff=0.5)

        credit_entries.add( pixabay_entry, canva_entry)
        credit_entries.arrange(DOWN, buff=0.8, aligned_edge=LEFT)
        credit_entries.move_to(ORIGIN + DOWN * 0.5)

        for entry in credit_entries:
            self.play(
                FadeIn(entry[0], shift=RIGHT*0.5),
                Write(entry[1], run_time=1.5)
            )
            self.wait(0.5)

        self.wait(2)
        self.play(FadeOut(Group(*self.mobjects)), run_time=1)
