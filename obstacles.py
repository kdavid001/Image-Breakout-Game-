from random import randint, random
from turtle import Turtle

COLORS = ['red', 'orange', 'yellow', 'green', 'blue', 'violet']
class Obstacles(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("blue")
        self.shape('square')
        self.shapesize(1, 10)
        self.setpos(0, 50)