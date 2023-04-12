from manim import *
import math

class FreeFall1(Scene):
    def construct(self):
        square = Square(0.5)
        square.set_fill(PINK, opacity=0.5)
        dot = Dot()
        obj = Group(*[square, dot])
        obj.move_to(3.5 * UP + LEFT * 3)
        numberLine = NumberLine(x_range=[0, 156.25, 25], length=7, rotation=-math.pi / 2, include_ticks=True,
                                include_tip=True, include_numbers=True, label_direction=LEFT, font_size=36).shift(
            LEFT * 4)
        y_label = MathTex(r"y/\mbox{m}", font_size=36).move_to(LEFT * 4.5 + DOWN * 3.8)
        timer = ValueTracker(0)

        def v_arrow():
            arrow = Line(start=obj.get_center(), end=obj.get_center() + 0.2 * timer.get_value() * DOWN,
                         stroke_color=GREEN).add_tip(tip_width=0.25)
            v_text = DecimalNumber(font_size=24).set_value(0.2 * timer.get_value()).next_to(arrow.get_end())
            v_unit = Tex("m/s", font_size=24).next_to(v_text)
            return VGroup(arrow, v_text, v_unit)

        data = []
        for i in range(10):
            data.append([0.5 * i, 1.25 * i ** 2, 5 * i])
        table = DecimalTable(
            data,
            col_labels=[MathTex(r"t/\mbox{s}"), MathTex(r"y/\mbox{m}"), MathTex(r"v/ m \cdot s^{-1}")],
            h_buff=1,
            line_config={"stroke_width": 1},
            arrange_in_grid_config={"col_widths": [2, 2, 2], "col_alignments": "ccc"},
            element_to_mobject_config={"num_decimal_places": 2}
        ).scale(0.6).shift(RIGHT * 4)

        self.play(FadeIn(obj))
        self.play(Create(numberLine))
        self.add(y_label)
        self.play(AnimationGroup(Create(table.get_horizontal_lines()),
                                 Create(table.get_vertical_lines()),
                                 Create(table.get_col_labels())))
        self.add(always_redraw(v_arrow))
        for i in range(200):
            timer.set_value(i * 0.05)
            if i % 20 == 0:
                cur_pos = Dot(3 * LEFT + (3.5 - i ** 2 * 0.0002) * UP)
                self.add(cur_pos)
                row_number = i // 20 + 1
                self.add(table.get_entries_without_labels((row_number, 1)),
                         table.get_entries_without_labels((row_number, 2)),
                         table.get_entries_without_labels((row_number, 3)))
            self.play(obj.animate(run_time=0.01).move_to(3 * LEFT + (3.5 - i ** 2 * 0.0002) * UP))

        self.remove(numberLine,square,dot,y_label)
        self.play(table.animate().move_to(LEFT * 4.5))

class FreeFall2(Scene):
    def construct(self):
        data = []
        for i in range(10):
            data.append([0.5 * i, 1.25 * i ** 2, 5 * i])
        table = DecimalTable(
            data,
            col_labels=[MathTex(r"t/\mbox{s}"), MathTex(r"y/\mbox{m}"), MathTex(r"v/ m \cdot s^{-1}")],
            h_buff=1,
            line_config={"stroke_width": 1},
            arrange_in_grid_config={"col_widths": [1.5, 1.5, 2], "col_alignments": "ccc"},
            element_to_mobject_config={"num_decimal_places": 2}
        ).scale(0.6).shift(LEFT * 4.5)
        self.add(table)
        coord_xt = Axes(x_range=[0, 5, 0.5], y_range=[0, 160, 25], x_length=7, y_length=3,
                        axis_config={'tip_width': 0.2,"font_size":24}).shift(RIGHT * 3 + UP * 2).add_coordinates()
        coord_vt = Axes(x_range=[0, 5, 0.5], y_range=[0, 50, 10], x_length=7, y_length=3,
                        axis_config={'tip_width': 0.2,"font_size":24}).shift(RIGHT * 3 + DOWN * 2).add_coordinates()
        labels_xt = coord_xt.get_axis_labels(MathTex(r"y/\mbox{m}",font_size=24), MathTex(r"t/\mbox{s}",font_size=24))
        labels_vt = coord_vt.get_axis_labels(MathTex(r"y/\mbox{m}",font_size=24), MathTex(r"v/ m \cdot s^{-1}",font_size=24))
        self.play(AnimationGroup(Create(coord_xt), Create(coord_vt)))
        self.add(labels_xt, labels_vt)
        for i in range(10):
            self.add(Dot(data[i][0] * 1.4 * RIGHT + data[i][1] * 3 / 160 * UP).shift(LEFT * 0.5 + UP * 0.5)
                     , Dot(data[i][0] * 1.4 * RIGHT + data[i][2] * 3 / 50 * UP).shift(LEFT * 0.5 + DOWN * 3.5))
            self.wait(0.5)
        graph_xt=coord_xt.plot(lambda t:5*t**2,color=YELLOW)
        graph_vt=coord_vt.plot(lambda t:10*t,color=GREEN)
        self.play(AnimationGroup(Create(graph_xt),Create(graph_vt)))
        self.wait()

