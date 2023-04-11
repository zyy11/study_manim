from manim import *
import math

class FreeFall(Scene):
    def construct(self):
        square = Square(0.5)
        square.set_fill(PINK, opacity=0.5)
        dot = Dot()
        obj = Group(*[square,dot])
        obj.move_to(np.array([0, 3, 0]))
        #numberLine=NumberLine(x_range=[0,10,1],length=6,rotation=-math.pi/2,include_ticks=True,include_tip=True,include_numbers=True)
        self.play(Create(square))
        self.add(obj)
        steps=[[] for _ in range(200)]
        for i in range(200):
            steps[i]=[0,3-i**2*0.00015,0]
        for i in range(200):
            if i%20==0:
                self.add(Dot(steps[i]))
            self.play(obj.animate(run_time=0.01).move_to(steps[i]))

        #self.add(numberLine)
        #obj=Group([square,dot])
        #obj.move_to(np.array([-2,2,0]))
        #self.play(Create(obj))

class Ball(Circle):
    velocity=0

class FreeFall2(Scene):
    def construct(self):
        def move_obj(obj, dt):
            force = DOWN
            obj.velocity += force * dt
            obj.velocity *= 0.95
            obj.shift(obj.velocity * dt)

        #square = Square(0.5)
        #square.set_fill(PINK, opacity=0.5)
        #dot = Dot()
        #obj = Group(*[square, dot])

        obj = Ball(radius=0.3)
        obj.move_to(np.array([0, 3, 0]))
        obj.add_updater(move_obj)
        self.add(obj)
        self.wait(10)