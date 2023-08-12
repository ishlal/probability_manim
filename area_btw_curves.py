from manim import *

class AreaBtwCurves(Scene):
    def construct(self):
        # Create axes
        axes = Axes(
            x_range=[0, 1.2],
            y_range=[0, 1.2],
            axis_config={"color": BLUE},
            x_length=6,
            y_length=6,
        )

        # Create dotted lines
        x_line = DashedLine(axes.c2p(1, 0), axes.c2p(1, 1), color=GRAY)
        y_line = DashedLine(axes.c2p(0, 1), axes.c2p(1, 1), color=GRAY)
        y_eq_x_line = DashedLine(axes.c2p(0, 0), axes.c2p(1, 1), color=GRAY)
        y_eq_third = DashedLine(axes.c2p(0, 5/12), axes.c2p(1, 5/12), color=GRAY)
        y_eq_third_line = DashedLine(axes.c2p(0, 7/12), axes.c2p(1, 7/12), color=GRAY)
        x_eq_third_line = DashedLine(axes.c2p(5/12, 0), axes.c2p(5/12, 1), color=GRAY)
        
        top_line = DashedLine(axes.c2p(0, 5/12), axes.c2p(7/12, 1), color=GRAY)

        self.play(Create(axes), Create(x_line), Create(y_line))
        self.play(Create(y_eq_x_line),
                  Create(y_eq_third),
                Create(y_eq_third_line),
                Create(top_line),
                Create(x_eq_third_line))
        self.wait(2)
        # self.play(Create(area1))
        self.wait(2)