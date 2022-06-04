from turtle import Turtle
# Create paddles (class)
# Move paddles (method in class)
STARTING_POSITIONS = [(-280, 0), (280, 0)]


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.pu()
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.setpos(position)

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
