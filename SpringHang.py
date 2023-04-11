import numpy as np
from manim import *
import math

class Spring():
    def __init__(self,l0,k,obj1,obj2):
        self.k=k
        self.l0=l0
        self.start_obj=obj1
        self.end_obj=obj2
    def get_force(self):
        vec=self.end_obj.get_center()-self.start_obj.get_center()
        l=np.linalg.norm(vec)
        return -self.k*(l-self.l0)*vec/l

    def redraw_spring(self):
        group = []
        start = self.start_obj.get_center()
        end = self.end_obj.get_center()
        delta_x = (end - start) / 16
        dir_y = np.array([delta_x[1], -delta_x[0], 0])
        delta_y = dir_y / np.linalg.norm(dir_y) * 0.1
        group.append(Line(start, start + delta_x - delta_y))
        for i in range(7):
            group.append(Line(start + delta_x * (2 * i + 1) + delta_y * (i % 2 * 2 - 1),
                              start + delta_x * (2 * i + 3) + delta_y * (1 - i % 2 * 2)))
        group.append(Line(end - delta_x + delta_y, end))
        return VGroup(*group)

class Object():
    def __init__(self,mass,p0,v0):
        self.geo=Group(*[Circle(0.5),Dot()]).move_to(p0)
        self.mass=mass
        self.velocity=v0
        self.pos = p0
        self.last_pos = p0

class SpringVibrator(Scene):
    def construct(self):
        obj=Object(0.01,ORIGIN,ORIGIN)
        fix_point=Dot().move_to(UP*3)
        ceiling=Line(UP*3+LEFT*0.5,UP*3+RIGHT*0.5)
        spring=Spring(3,10,fix_point,obj.geo)
        draw_spring=always_redraw(spring.redraw_spring)
        self.add(obj.geo, draw_spring,ceiling)
        dt=0.01

        for i in range(200):
            last_pos=obj.pos
            f=spring.get_force()+np.array([0,-10,0])
            a=f/obj.mass
            obj.pos=2*obj.pos-obj.last_pos+a*dt**2
            obj.last_pos=last_pos
            self.play(obj.geo.animate(run_time=dt).move_to(obj.pos))

