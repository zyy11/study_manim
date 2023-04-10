from manim import *

class Object():
    def __init__(self,mass,p0,v0):
        self.geo = Group(*[Circle(0.25),Dot()]).move_to(p0)
        self.mass = mass
        self.velocity = v0
        self.pos = p0
        self.last_pos = p0-v0*0.01

class HorizontalThrow(Scene):
    def construct(self):
        obj = Object(0.1, LEFT * 5 + UP * 2, RIGHT*5)
        self.add(obj.geo)
        dt=0.01
        for i in range(200):
            if i % 20 == 0:
                self.add(Dot(obj.geo.get_center()))
            last_pos = obj.pos
            f = np.array([0, -1, 0])
            a = f / obj.mass
            obj.pos = 2 * obj.pos - obj.last_pos + a * dt ** 2
            # obj.velocity+=a*dt
            obj.last_pos = last_pos
            self.play(obj.geo.animate(run_time=dt).move_to(obj.pos))

class HorizontalThrowWithFloor(Scene):
    def construct(self):
        floor=Line(LEFT*5+DOWN*2,RIGHT*5+DOWN*2)
        obj = Object(0.1, LEFT * 5 + UP * 2, RIGHT*5)
        self.add(obj.geo,floor)
        dt=0.01
        e=0.5
        for i in range(200):
            if i % 20 == 0:
                self.add(Dot(obj.geo.get_center()))
            last_pos = obj.pos
            f = np.array([0, -1, 0])
            a = f / obj.mass
            obj.pos = 2 * obj.pos - obj.last_pos + a * dt ** 2
            # obj.velocity+=a*dt
            obj.last_pos = last_pos
            if obj.pos[1]<-2:
                obj.pos[1]=-obj.pos[1]-4
                obj.last_pos[1]=-obj.last_pos[1]-4
                obj.last_pos=(1-e)*obj.pos+e*obj.last_pos
            self.play(obj.geo.animate(run_time=dt).move_to(obj.pos))