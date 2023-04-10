from manim import *
import math
import random

class Spring():
    def __init__(self, obj1, obj2, length, k):
        self.start = obj1
        self.end = obj2
        self.length = length
        self.k = k
        self.line = Line()
        self.line.add_updater(lambda m: \
                                  m.put_start_and_end_on(
                                      obj1.get_center(),
                                      obj2.get_center())
                              )

    def get_force(self):
        pos1 = self.start.get_center()
        pos2 = self.end.get_center()
        v = pos2 - pos1
        dist = math.sqrt(v[0]**2+v[1]**2+v[2]**2)
        return normalize(v) * (self.length - dist) * self.k


class MultiSpring(Scene):
    def construct(self):
        def move_ball(ball, dt):
            force = DOWN * 20
            force += ball.spring.get_force()
            ball.velocity += force * dt
            ball.velocity *= 0.95
            ball.shift(ball.velocity * dt)

        balls = []
        fix_point = Dot().move_to(UP * 4)
        for i in range(4):
            ball = Circle(radius=0.3)
            ball.move_to((3 - i) * UP + random.random() * RIGHT)
            ball.set_fill(RED, opacity=1)

            start = fix_point if i == 0 else balls[i - 1]
            end = ball

            spring = Spring(start, end, 1, 40)
            ball.spring = spring
            ball.velocity = 0
            ball.add_updater(move_ball)
            self.add(spring.line)
            self.add(ball)

            balls.append(ball)

        self.wait(10)
        self.play(fix_point.animate().shift(RIGHT*3))
        #self.play(fix_point.shift, RIGHT * 3)
        self.wait(10)
        #self.play(fix_point.shift, LEFT * 6, run_time=2)
        #self.wait(15)