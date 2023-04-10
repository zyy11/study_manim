import numpy as np
from manim import *
import math

def spring_updater(spring,obj1,obj2):
    curr_start, curr_end = spring.get_start_and_end()
    curr_center=(curr_start+curr_end)/2
    curr_vect = curr_end - curr_start
    target_vect = obj2.get_center()-obj1.get_center()
    target_center=(obj2.get_center()+obj1.get_center())/2
    axis = (
        normalize(np.cross(curr_vect, target_vect))
        if np.linalg.norm(np.cross(curr_vect, target_vect)) != 0
        else OUT
    )
    spring.stretch(
        np.linalg.norm(target_vect)/np.linalg.norm(curr_vect),
        1,
        about_point=curr_center,
    )
    spring.rotate(
        angle_between_vectors(curr_vect, target_vect),
        about_point=curr_center,
        axis=axis,
    )
    spring.shift(target_center - curr_center)

class Spring():
    def __init__(self,l0,k,obj1,obj2):
        self.geo=Group(*[Line(obj1.get_center(),obj2.get_center())])
        self.geo.points=[obj1.get_center(),obj2.get_center()]
        self.k=k
        self.l0=l0
        self.geo.add_updater(lambda x:x.put_start_and_end_on(obj1.get_center(),obj2.get_center()))
        #self.geo.add_updater(lambda x:spring_updater(x,obj1,obj2))
    def get_force(self):
        vec=self.geo.get_start()-self.geo.get_end()
        l=np.linalg.norm(vec)
        return self.k*(l-self.l0)*vec/l

class Object():
    def __init__(self,mass,p0,v0):
        self.geo=Group(*[Circle(0.5),Dot()]).move_to(p0)
        self.mass=mass
        self.velocity=v0
        self.pos = p0
        self.last_pos = p0

class SpringVibrator(Scene):
    def construct(self):
        obj=Object(0.01,np.array([1,0,0],dtype=np.double),np.array([0,0,0],dtype=np.double))
        fix_point=Dot().move_to(UP*3)
        spring=Spring(3,10,fix_point,obj.geo)
        self.add(obj.geo,spring.geo)
        dt=0.01
        for i in range(200):
            last_pos=obj.pos
            f=spring.get_force()+np.array([0,-10,0])
            a=f/obj.mass
            obj.pos=2*obj.pos-obj.last_pos+a*dt**2
            #obj.velocity+=a*dt
            obj.last_pos=last_pos
            self.play(obj.geo.animate(run_time=dt).move_to(obj.pos))

