from manim import *
import numpy as np            
import random


class MeshTopologyAnimation(ThreeDScene):
    def create_pyramid(self):
        # Simplified pyramid with fewer vertices
        height = 1
        base_size = 0.8
        
        # Base vertices
        v1 = np.array([-base_size/2, -base_size/2, 0])
        v2 = np.array([base_size/2, -base_size/2, 0])
        v3 = np.array([base_size/2, base_size/2, 0])
        v4 = np.array([-base_size/2, base_size/2, 0])
        apex = np.array([0, 0, height])
        
        # Create faces more efficiently and set them to green
        faces = VGroup(
            Triangle().set_points_as_corners([apex, v1, v2]).set_color(GREEN),
            Triangle().set_points_as_corners([apex, v2, v3]).set_color(GREEN),
            Triangle().set_points_as_corners([apex, v3, v4]).set_color(GREEN),
            Triangle().set_points_as_corners([apex, v4, v1]).set_color(GREEN),
            Polygon(v1, v2, v3, v4).set_color(GREEN)
        )
        return faces

    def construct(self):
        # Configuration
        self.set_camera_orientation(phi=75*DEGREES, theta=-45*DEGREES)
        
        # Create title and legend
        title = Text("Mesh Topology Animation", font_size=24,color=BLUE).to_edge(UP*0.5)
        self.add_fixed_in_frame_mobjects(title)
        
        # Batch creation of PCs and their labels
        radius = 4
        pcs = VGroup()
        pc_labels = VGroup()
        
        for i in range(10):
            angle = i * (2*PI/10)
            x = radius * np.cos(angle)
            y = radius * np.sin(angle)
            z = np.sin(angle) * 0.5
            
            pc = Cube(side_length=0.4).set_color(BLUE)
            pc.move_to([x, y, z])
            pcs.add(pc)
            
            label = Text(f"PC{i+1}", font_size=16)
            label.next_to(pc, DOWN)
            label.rotate(angle, axis=OUT)
            pc_labels.add(label)
        
        # Batch creation of routers and their labels
        routers = VGroup()
        router_labels = VGroup()
        
        for i in range(2):
            angle = i * (2*PI/2)
            x = (radius*0.5) * np.cos(angle)
            y = (radius*0.5) * np.sin(angle)
            z = 1
            
            router = Sphere(radius=0.2).set_color(RED)
            router.move_to([x, y, z])
            routers.add(router)
            
            label = Text(f"R{i+1}", font_size=18)
            label.next_to(router, UP)
            router_labels.add(label)
        
        # Server creation
        server = self.create_pyramid()
        server.set_color(GREEN)
        server.move_to([0, 0, 2])
        server_label = Text("Main Server", font_size=20).next_to(server, UP)
        
        # Optimized connection creation
        def create_connections(start_objects, end_objects, bandwidth_type='high'):
            connections = VGroup()
            colors = {'high': '#FFA500', 'medium': '#FFFF00', 'low': '#ADD8E6'}
            thickness = {'high': 0.03, 'medium': 0.02, 'low': 0.01}
            
            for start in start_objects:
                for end in end_objects:
                    line = Line3D(
                        start=start.get_center(),
                        end=end.get_center(),
                        thickness=thickness[bandwidth_type],
                        color=colors[bandwidth_type]
                    )
                    connections.add(line)
            return connections
        
        # Create connections in batches
        pc_router_connections = create_connections(pcs, routers, 'medium')
        router_router_connections = create_connections(routers, routers, 'high')
        server_connections = create_connections(routers, [server], 'high')
        
        # Animation sequence with optimized grouping
        self.play(
            Create(pcs),
            Write(pc_labels),
            run_time=7
        )
        
        for router, label in zip(routers, router_labels):
            self.play(
                Create(router),
                Write(label),
                Flash(router.get_center(), color=GREY, line_length=0.5),
                run_time=3
            )
        
        self.play(
            Create(server),
            Write(server_label),
            Flash(server.get_center(), color=GREEN, line_length=0.8),
            run_time=1.5
        )
        
        # Create connections in batches
        self.play(Create(pc_router_connections), run_time=6)
        self.wait(0.5)
        self.play(Create(router_router_connections), run_time=3)
        self.play(Create(server_connections), run_time=3)
        

        # Camera rotation
        self.begin_ambient_camera_rotation(rate=0.1)
        self.wait(3)
        self.stop_ambient_camera_rotation()
        
        self.move_camera(phi=45 * DEGREES, theta=45 * DEGREES, run_time=4)
        self.wait()
        
                # Optimized data flow animation
        for _ in range(2):
            packet = Sphere(radius=0.1).set_color(WHITE)
            start_pc = random.choice(pcs)
            mid_router = random.choice(routers)
            
            self.play(
                packet.animate.move_to(start_pc.get_center()),
                run_time=3
            )
            self.play(
                packet.animate.move_to(mid_router.get_center()),
                run_time=3
            )
            self.play(
                packet.animate.move_to(server.get_center()),
                run_time=3
            )
            self.play(FadeOut(packet), run_time=1)
        # Camera movements

        self.move_camera(phi=45 * DEGREES, theta=(360+45) * DEGREES, rate_func=rate_functions.linear, run_time=6)
        self.wait()
        self.move_camera(phi=0 * DEGREES, theta=(360+45) * DEGREES, rate_func=rate_functions.linear, run_time=6)
        self.wait()

        self.move_camera(phi=180 * DEGREES, theta=(360+45) * DEGREES, rate_func=rate_functions.linear, run_time=6)
        self.wait()

        # Fade out all elements in the scene
        self.play(
            *[FadeOut(mob) for mob in self.mobjects],  # Fade out all objects in the scene
            run_time=5,
            rate_func=rate_functions.smooth  # Make the fade-out smooth
        )