class FreeFall3(Scene):
    def construct(self):
        coord_xt = Axes(x_range=[0, 5, 0.5], y_range=[0, 160, 25], x_length=7, y_length=3,
                        axis_config={'tip_width': 0.2, "font_size": 24}).shift(RIGHT * 3 + UP * 2).add_coordinates()
        coord_vt = Axes(x_range=[0, 5, 0.5], y_range=[0, 50, 10], x_length=7, y_length=3,
                        axis_config={'tip_width': 0.2, "font_size": 24}).shift(RIGHT * 3 + DOWN * 2).add_coordinates()
        labels_xt = coord_xt.get_axis_labels(MathTex(r"y/\mbox{m}", font_size=24), MathTex(r"t/\mbox{s}", font_size=24))
        labels_vt = coord_vt.get_axis_labels(MathTex(r"y/\mbox{m}", font_size=24),
                                             MathTex(r"v/ m \cdot s^{-1}", font_size=24))

        f_xt=lambda t: 5 * t ** 2
        f_vt=lambda t: 10 * t
        graph_xt = coord_xt.plot(f_xt, color=YELLOW)
        graph_vt = coord_vt.plot(f_vt, color=GREEN)
        self.add(coord_xt, coord_vt, labels_xt, labels_vt,graph_xt,graph_vt)

        square = Square(0.5)
        square.set_fill(PINK, opacity=0.5)
        dot = Dot()
        obj = Group(*[square, dot])
        obj.move_to(3.5 * UP + LEFT * 3)
        numberLine = NumberLine(x_range=[0, 156.25, 25], length=7, rotation=-math.pi / 2, include_ticks=True,
                                include_tip=True, include_numbers=True, label_direction=LEFT, font_size=36).shift(
            LEFT * 4)
        y_label = MathTex(r"y/\mbox{m}", font_size=36).move_to(LEFT * 4.5 + DOWN * 3.8)
        timer = ValueTracker(0)

        def v_arrow():
            arrow = Line(start=obj.get_center(), end=obj.get_center() + 0.2 * timer.get_value() * DOWN,
                         stroke_color=GREEN).add_tip(tip_width=0.25)
            v_text = DecimalNumber(font_size=24).set_value(0.2 * timer.get_value()).next_to(arrow.get_end())
            v_unit = Tex("m/s", font_size=24).next_to(v_text)
            return VGroup(arrow, v_text, v_unit)

        dot_xt = Dot().add_updater(lambda x:x.move_to(coord_xt.c2p(timer.get_value(), f_xt(timer.get_value()))))
        dot_vt = Dot().add_updater(lambda x:x.move_to(coord_vt.c2p(timer.get_value(), f_vt(timer.get_value()))))

        self.play(FadeIn(obj, numberLine, y_label))
        self.add(always_redraw(v_arrow),dot_xt,dot_vt)

        for i in range(200):
            timer.set_value(i * 0.025)
            if i % 20 == 0:
                cur_pos = Dot(3 * LEFT + (3.5 - i ** 2 * 0.0002) * UP)
                self.add(cur_pos)
            self.play(obj.animate(run_time=0.01).move_to(3 * LEFT + (3.5 - i ** 2 * 0.0002) * UP))

        self.play(FadeOut(coord_xt,coord_vt))

