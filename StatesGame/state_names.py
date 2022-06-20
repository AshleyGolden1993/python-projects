from turtle import Turtle
import pandas as pd


class StateName(Turtle):
    def __init__(self):
        super().__init__()
        self.pu()
        self.ht()

    def write_state(self, x, y, answer_state):
        self.goto(x, y)
        self.write(arg=f"{answer_state}")
