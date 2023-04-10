from manim import *
import math

class Object():
    def __init__(self,mass,ang):
        self.ang = ang
        self.last_ang = ang
        #self.pos = self.origin+np.array([dist*math.cos(ang),dist*math.sin(ang),0])
        self.geo=Group(*[Circle(0.25),Dot()])
        self.mass=mass


class Hang(Scene):
    def construct(self):
        fix_point = Dot().move_to(UP * 3)
        obj = Object(1,math.pi)
        line=Line().add_updater(lambda x:x.put_start_and_end_on(obj.geo.get_center(),fix_point.get_center()))
        self.add(obj.geo,line)
        dt=0.01
        for i in range(200):
            last_ang = obj.ang
            F = np.array([0, -50, 0])
            M=np.cross(F,(line.get_end()-line.get_start()))
            a = M[2] / obj.mass
            obj.ang = 2 * obj.ang - obj.last_ang + a * dt ** 2
            obj.last_ang = last_ang
            self.play(obj.geo.animate(run_time=dt).move_to(fix_point.get_center()+np.array([3*math.cos(obj.ang),3*math.sin(obj.ang),0])))

class TwoHang(Scene):
    def construct(self):
        fix_point = Dot().move_to(UP * 3)
        obj1 = Object(1,math.pi)
        obj2= Object(1,math.pi)
        line1=Line().add_updater(lambda x:x.put_start_and_end_on(obj1.geo.get_center(),fix_point.get_center()))
        line2=Line().add_updater(lambda x:x.put_start_and_end_on(obj1.geo.get_center(),obj2.geo.get_center()))
        self.add(obj1.geo,obj2.geo,line1,line2)
        dt=0.01
        for i in range(200):
            last_ang1 = obj1.ang
            last_ang2 = obj2.ang
            F = np.array([0, -50, 0])

            M1 = np.cross(F, (line1.get_end() - line1.get_start()))
            a1 = M1[2] / obj1.mass

            M2 = np.cross(F, (line2.get_end() - line2.get_start()))
            a2 = M2[2] / obj2.mass

            obj1.ang = 2 * obj1.ang - obj1.last_ang + a1 * dt ** 2
            obj1.last_pos = last_ang1

            obj2.ang = 2 * obj2.ang - obj2.last_ang + a2 * dt ** 2
            obj2.last_ang = last_ang2

            pos1=fix_point.get_center()+np.array([3*math.cos(obj1.ang),3*math.sin(obj1.ang),0])
            pos2=pos1+np.array([1*math.cos(obj2.ang),1*math.sin(obj2.ang),0])

            self.play(
                AnimationGroup(
                    obj1.geo.animate(run_time=dt).move_to(pos1),
                    obj2.geo.animate(run_time=dt).move_to(pos2)
                )
            )