class FreeFall4(Scene):
    def construct(self):
        square = Square(0.5)
        square.set_fill(PINK, opacity=0.5)
        dot = Dot()
        obj = Group(*[square, dot])
        obj.move_to(3.5 * UP + LEFT * 3)
        numberLine = NumberLine(x_range=[0, 156.25, 25], length=7, rotation=-math.pi / 2, include_ticks=True,
                                include_tip=True, include_numbers=True, label_direction=LEFT, font_size=36).shift(
            LEFT * 4)
        y_label = MathTex(r"y/\mbox{m}", font_size=36).move_to(LEFT * 4.5 + DOWN * 3.8)
        timer = ValueTracker(0)

        def v_arrow():
            arrow = Line(start=obj.get_center(), end=obj.get_center() + 0.2 * timer.get_value() * DOWN,
                         stroke_color=GREEN).add_tip(tip_width=0.25)
            v_text = DecimalNumber(font_size=24).set_value(0.2 * timer.get_value()).next_to(arrow.get_end())
            v_unit = Tex("m/s", font_size=24).next_to(v_text)
            return VGroup(arrow, v_text, v_unit)

        coord_e = Axes(x_range=[0, 160, 50], y_range=[-160, 160, 50], x_length=7, y_length=6,
                       axis_config={'tip_width': 0.2, "font_size": 24,'tip_height':0.2}).shift(RIGHT * 3).add_coordinates()
        labels_e = coord_e.get_axis_labels(MathTex(r"y/\mbox{m}", font_size=24), MathTex(r"E/\mbox{J}", font_size=24))

        f_ek = lambda t: 5 * t ** 2
        f_ep = lambda t: -5 * t ** 2
        f_y = lambda t: 5 * t ** 2
        graph_ek = coord_e.plot(lambda x:x, color=ORANGE)
        graph_ep = coord_e.plot(lambda x:-x, color=BLUE)
        self.play(Create(coord_e))
        self.add(labels_e)

        def point_graph_e():
            dot_ek = Dot(coord_e.c2p(f_y(timer.get_value()), f_ek(timer.get_value())))
            dot_ep = Dot(coord_e.c2p(f_y(timer.get_value()), f_ep(timer.get_value())))
            arrow_ek = DashedLine(coord_e.c2p(f_y(timer.get_value()), 0),dot_ek.get_center(),color=ORANGE)
            arrow_ep = DashedLine(coord_e.c2p(f_y(timer.get_value()), 0),dot_ep.get_center(),color=BLUE)
            text_ek = MathTex(r"E_k").next_to(arrow_ek)
            text_ep = MathTex(r"E_p").next_to(arrow_ep)
            return VGroup(dot_ek,dot_ep,arrow_ek,arrow_ep,text_ek,text_ep)

        self.play(FadeIn(obj, numberLine, y_label))
        self.add(always_redraw(v_arrow),always_redraw(point_graph_e),graph_ek,graph_ep)

        for i in range(200):
            timer.set_value(i * 0.025)
            if i % 20 == 0:
                cur_pos = Dot(3 * LEFT + (3.5 - i ** 2 * 0.0002) * UP)
                self.add(cur_pos)
            self.play(obj.animate(run_time=0.01).move_to(3 * LEFT + (3.5 - i ** 2 * 0.0002) * UP))

