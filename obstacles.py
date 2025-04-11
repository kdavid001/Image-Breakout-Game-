import random
from turtle import Turtle
COLORS = ["red", "blue", "green", "yellow", "orange", "purple"]
pos = 20
class Obstacles(Turtle):
    def __init__(self):
        super().__init__()
        self.all_blocks = []

    def load(self):
        for row in range(4):
            y = 60 + row * 30
            for x in range(-300, 355, 110):  # From -200 to 210 with steps of 40
                block = Turtle("square")
                block.penup()
                block.shapesize(1, 5)
                block.color(random.choice(COLORS))
                block.goto(x, y)
                self.all_blocks.append(block)




