import turtle

from pad import Paddle
from turtle import *
from ball import Ball
from scoresheet import Scores
from pwg import Gameover
from obstacles import Obstacles
import random

paddle = Paddle()
ball = Ball()
scores = Scores()
highscore = str(scores.highscore)
obstacles = Obstacles()
# obstacles.load()

screen = Screen()
screen.listen()
screen.tracer(0)
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Image Breakout Game")

screen.onkey(key='Right', fun=paddle.move_up)
screen.onkey(key='Left', fun=paddle.move_down)


def reset_game():
    global game_start
    scores.reset_score()
    ball.reset_ball()
    game_start = True


max_x1 = -375
max_x2 = 375

# generate the obstacles once
obstacles.load()


def end_reset_game():
    user_pick = screen.textinput("TRY AGAIN.", "would you like to try again? y/n").lower()
    if user_pick == "y":
        reset_game()
    if user_pick == "n":
        scores.reset_score()
        game_is_on = False
        pwg = Gameover()


game_start = True
while game_start:
    screen.update()

    ball.move()

    # for Top Wall
    if ball.ycor() > 280:
        ball.bounce_y()

    # for bottom wall -> reset game.
    elif ball.ycor() < -280:
        end_reset_game()

    # for vertical (side) walls
    if ball.xcor() > 375 or ball.xcor() < -375:
        ball.bounce_x()

    # if the ball touches the white paddle bounce
    if (ball.distance(paddle)) < 65 and ball.ycor() < -245:
        ball.bounce_paddle()

    for block in obstacles.all_blocks:
        if ball.distance(block) < 40:  # adjust value as needed for size
            block.hideturtle()  # visually remove it
            ball.bounce_y()
            # for the scoring -> if the ball hits some of the blocks.
            scores.paddle_point()
            obstacles.all_blocks.remove(block)  # remove from list
            break  # avoid changing list size during iteration
    if len(obstacles.all_blocks) == 0:
        end_reset_game()

screen.exitonclick()