class FreeFall(Scene):
    def construct(self):
        square = Square(0.5)
        square.set_fill(PINK, opacity=0.5)
        dot = Dot()
        obj = Group(*[square, dot])
        obj.move_to(3.5 * UP + LEFT * 3)
        numberLine = NumberLine(x_range=[0, 156.25, 25], length=7, rotation=-math.pi / 2, include_ticks=True,
                                include_tip=True, include_numbers=True, label_direction=LEFT, font_size=36).shift(
            LEFT * 4)
        y_label = MathTex(r"y/\mbox{m}", font_size=36).move_to(LEFT * 4.5 + DOWN * 3.8)
        timer = ValueTracker(0)

        def v_arrow():
            arrow = Line(start=obj.get_center(), end=obj.get_center() + 0.2 * timer.get_value() * DOWN,
                         stroke_color=GREEN).add_tip(tip_width=0.25)
            v_text = DecimalNumber(font_size=24).set_value(0.2 * timer.get_value()).next_to(arrow.get_end())
            v_unit = Tex("m/s", font_size=24).next_to(v_text)
            return VGroup(arrow, v_text, v_unit)

        data = []
        for i in range(10):
            data.append([0.5 * i, 1.25 * i ** 2, 5 * i])
        table = DecimalTable(
            data,
            col_labels=[MathTex(r"t/\mbox{s}"), MathTex(r"y/\mbox{m}"), MathTex(r"v/ m \cdot s^{-1}")],
            h_buff=1,
            line_config={"stroke_width": 1},
            arrange_in_grid_config={"col_widths": [2, 2, 2], "col_alignments": "ccc"},
            element_to_mobject_config={"num_decimal_places": 2}
        ).scale(0.6).shift(RIGHT * 4)

        self.play(FadeIn(obj))
        self.play(Create(numberLine))
        self.add(y_label)
        self.play(AnimationGroup(Create(table.get_horizontal_lines()),
                                 Create(table.get_vertical_lines()),
                                 Create(table.get_col_labels())))
        self.add(always_redraw(v_arrow))
        for i in range(200):
            timer.set_value(i * 0.05)
            if i % 20 == 0:
                cur_pos = Dot(3 * LEFT + (3.5 - i ** 2 * 0.0002) * UP)
                self.add(cur_pos)
                row_number = i // 20 + 1
                self.add(table.get_entries_without_labels((row_number, 1)),
                         table.get_entries_without_labels((row_number, 2)),
                         table.get_entries_without_labels((row_number, 3)))
            self.play(obj.animate(run_time=0.01).move_to(3 * LEFT + (3.5 - i ** 2 * 0.0002) * UP))

        self.remove(numberLine,square,dot,y_label)
        self.play(table.animate().move_to(LEFT * 4.5))

        coord_xt = Axes(x_range=[0, 5, 0.5], y_range=[0, 160, 25], x_length=7, y_length=3,
                        axis_config={'tip_width': 0.2, "font_size": 24}).shift(RIGHT * 3 + UP * 2).add_coordinates()
        coord_vt = Axes(x_range=[0, 5, 0.5], y_range=[0, 50, 10], x_length=7, y_length=3,
                        axis_config={'tip_width': 0.2, "font_size": 24}).shift(RIGHT * 3 + DOWN * 2).add_coordinates()
        labels_xt = coord_xt.get_axis_labels(MathTex(r"y/\mbox{m}", font_size=24), MathTex(r"t/\mbox{s}", font_size=24))
        labels_vt = coord_vt.get_axis_labels(MathTex(r"y/\mbox{m}", font_size=24),
                                             MathTex(r"v/ m \cdot s^{-1}", font_size=24))
        self.play(AnimationGroup(Create(coord_xt), Create(coord_vt)))
        self.add(labels_xt, labels_vt)
        for i in range(10):
            self.add(Dot(data[i][0] * 1.4 * RIGHT + data[i][1] * 3 / 160 * UP).shift(LEFT * 0.5 + UP * 0.5)
                     , Dot(data[i][0] * 1.4 * RIGHT + data[i][2] * 3 / 50 * UP).shift(LEFT * 0.5 + DOWN * 3.5))
            self.wait(0.5)

        f_xt = lambda t: 5 * t ** 2
        f_vt = lambda t: 10 * t
        graph_xt = coord_xt.plot(f_xt, color=YELLOW)
        graph_vt = coord_vt.plot(f_vt, color=GREEN)
        self.play(AnimationGroup(Create(graph_xt), Create(graph_vt)))

        dot_xt = Dot().add_updater(lambda x: x.move_to(coord_xt.c2p(timer.get_value(), f_xt(timer.get_value()))))
        dot_vt = Dot().add_updater(lambda x: x.move_to(coord_vt.c2p(timer.get_value(), f_vt(timer.get_value()))))

        self.play(FadeIn(obj, numberLine, y_label))
        self.add(always_redraw(v_arrow), dot_xt, dot_vt)

        for i in range(200):
            timer.set_value(i * 0.025)
            if i % 20 == 0:
                cur_pos = Dot(3 * LEFT + (3.5 - i ** 2 * 0.0002) * UP)
                self.add(cur_pos)
            self.play(obj.animate(run_time=0.01).move_to(3 * LEFT + (3.5 - i ** 2 * 0.0002) * UP))

        self.play(FadeOut(coord_xt, coord_vt))

        coord_e = Axes(x_range=[0, 160, 50], y_range=[-160, 160, 50], x_length=7, y_length=6,
                       axis_config={'tip_width': 0.2, "font_size": 24, 'tip_height': 0.2}).shift(
            RIGHT * 3).add_coordinates()
        labels_e = coord_e.get_axis_labels(MathTex(r"y/\mbox{m}", font_size=24), MathTex(r"E/\mbox{J}", font_size=24))

        f_ek = lambda t: 5 * t ** 2
        f_ep = lambda t: -5 * t ** 2
        f_y = lambda t: 5 * t ** 2
        graph_ek = coord_e.plot(lambda x: x, color=ORANGE)
        graph_ep = coord_e.plot(lambda x: -x, color=BLUE)
        self.play(Create(coord_e))
        self.add(labels_e)

        def point_graph_e():
            dot_ek = Dot(coord_e.c2p(f_y(timer.get_value()), f_ek(timer.get_value())))
            dot_ep = Dot(coord_e.c2p(f_y(timer.get_value()), f_ep(timer.get_value())))
            arrow_ek = DashedLine(coord_e.c2p(f_y(timer.get_value()), 0), dot_ek.get_center(), color=ORANGE)
            arrow_ep = DashedLine(coord_e.c2p(f_y(timer.get_value()), 0), dot_ep.get_center(), color=BLUE)
            text_ek = MathTex(r"E_k").next_to(arrow_ek)
            text_ep = MathTex(r"E_p").next_to(arrow_ep)
            return VGroup(dot_ek, dot_ep, arrow_ek, arrow_ep, text_ek, text_ep)

        self.play(FadeIn(obj, numberLine, y_label))
        self.add(always_redraw(v_arrow), always_redraw(point_graph_e), graph_ek, graph_ep)

        for i in range(200):
            timer.set_value(i * 0.025)
            if i % 20 == 0:
                cur_pos = Dot(3 * LEFT + (3.5 - i ** 2 * 0.0002) * UP)
                self.add(cur_pos)
            self.play(obj.animate(run_time=0.01).move_to(3 * LEFT + (3.5 - i ** 2 * 0.0002) * UP))