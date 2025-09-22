from manim import *
import numpy as np

class SinAndCosFunctionPlot(Scene):
    def construct(self):
        axes = Axes(
            x_range=[0, 200],
            y_range=[-100, 100],
            x_length=10,
            axis_config={"color": GREEN},
            x_axis_config={
                "numbers_to_include": np.arange(0, 400, 40),
                "numbers_with_elongated_ticks": np.arange(0, 400, 40),
            },
            tips=False,
        )

        A = 100
        f = 10**5

        axes_labels = axes.get_axis_labels()
        sin_graph = axes.plot(lambda x: A * np.sin(2 * np.pi * f * x)*np.exp(-0.1*x), color=BLUE)

        sin_label = axes.get_graph_label(
            sin_graph, "\\sin(x)", x_val=200, direction=UP / 2
        )

        plot = VGroup(axes, sin_graph)
        labels = VGroup(axes_labels, sin_label)
        self.add(plot, labels)