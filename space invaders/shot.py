from turtle import Turtle

class Shot(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=1.7, stretch_len=0.7)  # Adjust shape as needed
        self.penup()
        self.x_move = 0.0
        self.y_move = 0.0
        self.hideturtle()

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def shoot(self, position):
        self.showturtle()
        self.setposition(position[0], position[1])
        self.x_move = 0.0
        self.y_move = -0.8

    def reset_position(self):
        self.hideturtle()
        self.goto(1000, 1000)

    def destroy(self):
        self.hideturtle()
        self.goto(1000, 1000)