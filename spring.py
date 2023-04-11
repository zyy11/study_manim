import numpy as np
from manim import *
import math

class Object():
    def __init__(self):
        self.geo=Group(*[Circle(0.25),Dot()])
        self.velocity=np.array([0.0,0.0,0.0],dtype=np.float64)
        self.pos=np.array([0.0,0.0,0.0],dtype=np.float64)
    def get_center(self):
        return self.pos

class Spring():
    def __init__(self, obj1, obj2, reps):
        #self.submobjects=[Line(obj1.get_center(),obj2.get_center())
        p1=obj1.get_center()
        p2=obj2.get_center()
        line_array=[]
        line_array.append(Line(LEFT,LEFT+np.array([2/reps/4,0.5,0])))
        line_array.append(Line(LEFT + np.array([2 / reps / 4, 0.5, 0]), LEFT + np.array([2 / reps / 4 * 3, -0.5, 0])))
        for i in range(1,reps):
            line_array.append(Line(LEFT + np.array([2 / reps / 4 * (4 * i - 1), -0.5, 0]),
                                   LEFT + np.array([2 / reps / 4 * (4 * i + 1), 0.5, 0])))
            line_array.append(Line(LEFT + np.array([2 / reps / 4 * (4 * i + 1), 0.5, 0]),
                                   LEFT + np.array([2 / reps / 4 * (4 * i + 3), -0.5, 0])))
        line_array.append(Line(LEFT+np.array([2/reps/4*(4*reps-1),-0.5,0]),RIGHT))
        self.geo=Group(*line_array)
        #self.geo=Group([Line(np.array([-1.0,0.0,0.0]),np.array([1.0,0.0,0.0]))])
        self.geo.set_points([LEFT,RIGHT])
        self.geo.add_updater(lambda x:
                             x.put_start_and_end_on(p1,p2)
                             )


class SpringScene(Scene):
    def construct(self):
        Ground=Line(np.array([-3,-0.25,0],dtype=np.float64),np.array([3,-0.25,0],dtype=np.float64))
        self.add(Ground)
        obj1=Object()
        obj1.pos=np.array([-2.5,0,0],dtype=np.float64)
        obj1.geo.move_to(obj1.pos)
        obj2 = Object()
        obj2.pos = np.array([2.5, 0, 0],dtype=np.float64)
        obj2.geo.move_to(obj2.pos)
        spring=Spring(obj1,obj2,10)

        self.add(obj1.geo, obj2.geo,spring.geo)

        dt=0.01
        rec=[]
        for i in range(1,200):
            f1=np.array([1000.0*(-obj1.pos[0]+obj2.pos[0]-4),0.0,0.0],dtype=np.float64)
            f2=-f1
            obj1.pos+=obj1.velocity*dt+f1*dt**2
            obj1.velocity+=f1*dt
            obj2.pos+=obj2.velocity*dt+f2*dt**2
            obj2.velocity+=f2*dt
            #rec.append(f1)
            #self.wait(dt)
            self.play(AnimationGroup(*[
                obj1.geo.animate(run_time=dt).move_to(obj1.pos),
                obj2.geo.animate(run_time=dt).move_to(obj2.pos)
            ]))
        #print(rec)

