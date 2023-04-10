import numpy as np
from manim import *
import math

class Circular(Scene):
    def construct(self):
        orbit=Circle(2)
        obj=Circle(0.25).move_to(RIGHT*2)
        horizontal=Line(LEFT*2.5+DOWN*3,RIGHT*2.5+DOWN*3)
        shadow=Circle(0.25).move_to(RIGHT*2+DOWN*3)
        dash=DashedLine()
        dash.add_updater(lambda x:x.put_start_and_end_on(obj.get_center(),shadow.get_center()))
        self.add(orbit, obj,horizontal,shadow,dash)
        dt=0.01
        for i in range(200):
            self.play(
                AnimationGroup(
                    obj.animate(run_time=dt).move_to(np.array([2*math.cos(dt*i*5),2*math.sin(dt*i*5),0])),
                    shadow.animate(run_time=dt).move_to(np.array([2*math.cos(dt*i*5),-3,0]))
                )
            )
