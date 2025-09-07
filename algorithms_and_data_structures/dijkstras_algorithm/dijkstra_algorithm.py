from manim import *

class DijkstraStepByStep(Scene):
    def construct(self):
        self.camera.background_color = "#0a0a0a"
        self.introduction()
        self.setup_graph_dynamically()
        self.run_dijkstra_with_effects()
        self.highlight_shortest_path()
        self.stunning_applications()

    def introduction(self):
        title = Text("Dijkstra's Algorithm", font_size=48, color=WHITE)
        subtitle = Text("Finding the Shortest Path", font_size=24, color=WHITE)
        title.to_edge(UP)
        subtitle.next_to(title, DOWN)

        self.play(Write(title), run_time=1.5)
        self.play(Write(subtitle), run_time=1)
        self.wait(0.5)
        self.play(FadeOut(title), FadeOut(subtitle))

    def setup_graph_dynamically(self):
        self.positions = {
            'A': LEFT * 3 + UP * 1,
            'B': LEFT * 1 + UP * 2,
            'C': LEFT * 1 + DOWN * 2,
            'D': RIGHT * 1 + UP * 1,
            'E': RIGHT * 3 + DOWN * 1,
        }

        self.graph = {
            'A': {'B': 4, 'C': 2},
            'B': {'D': 3},
            'C': {'D': 5, 'E': 1},
            'D': {'E': 2}
        }

        self.nodes = {}
        self.edges = {}
        self.distances = {node: float('inf') for node in self.positions}
        self.distances['A'] = 0
        self.previous = {}

        self.display_text("Setting up graph...")
        self.wait(0.5)

        # Create nodes with proper initial distance labels
        for name, pos in self.positions.items():
            dot = Dot(pos, color=WHITE, radius=0.3)
            label = Text(name, font_size=24, color=WHITE).next_to(dot, DOWN)

            # Set initial distance display
            if name == 'A':
                distance_text = "0"
                distance_color = GREEN
            else:
                distance_text = "∞"
                distance_color = RED

            distance_label = Text(distance_text, font_size=20, color=distance_color).next_to(dot, UP)
            self.nodes[name] = VGroup(dot, label, distance_label)
            self.play(Create(dot), Write(label), Write(distance_label), run_time=0.3)

        self.display_text("Adding weighted edges...")
        self.wait(0.5)

        # Create edges with weights
        for u in self.graph:
            for v in self.graph[u]:
                line = Line(self.positions[u], self.positions[v], color=GRAY, stroke_width=3)
                weight = self.graph[u][v]
                weight_text = Text(str(weight), font_size=20, color=BLUE, weight=BOLD)
                mid_point = (self.positions[u] + self.positions[v]) / 2
                weight_text.move_to(mid_point + UP * 0.3)
                self.edges[(u, v)] = VGroup(line, weight_text)
                self.play(Create(line), Write(weight_text), run_time=0.3)

        self.wait(1)
        self.clear_text()

    def display_text(self, text):
        if hasattr(self, 'current_text'):
            self.play(FadeOut(self.current_text))

        self.current_text = Text(text, font_size=20, color=YELLOW)
        self.current_text.to_edge(DOWN, )
        self.play(Write(self.current_text), run_time=1)


    def clear_text(self):
        if hasattr(self, 'current_text'):
            self.play(FadeOut(self.current_text), run_time=0.3)

    def run_dijkstra_with_effects(self):
        self.display_text("Running Dijkstra's Algorithm...")
        self.wait(1)

        unvisited = set(self.positions.keys())
        step = 1

        while unvisited:
            # Find the unvisited node with minimum distance
            current = min(unvisited, key=lambda node: self.distances[node])
            if self.distances[current] == float('inf'):
                break

            # Highlight current node being processed
            self.play(self.nodes[current][0].animate.set_color(BLUE).scale(1.2), run_time=0.5)
            self.display_text(f"Processing node {current} (distance: {self.distances[current]})")
            self.wait(0.8)

            # Check all neighbors of current node
            for neighbor in self.graph.get(current, {}):
                if neighbor in unvisited:
                    edge_line, edge_weight = self.edges[(current, neighbor)]
                    weight = self.graph[current][neighbor]
                    new_distance = self.distances[current] + weight

                    # Highlight the edge being examined
                    self.play(edge_line.animate.set_color(GREEN).set_stroke_width(5), run_time=0.3)
                    self.display_text(f"Checking {neighbor}: {self.distances[current]} + {weight} = {new_distance}")
                    self.wait(0.8)

                    # Update distance if we found a shorter path
                    if new_distance < self.distances[neighbor]:
                        old_distance = "∞" if self.distances[neighbor] == float('inf') else str(self.distances[neighbor])
                        self.distances[neighbor] = new_distance
                        self.previous[neighbor] = current

                        # Update the distance label
                        new_distance_label = Text(str(new_distance), font_size=20, color=GREEN).next_to(self.nodes[neighbor][0], UP)
                        self.play(Transform(self.nodes[neighbor][2], new_distance_label), run_time=0.5)
                        self.display_text(f"Updated {neighbor}: {old_distance} → {new_distance}")
                        self.wait(0.8)

                    # Reset edge color
                    self.play(edge_line.animate.set_color(GRAY).set_stroke_width(3), run_time=0.2)

            # Mark current node as visited
            unvisited.remove(current)
            self.play(
                self.nodes[current][0].animate.set_color(ORANGE).set_fill(ORANGE, opacity=0.3).scale(1/1.2),
                run_time=0.5
            )
            step += 1

        self.display_text("Algorithm complete!")
        self.wait(1)
        self.clear_text()

    def highlight_shortest_path(self):
        # Reconstruct the shortest path
        path = []
        node = 'E'
        while node in self.previous:
            path.append(node)
            node = self.previous[node]
        path.append('A')
        path = list(reversed(path))

        # Display path information
        path_text = Text("Shortest Path: " + " → ".join(path), font_size=26, color=GOLD, weight=BOLD)
        path_text.to_edge(UP, buff=0.5)
        self.play(Write(path_text), run_time=1.5)



        # Highlight the path edges and nodes
        for i in range(len(path) - 1):
            edge_line = self.edges[(path[i], path[i+1])][0]
            self.play(edge_line.animate.set_color(GOLD).set_stroke_width(8), run_time=0.5)
            self.play(self.nodes[path[i]][0].animate.set_color(GOLD), run_time=0.3)

        # Highlight the final node
        self.play(self.nodes[path[-1]][0].animate.set_color(GOLD), run_time=0.3)

        self.wait(2)

        # Fade out everything for the next scene
        self.play(*[FadeOut(obj) for obj in self.mobjects], run_time=1.5)

    def stunning_applications(self):
        # Clear screen and start fresh
        self.wait(0.5)

        apps_title = Text("Real World Applications", font_size=36, color=GREEN)
        apps_title.to_edge(UP)
        self.play(Write(apps_title), run_time=2)
        self.wait(1)

        applications = [
            ("GPS Navigation", "Shortest routes in maps"),
            ("Network Routing", "Optimal data packet paths"),
            ("Robotics", "Pathfinding for autonomous systems")
        ]

        for i, (title, description) in enumerate(applications):
            y_pos = 1.5 - i * 1.8

            # Application title
            app_title = Text(title, font_size=24, color=BLUE, weight=BOLD)
            app_title.shift(UP * y_pos)

            # Application description
            app_desc = Text(description, font_size=18, color=WHITE)
            app_desc.next_to(app_title, DOWN, buff=0.2)

            self.play(Write(app_title), run_time=0.8)
            self.play(Write(app_desc), run_time=0.8)

        self.wait(2)
        self.play(FadeOut(Group(*self.mobjects)), run_time=1)


                # Credits section
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
