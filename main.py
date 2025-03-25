from pad import Paddle
from turtle import *
from ball import Ball

paddle = Paddle()
ball = Ball()

screen = Screen()

screen.listen()
screen.tracer(0)
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Image Breakout Game")

screen.onkey(key='Right', fun=paddle.move_up)
screen.onkey(key='Left', fun=paddle.move_down)

game_start = True
while game_start:
    screen.update()
    ball.move()

    if ball.ycor() > 280:
        ball.bounce_y()

    elif ball.ycor() < -280:
        ball.reset_ball()

    if ball.xcor() > 375 or ball.xcor() < -375:
        ball.bounce_x()

    if (ball.distance(paddle)) < 65 and ball.ycor() < -245:
        ball.bounce_paddle()




screen.exitonclick()
