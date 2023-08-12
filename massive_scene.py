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
        label_y_eq_third = MathTex("y = a").add_updater(lambda m: m.next_to(y_eq_third, LEFT)).scale(0.8)
        y_eq_third_line = DashedLine(axes.c2p(0, 7/12), axes.c2p(1, 7/12), color=GRAY)
        label_y_eq_one_minues = MathTex("y = 1 - a").add_updater(lambda m: m.next_to(y_eq_third_line, LEFT)).scale(0.8)
        x_eq_third_line = DashedLine(axes.c2p(5/12, 0), axes.c2p(5/12, 1), color=GRAY)
        label_x_eq_third = MathTex("x = a").add_updater(lambda m: m.next_to(x_eq_third_line, DOWN)).scale(0.8)
        
        top_line = DashedLine(axes.c2p(0, 5/12), axes.c2p(7/12, 1), color=GRAY)
        label_top_line = MathTex("y = x + a").add_updater(lambda m: m.next_to(top_line, UP + RIGHT*0.3)).scale(0.8)

        # Create the area polygon

        leq_x = [
            axes.c2p(0, 0),
            axes.c2p(0, 1),
            axes.c2p(5/12, 1),
            axes.c2p(5/12, 0)
        ]
        leq_x_polygon = Polygon(*leq_x, color=BLUE, fill_opacity=0.5)

        leq_slant = [
            axes.c2p(0, 0),
            axes.c2p(0, 5/12),
            axes.c2p(7/12, 1),
            axes.c2p(1, 1),
            axes.c2p(1, 0)
        ]
        leq_slant_polygon = Polygon(*leq_slant, color=GREEN, fill_opacity=0.5)

        geq_a = [
            axes.c2p(0, 7/12),
            axes.c2p(0, 1),
            axes.c2p(1, 1),
            axes.c2p(1, 7/12)
        ]
        geq_a_polygon = Polygon(*geq_a, color=RED, fill_opacity=0.5)


        true_vertices = [
            axes.c2p(2/12, 7/12),
            axes.c2p(5/12, 7/12),
            axes.c2p(5/12, 10/12),
        ]
        area_polygon = Polygon(*true_vertices, color=YELLOW, fill_opacity=0.5)

        dec_area_polygon = DecimalNumber(0, num_decimal_places=5, include_sign=False, unit=None, color=YELLOW)
        dec_area_polygon.add_updater(lambda d: d.set_value(0.5 * (axes.p2c(y_eq_third.get_center())[1]*3 - 1)**2))
        dec_a_value = DecimalNumber(0, num_decimal_places=5, include_sign=False, unit=None)
        dec_a_value.add_updater(lambda d: d.set_value(axes.p2c(y_eq_third.get_center())[1]))
        label_area = Text("Area: ", color=YELLOW).scale(0.7)
        label_a = MathTex("a = ").scale(1.02)
        label_a.shift(RIGHT * 4)
        dec_a_value.next_to(label_a, RIGHT)
        label_area.shift(RIGHT*4 + DOWN)
        dec_area_polygon.next_to(label_area, RIGHT)
        

        self.play(Create(axes), Create(x_line), Create(y_line))
        self.add(label_y_eq_third, label_y_eq_one_minues, label_x_eq_third, label_top_line)
        self.play(Create(y_eq_x_line),
                  Create(y_eq_third),
                  Create(y_eq_third_line),
                  Create(top_line),
                  Create(x_eq_third_line))
        
        # Animate the appearance of the area polygon
        leq_x_eq = MathTex("x \\leq a", color=BLUE)
        leq_x_eq.shift(RIGHT*4 + UP)
        self.play(FadeIn(leq_x_eq))
        self.play(Create(leq_x_polygon))
        self.wait(0.8)
        self.play(FadeOut(leq_x_eq))
        self.wait(0.8)
        leq_slant_eq = MathTex("y \\leq x + a", color=GREEN)
        leq_slant_eq.shift(RIGHT*4 + UP)
        self.play(FadeIn(leq_slant_eq))
        self.play(Create(leq_slant_polygon))
        self.wait(0.8)
        self.play(FadeOut(leq_slant_eq))
        self.wait(0.8)
        geq_a_eq = MathTex("y \\geq 1-a", color=RED)
        geq_a_eq.shift(RIGHT*4 + UP)
        self.play(FadeIn(geq_a_eq))
        self.play(Create(geq_a_polygon))
        self.wait(0.8)
        self.play(FadeOut(geq_a_eq))
        self.wait(1)
        self.play(Create(area_polygon))
        self.wait(0.8)

        # animate y_eq_third shifting down, and the polygon filling the new area
        new_y_eq_third = DashedLine(axes.c2p(0, 4.1/12), axes.c2p(1, 4.1/12), color=GRAY)
        new_x_eq_third_line = DashedLine(axes.c2p(4.1/12, 0), axes.c2p(4.1/12, 1), color=GRAY)
        neq_y_eq_one_minues = DashedLine(axes.c2p(0, 7.9/12), axes.c2p(1, 7.9/12), color=GRAY)
        new_top = DashedLine(axes.c2p(0, 4.1/12), axes.c2p(7.9/12, 1), color=GRAY)
        new_polygon = Polygon(
            axes.c2p(3.8/12, 7.9/12),
            axes.c2p(4.1/12, 8.2/12),
            axes.c2p(4.1/12, 7.9/12),
            color=YELLOW,
            fill_opacity=0.5
        )
        self.play(FadeOut(leq_x_polygon), FadeOut(leq_slant_polygon), FadeOut(geq_a_polygon))
        self.add(label_area, dec_area_polygon, label_a, dec_a_value)
        self.play(Transform(y_eq_third, new_y_eq_third),
                    Transform(x_eq_third_line, new_x_eq_third_line),
                    Transform(y_eq_third_line, neq_y_eq_one_minues),
                    Transform(top_line, new_top),
                  Transform(area_polygon, new_polygon), run_time=4)
        self.wait(2)

        new_y_eq_third_2 = DashedLine(axes.c2p(0, 5.8/12), axes.c2p(1, 5.8/12), color=GRAY)
        new_x_eq_third_line_2 = DashedLine(axes.c2p(5.8/12, 0), axes.c2p(5.8/12, 1), color=GRAY)
        neq_y_eq_one_minues_2 = DashedLine(axes.c2p(0, 6.2/12), axes.c2p(1, 6.2/12), color=GRAY)
        new_top_2 = DashedLine(axes.c2p(0, 5.8/12), axes.c2p(6.2/12, 1), color=GRAY)
        new_polygon_2 = Polygon(
            axes.c2p(0.4/12, 6.2/12),
            axes.c2p(5.8/12, 11.6/12),
            axes.c2p(5.8/12, 6.2/12),
            color=YELLOW,
            fill_opacity=0.5
        )
        self.play(Transform(y_eq_third, new_y_eq_third_2),
                    Transform(x_eq_third_line, new_x_eq_third_line_2),
                    Transform(y_eq_third_line, neq_y_eq_one_minues_2),
                    Transform(top_line, new_top_2),
                  Transform(area_polygon, new_polygon_2), run_time=4.2)
        self.wait(2)
        self.play(FadeOut(label_a), FadeOut(dec_a_value), FadeOut(label_area), FadeOut(dec_area_polygon))


        new_y_eq_third_2 = DashedLine(axes.c2p(0, 7/12), axes.c2p(1, 7/12), color=GRAY)
        new_x_eq_third_line_2 = DashedLine(axes.c2p(7/12, 0), axes.c2p(7/12, 1), color=GRAY)
        neq_y_eq_one_minues_2 = DashedLine(axes.c2p(0, 5/12), axes.c2p(1, 5/12), color=GRAY)
        new_top_2 = DashedLine(axes.c2p(0, 7/12), axes.c2p(5/12, 1), color=GRAY)
        # new_polygon_2 = Polygon(
        #     axes.c2p(0.4/12, 6.2/12),
        #     axes.c2p(5.8/12, 11.6/12),
        #     axes.c2p(5.8/12, 6.2/12),
        #     color=YELLOW,
        #     fill_opacity=0.5
        # )
        self.play(Transform(y_eq_third, new_y_eq_third_2),
                    Transform(x_eq_third_line, new_x_eq_third_line_2),
                    Transform(y_eq_third_line, neq_y_eq_one_minues_2),
                    Transform(top_line, new_top_2),
                  FadeOut(area_polygon), run_time=4.2)
        
        leq_x = [
            axes.c2p(0, 0),
            axes.c2p(0, 1),
            axes.c2p(7/12, 1),
            axes.c2p(7/12, 0)
        ]
        leq_x_polygon = Polygon(*leq_x, color=BLUE, fill_opacity=0.5)

        leq_slant = [
            axes.c2p(0, 0),
            axes.c2p(0, 7/12),
            axes.c2p(5/12, 1),
            axes.c2p(1, 1),
            axes.c2p(1, 0)
        ]
        leq_slant_polygon = Polygon(*leq_slant, color=GREEN, fill_opacity=0.5)

        geq_a = [
            axes.c2p(0, 5/12),
            axes.c2p(0, 1),
            axes.c2p(1, 1),
            axes.c2p(1, 5/12)
        ]
        geq_a_polygon = Polygon(*geq_a, color=RED, fill_opacity=0.5)


        true_vertices = [
            axes.c2p(0, 5/12),
            axes.c2p(0, 7/12),
            axes.c2p(5/12, 1),
            axes.c2p(7/12, 1),
            axes.c2p(7/12, 7/12),
            axes.c2p(5/12, 5/12)
        ]
        area_polygon = Polygon(*true_vertices, color=YELLOW, fill_opacity=0.5)


        self.wait(3)
        self.play(FadeIn(leq_x_eq))
        self.play(Create(leq_x_polygon))
        self.wait(0.8)
        self.play(FadeOut(leq_x_eq))
        self.wait(0.8)
        self.play(FadeIn(leq_slant_eq))
        self.play(Create(leq_slant_polygon))
        self.wait(0.8)
        self.play(FadeOut(leq_slant_eq))
        self.wait(0.8)
        self.play(FadeIn(geq_a_eq))
        self.play(Create(geq_a_polygon))
        self.wait(0.8)
        self.play(FadeOut(geq_a_eq))
        self.wait(0.8)

        self.play(Create(area_polygon))
        self.wait(3)

        self.play(FadeOut(geq_a_polygon), FadeOut(leq_slant_polygon), FadeOut(leq_x_polygon), FadeOut(area_polygon))
        self.wait(2)

        
        big_triangle = [
            axes.c2p(0, 0),
            axes.c2p(0, 1),
            axes.c2p(1, 1)
        ]
        big_triangle_poly = Polygon(*big_triangle, color=GREEN, fill_opacity=0.3)
        self.play(Create(big_triangle_poly))
        self.wait(2)
        small_triangle_1 = [
            axes.c2p(0, 0),
            axes.c2p(0, 5/12),
            axes.c2p(5/12, 5/12)
        ]
        small_triangle_2 = [
            axes.c2p(0, 7/12),
            axes.c2p(0, 1),
            axes.c2p(5/12, 1)
        ]
        small_triangle_3 = [
            axes.c2p(7/12, 1),
            axes.c2p(1, 1),
            axes.c2p(7/12, 7/12)
        ]
        tri_1 = Polygon(*small_triangle_1, color=RED, fill_opacity=0.3)
        tri_2 = Polygon(*small_triangle_2, color=RED, fill_opacity=0.3)
        tri_3 = Polygon(*small_triangle_3, color=RED, fill_opacity=0.3)
        self.play(Create(tri_1),
                    Create(tri_2),
                    Create(tri_3),
                )
        self.wait(1)
        self.play(FadeIn(area_polygon))
        self.wait(2)

        length_1_minus_a = MathTex("1-a").add_updater(lambda m: m.next_to(tri_1, LEFT)).scale(0.5)
        length_1_minus_a_2 = MathTex("1-a").add_updater(lambda m: m.next_to(tri_1, UP)).scale(0.5)
        length_1_minus_a_3 = MathTex("1-a").add_updater(lambda m: m.next_to(tri_2, LEFT)).scale(0.5)
        length_1_minus_a_4 = MathTex("1-a").add_updater(lambda m: m.next_to(tri_2, UP)).scale(0.5)
        length_1_minus_a_5 = MathTex("1-a").add_updater(lambda m: m.next_to(tri_3, UP)).scale(0.5)
        length_1_minus_a_6 = MathTex("1-a").add_updater(lambda m: m.next_to(tri_3, LEFT)).scale(0.5)
        self.play(FadeIn(length_1_minus_a), FadeIn(length_1_minus_a_2), FadeIn(length_1_minus_a_3), FadeIn(length_1_minus_a_4), FadeIn(length_1_minus_a_5), FadeIn(length_1_minus_a_6))
        self.wait(1)
        # FadeOut everything except the small_triangles and the area_polygon
        self.play(
            FadeOut(axes),
            FadeOut(x_line),
            FadeOut(y_line),
            FadeOut(x_eq_third_line),
            FadeOut(y_eq_third_line),
            FadeOut(y_eq_third),
            FadeOut(y_eq_x_line),
            FadeOut(top_line),
            FadeOut(new_x_eq_third_line_2),
            FadeOut(neq_y_eq_one_minues_2),
            FadeOut(new_top_2),
            FadeOut(new_y_eq_third_2),
            FadeOut(label_y_eq_one_minues),
            FadeOut(label_y_eq_third),
            FadeOut(label_x_eq_third),
            FadeOut(label_top_line)
            
        )
        self.wait(2)

        group_poly = Group(tri_1, tri_2, tri_3, area_polygon, big_triangle_poly)
        self.play(group_poly.animate.shift(LEFT*3))
        self.play(group_poly.animate.scale(0.75))
        # tri_1.shift(LEFT*1.5)
        # tri_2.shift(LEFT*1.5)
        # tri_3.shift(LEFT*1.5)
        # area_polygon.shift(LEFT*1.5)
        self.wait(2)
        polygon_copy = tri_3.copy()
        polygon_copy.move_to(tri_3.get_center())
        polygon_copy_1 = tri_1.copy()
        polygon_copy_1.move_to(tri_1.get_center())
        polygon_copy_2 = tri_2.copy()
        polygon_copy_2.move_to(tri_2.get_center())
        self.add(polygon_copy, polygon_copy_1, polygon_copy_2)
        target_poly = tri_1.copy()
        target_poly.move_to(tri_3.get_center() + RIGHT*3.5 + DOWN)
        # self.add(target_poly)
        self.play(polygon_copy.animate.move_to(target_poly.get_center()),
                  polygon_copy_1.animate.move_to(target_poly.get_center()),
                    polygon_copy_2.animate.move_to(target_poly.get_center()),
                    )
        self.play(FadeOut(polygon_copy_1), FadeOut(polygon_copy_2), run_time=0.3)
        self.wait(0.5)
        minus_3 = MathTex("- 3 \cdot     ").scale(2)
        minus_3.next_to(polygon_copy, LEFT*2)
        self.play(FadeIn(minus_3))
        equals = MathTex(" = ").scale(2)
        equals.next_to(polygon_copy, RIGHT)
        self.play(FadeIn(equals))
        wonky_poly_copy = area_polygon.copy()
        wonky_poly_copy.move_to(area_polygon.get_center())
        self.play(wonky_poly_copy.animate.move_to(equals.get_center() + RIGHT*2))
        self.wait(1)
        equation_group = Group(group_poly, minus_3, polygon_copy, equals, wonky_poly_copy)
        self.play(equation_group.animate.scale(0.65))
        self.play(equation_group.animate.shift(UP*2.6))
        l = Line(LEFT*8 + UP*0.7, RIGHT*8 + UP*0.7)
        self.play(Create(l))
        self.wait(2)

        triangle_copy = big_triangle_poly.copy()
        triangle_copy.move_to(big_triangle_poly.get_center())
        self.play(triangle_copy.animate.shift(DOWN*3.7))
        self.wait(1)
        label_1 = MathTex("1").scale(1.2)
        label_1_2 = MathTex("1").scale(1.2)
        label_1.next_to(triangle_copy, LEFT)
        label_1_2.next_to(triangle_copy, UP)
        self.play(FadeIn(label_1), FadeIn(label_1_2))
        self.wait(1)
        eq_area = MathTex(r"A = \frac{1}{2} \cdot b \cdot h").scale(1.2)
        eq_area.next_to(triangle_copy, RIGHT*3)
        self.play(FadeIn(eq_area))
        self.wait(1)
        eq_area_trans = MathTex(r"A = \frac{1}{2} \cdot 1 \cdot h").scale(1.2)
        eq_area_trans.move_to(eq_area.get_center())
        self.play(Transform(eq_area, eq_area_trans))
        self.wait(1)
        eq_area_trans2 = MathTex(r"A = \frac{1}{2} \cdot 1 \cdot 1").scale(1.2)
        eq_area_trans2.move_to(eq_area.get_center())
        self.play(Transform(eq_area, eq_area_trans2))
        self.wait(1)
        eq_area_trans3 = MathTex(r"A = \frac{1}{2}").scale(1.2)
        eq_area_trans3.move_to(eq_area.get_center())
        self.play(Transform(eq_area, eq_area_trans3))
        self.wait(2)
        group_triangle = Group(triangle_copy, label_1, label_1_2)
        self.play(group_triangle.animate.move_to(group_poly.get_center()),
                  eq_area.animate.move_to(group_poly.get_center()))
        self.play(FadeOut(group_triangle), FadeOut(eq_area), run_time=0.3)
        eq_ans = MathTex(r"\frac{1}{2}").scale(1.4)
        eq_ans.move_to(group_poly.get_center())
        self.play(Transform(group_poly, eq_ans), FadeOut(length_1_minus_a), FadeOut(length_1_minus_a_2), FadeOut(length_1_minus_a_3),
                  FadeOut(length_1_minus_a_4), FadeOut(length_1_minus_a_5), FadeOut(length_1_minus_a_6))
        self.wait(3)

        red_poly_copy = polygon_copy.copy()
        red_poly_copy.move_to(polygon_copy.get_center())
        self.play(red_poly_copy.animate.shift(DOWN*3.7 + LEFT*3.5))
        self.wait(1)
        side_length_1 = MathTex("1 - a").scale(0.7)
        side_length_1.next_to(red_poly_copy, LEFT)
        side_length_1_2 = MathTex("1 - a").scale(0.7)
        side_length_1_2.next_to(red_poly_copy, UP)
        self.play(FadeIn(side_length_1), FadeIn(side_length_1_2))
        eq_small_triangle = MathTex(r"A = \frac{1}{2} \cdot b \cdot h").scale(1.2)
        eq_small_triangle.move_to(red_poly_copy.get_center() + RIGHT*5)
        self.play(FadeIn(eq_small_triangle))
        self.wait(1.5)
        eq_small_triangle_copy = MathTex(r"A = \frac{1}{2} \cdot (1-a) \cdot (1-a)").scale(1.2)
        eq_small_triangle_copy.move_to(eq_small_triangle.get_center())
        self.play(Transform(eq_small_triangle, eq_small_triangle_copy))
        self.wait(1.5)
        eq_small_triangle_copy_2 = MathTex(r"A = \frac{1}{2} \cdot (1-a)^2").scale(1.2)
        eq_small_triangle_copy_2.move_to(eq_small_triangle.get_center())
        self.play(Transform(eq_small_triangle, eq_small_triangle_copy_2))
        self.wait(1)
        self.play(
            FadeOut(side_length_1),
            FadeOut(side_length_1_2),
            red_poly_copy.animate.move_to(polygon_copy.get_center()),
            eq_small_triangle.animate.move_to(polygon_copy.get_center())
        )
        self.play(FadeOut(red_poly_copy), FadeOut(eq_small_triangle))

        red_poly_area = MathTex(r"(\frac{1}{2} \cdot (1-a)^2)")
        new_eq_overall = MathTex(r"\frac{1}{2} - 3 \cdot \frac{1}{2} \cdot (1-a)^2 = ")
        # wonky_poly_copy.next_to(new_eq_overall, RIGHT)
        wonky_poly_copy_copy = wonky_poly_copy.copy()
        # wonky_poly_copy_copy.move_to(wonky_poly_copy.get_center())
        wonky_poly_copy_copy.next_to(new_eq_overall, RIGHT)
        eq_group = Group(new_eq_overall, wonky_poly_copy_copy).scale(1.4)
        old_group = Group(eq_ans, minus_3, red_poly_area, equals, wonky_poly_copy)
        eq_group.move_to(old_group.get_center() + UP)
        # self.play( Transform(old_group, eq_group), FadeOut(group_poly), FadeOut(equation_group))
        self.play(FadeOut(equation_group))
        self.play(FadeIn(eq_group))
        self.wait(1.5)
        self.play(FadeOut(eq_group), FadeOut(l))
        self.wait(2)
        


