import numpy as np
from manim import *
import math

class Spring():
    def __init__(self,l0,k,obj1,obj2):
        self.start_obj = obj1
        self.end_obj = obj2
        self.k=k
        self.l0=l0
    def get_force(self):
        vec=self.end_obj.get_center()-self.start_obj.get_center()
        l=np.linalg.norm(vec)
        return -self.k*(l-self.l0)*vec/l

    def redraw_spring(self):
        # return Line(spring.start_obj.get_center(),spring.end_obj.get_center())
        group = []
        start = self.start_obj.get_center()
        end = self.end_obj.get_center()
        delta_x = (end - start) / 24
        dir_y = np.array([delta_x[1], -delta_x[0], 0])
        delta_y = dir_y / np.linalg.norm(dir_y) * 0.15
        group.append(Line(start, start + delta_x - delta_y))
        for i in range(11):
            group.append(Line(start + delta_x * (2 * i + 1) + delta_y * (i % 2 * 2 - 1),
                              start + delta_x * (2 * i + 3) + delta_y * (1 - i % 2 * 2)))
        group.append(Line(end - delta_x + delta_y, end))
        return VGroup(*group)

class Object():
    def __init__(self,mass,p0,v0):
        self.geo=Group(*[Circle(0.25),Dot()]).move_to(p0)
        self.mass=mass
        self.velocity=v0
        self.pos = p0
        self.last_pos = p0-v0*0.01

class TwoObjects(Scene):
    def construct(self):
        obj1 = Object(0.3, LEFT * 5, np.array([0,0,0],dtype=np.double))
        obj2 = Object(0.3, LEFT * 4, np.array([0,0,0],dtype=np.double))
        dot=Dot().add_updater(lambda x:x.move_to((obj1.pos*obj1.mass+obj2.pos*obj2.mass)/(obj1.mass+obj2.mass)))
        spring=Spring(3,10,obj1.geo,obj2.geo)
        draw_spring = always_redraw(spring.redraw_spring)
        trail=Group(Line(LEFT*5.25+UP*0.5,LEFT*5.25+DOWN*0.25),Line(LEFT*5.25+DOWN*0.25,RIGHT*6+DOWN*0.25))
        self.add(obj1.geo,obj2.geo,draw_spring,trail,dot)
        dt=0.01
        for i in range(200):
            if i%20==1:
                self.add(Dot(dot.get_center()))
            last_pos1 = obj1.pos
            last_pos2 = obj2.pos

            f = spring.get_force()
            a1 = -f / obj1.mass

            if a1[0]<0 and obj1.pos[0]<=-5:
                a1=np.array([0,0,0],dtype=np.double)

            a2 = f / obj2.mass

            obj1.pos = 2 * obj1.pos - obj1.last_pos + a1 * dt ** 2
            obj2.pos = 2 * obj2.pos - obj2.last_pos + a2 * dt ** 2

            obj1.last_pos = last_pos1
            obj2.last_pos = last_pos2

            self.play(AnimationGroup(
                    obj1.geo.animate(run_time=dt).move_to(obj1.pos),
                    obj2.geo.animate(run_time=dt).move_to(obj2.pos)
                )
            )
