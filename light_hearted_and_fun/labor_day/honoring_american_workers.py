class HonoringAmericanWorkers(Scene):
    def construct(self):
        self.camera.background_color = BLACK

        night_sky = Rectangle(
            width=config.frame_width,
            height=config.frame_height,
            color=BLACK,
            fill_opacity=1
        )
        self.add(night_sky)

        stars = VGroup()
        for _ in range(50):
            star = Dot(
                radius=random.uniform(0.02, 0.05),
                color=WHITE
            ).move_to([
                random.uniform(-7, 7),
                random.uniform(-4, 4),
                0
            ])
            stars.add(star)

        self.play(FadeIn(stars))

        tribute = Text(
            "Honoring American Workers",
            font_size=36,
            color=WHITE
        ).to_edge(UP, buff=0.5)

        self.play(Write(tribute))
        self.wait(1)
        self.play(FadeOut(tribute), run_time=1.5)

        firework_colors = [RED, WHITE, BLUE, "#FF1744", "#1976D2", "#F5F5F5", "#FF4081", "#3F51B5"]

        first_wave_positions = [
            LEFT*5 + UP*2.5,
            RIGHT*4 + UP*1.8,
            LEFT*2 + UP*3,
            RIGHT*6 + UP*1.2,
            LEFT*6 + UP*2,
            RIGHT*1 + UP*2.8,
            LEFT*3.5 + UP*1.5,
            RIGHT*5.5 + UP*2.2
        ]

        for i, pos in enumerate(first_wave_positions):
            color = firework_colors[i % len(firework_colors)]
            firework = self.create_realistic_firework(pos, color)
            self.play(firework, run_time=0.9)
            if i % 2 == 0:
                self.wait(0.1)
            else:
                self.wait(0.3)

        second_wave_positions = [
            LEFT*4.5 + UP*2.2,
            RIGHT*3.5 + UP*2.7,
            LEFT*1.5 + UP*1.8,
            RIGHT*2 + UP*3.2,
            LEFT*5.5 + UP*1.4,
            UP*2.5,  # Center
            RIGHT*4.8 + UP*1.9,
            LEFT*2.8 + UP*2.9
        ]

        second_wave_fireworks = []
        for i, pos in enumerate(second_wave_positions):
            color = firework_colors[(i+3) % len(firework_colors)]
            firework = self.create_realistic_firework(pos, color, scale=1.2)
            second_wave_fireworks.append(firework)

        for i in range(0, len(second_wave_fireworks), 2):
            if i+1 < len(second_wave_fireworks):
                self.play(
                    second_wave_fireworks[i],
                    second_wave_fireworks[i+1],
                    run_time=1.0
                )
            else:
                self.play(second_wave_fireworks[i], run_time=1.0)
            self.wait(0.4)

        third_wave_positions = [
            LEFT*6 + UP*3,
            LEFT*3 + UP*2.5,
            UP*3.5,
            RIGHT*3 + UP*2.5,
            RIGHT*6 + UP*3,
            LEFT*4.5 + UP*1.5,
            RIGHT*4.5 + UP*1.5,
            LEFT*1 + UP*2,
            RIGHT*1 + UP*2,
            UP*1.8
        ]

        for i, pos in enumerate(third_wave_positions):
            color = firework_colors[(i+1) % len(firework_colors)]
            firework = self.create_realistic_firework(pos, color, scale=0.9)
            self.play(firework, run_time=0.7)
            self.wait(0.15)

        finale_positions = []
        for _ in range(15):
            pos = [
                random.uniform(-6, 6),
                random.uniform(0.5, 3.5),
                0
            ]
            finale_positions.append(pos)

        finale_fireworks = []
        for i, pos in enumerate(finale_positions):
            color = random.choice(firework_colors)
            scale_factor = random.uniform(1.0, 1.8)
            finale_fireworks.append(
                self.create_realistic_firework(pos, color, scale=scale_factor)
            )

        group1 = finale_fireworks[:5]
        group2 = finale_fireworks[5:10]
        group3 = finale_fireworks[10:]

        self.play(*group1, run_time=1.2)
        self.wait(0.2)
        self.play(*group2, run_time=1.2)
        self.wait(0.2)
        self.play(*group3, run_time=1.2)

        patriotic_finale = []
        patriotic_colors = [RED, WHITE, BLUE]

        for _ in range(20):
            pos = [
                random.uniform(-7, 7),
                random.uniform(-1, 4),
                0
            ]
            color = random.choice(patriotic_colors)
            patriotic_finale.append(
                self.create_realistic_firework(pos, color, scale=1.3, opacity=0.8)
            )

        self.play(*patriotic_finale, run_time=2.5)

        mega_finale = []
        for _ in range(25):
            pos = [
                random.uniform(-8, 8),
                random.uniform(-2, 4),
                0
            ]
            color = random.choice([RED, WHITE, BLUE, "#FF1744", "#F5F5F5"])
            mega_finale.append(
                self.create_realistic_firework(pos, color, scale=random.uniform(0.8, 2.0), opacity=0.7)
            )

        self.play(*mega_finale, run_time=3)
        self.wait(2)
        self.play(FadeOut(Group(*self.mobjects)), run_time=1.5)

        self.demonstrate_firework_code()

        # Credits
        credits_title = Text("Sources Used", font_size=42, color=BLUE, weight=BOLD)
        credits_title.to_edge(UP, buff=1)
        self.play(Write(credits_title))
        self.wait(1)

        # Create credit entries
        credit_entries = VGroup()

        # Pixabay Icon
        pixabay_icon = VGroup(
            Circle(radius=0.3, fill_color=GREEN, fill_opacity=0.8, stroke_color=WHITE),
            Text("P", font_size=20, color=WHITE, weight=BOLD)
        )
        pixabay_text = Text("Pixabay - Music", font_size=24, color=WHITE)
        pixabay_entry = VGroup(pixabay_icon, pixabay_text)
        pixabay_entry.arrange(RIGHT, buff=0.5)
        pixabay_entry.shift(UP*0.5)

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
        credit_entries.add(pixabay_entry, canva_entry)
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
        self.play(FadeOut(Group(*self.mobjects)), run_time=1.5)

    def create_realistic_firework(self, position, color, scale=1.0, opacity=1.0):

        launch_start = position + DOWN*4
        trail = Line(launch_start, position, color=color, stroke_width=3)

        particles = VGroup()
        num_particles = int(40 * scale)

        for i in range(num_particles):
            angle = i * 2 * PI / num_particles + random.uniform(-0.2, 0.2)

            particle_length = random.uniform(0.3, 0.8) * scale
            end_pos = position + particle_length * np.array([
                np.cos(angle), np.sin(angle), 0
            ])

            particle_trail = VGroup()
            segments = 8
            for seg in range(segments):
                seg_start = position + (seg/segments) * (end_pos - position)
                seg_end = position + ((seg+1)/segments) * (end_pos - position)

                seg_opacity = opacity * (1 - seg/segments) * 0.8
                segment = Line(
                    seg_start, seg_end,
                    color=color,
                    stroke_width=max(1, 4 * scale * (1 - seg/segments)),
                    stroke_opacity=seg_opacity
                )
                particle_trail.add(segment)

            particles.add(particle_trail)

        secondary_particles = VGroup()
        for i in range(int(20 * scale)):
            angle = random.uniform(0, 2*PI)
            distance = random.uniform(0.1, 0.4) * scale
            end_pos = position + distance * np.array([
                np.cos(angle), np.sin(angle), 0
            ])

            particle = Line(
                position, end_pos,
                color=color,
                stroke_width=2,
                stroke_opacity=opacity * 0.6
            )
            secondary_particles.add(particle)

        center_flash = Circle(
            radius=0.1 * scale,
            color=WHITE,
            fill_opacity=opacity
        ).move_to(position)

        return AnimationGroup(
            Succession(
                Create(trail, run_time=0.3),
                FadeOut(trail, run_time=0.1)
            ),
            Succession(
                Wait(0.3),
                AnimationGroup(
                    GrowFromCenter(center_flash),
                    LaggedStart(
                        *[Create(particle) for particle in particles],
                        lag_ratio=0.02
                    ),
                    LaggedStart(
                        *[Create(particle) for particle in secondary_particles],
                        lag_ratio=0.05
                    )
                ),
                AnimationGroup(
                    FadeOut(center_flash),
                    FadeOut(particles),
                    FadeOut(secondary_particles),
                    run_time=1.0
                )
            )
        )

    def demonstrate_firework_code(self):

        demo_title = Text(
            "How the Fireworks are Made",
            font_size=32,
            color=WHITE
        ).to_edge(UP, buff=0.5)

        self.play(Write(demo_title))
        self.wait(1)
        self.play(FadeOut(demo_title), run_time=1.5)
        divider = Line(
            start=UP*3.5,
            end=DOWN*3.5,
            color=WHITE,
            stroke_width=2
        )

        code_lines = [
            "def create_realistic_firework(self, position, color):",
            "    # Launch trail",
            "    launch_start = position + DOWN*4",
            "    trail = Line(launch_start, position,",
            "                color=color, stroke_width=3)",
            "",
            "    # Explosion particles",
            "    particles = VGroup()",
            "    for i in range(40):",
            "        angle = i * 2 * PI / 40",
            "        particle_length = random.uniform(0.3, 0.8)",
            "        end_pos = position + particle_length *",
            "                 np.array([np.cos(angle),",
            "                          np.sin(angle), 0])",
            "",
            "        particle = Line(position, end_pos,",
            "                       color=color, stroke_width=4)",
            "        particles.add(particle)",
            "",
            "    return AnimationGroup(",
            "        Create(trail), FadeOut(trail),",
            "        Create(particles), FadeOut(particles))"
        ]

        code_snippet = VGroup()
        for i, line in enumerate(code_lines):
            text_line = Text(line, font_size=12, color=GREEN, font="monospace")
            text_line.move_to(LEFT*3.5 + UP*(2.5 - i*0.25))
            code_snippet.add(text_line)

        self.play(Create(divider), run_time=1)
        self.play(LaggedStart(*[Write(line) for line in code_snippet], lag_ratio=0.1), run_time=3)
        self.wait(1)

        demo_positions = [
            RIGHT*2 + UP*2,
            RIGHT*4 + UP*1,
            RIGHT*3 + UP*2.5,
            RIGHT*5 + UP*1.8,
            RIGHT*2.5 + UP*1.2
        ]

        demo_colors = [RED, WHITE, BLUE, "#FF1744", "#1976D2"]

        for i, (pos, color) in enumerate(zip(demo_positions, demo_colors)):
            firework = self.create_realistic_firework(pos, color, scale=0.8)
            self.play(firework, run_time=1.0)
            self.wait(0.3)

        final_demo = []
        for _ in range(8):
            pos = [
                random.uniform(1, 6),
                random.uniform(0.5, 3),
                0
            ]
            color = random.choice([RED, WHITE, BLUE])
            final_demo.append(
                self.create_realistic_firework(pos, color, scale=1.1)
            )

        self.play(*final_demo, run_time=1.5)
        self.wait(1)

        self.play(
            FadeOut(divider),
            FadeOut(code_snippet),
            run_time=1.5
        )
        self.wait(1)

    def create_realistic_firework(self, position, color, scale=1.0, opacity=1.0):

        launch_start = position + DOWN*4
        trail = Line(launch_start, position, color=color, stroke_width=3)

        particles = VGroup()
        num_particles = int(40 * scale)

        for i in range(num_particles):
            angle = i * 2 * PI / num_particles + random.uniform(-0.2, 0.2)

            particle_length = random.uniform(0.3, 0.8) * scale
            end_pos = position + particle_length * np.array([
                np.cos(angle), np.sin(angle), 0
            ])

            particle_trail = VGroup()
            segments = 8
            for seg in range(segments):
                seg_start = position + (seg/segments) * (end_pos - position)
                seg_end = position + ((seg+1)/segments) * (end_pos - position)

                seg_opacity = opacity * (1 - seg/segments) * 0.8
                segment = Line(
                    seg_start, seg_end,
                    color=color,
                    stroke_width=max(1, 4 * scale * (1 - seg/segments)),
                    stroke_opacity=seg_opacity
                )
                particle_trail.add(segment)

            particles.add(particle_trail)

        secondary_particles = VGroup()
        for i in range(int(20 * scale)):
            angle = random.uniform(0, 2*PI)
            distance = random.uniform(0.1, 0.4) * scale
            end_pos = position + distance * np.array([
                np.cos(angle), np.sin(angle), 0
            ])

            particle = Line(
                position, end_pos,
                color=color,
                stroke_width=2,
                stroke_opacity=opacity * 0.6
            )
            secondary_particles.add(particle)

        center_flash = Circle(
            radius=0.1 * scale,
            color=WHITE,
            fill_opacity=opacity
        ).move_to(position)

        return AnimationGroup(
            Succession(
                Create(trail, run_time=0.3),
                FadeOut(trail, run_time=0.1)
            ),
            Succession(
                Wait(0.3),
                AnimationGroup(
                    GrowFromCenter(center_flash),
                    LaggedStart(
                        *[Create(particle) for particle in particles],
                        lag_ratio=0.02
                    ),
                    LaggedStart(
                        *[Create(particle) for particle in secondary_particles],
                        lag_ratio=0.05
                    )
                ),
                AnimationGroup(
                    FadeOut(center_flash),
                    FadeOut(particles),
                    FadeOut(secondary_particles),
                    run_time=1.0
                )
            )
        )
