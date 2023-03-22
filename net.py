from turtle import Turtle
import random

class Net(Turtle):

    def __init__(self, screen_width, screen_height):
        super().__init__()
        self.color("white")
        self.screen_height = screen_height
        self.screen_width = screen_width
        self.hideturtle()
        self._draw_outbounds()
        self._draw_net()


    def _draw_outbounds(self):
        self.penup()
        self.setposition(x=self.screen_width / 2 * -1, y=self.screen_height / 2)
        self.pensize(10)
        self.pendown()
        #Move right
        self.goto(x=self.screen_width / 2, y=self.screen_height / 2)
        #Move down
        self.goto(x=self.screen_width / 2, y=self.screen_height / 2 * -1)
        #Move left
        self.goto(x=self.screen_width / 2 * -1, y=self.screen_height / 2 * -1)
        #Move up
        self.goto(x=self.screen_width / 2 * -1, y=self.screen_height / 2)

    def _draw_net(self):
        y_pos = self.screen_height / 2
        self.penup()
        self.setposition(x=0, y=y_pos - 5)
        self.pensize(1)
        semaphore = True
        self.pendown()
        self.right(90)
        while self.ycor() > (self.screen_height / 2 * -1):
            if semaphore:
                self.pendown()
            else:
                self.penup()

            self.forward(19)
            semaphore = not semaphore
