from turtle import Turtle
import random


class Block(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("green")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.penup()
        self.goto(position)

    def destroy(self):
        self.goto(1000, 1000)