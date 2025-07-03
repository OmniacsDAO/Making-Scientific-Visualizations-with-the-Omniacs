from manim import *
from manim_rubikscube import *

class CombinedRubiksCubeAnimations(ThreeDScene):
    def construct(self):
        # Create the static title
        title = Text("CFOP Method To Solve Rubik's Cube", font_size=30, color=BLUE).to_edge(UP)
        self.play(Write(title))
        
        # Add the title to the scene
        self.add_fixed_in_frame_mobjects(title)

        # Part 1: 
        title_part1 = Text("CFOP Method To Solve Rubik's Cube", font_size=28, color=BLUE).to_edge(UP, buff=0.2)
        self.play(Transform(title, title_part1))

        cube1 = RubiksCube(colors=[WHITE, ORANGE, DARK_BLUE, YELLOW, PINK, "#00FF00"]).scale(0.6)
        self.move_camera(phi=50 * DEGREES, theta=160 * DEGREES)
        self.renderer.camera.frame_center = cube1.get_center()

        state = "BBFBUBUDFDDUURDDURLLLDFRBFRLLFFDLUFBDUBBLFFUDLRRRBLURR"
        cube1.set_state(state)
        self.wait(0.5)

        self.play(FadeIn(cube1))
        self.wait(0.3)

        for m in cube1.solve_by_kociemba(state):
            self.play(CubeMove(cube1, m), run_time=1.5)
            self.wait(0.3)

        # Rotate the cube 360 degrees
        self.play(Rotating(cube1, radians=2 * PI, run_time=2))
        self.begin_ambient_camera_rotation(rate=0.5)
        self.wait(4)
        self.stop_ambient_camera_rotation()
        
        # Transition to next animation
        self.play(FadeOut(cube1))
        self.wait(0.4)

        # Part 2: ThreeOffset
        title_part2 = Text("Three Offset", font_size=28, color=BLUE).to_edge(UP, buff=0.2)
        self.play(Transform(title, title_part2))

        cube2 = RubiksCube(x_offset=3, y_offset=3, z_offset=3, 
                          colors=[WHITE, ORANGE, DARK_BLUE, YELLOW, PINK, "#00FF00"]).scale(0.5)
        self.move_camera(phi=50 * DEGREES, theta=160 * DEGREES)
        self.renderer.camera.frame_center = cube2.get_center()

        self.play(FadeIn(cube2))
        self.begin_ambient_camera_rotation(rate=0.5)
        self.wait(3)
        self.stop_ambient_camera_rotation()
        self.play(FadeOut(cube2))
        self.wait(0.4)

        # Part 3: Y_Offset 4
        title_part3 = Text("Y-Offset 4", font_size=28, color=BLUE).to_edge(UP, buff=0.2)
        self.play(Transform(title, title_part3))

        cube3 = RubiksCube(y_offset=4, 
                          colors=[WHITE, ORANGE, DARK_BLUE, YELLOW, PINK, "#00FF00"]).scale(0.6)
        self.move_camera(phi=50 * DEGREES, theta=160 * DEGREES)
        self.renderer.camera.frame_center = cube3.get_center()

        self.play(FadeIn(cube3))
        self.begin_ambient_camera_rotation(rate=0.5)
        self.wait(3)
        self.stop_ambient_camera_rotation()
        self.play(FadeOut(cube3))
        self.wait(0.4)

        # Part 4: Indicate Face
        title_part4 = Text("Indicate Front Face ", font_size=28, color=BLUE).to_edge(UP, buff=0.2)
        self.play(Transform(title, title_part4))

        cube4 = RubiksCube(colors=[WHITE, ORANGE, DARK_BLUE, YELLOW, PINK, "#00FF00"]).scale(0.6)
        self.move_camera(phi=50 * DEGREES, theta=160 * DEGREES)
        self.renderer.camera.frame_center = cube4.get_center()

        self.play(FadeIn(cube4))
        self.wait()

        self.play(Indicate(VGroup(*cube4.get_face("F"))))
        self.wait()
        
        # Final fade out
        self.play(FadeOut(cube4))
        self.wait(0.4)
        self.play(FadeOut(title))
        self.wait(0.3)
