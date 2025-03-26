import random
from turtle import Turtle

COLORS = ['red', 'orange', 'yellow', 'green', 'blue', 'violet']
pos = 20
class Obstacles(Turtle):
    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-250, 250)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)


def load(self):
        for _ in range(8):
            self.penup()
            self.pendown()
            self.shape("square")  # Set turtle shape
            self.shapesize(1, 6)
            self.color(random.choice(["red", "blue", "green", "orange", "purple"]))  # Random color
            self.new_x = self.xcor() + 50
            self.setpos(self.new_x, self.ycor())


