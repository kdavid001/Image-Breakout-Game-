from pad import Paddle
from turtle import *
from ball import Ball
from scoresheet import Scores
from pwg import Gameover
from obstacles import Obstacles

paddle = Paddle()
ball = Ball()
scores = Scores()
highscore = str(scores.highscore)
obstacles = Obstacles()

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


game_start = True
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
