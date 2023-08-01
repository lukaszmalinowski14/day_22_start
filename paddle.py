from turtle import Turtle, Screen


class Paddle(Turtle):
    def __init__(self, color, wid, len, x_pos, y_pos):
        self = Turtle()
        self.shape("square")
        self.color(color)
        self.shapesize(wid, len, None)
        self.penup()
        self.goto(x_pos, y_pos)
