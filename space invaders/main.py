from turtle import Screen
from shooter import Shooter
from ball import Ball
from block import Block
from aliens import Aliens
from shot import Shot
from game_over import Gameover
import time
import random

time_shot = time.time()

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Space invaders")
screen.tracer(0)

shooter = Shooter((0, -250))
balls = []
shots = []

blocks = []
aliens = []
x_start = -380
y_start = 250
shot_time = random.randint(160, 200)/100
alien_time = random.randint(30, 50)/1000000

for row in range(3):
    for col in range(6):
        position = (x_start + col * 40, y_start - row * 20)
        alien = Aliens(position)
        aliens.append(alien)

pos = 0
for i in range(5):
    for row in range(6):
        for col in range(8):
            position = (x_start + pos + col * 20, 150 - row * 20)
            block = Block(position)
            blocks.append(block)
    pos += 200

screen.listen()
screen.onkey(shooter.go_r, "Right")
screen.onkey(shooter.go_l, "Left")

def add_ball():
    global time_shot
    current_time = time.time()
    if current_time - time_shot >= shot_time:
        new_ball = Ball()
        new_ball.start(shooter)
        balls.append(new_ball)
        time_shot = current_time

def shoot_back():
    for alien in aliens: 
        if random.random() < alien_time:
            new_shot = Shot()
            new_shot.shoot(alien.position())
            shots.append(new_shot)

screen.onkey(add_ball, "space")

game_is_on = True
while game_is_on:
    screen.update()

    for alien in aliens:
        alien.move()
        shoot_back()

    if alien.xcor() > 370 or alien.xcor() < -190:
        for alien in aliens:
            alien.change()

    for ball in balls:
        ball.move()

        for block in blocks:
            if ball.distance(block) < 20:
                block.destroy()
                blocks.remove(block)
                ball.destroy()
                balls.remove(ball)
                break

        for alien in aliens:
            if ball.distance(alien) < 20:
                alien.destroy()
                aliens.remove(alien)
                ball.destroy()
                balls.remove(ball)
                if len(aliens) == 0:
                    game_is_on = False
                    game_over = Gameover()
                    game_over.win()
                break

    for shot in shots:
        shot.move()

        shot_pos = shot.pos()
        shooter_pos = shooter.pos()

        #print(f"Shot Position: {shot.position()}, Shooter Position: {shooter.position()}, Is Visible: {shot.isvisible()}")

        for block  in blocks:
            if shot.distance(block) < 20:
                block.destroy()
                blocks.remove(block)
                shot.destroy()
                shots.remove(shot)
                break

        if shot.isvisible() and shot.distance(shooter.pos()) < 45:
            game_is_on = False
            game_over = Gameover()
            game_over.show()

screen.exitonclick()