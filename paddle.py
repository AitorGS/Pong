from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, screen_width, screen_height, paddle_type, height, width):
        super().__init__()
        self.shape("square")
        self.size = 5
        self.height = height
        self.width = width
        self.shapesize(self.size, height / 20, width / 20)
        self.color("white")
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.paddle_type = paddle_type
        self.penup()
        modifier = 1
        if paddle_type == "LOCAL":
            modifier = -1
        self.setposition(x=screen_width / 2 * modifier + (20 * modifier * -1), y=0)

        if paddle_type == "AWAY":
            self.direction = "NORTH"

    def can_move_up(self):
        return self.ycor() + 60 <= self.screen_height / 2 - 10

    def can_move_down(self):
        return self.ycor() - 80 >= self.screen_height / 2 * -1 - 10

    def move_up(self):
        if self.can_move_up():
            self.sety(self.ycor() + 20)

    def move_down(self):
        if self.can_move_down():
            self.sety(self.ycor() - 20)

    def move_automatically(self):
        if self.direction == "NORTH":
            if self.can_move_up():
                self.move_up()
            else:
                self.direction = "SOUTH"

        else:
            if self.can_move_down():
                self.move_down()
            else:
                self.direction = "NORTH"

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

    def get_paddle_type(self):
        return self.paddle_type
