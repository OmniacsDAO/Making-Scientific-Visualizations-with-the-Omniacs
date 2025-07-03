from manim import *

class PathFinder(MovingCameraScene):
    def construct(self):
        title = Text("Path Finding with the Nearest Neighbor Algorithm", font_size=26, color=BLUE).to_edge(UP*0.5)
        self.play(FadeIn(title))
        
        def closest_neighbor(given_point, points):
            points_array = np.array(points)
            distances = np.linalg.norm(points_array - given_point, axis=1)
            closest_index = np.argmin(distances)
            return closest_index

        npl = NumberPlane(
            x_range=[-30,30,1],
            y_range=[-30,30,1],
            background_line_style={
                "stroke_color": WHITE,
                "stroke_width": 1,
                "stroke_opacity": 0.2,
            },
        )
        npl.axes.set_opacity(0)  # Hide axes
        self.add(npl)

        pts = [(np.random.uniform(-6,6), np.random.uniform(-3,3), 0) for _ in range(50)]
        pt2 = np.array(pts)
        start = None
        maxsum = 0
        isodist = 0
        for pt in pts[0:100]:
            dists = np.sort(np.linalg.norm(pt2 - pt, axis=1))
            sum = np.sum(dists[0:3])
            if sum > maxsum:
                maxsum = sum
                isodist = dists[1]
                start = pt
        print(start)
        sorted_pts = [start]
        pts.remove(start)
        while len(pts) > 0:
            idx = closest_neighbor(sorted_pts[-1], pts)
            sorted_pts.append(pts[idx])
            pts.remove(pts[idx])

        # Visualize the path with circles
        circs = VGroup(
            *[Circle(radius=isodist, stroke_width=0, color=BLUE, fill_opacity=0.25)
            .set_z_index(-2).move_to(pt) for pt in sorted_pts]
        )

        path = VMobject()
        path.set_points_smoothly(sorted_pts).set_stroke(width=.05)
        
        start_label = Text("Start", font_size=24, color=YELLOW).move_to(start)
        self.play(FadeIn(start_label))
        self.wait(0.2)

        for pt in sorted_pts:
            dot = Dot(point=pt, radius=.05, color=RED)
            self.add(dot)

        self.wait()


        self.play(
            *[GrowFromPoint(circ, circ.get_center()) for circ in circs],
            run_time=4,
            rate_func=rate_functions.linear,
        )
        self.wait()
        self.play(circs[0].animate.set_fill(color=YELLOW))
        self.wait(2)

        #fade out the title
        
        self.play(FadeOut(title))
        
        d = Dot(radius=0.10, color=YELLOW, fill_opacity=1, stroke_width=0).move_to(path.get_start())

        self.play(
            self.camera.frame.animate.scale(0.25).move_to(path.get_start()),
            *[FadeOut(circ) for circ in circs],
            run_time=3
        )

        trace = TracedPath(d.get_center, stroke_width=2.5, stroke_color=YELLOW)
        self.add(d, trace)

        for pt in sorted_pts[1:]:
            startprop = path.proportion_from_point(d.get_center())
            endprop = path.proportion_from_point(pt)
            radius = np.linalg.norm(d.get_center()-pt)
            circ = Circle(radius=radius, color=YELLOW, fill_opacity=0.4, stroke_width=0).move_to(d.get_center())
            self.play(
                self.camera.frame.animate.scale_to_fit_height(2*radius)
            )
            self.play(
                GrowFromPoint(circ, d.get_center()),
            )
            self.play(
                MoveAlongPath(d, path, rate_func=lambda t: startprop + t * (endprop - startprop)),
                MoveAlongPath(self.camera.frame, path, rate_func=lambda t: startprop + t * (endprop - startprop)),
                FadeOut(circ)
            )
        self.wait()
        
        endpoint_label = Text("End", font_size=24, color=YELLOW).move_to(path.get_end())
        self.add(endpoint_label)

        self.play(self.camera.frame.animate.scale_to_fit_height(8).move_to(ORIGIN), run_time=3)
        self.wait()
        
        # Dissolve all elements
        self.play(FadeOut(Group(*self.mobjects)))

        # Final concluding text
        final_text = Text(
            "The nearest neighbor algorithm is a method for finding the closest point in a set by calculating the distance between any given point and its nearest neighbors in space.",
            font_size=18, color=WHITE
        ).move_to(ORIGIN)

        self.play(FadeIn(final_text, run_time=3))
        self.wait(4)
