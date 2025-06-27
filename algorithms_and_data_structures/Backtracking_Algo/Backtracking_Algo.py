from manim import *

class PegGame(Scene):
    # Adjusted positions - moved down by adding 1 to all y-coordinates and scaled x-coordinates
    positions = [
        (0, 2, 0),    # Peg 1
        (-1.5, 1, 0), (1.5, 1, 0),  # Pegs 2, 3
        (-3, 0, 0), (0, 0, 0), (3, 0, 0),  # Pegs 4, 5, 6
        (-4.5, -1, 0), (-1.5, -1, 0), (1.5, -1, 0), (4.5, -1, 0),  # Pegs 7-10
        (-6, -2, 0), (-3, -2, 0), (0, -2, 0), (3, -2, 0), (6, -2, 0),  # Pegs 11-15
    ]

    def draw_board(self, board, highlight_reversed=False):
        """Draws the current state of the peg board."""
        # Create a group for the game elements
        game_elements = VGroup()
        for idx, pos in enumerate(self.positions, start=1):
            if idx in board:
                # Highlight reversed pegs
                if highlight_reversed and idx in self.reversed_pegs:
                    peg = Circle(radius=0.4, color=RED, fill_opacity=0.2).move_to(pos)
                else:
                    peg = Circle(radius=0.4, color=BLUE).move_to(pos)
                game_elements.add(peg)
                # Adjusted text size for better visibility
                game_elements.add(Text(str(idx), font_size=24).move_to(pos))
            else:
                peg = Circle(radius=0.4, color=GRAY, fill_opacity=0.2).move_to(pos)
                game_elements.add(peg)

        self.play(Create(game_elements),run_time=2.5)
        
        return game_elements

    def play_move(self, peg, over, land, board, is_reversed=False):
        """Animates a move from `peg` to `land`, removing `over`."""
        # Remove `peg` and `over`, add `land`
        board.remove(peg)
        board.remove(over)
        board.append(land)

        # Animate peg jump with larger dot
        peg_start = self.positions[peg - 1]
        peg_end = self.positions[land - 1]
        self.play(
            MoveAlongPath(Dot(radius=0.2, color=BLUE).move_to(peg_start), Line(peg_start, peg_end))
        )

        # Animate removal of the "over" peg
        over_pos = self.positions[over - 1]
        self.play(FadeOut(Dot(radius=0.2, color=BLUE).move_to(over_pos)))

        # Clear only the game elements, not the title
        for mob in self.mobjects[:]:
            if not isinstance(mob, Text) or mob.get_center()[1] < 3:  # Preserve objects near the top
                self.remove(mob)
        
        # Redraw board
        self.draw_board(board, highlight_reversed=is_reversed)

    def construct(self):
        # Title and subtitle with more space
        title = Text("Backtracking Algorithm for Solving the Triangle Solitaire Puzzle", font_size=22, color=BLUE).to_edge(UP*0.5)
        subtitle = Text("Backtracking Moves", font_size=20, color=DARK_GREY).next_to(title, DOWN, buff=0.1)
        
        
        # Add stroke to subtitle for better visibility
        subtitle.set_stroke(color=WHITE, width=1, opacity=0.4)

        # Apply blue edge-up effect on title
        title.set_stroke(color=BLUE, width=1)
        self.play(Create(title))
        
        run_time=4
        
        # Initial board setup
        board = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
        empty_peg = 1
        board.remove(empty_peg)

        # Draw initial board
        self.draw_board(board)
        self.wait(1)
        
        # Solution moves up to (14, 13, 12)
        solution_moves = [(4, 2, 1), (6, 5, 4), (1, 3, 6),
                 (7, 4, 2), (12, 8, 5), (14, 13, 12),
                 (6, 9, 13),(2, 5, 9), (12, 13, 14), 
                 (15, 10, 6)
                 ]

        # Perform correct moves up to (14, 13, 12)
        for peg, over, land in solution_moves:
            self.play_move(peg, over, land, board)
            self.wait(1)
        
        # Introduce wrong moves
        wrong_moves = [(6, 9, 13), (13,14,15)]
        
        for peg, over, land in wrong_moves:
            self.play_move(peg, over, land, board)
            self.wait(1)

        # Add subtitle when backtracking starts
        self.play(Create(subtitle))
        self.wait(0.5)

        # Backtrack: Undo the wrong moves and highlight the reversed moves
        self.reversed_pegs = []
        for peg, over, land in reversed(wrong_moves):
            # Revert the last move by re-adding the "over" peg and moving "land" back to "peg"
            board.remove(land)
            board.append(over)
            board.append(peg)
            self.reversed_pegs = [peg, over]  # Track which pegs are being reversed
            
            # Clear only game elements, not the title/subtitle
            for mob in self.mobjects[:]:
                if not isinstance(mob, Text) or mob.get_center()[1] < 3:
                    self.remove(mob)
                    
            self.draw_board(board, highlight_reversed=True)
            self.wait(1)

        # Continue with correct moves after backtracking
        correct_moves_after_backtrack = [(6, 9, 13), (14, 13, 12), (11, 12, 13)]
        
        for peg, over, land in correct_moves_after_backtrack:
            self.play_move(peg, over, land, board)
            self.wait(1)
            
        # final fadeout
        final_group = Group(*self.mobjects)
        self.wait(2)
        self.play(FadeOut(final_group, run_time=4))  # Quick fadeout in 0.5 seconds