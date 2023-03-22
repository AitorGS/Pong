from turtle import Turtle

FONT = ("Courier", 70, "normal")
LOCAL_POSITION = (-100, 300 - 100)
AWAY_POSITION = (50, 300 - 100)


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.local_score = 0
        self.away_score = 0
        self.hideturtle()
        self.penup()
        self.color("white")
        self.paint_scores()

    def paint_scores(self):
        self.clear()
        self.goto(LOCAL_POSITION)
        self.write(self.local_score, font=FONT)
        self.goto(AWAY_POSITION)
        self.write(self.away_score, font=FONT)

    def local_goal(self):
        self.local_score += 1
        self.paint_scores()

    def away_goal(self):
        self.away_score += 1
        self.paint_scores()