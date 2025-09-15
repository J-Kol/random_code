from turtle import Turtle
import time


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.shapesize(stretch_wid=0.4, stretch_len=0.4)
        self.penup()
        self.x_move = 0.0
        self.y_move = 0.0
        self.move_speed = 0.00
        self.hideturtle()

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def reset_position(self):
        pass

    def start(self, shooter):
        self.showturtle() 
        self.setposition(shooter.xcor(), -200)
        self.x_move = 0.0
        self.y_move = 0.8
        self.move_speed = 0.1

    def destroy(self):
        self.hideturtle()
        self.goto(1000, -10000)
