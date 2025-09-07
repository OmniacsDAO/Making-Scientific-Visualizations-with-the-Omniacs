
from manim import *
import numpy as np

class MastersTheoremVisualization(Scene):
    def construct(self):
        self.camera.background_color = "#0f0f0f"
        self.title_scene()
        self.formula_scene()
        self.problem_breakdown_scene()
        self.three_cases_scene()
        self.merge_sort_case_animation()
        self.binary_search_case_animation()
        self.expensive_combining_case_animation()
        self.final_visual_summary()

    def title_scene(self):
        title = Text("Master's Theorem", font_size=48, color=BLUE)
        title.set_weight(BOLD)

        self.play(Write(title), run_time=2)
        self.wait(2)
        self.play(FadeOut(title), run_time=1)

    def formula_scene(self):

        formula = MathTex(r"T(n) = aT\left(\frac{n}{b}\right) + f(n)",
                         font_size=40, color=YELLOW)
        formula.next_to(DOWN, buff=0.8)

        a_highlight = Circle(radius=0.3, color=RED, stroke_width=3).move_to(formula[0][4])
        b_highlight = Circle(radius=0.3, color=GREEN, stroke_width=3).move_to(formula[0][8])
        f_highlight = Circle(radius=0.4, color=PURPLE, stroke_width=3).move_to(formula[0][12])

        self.play(Write(formula), run_time=1.5)

        self.play(Create(a_highlight), run_time=0.5)
        self.play(Transform(a_highlight, Text("# subproblems", font_size=16, color=RED).move_to(UP*2.5 + LEFT*3)))

        self.play(Create(b_highlight), run_time=0.5)
        self.play(Transform(b_highlight, Text("division factor", font_size=16, color=GREEN).move_to(UP*2.5)))

        self.play(Create(f_highlight), run_time=0.5)
        self.play(Transform(f_highlight, Text("combining cost", font_size=16, color=PURPLE).move_to(UP*2.5 + RIGHT*3)))

        self.wait(1)
        self.play(FadeOut(VGroup(formula, a_highlight, b_highlight, f_highlight)), run_time=0.8)

    def problem_breakdown_scene(self):

        big_problem = Circle(radius=1.5, color=BLUE, fill_opacity=0.8)
        big_problem.move_to(UP * 2)
        problem_text = Text("Problem\nSize n", font_size=20, color=WHITE)
        problem_text.move_to(big_problem.get_center())

        self.play(Create(big_problem), Write(problem_text), run_time=1)

        arrow1 = Arrow(big_problem.get_center(), LEFT*2 + UP*0.5, color=WHITE, stroke_width=3)
        arrow2 = Arrow(big_problem.get_center(), RIGHT*2 + UP*0.5, color=WHITE, stroke_width=3)

        sub1 = Circle(radius=1, color=ORANGE, fill_opacity=0.7)
        sub1.move_to(LEFT*2 + UP*0.5)
        sub1_text = Text("n/2", font_size=16, color=WHITE)
        sub1_text.move_to(sub1.get_center())

        sub2 = Circle(radius=1, color=ORANGE, fill_opacity=0.7)
        sub2.move_to(RIGHT*2 + UP*0.5)
        sub2_text = Text("n/2", font_size=16, color=WHITE)
        sub2_text.move_to(sub2.get_center())

        self.play(
            Create(arrow1), Create(arrow2),
            Create(sub1), Write(sub1_text),
            Create(sub2), Write(sub2_text),
            run_time=1.5
        )

        arrows_level2 = VGroup(
            Arrow(sub1.get_center(), LEFT*3.5 + DOWN*0.8, color=WHITE),
            Arrow(sub1.get_center(), LEFT*0.5 + DOWN*0.8, color=WHITE),
            Arrow(sub2.get_center(), RIGHT*0.5 + DOWN*0.8, color=WHITE),
            Arrow(sub2.get_center(), RIGHT*3.5 + DOWN*0.8, color=WHITE)
        )

        subs_level2 = VGroup()
        positions = [LEFT*3.5 + DOWN*0.8, LEFT*0.5 + DOWN*0.8,
                    RIGHT*0.5 + DOWN*0.8, RIGHT*3.5 + DOWN*0.8]
        for pos in positions:
            small_sub = Circle(radius=0.6, color=RED, fill_opacity=0.6)
            small_sub.move_to(pos)
            small_text = Text("n/4", font_size=12, color=WHITE)
            small_text.move_to(small_sub.get_center())
            subs_level2.add(VGroup(small_sub, small_text))

        self.play(Create(arrows_level2), Create(subs_level2), run_time=1.5)

        question = Text("Which dominates the total runtime?", font_size=24, color=YELLOW)
        question.set_weight(BOLD)
        question.move_to(DOWN * 2.2)

        subtext = Text("The work splitting/combining OR the work solving subproblems?",
                      font_size=18, color=WHITE)
        subtext.move_to(DOWN * 2.8)

        self.play(Write(question), run_time=1.2)
        self.play(Write(subtext), run_time=1.2)
        self.wait(2)

        self.play(FadeOut(Group(*self.mobjects)), run_time=1)

    def three_cases_scene(self):

        title = Text("3 Cases of Master's Theorem", font_size=36, color=WHITE)
        title.set_weight(BOLD)
        title.move_to(UP * 3.2)
        cases_group = VGroup()

        case_colors = [BLUE, ORANGE, RED]
        case_names = ["Case 1", "Case 2", "Case 3"]
        x_positions = [LEFT*4, ORIGIN, RIGHT*4]

        for i, (color, name, x_pos) in enumerate(zip(case_colors, case_names, x_positions)):
            case_title = Text(name, font_size=20, color=color)
            case_title.set_weight(BOLD)
            case_title.move_to(x_pos + UP*2.2)

            scale_base = Line(LEFT*1.5, RIGHT*1.5, color=WHITE, stroke_width=4)
            scale_base.move_to(x_pos + UP*0.8)

            scale_center = Line(UP*0.3, DOWN*0.3, color=WHITE, stroke_width=4)
            scale_center.move_to(x_pos + UP*0.8)

            sub_weight = Rectangle(width=1, height=0.8, color=GRAY, fill_opacity=0.8)
            sub_weight.move_to(x_pos + LEFT*1 + UP*1.3)
            sub_text = Text("Subproblems", font_size=10, color=WHITE)
            sub_text.move_to(sub_weight.get_center())

            if i == 0:  # Case 1: combining is lighter
                combine_height = 0.4
                scale_rotation = -15 * DEGREES  # Tips left (subproblems heavier)
            elif i == 1:  # Case 2: balanced
                combine_height = 0.8
                scale_rotation = 0  # Balanced
            else:  # Case 3: combining is heavier
                combine_height = 1.6
                scale_rotation = 15 * DEGREES  # Tips right (combining heavier)

            combine_weight = Rectangle(width=1, height=combine_height, color=color, fill_opacity=0.8)
            combine_weight.move_to(x_pos + RIGHT*1 + UP*(0.8 + combine_height/2))
            combine_text = Text("Combining", font_size=10, color=WHITE)
            combine_text.move_to(combine_weight.get_center())

            # Rotate scale
            scale_base.rotate(scale_rotation, about_point=x_pos + UP*0.8)

            case_group = VGroup(case_title, scale_base, scale_center,
                               sub_weight, sub_text, combine_weight, combine_text)
            cases_group.add(case_group)

        self.play(Write(title), run_time=1)

        for case_group in cases_group:
            self.play(Create(case_group), run_time=1.2)
            self.wait(0.3)

        results = VGroup(
            MathTex(r"O(n^{\log a})", font_size=18, color=BLUE).move_to(LEFT*4 + DOWN*0.2),
            MathTex(r"O(n^{\log a} \log n)", font_size=16, color=ORANGE).move_to(ORIGIN + DOWN*0.2),
            MathTex(r"O(f(n))", font_size=18, color=RED).move_to(RIGHT*4 + DOWN*0.2)
        )

        self.play(Write(results), run_time=1.5)

        explanation = VGroup(
            Text("Case 1: Subproblems dominate", font_size=16, color=BLUE).move_to(LEFT*4 + DOWN*0.8),
            Text("(many small problems)", font_size=12, color=BLUE).move_to(LEFT*4 + DOWN*1.1),

            Text("Case 2: Perfectly balanced", font_size=16, color=ORANGE).move_to(ORIGIN + DOWN*0.8),
            Text("(equal work each level)", font_size=12, color=ORANGE).move_to(ORIGIN + DOWN*1.1),

            Text("Case 3: Combining dominates", font_size=16, color=RED).move_to(RIGHT*4 + DOWN*0.8),
            Text("(expensive merging)", font_size=12, color=RED).move_to(RIGHT*4 + DOWN*1.1)
        )

        self.play(Write(explanation), run_time=2)

        bottom_explanation = VGroup(
            Text("The Master's Theorem compares f(n) with n^(log a)", font_size=18, color=YELLOW),
            Text("to determine which of these three cases applies", font_size=18, color=YELLOW)
        )
        bottom_explanation.arrange(DOWN, buff=0.2)
        bottom_explanation.move_to(DOWN * 2.5)

        self.play(Write(bottom_explanation), run_time=1.5)
        self.wait(3)

        self.play(FadeOut(Group(*self.mobjects)), run_time=1)

    def merge_sort_case_animation(self):
        title = Text("Merge Sort - Case 2", font_size=32, color=ORANGE)
        title.move_to(UP * 3.5)

        numbers = [8, 3, 7, 1, 6, 2, 5, 4]

        # Initial array
        initial_array = VGroup()
        for i, num in enumerate(numbers):
            rect = Rectangle(width=0.5, height=0.5, color=BLUE, fill_opacity=0.7, stroke_width=2)
            rect.move_to(LEFT*1.75 + RIGHT*i*0.5 + UP*2.8)
            text = Text(str(num), font_size=16, color=WHITE)
            text.move_to(rect.get_center())
            initial_array.add(VGroup(rect, text))

        array_label = Text("Unsorted Array", font_size=14, color=WHITE)
        array_label.move_to(UP * 2.2)

        self.play(Write(title), run_time=1)
        self.play(Create(initial_array), Write(array_label), run_time=1.5)

        self.wait(0.5)

        level0_y = UP * 1.5
        level0_label = Text("Level 0: Merge pairs (4 merges)", font_size=14, color=WHITE)
        level0_label.move_to(LEFT*4.5 + level0_y)

        # Show 4 pairs being merged
        pairs = [
            ([8, 3], [3, 8]), ([7, 1], [1, 7]),
            ([6, 2], [2, 6]), ([5, 4], [4, 5])
        ]

        merge_groups = VGroup()
        for i, (unsorted, sorted_pair) in enumerate(pairs):
            x_pos = LEFT*1.5 + RIGHT*i*1

            pair_group = VGroup()
            for j, num in enumerate(unsorted):
                rect = Rectangle(width=0.4, height=0.4, color=RED, fill_opacity=0.6, stroke_width=2)
                rect.move_to(x_pos + RIGHT*j*0.4 + level0_y + UP*0.3)
                text = Text(str(num), font_size=12, color=WHITE)
                text.move_to(rect.get_center())
                pair_group.add(VGroup(rect, text))

            arrow = Arrow(x_pos + RIGHT*0.2 + level0_y + UP*0.1,
                         x_pos + RIGHT*0.2 + level0_y - UP*0.3,
                         color=WHITE, stroke_width=2, max_tip_length_to_length_ratio=0.3)

            sorted_group = VGroup()
            for j, num in enumerate(sorted_pair):
                rect = Rectangle(width=0.4, height=0.4, color=GREEN, fill_opacity=0.6, stroke_width=2)
                rect.move_to(x_pos + RIGHT*j*0.4 + level0_y - UP*0.6)
                text = Text(str(num), font_size=12, color=WHITE)
                text.move_to(rect.get_center())
                sorted_group.add(VGroup(rect, text))

            merge_groups.add(VGroup(pair_group, arrow, sorted_group))

        work_indicator_0 = Text("Work: 8 elements processed", font_size=12, color=YELLOW)
        work_indicator_0.move_to(RIGHT*3 + level0_y)

        self.play(Write(level0_label), run_time=0.8)
        self.play(Create(merge_groups), Write(work_indicator_0), run_time=2)

        level1_y = UP * 0.3
        level1_label = Text("Level 1: Merge groups of 4 (2 merges)", font_size=14, color=WHITE)
        level1_label.move_to(LEFT*4.5 + level1_y)

        merge1 = VGroup()
        # First merge: [3,8] + [1,7] = [1,3,7,8]
        for i, num in enumerate([1, 3, 7, 8]):
            rect = Rectangle(width=0.4, height=0.4, color=GREEN, fill_opacity=0.8, stroke_width=2)
            rect.move_to(LEFT*1 + RIGHT*i*0.4 + level1_y)
            text = Text(str(num), font_size=12, color=WHITE)
            text.move_to(rect.get_center())
            merge1.add(VGroup(rect, text))

        # Second merge: [2,6] + [4,5] = [2,4,5,6]
        merge2 = VGroup()
        for i, num in enumerate([2, 4, 5, 6]):
            rect = Rectangle(width=0.4, height=0.4, color=GREEN, fill_opacity=0.8, stroke_width=2)
            rect.move_to(RIGHT*0.6 + RIGHT*i*0.4 + level1_y)
            text = Text(str(num), font_size=12, color=WHITE)
            text.move_to(rect.get_center())
            merge2.add(VGroup(rect, text))

        work_indicator_1 = Text("Work: 8 elements processed", font_size=12, color=YELLOW)
        work_indicator_1.move_to(RIGHT*3 + level1_y)

        self.play(Write(level1_label), run_time=0.8)
        self.play(Create(merge1), Create(merge2), Write(work_indicator_1), run_time=1.5)

        level2_y = DOWN * 0.9
        level2_label = Text("Level 2: Final merge (1 merge)", font_size=14, color=WHITE)
        level2_label.move_to(LEFT*4.5 + level2_y)

        # Final sorted array
        final_array = VGroup()
        sorted_nums = [1, 2, 3, 4, 5, 6, 7, 8]
        for i, num in enumerate(sorted_nums):
            rect = Rectangle(width=0.5, height=0.5, color=GOLD, fill_opacity=0.9, stroke_width=2)
            rect.move_to(LEFT*1.75 + RIGHT*i*0.5 + level2_y)
            text = Text(str(num), font_size=16, color=BLACK)
            text.move_to(rect.get_center())
            final_array.add(VGroup(rect, text))

        work_indicator_2 = Text("Work: 8 elements processed", font_size=12, color=YELLOW)
        work_indicator_2.move_to(RIGHT*3 + level2_y)

        self.play(Write(level2_label), run_time=0.8)
        self.play(Create(final_array), Write(work_indicator_2), run_time=1.5)

        key_insight = Text("Key Insight: Each level processes ALL n elements",
                          font_size=16, color=ORANGE)
        key_insight.set_weight(BOLD)
        key_insight.move_to(DOWN * 1.8)

        levels_count = Text("Number of levels: log₂(8) = 3", font_size=16, color=WHITE)
        levels_count.move_to(DOWN * 2.3)

        final_result = MathTex(r"T(n) = 3 \times n = O(n \log n)", font_size=20, color=ORANGE)
        final_result.set_weight(BOLD)
        final_result.move_to(DOWN * 2.8)

        self.play(Write(key_insight), run_time=1.2)
        self.play(Write(levels_count), run_time=1)
        self.play(Write(final_result), run_time=1.5)

        self.wait(3)
        self.play(FadeOut(Group(*self.mobjects)), run_time=1)

    def binary_search_case_animation(self):

        title = Text("Binary Search - Case 1", font_size=32, color=BLUE)
        title.move_to(UP * 3.5)

        recurrence_relation = MathTex(r"T(n) = 1 \cdot T\left(\frac{n}{2}\right) + O(1)",
                                     font_size=24, color=YELLOW)
        recurrence_relation.move_to(UP * 2.8)

        parameters = Text("a = 1, b = 2, f(n) = O(1)", font_size=16, color=WHITE)
        parameters.move_to(UP * 2.4)

        self.play(Write(title), run_time=1)
        self.play(Write(recurrence_relation), run_time=1)
        self.play(Write(parameters), run_time=1)
        self.wait(1)

        self.play(FadeOut(VGroup(recurrence_relation, parameters)), run_time=0.5)

        # Create a visual representation of the binary search tree
        # Level 0= Full array (n elements)
        level0_box = Rectangle(width=4, height=0.6, color=BLUE, fill_opacity=0.3)
        level0_box.move_to(UP * 1.8)
        level0_text = Text("Search in n elements", font_size=14, color=WHITE)
        level0_text.move_to(level0_box.get_center())
        level0_work = Text("Work: O(1)", font_size=12, color=YELLOW)
        level0_work.move_to(level0_box.get_center() + RIGHT * 2.8)

        # Level 1= Half array (n/2 elements)
        arrow_to_level1 = Arrow(level0_box.get_bottom(), LEFT * 0 + UP * 0.8,
                               color=WHITE, stroke_width=2)
        level1_box = Rectangle(width=2, height=0.6, color=BLUE, fill_opacity=0.5)
        level1_box.move_to(UP * 0.8)
        level1_text = Text("Search in n/2 elements", font_size=12, color=WHITE)
        level1_text.move_to(level1_box.get_center())
        level1_work = Text("Work: O(1)", font_size=12, color=YELLOW)
        level1_work.move_to(level1_box.get_center() + RIGHT * 1.8)

        # Level 2= Quarter array (n/4 elements)
        arrow_to_level2 = Arrow(level1_box.get_bottom(), LEFT * 0 + DOWN * 0.2,
                               color=WHITE, stroke_width=2)
        level2_box = Rectangle(width=1, height=0.6, color=BLUE, fill_opacity=0.7)
        level2_box.move_to(DOWN * 0.2)
        level2_text = Text("Search in n/4 elements", font_size=12, color=WHITE)
        level2_text.move_to(level2_box.get_center())
        level2_work = Text("Work: O(1)", font_size=12, color=YELLOW)
        level2_work.move_to(level2_box.get_center() + RIGHT * 1.3)

        # Level 3= Continue until only 1 element remains
        arrow_to_level3 = Arrow(level2_box.get_bottom(), LEFT * 0 + DOWN * 1.2,
                               color=WHITE, stroke_width=2)
        level3_text = Text("... continue until 1 element", font_size=12, color=WHITE)
        level3_text.move_to(DOWN * 1.2)
        level3_work = Text("Work: O(1)", font_size=12, color=YELLOW)
        level3_work.move_to(level3_text.get_center() + RIGHT * 1.8)

        # Animate the construction of the binary search tree
        self.play(Create(level0_box), Write(level0_text), Write(level0_work), run_time=1.2)
        self.play(Create(arrow_to_level1), run_time=0.5)
        self.play(Create(level1_box), Write(level1_text), Write(level1_work), run_time=1.2)
        self.play(Create(arrow_to_level2), run_time=0.5)
        self.play(Create(level2_box), Write(level2_text), Write(level2_work), run_time=1.2)
        self.play(Create(arrow_to_level3), run_time=0.5)
        self.play(Write(level3_text), Write(level3_work), run_time=1)

        insight_box = Rectangle(width=6, height=1.5, color=GREEN, stroke_width=2, fill_opacity=0.1)
        insight_box.move_to(DOWN * 2.8)

        insight_title = Text("Key Insight:", font_size=16, color=GREEN)
        insight_title.set_weight(BOLD)
        insight_title.move_to(insight_box.get_top() + DOWN * 0.3)

        insight1 = Text("• Only 1 subproblem per level (a = 1)", font_size=14, color=WHITE)
        insight1.move_to(insight_box.get_center() + UP * 0.2)

        insight2 = Text("• Each level does O(1) work", font_size=14, color=WHITE)
        insight2.move_to(insight_box.get_center() + DOWN * 0.2)

        insight3 = Text("• log₂(n) levels total", font_size=14, color=WHITE)
        insight3.move_to(insight_box.get_center() + DOWN * 0.6)

        self.play(Create(insight_box), run_time=0.5)
        self.play(Write(insight_title), run_time=0.8)
        self.play(Write(insight1), run_time=0.8)
        self.play(Write(insight2), run_time=0.8)
        self.play(Write(insight3), run_time=0.8)

        final_result = MathTex(r"T(n) = O(1) \times \log n = O(\log n)",
                              font_size=20, color=BLUE)
        final_result.set_weight(BOLD)
        final_result.move_to(DOWN * 3.8)

        self.play(Write(final_result), run_time=1.5)
        self.wait(3)

        self.play(FadeOut(Group(*self.mobjects)), run_time=1)

    def expensive_combining_case_animation(self):

        title = Text("Case 3: When Combining Work Dominates", font_size=28, color=RED)
        title.set_weight(BOLD)
        title.move_to(UP * 3.5)

        subtitle = Text("Example: Matrix Multiplication (Naive Method)", font_size=18, color=WHITE)
        subtitle.move_to(UP * 3)

        self.play(Write(title), run_time=1.5)
        self.play(Write(subtitle), run_time=1)
        self.wait(1)

        problem_explanation = Text("To multiply two n×n matrices, we can:", font_size=16, color=WHITE)
        problem_explanation.move_to(UP * 2.3)

        step1 = Text("1. Split each matrix into 4 quadrants", font_size=14, color=YELLOW)
        step1.move_to(UP * 1.9)

        step2 = Text("2. This creates 8 subproblems of size n/2", font_size=14, color=YELLOW)
        step2.move_to(UP * 1.6)

        step3 = Text("3. Combine results requires O(n²) operations", font_size=14, color=YELLOW)
        step3.move_to(UP * 1.3)

        self.play(Write(problem_explanation), run_time=1)
        self.play(Write(step1), run_time=0.8)
        self.play(Write(step2), run_time=0.8)
        self.play(Write(step3), run_time=0.8)
        self.wait(1.5)

        self.play(FadeOut(VGroup(subtitle, problem_explanation, step1, step2, step3)), run_time=0.8)

        recurrence = MathTex(r"T(n) = 8T\left(\frac{n}{2}\right) + \Theta(n^2)",
                            font_size=26, color=YELLOW)
        recurrence.move_to(UP * 2.5)

        parameters_box = Rectangle(width=5, height=0.8, color=BLUE, stroke_width=2, fill_opacity=0.1)
        parameters_box.move_to(UP * 1.8)

        parameters = VGroup(
            Text("a = 8 (subproblems)", font_size=14, color=WHITE),
            Text("b = 2 (division factor)", font_size=14, color=WHITE),
            Text("f(n) = Θ(n²) (combining cost)", font_size=14, color=WHITE)
        )
        parameters.arrange(RIGHT, buff=0.8)
        parameters.move_to(parameters_box.get_center())

        self.play(Write(recurrence), run_time=1.5)
        self.play(Create(parameters_box), Write(parameters), run_time=1.5)
        self.wait(1)

        self.play(FadeOut(VGroup(parameters_box, parameters)), run_time=0.8)

        tree_title = Text("Recursion Tree Analysis", font_size=20, color=GREEN)
        tree_title.set_weight(BOLD)
        tree_title.move_to(UP * 1.5)

        self.play(Write(tree_title), run_time=1)
        root = Circle(radius=0.5, color=RED, fill_opacity=0.2, stroke_width=3)
        root.move_to(UP * 0.8)

        root_info = VGroup(
            Text("n×n", font_size=14, color=WHITE),
            Text("Cost: n²", font_size=10, color=YELLOW)
        )
        root_info.arrange(DOWN, buff=0.1)
        root_info.move_to(root.get_center())

        level0_label = Text("Level 0: 1 problem, n² work", font_size=12, color=WHITE)
        level0_label.move_to(LEFT * 4.5 + UP * 0.8)

        self.play(Create(root), Write(root_info), Write(level0_label), run_time=1.5)

        level1_positions = [
            LEFT*2.5 + DOWN*0.2, LEFT*0.8 + DOWN*0.2, RIGHT*0.8 + DOWN*0.2, RIGHT*2.5 + DOWN*0.2,
            LEFT*2.5 + DOWN*0.8, LEFT*0.8 + DOWN*0.8, RIGHT*0.8 + DOWN*0.8, RIGHT*2.5 + DOWN*0.8
        ]

        level1_nodes = VGroup()
        level1_arrows = VGroup()

        for i, pos in enumerate(level1_positions):
            arrow = Line(root.get_center(), pos, color=WHITE, stroke_width=2)
            arrow.add_tip(tip_length=0.15)

            node = Circle(radius=0.2, color=ORANGE, fill_opacity=0.4, stroke_width=2)
            node.move_to(pos)

            node_info = VGroup(
                Text("n/2", font_size=8, color=WHITE),
                Text("(n/2)²", font_size=6, color=YELLOW)
            )
            node_info.arrange(DOWN, buff=0.05)
            node_info.move_to(node.get_center())

            level1_arrows.add(arrow)
            level1_nodes.add(VGroup(node, node_info))

        level1_label = Text("Level 1: 8 problems, each (n/2)² work = 2n² total",
                           font_size=12, color=WHITE)
        level1_label.move_to(LEFT * 4.5 + DOWN * 0.5)

        self.play(Create(level1_arrows), run_time=1.5)
        self.play(Create(level1_nodes), Write(level1_label), run_time=1.5)

        level2_sample_positions = [LEFT*2.5 + DOWN*1.6, LEFT*0.8 + DOWN*1.6, RIGHT*0.8 + DOWN*1.6]
        level2_nodes = VGroup()
        level2_arrows = VGroup()

        for pos in level2_sample_positions:
            for j in range(3):  # Just show 3 for each to avoid clutter
                tiny_pos = pos + RIGHT*j*0.15 + DOWN*0.1
                arrow = Line(pos + UP*0.7, tiny_pos, color=WHITE, stroke_width=1)
                arrow.add_tip(tip_length=0.08)

                tiny_node = Circle(radius=0.08, color=YELLOW, fill_opacity=0.6)
                tiny_node.move_to(tiny_pos)

                level2_arrows.add(arrow)
                level2_nodes.add(tiny_node)

        dots = Text("...", font_size=20, color=WHITE)
        dots.move_to(RIGHT*2 + DOWN*1.6)

        level2_label = Text("Level 2: 64 problems, each (n/4)² work = 4n² total",
                           font_size=12, color=WHITE)
        level2_label.move_to(LEFT * 4.5 + DOWN * 1.6)

        self.play(Create(level2_arrows), Create(level2_nodes), Write(dots),
                 Write(level2_label), run_time=1.5)

        self.wait(1)

        analysis_title = Text("Work Per Level Analysis", font_size=18, color=GREEN)
        analysis_title.set_weight(BOLD)
        analysis_title.move_to(DOWN * 2.3)

        analysis_box = Rectangle(width=8, height=1.8, color=GREEN, stroke_width=2, fill_opacity=0.05)
        analysis_box.move_to(DOWN * 3.2)

        level_header = Text("Level", font_size=14, color=GREEN)
        level_header.set_weight(BOLD)
        level_header.move_to(LEFT*3.5 + DOWN*2.6)

        problems_header = Text("# Problems", font_size=14, color=GREEN)
        problems_header.set_weight(BOLD)
        problems_header.move_to(LEFT*1.5 + DOWN*2.6)

        work_per_header = Text("Work Each", font_size=14, color=GREEN)
        work_per_header.set_weight(BOLD)
        work_per_header.move_to(RIGHT*0.5 + DOWN*2.6)

        total_header = Text("Total Work", font_size=14, color=GREEN)
        total_header.set_weight(BOLD)
        total_header.move_to(RIGHT*2.8 + DOWN*2.6)

        level_data = VGroup(
            Text("0", font_size=12, color=WHITE).move_to(LEFT*3.5 + DOWN*3),
            Text("1", font_size=12, color=WHITE).move_to(LEFT*1.5 + DOWN*3),
            Text("n²", font_size=12, color=WHITE).move_to(RIGHT*0.5 + DOWN*3),
            MathTex(r"n^2", font_size=12, color=YELLOW).move_to(RIGHT*2.8 + DOWN*3)
        )

        level1_data = VGroup(
            Text("1", font_size=12, color=WHITE).move_to(LEFT*3.5 + DOWN*3.3),
            Text("8", font_size=12, color=WHITE).move_to(LEFT*1.5 + DOWN*3.3),
            MathTex(r"(\frac{n}{2})^2", font_size=10, color=WHITE).move_to(RIGHT*0.5 + DOWN*3.3),
            MathTex(r"8 \cdot \frac{n^2}{4} = 2n^2", font_size=10, color=YELLOW).move_to(RIGHT*2.8 + DOWN*3.3)
        )

        level2_data = VGroup(
            Text("2", font_size=12, color=WHITE).move_to(LEFT*3.5 + DOWN*3.6),
            Text("64", font_size=12, color=WHITE).move_to(LEFT*1.5 + DOWN*3.6),
            MathTex(r"(\frac{n}{4})^2", font_size=10, color=WHITE).move_to(RIGHT*0.5 + DOWN*3.6),
            MathTex(r"64 \cdot \frac{n^2}{16} = 4n^2", font_size=10, color=YELLOW).move_to(RIGHT*2.8 + DOWN*3.6)
        )

        pattern_row = Text("Pattern: Work doubles each level!", font_size=14, color=RED)
        pattern_row.set_weight(BOLD)
        pattern_row.move_to(DOWN*3.9)

        self.play(Write(analysis_title), Create(analysis_box), run_time=1)
        self.play(Write(VGroup(level_header, problems_header, work_per_header, total_header)), run_time=1)
        self.play(Write(level_data), run_time=1)
        self.play(Write(level1_data), run_time=1)
        self.play(Write(level2_data), run_time=1)
        self.play(Write(pattern_row), run_time=1.5)

        self.wait(2)

        self.play(FadeOut(Group(*self.mobjects)), run_time=1)

        final_title = Text("Final Complexity Calculation", font_size=24, color=RED)
        final_title.set_weight(BOLD)
        final_title.move_to(UP * 3)

        series_intro = Text("Total work across all levels:", font_size=16, color=WHITE)
        series_intro.move_to(UP * 2.2)

        geometric_series = MathTex(r"n^2 + 2n^2 + 4n^2 + 8n^2 + ... + ?",
                                  font_size=18, color=YELLOW)
        geometric_series.move_to(UP * 1.7)

        factored_form = MathTex(r"= n^2(1 + 2 + 4 + 8 + ... + 2^{\log_2 n - 1})",
                               font_size=16, color=WHITE)
        factored_form.move_to(UP * 1.2)

        geometric_formula = MathTex(r"= n^2 \cdot (2^{\log_2 n} - 1)",
                                   font_size=16, color=WHITE)
        geometric_formula.move_to(UP * 0.7)

        simplification = MathTex(r"= n^2 \cdot (n - 1)",
                                font_size=16, color=WHITE)
        simplification.move_to(UP * 0.2)

        final_result = MathTex(r"= O(n^3)", font_size=24, color=RED)
        final_result.set_weight(BOLD)
        final_result.move_to(DOWN * 0.5)

        insight_box = Rectangle(width=7, height=1.5, color=RED, stroke_width=3, fill_opacity=0.1)
        insight_box.move_to(DOWN * 1.8)

        insight_title = Text("Why Case 3?", font_size=16, color=RED)
        insight_title.set_weight(BOLD)
        insight_title.move_to(insight_box.get_top() + DOWN*0.3)

        case3_condition = MathTex(r"f(n) = \Theta(n^2) > \Theta(n^{\log_2 8}) = \Theta(n^3)",
                                 font_size=14, color=WHITE)
        case3_condition.move_to(insight_box.get_center() + UP*0.1)

        case3_conclusion = Text("Combining work dominates over recursive work!",
                               font_size=14, color=WHITE)
        case3_conclusion.move_to(insight_box.get_center() + DOWN*0.3)

        case3_condition_fixed = MathTex(r"f(n) = \Theta(n^2) \text{ but we get } O(n^3)",
                                       font_size=14, color=WHITE)
        case3_condition_fixed.move_to(insight_box.get_center() + UP*0.1)

        self.play(Write(final_title), run_time=1.5)
        self.play(Write(series_intro), run_time=1)
        self.play(Write(geometric_series), run_time=1.5)
        self.play(Write(factored_form), run_time=1.5)
        self.play(Write(geometric_formula), run_time=1.5)
        self.play(Write(simplification), run_time=1.5)
        self.play(Write(final_result), run_time=2)

        self.play(Create(insight_box), Write(insight_title), run_time=1)
        self.play(Write(case3_condition_fixed), Write(case3_conclusion), run_time=1.5)

        self.wait(4)
        self.play(FadeOut(Group(*self.mobjects)), run_time=1.5)

        credits_title = Text("Sources Used", font_size=42, color=BLUE, weight=BOLD)
        credits_title.to_edge(UP, buff=1)
        self.play(Write(credits_title))
        self.wait(1)

        # Create credit entries
        credit_entries = VGroup()

        # Claude AI Icon
        claude_icon = VGroup(
            RoundedRectangle(width=0.6, height=0.6, corner_radius=0.1,
                           fill_color=BLUE, fill_opacity=0.8, stroke_color=WHITE),
            Text("AI", font_size=16, color=WHITE, weight=BOLD)
        )
        claude_text = Text("Claude - Initial Code", font_size=24, color=WHITE)
        claude_entry = VGroup(claude_icon, claude_text)
        claude_entry.arrange(RIGHT, buff=0.5)

        # Pixabay Icon
        pixabay_icon = VGroup(
            Circle(radius=0.3, fill_color=GREEN, fill_opacity=0.8, stroke_color=WHITE),
            Text("P", font_size=20, color=WHITE, weight=BOLD)
        )
        pixabay_text = Text("Pixabay - Music", font_size=24, color=WHITE)
        pixabay_entry = VGroup(pixabay_icon, pixabay_text)
        pixabay_entry.arrange(RIGHT, buff=0.5)

        # Canva Icon
        canva_icon = VGroup(
            RoundedRectangle(width=0.6, height=0.6, corner_radius=0.3,
                           fill_color=PURPLE, fill_opacity=0.8, stroke_color=WHITE),
            Text("C", font_size=20, color=WHITE, weight=BOLD)
        )
        canva_text = Text("Canva - Video Editing", font_size=24, color=WHITE)
        canva_entry = VGroup(canva_icon, canva_text)
        canva_entry.arrange(RIGHT, buff=0.5)

        # Arrange all credits
        credit_entries.add(claude_entry, pixabay_entry, canva_entry)
        credit_entries.arrange(DOWN, buff=0.8, aligned_edge=LEFT)
        credit_entries.move_to(ORIGIN + DOWN * 0.5)

        # Animate each credit entry
        for entry in credit_entries:
            self.play(
                FadeIn(entry[0], shift=RIGHT*0.5),
                Write(entry[1], run_time=1.5)
            )
            self.wait(0.5)

        self.wait(2)
        self.play(FadeOut(Group(*self.mobjects)), run_time=1)

# %%manim -qh MastersTheoremVisualization
