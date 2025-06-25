from manim import *

class BFSVisualization(Scene):
    def create_circle_node(self, node_id, position):
        circle = Circle(radius=0.4, color=WHITE, fill_opacity=0.3, stroke_width=4)
        text = Text(str(node_id), font_size=32).scale(0.8)
        node = VGroup(circle, text).move_to(position)
        return node

    def create_edge(self, start, end):
        return Line(
            start.get_center(), 
            end.get_center(), 
            color=WHITE,
            stroke_width=8
        )

    def create_legend_item(self, text, color):
        dot = Dot(color=color, radius=0.15, stroke_width=2)
        text = Text(text, font_size=14, color=WHITE)
        return VGroup(dot, text).arrange(RIGHT, buff=0.3)

    def construct(self):
        # Define colors with increased opacity
        UNVISITED_COLOR = "#E6E6E6"
        CURRENT_COLOR = "#00FF00"
        QUEUE_COLOR = "#ADD8E6"
        PROCESSED_COLOR = "#00BFFF"
        PATH_COLOR = "#FF4500"
        
        title = Text("Breadth-First Search (BFS)", font_size=28).to_edge(UP, buff=0.1)
        subtitle = Text("Level by Level Graph Traversal", font_size=20).next_to(title, DOWN, buff=0.1)

        # Adjusted node positions - moved entire graph down by adjusting Y coordinates
        positions = {
            0: ORIGIN + UP * 2.5,              # Moved down from 3.0
            1: LEFT * 3.5 + UP * 1.2,          # Moved down from 2.0
            2: ORIGIN + UP * 1.2,              # Moved down from 2.0
            3: RIGHT * 3.5 + UP * 1.2,         # Moved down from 2.0
            4: LEFT * 4.5 + DOWN * 1.0,        # Moved down from -0.5
            5: LEFT * 2.2 + DOWN * 1.0,        # Moved down from -0.5
            6: RIGHT * 2.2 + DOWN * 1.0,       # Moved down from -0.5
            7: RIGHT * 4.5 + DOWN * 1.0,       # Moved down from -0.5
            8: LEFT * 5.0 + DOWN * 2.2,        # Moved down from -1.6
            9: LEFT * 3.8 + DOWN * 2.2,        # Moved down from -1.6
            10: LEFT * 1.8 + DOWN * 2.2,       # Moved down from -1.6
            11: RIGHT * 1.8 + DOWN * 2.2,      # Moved down from -1.6
            12: RIGHT * 3.8 + DOWN * 2.2,      # Moved down from -1.6
            13: RIGHT * 5.0 + DOWN * 2.2       # Moved down from -1.6
        }

        # Rest of the setup remains the same
        nodes = {i: self.create_circle_node(i, pos) for i, pos in positions.items()}
        edges = [
            (0, 1), (0, 2), (0, 3),
            (1, 4), (1, 5),
            (2, 5), (2, 6),
            (3, 6), (3, 7),
            (4, 8), (4, 9),
            (5, 9), (5, 10),
            (6, 11), (6, 12),
            (7, 12), (7, 13)
        ]
        edge_objects = {edge: self.create_edge(nodes[edge[0]], nodes[edge[1]]) for edge in edges}

        # Smaller legend
        legend_title = Text("Legend:", font_size=20, color="#FFA500")
        legend_items = VGroup(
            legend_title,
            self.create_legend_item("Unvisited", UNVISITED_COLOR),
            self.create_legend_item("Current Node", CURRENT_COLOR),
            self.create_legend_item("In Queue", QUEUE_COLOR),
            self.create_legend_item("Processed", PROCESSED_COLOR),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        legend_bg = SurroundingRectangle(legend_items, color="#2C3E50", fill_opacity=0.1, buff=0.3, corner_radius=0.3)
        legend_group = VGroup(legend_bg, legend_items).scale(0.8).to_corner(UL, buff=0.3)

        # Smaller explanation
        explanation = VGroup(
            Text("BFS Algorithm:", font_size=20, color="#FFA500"),
            Text("• Explores nodes level by level", font_size=15, color=WHITE),
            Text("• Uses queue for traversal order", font_size=15, color=WHITE),
            Text("• Finds shortest paths", font_size=15, color=WHITE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        explanation_bg = SurroundingRectangle(explanation, color="#2C3E50", fill_opacity=0.1, buff=0.3, corner_radius=0.3)
        explanation_group = VGroup(explanation_bg, explanation).scale(0.8).to_corner(UR, buff=0.3)

        # Display animations
        self.play(Write(title, run_time=1.5))
        self.play(Write(subtitle, run_time=1.5))
        self.play(Create(VGroup(*edge_objects.values()), lag_ratio=0.2), run_time=2)
        self.play(FadeIn(VGroup(*nodes.values()), lag_ratio=0.2), run_time=2)
        self.play(FadeIn(legend_bg), Write(legend_items), FadeIn(explanation_bg), Write(explanation), run_time=2)

        # BFS variables
        queue = [0]
        visited = set()
        current_level = 0
        node_levels = {
            0: 0,
            1: 1, 2: 1, 3: 1,
            4: 2, 5: 2, 6: 2, 7: 2,
            8: 3, 9: 3, 10: 3, 11: 3, 12: 3, 13: 3
        }

        # Moved level label up slightly to create more space
        level_label = Text("Current Level: 0", font_size=26, color=WHITE).to_edge(DOWN, buff=0.6)
        self.play(Write(level_label), run_time=1.5)

        # BFS traversal
        while queue:
            current = queue.pop(0)
            if current in visited:
                continue

            current_node = nodes[current]
            self.play(current_node[0].animate.set_fill(CURRENT_COLOR, opacity=0.8), run_time=1)

            for start, end in edges:
                if start == current and end not in visited and end not in queue:
                    queue.append(end)
                    self.play(
                        edge_objects[(start, end)].animate.set_color(PATH_COLOR).set_stroke(width=8),
                        run_time=1
                    )
                    neighbor_node = nodes[end]
                    self.play(neighbor_node[0].animate.set_fill(QUEUE_COLOR, opacity=0.7), run_time=0.5)

            self.play(current_node[0].animate.set_fill(PROCESSED_COLOR, opacity=0.7), run_time=0.5)
            visited.add(current)

            new_level = node_levels[current]
            if new_level != current_level:
                current_level = new_level
                new_label = Text(f"Current Level: {current_level}", font_size=20, color=WHITE).to_edge(DOWN, buff=0.8)
                self.play(Transform(level_label, new_label), run_time=1)
                self.wait(2)

        self.wait(2.5)