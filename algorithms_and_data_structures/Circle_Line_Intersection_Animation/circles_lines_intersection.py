from manim import *

def circle_line_intersection(circle: Circle, line: Line):
    # source https://mathworld.wolfram.com/Circle-LineIntersection.html
    cline = line.copy().shift(-circle.get_arc_center())
    x0,y0 = circle.get_arc_center()[0:2]
    x1,y1 = cline.get_start()[0:2]
    x2,y2 = cline.get_end()[0:2]
    r = circle.width/2

    dx = x2-x1
    dy = y2-y1
    dr = np.sqrt(dx**2+dy**2)
    D = x1*y2 - x2*y1
    Delta = r**2*dr**2-D**2
    if Delta < 0:
        return []
    sx1 = (D*dy+np.sign(dy)*dx*np.sqrt(Delta))/(dr**2)+x0
    sx2 = (D*dy-np.sign(dy)*dx*np.sqrt(Delta))/(dr**2)+x0
    sy1 = (-D*dx+np.abs(dy)*np.sqrt(Delta))/(dr**2)+y0
    sy2 = (-D*dx-np.abs(dy)*np.sqrt(Delta))/(dr**2)+y0
    if Delta==0:
        return [np.array([sx1,sy1,0])]
    else:
        return [
            np.array([sx1,sy1,0]),
            np.array([sx2,sy2,0])
        ]

def circle_circle_intersection(circle1: Circle, circle2: Circle):
    # source https://www.johndcook.com/blog/2023/08/27/intersect-circles/
    c0 = circle1.get_center()
    c1 = circle2.get_center()
    r0 = circle1.width/2
    r1 = circle2.width/2
    v = c1 - c0
    d = np.linalg.norm(v)

    if d > r0 + r1 or d == 0:
        return []

    u = v/np.linalg.norm(v)
    xvec = c0 + (d**2 - r1**2 + r0**2)*u/(2*d)

    uperp = np.array([u[1], -u[0], 0])
    a = ((-d+r1-r0)*(-d-r1+r0)*(-d+r1+r0)*(d+r1+r0))**0.5/d
    return [xvec + a*uperp/2, xvec - a*uperp/2]

def line_line_intersection(line1: Line, line2: Line):
    return line_intersection([line1.get_start(),line1.get_end()],[line2.get_start(),line2.get_end()])

class IntersectionTest(Scene):
    def construct(self):
        # Title for the animation with adjusted font size and positioning
        title = Text("Circle-Line Intersections Animation", color=BLUE, font_size=24)
        title.to_edge(UP * 0.5)  # Position the title slightly lower from the top edge
        self.play(Write(title))  
        self.wait()
        
        number_plane = NumberPlane().add_coordinates().set_opacity(0.2)  # Adjust opacity here
        self.add(number_plane)
        self.wait()

        circ1 = Circle(radius=3, color=RED).shift(2*LEFT)
        circ2 = Circle(radius=2, color=YELLOW).shift(DOWN)
        self.play(Create(circ1), run_time=3)
        self.play(Create(circ2), run_time=3)
        
        # Line1 - Secant Line
        line1 = Line([-5,-2,0],[6,1,0],color=BLUE)
        self.play(Create(line1),run_time=3)
        
        # Line2
        line2 = Line([-1,4,0],[5,-2,0],color=MAROON)
        self.play(Create(line2),run_time=3)
        
        # Circle-Circle Intersection
        Cs = circle_circle_intersection(circle1=circ1, circle2=circ2)
        Cdots = VGroup(
            *[
                VGroup(Dot(point=p, color=ORANGE), MathTex(f"C_{{ {i+1} }}", color=ORANGE).next_to(p,UR,buff=0.05))
                for i,p in enumerate(Cs)
            ]
        )
        self.play(GrowFromCenter(Cdots))

        # Circle-Line Intersection (for first circle)
        Ds = circle_line_intersection(circle=circ1, line=line1)
        Ddots = VGroup(
            *[
                VGroup(Dot(point=p, color=GREEN), MathTex(f"D_{{ {i+1} }}", color=GREEN).next_to(p,DOWN,buff=0.1))
                for i,p in enumerate(Ds)
            ]
        )
        self.play(GrowFromCenter(Ddots))

        # Circle-Line Intersection (for second circle)
        Es = circle_line_intersection(circle=circ2, line=line1)
        Edots = VGroup(
            *[
                VGroup(Dot(point=p, color=TEAL), MathTex(f"E_{{ {i+1} }}", color=TEAL).next_to(p,DOWN,buff=0.1))
                for i,p in enumerate(Es)
            ]
        )
        self.play(GrowFromCenter(Edots))

        # Line-Line Intersection
        F = line_line_intersection(line1=line1, line2=line2)
        Fdot = VGroup(Dot(point=F, color=WHITE), MathTex(r"F", color=WHITE).next_to(F,UP,buff=0.1))
        self.play(GrowFromCenter(Fdot))

        # Add the general text for intersections in the upper-right corner
        text1 = Text("Circle-Circle Intersection; C1, C2", color=WHITE, font_size=14).shift(UP * 3 + RIGHT * 5)
        text2 = Text("Circle-Line Intersection; D1, D2, E1, E2", color=WHITE, font_size=14).next_to(text1, DOWN, buff=0.1)
        text3 = Text("Line-Line Intersection; F", color=WHITE, font_size=14).next_to(text2, DOWN, buff=0.1)

        # Animate the text appearing
        self.play(Write(text1))
        self.play(Write(text2))
        self.play(Write(text3))
        
        self.wait()
        # Dissolve (fade out) all the content at the end
        self.play(
            FadeOut(title, number_plane, circ1, circ2, line1, line2, Cdots, Ddots, Edots, Fdot, text1, text2, text3),
            run_time=4 # Fade out duration
        )
