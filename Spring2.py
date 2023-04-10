import numpy as np
from manim import *
import math

class Spring():
    def __init__(self,l0,k,obj1,obj2):
        self.geo=Group(*[Line(obj1.get_center(),obj2.get_center())])
        self.geo.points=[obj1.get_center(),obj2.get_center()]
        self.k=k
        self.l0=l0
        self.geo.add_updater(lambda x:x.put_start_and_end_on(obj1.get_center(),obj2.get_center()))
    def get_force(self):
        vec=self.geo.get_start()-self.geo.get_end()
        l=np.linalg.norm(vec)
        return self.k*(l-self.l0)*vec/l

class Object():
    def __init__(self,mass,p0,v0):
        self.geo=Group(*[Circle(0.25),Dot()]).move_to(p0)
        self.mass=mass
        self.velocity=v0
        self.pos = p0
        self.last_pos = p0

class TwoObjects(Scene):
    def construct(self):
        obj1 = Object(0.5, LEFT * 5, np.array([0,0,0],dtype=np.double))
        obj2 = Object(0.1, LEFT * 4, np.array([0,0,0],dtype=np.double))
        dot=Dot().add_updater(lambda x:x.move_to((obj1.pos*obj1.mass+obj2.pos*obj2.mass)/(obj1.mass+obj2.mass)))
        spring=Spring(3,10,obj1.geo,obj2.geo)
        trail=Group(Line(LEFT*5.25+UP*0.5,LEFT*5.25+DOWN*0.25),Line(LEFT*5.25+DOWN*0.25,RIGHT*6+DOWN*0.25))
        self.add(obj1.geo,obj2.geo,spring.geo,trail,dot)
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
