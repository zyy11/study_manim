from manim import *
import math
class Slope(Scene):
    def construct(self):
        Slope=Group(*[
            Line([-3,math.sqrt(3),0],[3,-math.sqrt(3),0]),
            Line([3,-math.sqrt(3),0],[9,-math.sqrt(3),0]),
            DashedLine([1,-math.sqrt(3),0],[3,-math.sqrt(3),0]),
            Arc(1,math.pi*5/6,math.pi/6,arc_center=[3,-math.sqrt(3),0]),
            Text("30°",font_size=24).move_to([1.5,0.3-math.sqrt(3),0]),
        ])
        Slope.shift([-0.125-3,-0.125*math.sqrt(3),0])
        self.add(Slope)

        circle = Circle(0.25)
        circle.set_fill(PINK, opacity=0.5)
        dot = Dot()
        obj = Group(*[circle, dot])
        obj.move_to(np.array([-2.5-3, math.sqrt(3)/3*2.5, 0]))
        self.add(obj)

        steps1=[[] for _ in range(200)]
        steps2=[[] for _ in range(120)]

        for i in range(200):
            steps1[i]=[-5.5+i**2*math.sqrt(3)/2*0.00015877,math.sqrt(3)/3*2.5-i**2/2*0.00015877,0]
        for i in range(120):
            steps2[i]=[0.063508*i,-math.sqrt(3),0]
        steps=steps1+steps2
        for i in range(320):
            if i%20==0:
                self.add(Dot(steps[i]))
            self.play(obj.animate(run_time=0.01).move_to(steps[i]))

