from turtle import Turtle

class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()

        self.shape('square')
        self.shapesize(1, 10)
        self.setpos(0,  -250)

    def move_up(self):
        self.new_x = self.xcor() + 35
        self.goto(self.new_x, self.ycor())

    def move_down(self):
        self.new_x = self.xcor() - 35
        self.goto(self.new_x, self.ycor())



