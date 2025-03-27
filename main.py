import turtle

from pad import Paddle
from turtle import *
from ball import Ball
from scoresheet import Scores
from pwg import Gameover
# from obstacles import Obstacles
import random

paddle = Paddle()
ball = Ball()
scores = Scores()
highscore = str(scores.highscore)
# obstacles = Obstacles()
# obstacles.load()
COLORS = ['red', 'orange', 'yellow', 'green', 'blue', 'violet']
all_cars = []

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
    ball.reset_ball()
    scores.reset_score()
    game_start = True

max_x1 = -375
max_x2 = 375

def obstacles():
    obstacle_list = []  # Store created obstacles
    color = random.choice(COLORS)
    x_positions = list(range(-375, 376, 50))  # Generate evenly spaced positions

    for x_pos in x_positions:
        if random.randint(1, 1) == 1:  # Adjust probability to control obstacle density
            new_obstacle = turtle.Turtle("square")
            new_obstacle.shapesize(stretch_wid=1, stretch_len=2)
            new_obstacle.penup()
            new_obstacle.color(color )
            new_obstacle.setpos(x_pos, 50)
            obstacle_list.append(new_obstacle)  # Store the obstacle

    return obstacle_list


# Generate obstacles once
all_obstacles = obstacles()
game_start = True
obstacles()
while game_start:
    screen.update()
    ball.move()


    # for Top Wall
    if ball.ycor() > 280:
        ball.bounce_y()

    # for bottom wall -> reset game.
    elif ball.ycor() < -280:
        user_pick = screen.textinput("TRY AGAIN.", "would you like to try again? y/n").lower()
        if user_pick == "y":
            reset_game()
        if user_pick == "n":
            game_is_on = False
            pwg = Gameover()

    # for vertical (side) walls
    if ball.xcor() > 375 or ball.xcor() < -375:
        ball.bounce_x()

    # if the ball touches the white paddle bounce
    if (ball.distance(paddle)) < 65 and ball.ycor() < -245:
        scores.paddle_point()
        ball.bounce_paddle()

    # for the scoring -> if the ball hits some of the blocks.

screen.exitonclick()
