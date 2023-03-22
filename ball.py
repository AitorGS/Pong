from turtle import Turtle
import random


class Ball(Turtle):
    def __init__(self, screen_width, screen_height):
        super().__init__()
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.move_x = random.choice([10, -10]);
        self.move_y = random.choice([10, -10]);
        self.color("white")
        self.shape("circle")
        self.ball_speed = 10
        self.penup()

    def restart_ball(self):
        self.increase_ball_speed()
        self.setposition(0, 0)
        self.expel_ball()

    def move_ball(self):
        self.goto(x=self.xcor() + self.move_x, y=self.ycor() + self.move_y)

    def bounce_ball(self):
        self.move_y *= -1

    def expel_ball(self):
        self.move_x *= -1

    def is_collision_with_wall(self, height):
        if abs(self.ycor()) + 20 >= height:
            return True
        return False

    def is_collision_with_paddle(self, paddle):
        #if we are hitting the paddle in the next move and we are close to its ends it's true
        #but we need to control that we have not overpassed the paddle position and hence the
        #second condition
        if abs(self.xcor()) + 20 >= abs(paddle.xcor()) and self.distance(paddle) < 50\
                and abs(self.xcor()) - abs(paddle.xcor()) < 10:
            return True
        return False

    def who_scored(self, local_paddle, away_paddle):
        if self.xcor() >= away_paddle.xcor() + 10: #and self.distance(away_paddle) > away_paddle.get_width():
            print(f"Goal with ball at {self.position()} and away paddel at {away_paddle.position()} and distance of"
                  f" {self.distance(away_paddle)}")
            return local_paddle

        if self.xcor() <= local_paddle.xcor() - 10: #and self.distance(local_paddle) > local_paddle.get_width():
            print(
                f"Goal with ball at {self.position()} and away paddel at {local_paddle.position()} and distance of"
                f" {self.distance(local_paddle)}")
            return away_paddle


        return None

    def increase_ball_speed(self):
        self.ball_speed += 1