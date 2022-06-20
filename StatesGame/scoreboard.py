from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.pu()
        self.ht()
        self.score = 0
        self.goto(0, 250)
        self.write_score()

    def update_score(self):
        self.score += 1

    def write_score(self):
        self.clear()
        self.write(f"{self.score}/50 States Correct", align="center", font=("Courier", 24, "normal"))
