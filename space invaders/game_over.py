from turtle import Turtle


class Gameover(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.goto(0, 0)
        self.penup()
        self.content = "Game over"
        self.wincontent = "You won"
        
    def show(self):
        self.write(self.content, align="center", font=("Arial", 24, "normal"))
    
    def win(self):
        self.write(self.content, align="center", font=("Arial", 24, "normal"))
        self.goto(self.xcor(), self.ycor() - 30)
        self.write(self.wincontent, align="center", font=("Arial", 24, "normal"))
