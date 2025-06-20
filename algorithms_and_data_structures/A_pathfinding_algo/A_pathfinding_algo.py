from manim import *
import numpy as np
import heapq

class PathfindingVisualization(Scene):
    def construct(self):
        # Grid Configuration
        self.grid_size = 10
        self.cell_size = 0.6
        
        # Color Palette
        self.COLORS = {
            'grid': GRAY,
            'start': GREEN,
            'goal': RED,
            'wall': DARK_GRAY,
            'explored': BLUE,
            'frontier': YELLOW,
            'path': PURPLE
        }
        
        # Set background color to dark gray
        self.camera.background_color = BLACK

        # Title
        self.create_title()
        self.wait(1)

        # Add legend, formula, and explanation sequentially
        self.add_legend()
        self.wait(1)
      
        # Create and display grid
        self.create_grid()
        self.wait(1)

        self.show_astar_formula()
        self.wait(1)

        self.add_explanation()
        self.wait(1)

        # Run A* algorithm visualization
        self.run_astar_algorithm()

    def create_title(self):
        """Create visualization title"""
        title = Text("A* Pathfinding Algorithm", font_size=26, color=BLUE)
        title.to_edge(UP, buff=0.2)
        self.play(FadeIn(title))
        self.wait(1)
        self.add(title)

    def create_grid(self):
        """Create grid with obstacles and start/goal points"""
        self.grid = VGroup()
        self.grid_cells = {}
        
        # Create grid
        for row in range(self.grid_size):
            for col in range(self.grid_size):
                cell = Square(
                    side_length=self.cell_size, 
                    color=self.COLORS['grid'], 
                    fill_opacity=0.2
                )
                cell.move_to(
                    RIGHT * col * self.cell_size + 
                    DOWN * row * self.cell_size
                )
                
                cell_data = {
                    'pos': (row, col),
                    'is_wall': False,
                    'cell': cell
                }
                
                self.grid.add(cell)
                self.grid_cells[(row, col)] = cell_data
        
        self.grid.center()
        self.play(FadeIn(self.grid, run_time=1))
        
        # Add start and goal
        self.start = (0, 0)
        self.goal = (self.grid_size - 1, self.grid_size - 1)
        self.mark_special_cells()
        self.add_obstacles()

    def mark_special_cells(self):
        """Mark start and goal cells"""
        start_cell = self.grid_cells[self.start]['cell']
        goal_cell = self.grid_cells[self.goal]['cell']
        
        self.play(
            start_cell.animate.set_fill(self.COLORS['start'], opacity=0.8),
            goal_cell.animate.set_fill(self.COLORS['goal'], opacity=0.8)
        )

    def add_obstacles(self):
        """Add hardcoded obstacles and walls on the top and right edges."""
        # Existing hardcoded obstacles
        obstacles = [
            (2, 2), (2, 3), (2, 4),
            (5, 5), (5, 6), (5, 7), (5, 8), (5, 9),
            (7, 0), (7, 1), (7, 5),
            (3, 7), (4, 7), (5, 7), (4, 1), (4, 2)
        ]
        
        # Add hardcoded obstacles
        for obs in obstacles:
            cell = self.grid_cells[obs]['cell']
            cell_data = self.grid_cells[obs]
            cell_data['is_wall'] = True
            
            self.play(
                cell.animate.set_fill(self.COLORS['wall'], opacity=0.8)
            )

    def get_neighbors(self, current):
        """Get valid neighboring cells"""
        neighbors = [
            (current[0]+1, current[1]),
            (current[0]-1, current[1]),
            (current[0], current[1]+1),
            (current[0], current[1]-1)
        ]
        
        valid_neighbors = [
            n for n in neighbors 
            if (n in self.grid_cells and 
                not self.grid_cells[n]['is_wall'])
        ]
        
        return valid_neighbors

    def heuristic(self, goal, next_cell):
        """Calculate Manhattan distance heuristic"""
        return abs(goal[0] - next_cell[0]) + abs(goal[1] - next_cell[1])

    def run_astar_algorithm(self):
        """Implement A* pathfinding algorithm visualization"""
        start = self.start
        goal = self.goal
        
        frontier = []
        heapq.heappush(frontier, (0, start))
        
        came_from = {}
        cost_so_far = {start: 0}
        
        explored_cells = set()
        frontier_cells = set([start])
        
        while frontier:
            current_cost, current = heapq.heappop(frontier)
            
            if current != start and current != goal:
                cell = self.grid_cells[current]['cell']
                self.play(
                    cell.animate.set_fill(self.COLORS['explored'], opacity=0.6),
                    run_time=0.2
                )
            
            if current == goal:
                break
            
            explored_cells.add(current)
            frontier_cells.remove(current)
            
            for next_cell in self.get_neighbors(current):
                new_cost = cost_so_far[current] + 1
                if (next_cell not in cost_so_far or 
                    new_cost < cost_so_far[next_cell]):
                    
                    cost_so_far[next_cell] = new_cost
                    priority = new_cost + self.heuristic(goal, next_cell)
                    heapq.heappush(frontier, (priority, next_cell))
                    
                    came_from[next_cell] = current
                    if next_cell not in explored_cells and next_cell != goal:
                        cell = self.grid_cells[next_cell]['cell']
                        if next_cell not in frontier_cells:
                            self.play(
                                cell.animate.set_fill(self.COLORS['frontier'], opacity=0.4),
                                run_time=0.2
                            )
                            frontier_cells.add(next_cell)
        
        self.visualize_path(came_from)

    def visualize_path(self, came_from):
        """Reconstruct and animate optimal path"""
        current = self.goal
        path = []
        
        while current != self.start:
            path.append(current)
            current = came_from[current]
        path.append(self.start)
        path.reverse()
        
        for cell in path:
            if cell != self.start and cell != self.goal:
                cell_obj = self.grid_cells[cell]['cell']
                self.play(
                    cell_obj.animate.set_fill(self.COLORS['path'], opacity=0.8),
                    run_time=0.3
                )

    def add_legend(self):
        """Add a legend explaining colors"""
        legend = VGroup(
            Text("Legend:", color=WHITE, font_size=16),
            Text("Start - Green", color=self.COLORS['start'], font_size=14),
            Text("Goal - Red", color=self.COLORS['goal'], font_size=14),
            Text("Wall - Gray", color=self.COLORS['wall'], font_size=14),
            Text("Explored - Blue", color=self.COLORS['explored'], font_size=14),
            Text("Frontier - Yellow", color=self.COLORS['frontier'], font_size=14),
            Text("Path - Purple", color=self.COLORS['path'], font_size=14)
        )
        legend.arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        legend.to_corner(UL, buff=0.5)
        self.add(legend)

    def show_astar_formula(self):
        """Display the A* formula on the screen"""
        formula = MathTex(r"f(n) = g(n) + h(n)", color=WHITE, font_size=28)
        formula.to_corner(UR, buff=0.5)
        self.add(formula)

    def add_explanation(self):
        """Add text explanation to the scene"""
        explanation = Text(
            "Exploration (Blue) → Frontier (Yellow → Path (Purple)\n" +
            "Heuristic: Estimates distance to Goal\n" +
            "Priority = Cost + Heuristic", font_size=10, color=WHITE
        )
        explanation.to_edge(DOWN, buff=0.3)
        self.play(FadeIn(explanation, run_time=0.5))
