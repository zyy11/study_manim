from manim import *
import math

class FreeFall1(Scene):
    def construct(self):
        square = Square(0.5)
        square.set_fill(PINK, opacity=0.5)
        dot = Dot()
        obj = Group(*[square,dot])
        obj.move_to(3.5*UP+LEFT*3)
        numberLine=NumberLine(x_range=[0,156.25,25],length=7,rotation=-math.pi/2,include_ticks=True,include_tip=True,include_numbers=True,label_direction=LEFT,font_size=36).shift(LEFT*4)
        y_label = MathTex(r"y/\mbox{m}", font_size=36).move_to(LEFT * 4.5 + DOWN * 3.8)
        timer = ValueTracker(0)

        def v_arrow():
            arrow=Line(start=obj.get_center(),end=obj.get_center()+0.2 * timer.get_value()*DOWN,stroke_width=6).set_color(GOLD).create_tip()
            v_text=DecimalNumber(font_size=24).set_value(0.2*timer.get_value()).next_to(arrow.get_end())
            v_unit=Tex("m/s",font_size=24).next_to(v_text)
            return VGroup(arrow,v_text,v_unit)

        data=[]
        for i in range(10):
            data.append([0.5*i,1.25*i**2,5*i])
        table=DecimalTable(
            data,
            col_labels=[MathTex(r"t/\mbox{s}"), MathTex(r"y/\mbox{m}"), MathTex(r"v/ m \cdot s^{-1}")],
            h_buff=1,
            line_config={"stroke_width":1},
            arrange_in_grid_config={"col_widths":[2,2,2]}
        ).scale(0.6).shift(RIGHT*4)

        self.play(Create(square))
        self.add(obj)
        self.play(Create(numberLine))
        self.play(Create(y_label))
        self.add(always_redraw(v_arrow))
        self.play(AnimationGroup(Create(table.get_horizontal_lines()),Create(table.get_vertical_lines()),Create(table.get_col_labels())))
        #for i in range(200):
        #    timer.set_value(i*0.05)
        #    if i%20==0:
        #        cur_pos=Dot(3*LEFT+(3.5-i**2*0.0002)*UP)
        #        self.add(cur_pos)
        #    self.play(obj.animate(run_time=0.01).move_to(3*LEFT+(3.5-i**2*0.0002)*UP))
