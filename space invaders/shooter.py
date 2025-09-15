from turtle import Turtle

class Shooter(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("triangle")
        self.color("green")
        self.shapesize(3, 3, 3)
        self.setheading(90)
        self.penup()
        self.goto(position)

    def go_r(self):
        if self.xcor() < 360:
            new_x = self.xcor() + 20
            self.goto(new_x, self.ycor())

    def go_l(self):
        if self.xcor() > -360:
            new_x = self.xcor() - 20
            self.goto(new_x, self.ycor())