import random
from turtle import Turtle

COLORS = ['red', 'orange', 'yellow', 'green', 'blue', 'violet']
pos = 20
class Obstacles(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('square')
        self.shapesize(1, 5)
        self.setpos(0, 50)



    def placements(self):
        for _ in range(8):
            self.penup()
            self.pendown()
            self.shape("square")  # Set turtle shape
            self.shapesize(1, 5)
            self.color(random.choice(["red", "blue", "green", "orange", "purple"]))  # Random color
            self.new_y = self.ycor() + 50
            self.goto(0, self.new_y)


