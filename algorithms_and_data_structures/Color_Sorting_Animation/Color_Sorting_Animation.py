from manim import *
import numpy as np

class ColorSortingPuzzle(Scene):
    def construct(self):
        # Set a background color
        self.background_color=(BLACK)
        # Title setup
        title = Text("Color Sort Algorithm", font_size=26, color=BLUE).to_edge(UP * 0.5)
        # Animate the title
        self.play(Write(title))  # Animate the title
        self.wait(1)  # Wait for 1 second to view the title
        
        # Show color then sort then algorithm
        self.play(title.animate.scale(1.3))
        self.wait(1)
        
        
        # Initial container states
        initial_state = [
            ["red", "green", "blue", "yellow"],  # Container 1
            ["blue", "yellow", "green", "red"],  # Container 2
            ["yellow", "blue", "yellow", "green"],  # Container 3
            ["red", "red", "blue", "green"],  # Container 4
            [],  # Container 5 (empty)
        ]

        # Container positions, excluding the last one
        container_positions = [
            LEFT * 5, LEFT * 3, LEFT, RIGHT, RIGHT * 3
        ]
        
        # Define colors
        color_map = {
            "red": RED,
            "green": GREEN,
            "blue": BLUE,
            "yellow": YELLOW,
        }

        # Create containers
        containers = self.create_containers(container_positions)

        # Create blocks
        blocks = self.create_blocks(initial_state, container_positions, color_map)

        # Define moves
        moves = [
            (1, 5), (3, 5), (4, 1), (4, 5), (2, 4),
            (1, 3), (2, 1), (2, 4), (5, 2), (1, 5), (1, 2),
            (1, 5), (4, 2), (1, 4), (5, 1), (5, 1), (5, 1),
            (3, 1), (3, 5), (2, 5), (3, 2), (3, 5),
        ]
        
        # Animate the solution
        for move in moves:
            self.animate_move(blocks, initial_state, move, container_positions)
            self.wait(0.5)

        # Show final message with number of moves
        self.show_final_message(len(moves))

        # Final state pause
        self.wait(2)

    def create_containers(self, positions):
        """Create the containers."""
        containers = []
        for pos in positions:
            container = Rectangle(height=4, width=1, color=LIGHT_GRAY).move_to(pos)
            self.play(FadeIn(container), run_time=0.3)
            self.wait(0.5)
            containers.append(container)
        return containers

    def create_blocks(self, state, positions, color_map):
        """Create the blocks."""
        blocks = []
        for i, container in enumerate(state):
            for level, color in enumerate(container):
                block = Square(side_length=0.8, fill_color=color_map[color], fill_opacity=1)
                block.move_to(positions[i] + UP * (1.5 - level))
                blocks.append(block)
                self.play(FadeIn(block), run_time=0.3)
                self.wait(0.5)
        return blocks

    def animate_move(self, blocks, state, move, positions):
        """Animate a block move from one container to another."""
        src, dest = move
        src_index = src - 1
        dest_index = dest - 1

        # Ensure there are blocks to move from the source container
        if not state[src_index]:
            raise ValueError(f"No blocks to move from container {src} to container {dest}")

        # Find the block to move
        source_top = len(state[src_index]) - 1
        block_to_move = self.get_block_at_position(blocks, positions[src_index], source_top)

        if block_to_move is None:
            raise ValueError(f"Cannot find block to move from container {src} to {dest}")

        # Calculate the destination position
        dest_top = len(state[dest_index])
        destination_position = positions[dest_index] + UP * (1.5 - dest_top)

        # Animate the move
        self.play(block_to_move.animate.move_to(destination_position))

        # Update the state
        color = state[src_index].pop()
        state[dest_index].append(color)

    def get_block_at_position(self, blocks, container_position, block_level):
        """Get the block at a specific level of a container."""
        target_position = container_position + UP * (1.5 - block_level)
        for block in blocks:
            if np.allclose(block.get_center(), target_position, atol=0.1):  # Allow small tolerance
                return block
        return None

    def show_final_message(self, moves_count):
        """Show the final message and animate the containers' flip and fade out."""
        
        # Fade out blocks
        for block in self.mobjects[5:]:  # The blocks
            self.play(
                block.animate.shift(UP * 3).set_opacity(0),
                run_time=0.2  # Speed up dissolve
            )
            self.wait(0.1)  # Short pause after each block fade-out

        # Display final message at the center with fade-in
        final_message = Text(f"Solved with {moves_count} Moves", font_size=24, color=BLUE).move_to(ORIGIN)
        self.play(FadeIn(final_message, run_time=0.5))  # Fade-in the final message slowly
        self.wait(0.8)  # Pause to view the final message
