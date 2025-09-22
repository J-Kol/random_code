from manim import *
import random as rd, numpy as np

class VectorArrow(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        dot = Dot(ORIGIN)
        self.add(dot, axes)

        x, y, z = rd.randint(1, 7), rd.randint(1, 3), rd.randint(1, 7)
        x_2, y_2, z_2 = rd.randint(-4, 3), rd.randint(-6, 1), rd.randint(-2, 4)
        len_1, len_2 = np.sqrt(x**2 + y**2 + z**2), np.sqrt(x_2**2 + y_2**2 + z_2**2)

        arrow = Arrow(ORIGIN, [x, y, z], buff=0, color=BLUE)
        arrow_2 = Arrow([x, y, z], [x_2, y_2, z_2], buff=0, color=GREEN)
        sum_v = Arrow([x_2, y_2, z_2], ORIGIN, buff=0, color=RED)
        grid = NumberPlane()
        origin_text = Text('(0, 0, 0)').next_to(dot, DOWN)
        tip_text = Text(f'({x}, {y}, {z})').next_to(arrow.get_end(), RIGHT)
        tip_text_2 = Text(f'({x_2}, {y_2}, {z_2})').next_to(arrow_2.get_end(), RIGHT)

        x_label = Text('X').scale(0.7).next_to(axes.x_axis.get_end(), RIGHT)
        y_label = Text('Y').scale(0.7).next_to(axes.y_axis.get_end(), UP)
        z_label = Text('Z').scale(0.7).next_to(axes.z_axis.get_end(), OUT)

        self.add(arrow, arrow_2, sum_v, origin_text, tip_text, tip_text_2, x_label, y_label, z_label, grid)
        self.play(Create(dot), Create(arrow), Create(arrow_2), Create(sum_v), Write(origin_text), Write(tip_text), Write(tip_text_2), Write(x_label), Write(y_label), Write(z_label))

        camera_distance = max(abs(x), abs(y), abs(z), abs(x_2), abs(y_2), abs(z_2)) * 1.5
        self.renderer.camera.light_source.move_to(camera_distance*IN)
        self.set_camera_orientation(phi=60 * DEGREES, theta=-45 * DEGREES, distance=camera_distance)

        self.begin_ambient_camera_rotation(rate=0.1)
        self.wait(5)
        self.stop_ambient_camera_rotation()
        #manim -pql vectors.py VectorArrow