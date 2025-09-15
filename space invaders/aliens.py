from turtle import Turtle
import random

pos = random.randint(70, 300)/100
class Aliens(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("circle")
        self.color("green")
        #self.x_move = 0.8
        self.x_move = pos
        self.shapesize(stretch_wid=0.8, stretch_len=1.5)
        self.penup()
        self.goto(position)  # Position is passed when the block is created

    def move(self):
        new_x = self.xcor() + self.x_move
        self.goto(new_x, self.ycor())

    def change(self):
        self.x_move *=-1

    def destroy(self):
        self.goto(1000, 1000)  # Move the block off-screen when hit
        self.hideturtle()  # Hide the block