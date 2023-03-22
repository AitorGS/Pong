from turtle import Screen
from net import Net
from score import Score
from paddle import Paddle
from ball import Ball
import time

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_COLOR = "black"

my_screen = Screen()
my_screen.title("Pong")
my_screen.tracer(0)
my_screen.bgcolor(SCREEN_COLOR)
my_screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)

#Net(SCREEN_WIDTH, SCREEN_HEIGHT)
score = Score()

local_paddle = Paddle(SCREEN_WIDTH, SCREEN_HEIGHT, "LOCAL", 10, 100)
away_paddle = Paddle(SCREEN_WIDTH, SCREEN_HEIGHT, "AWAY", 10 , 100)

ball = Ball(SCREEN_WIDTH, SCREEN_HEIGHT)

my_screen.onkeypress(local_paddle.move_up, "Up")
my_screen.onkeypress(local_paddle.move_down, "Down")

my_screen.listen()
game_is_on = True

away_paddle.move_up()
away_paddle.move_up()
away_paddle.move_up()
while game_is_on:

    time.sleep(0.1)
    away_paddle.move_automatically()
    ball.move_ball()

    if ball.is_collision_with_wall(SCREEN_HEIGHT / 2):
        ball.bounce_ball()
    elif ball.is_collision_with_paddle(local_paddle) or ball.is_collision_with_paddle(away_paddle):
        ball.expel_ball()

    scored_paddle = ball.who_scored(local_paddle, away_paddle)
    if scored_paddle is not None:
        if scored_paddle.get_paddle_type() == "AWAY":
            score.away_goal()
        else:
            score.local_goal()
        ball.restart_ball()

    my_screen.update()



my_screen.exitonclick()