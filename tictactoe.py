import turtle as t
import numpy as np
import random

board = np.zeros((3, 3), dtype=int)
cor = {
    1: (-50, 50), 2: (0, 50), 3: (50, 50), 
    4: (-50, 0), 5: (0, 0), 6: (50, 0), 
    7: (-50, -50), 8: (0, -50), 9: (50, -50)
}

def selection():
    while True:
        player = input("Do you want to play with another person (p) or against a computer with difficulty (1 = easy, 2 = hard, 3 = impossible)? ").lower()
        if player in {"p", "1", "2", "3"}:
            return player
        else:
            print("Invalid selection. Please choose 'p', '1', '2', or '3'.")
            selection()

def cross(x, y):
    t.penup()
    t.goto(x - 25, y + 25)
    t.pendown()
    t.setheading(-45)
    t.forward(70)
    t.penup()
    t.goto(x + 25, y + 25)
    t.pendown()
    t.setheading(-135)
    t.forward(70)
    t.penup()

def circle(x, y):
    t.penup()
    t.goto(x - 17, y + 18)
    t.pendown()
    t.circle(25)
    t.penup()

def draw_grid():
    t.speed("fastest")
    t.penup()
    t.goto(-75, 75)
    t.pendown()
    
    for _ in range(4):
        t.forward(150)
        t.right(90)

    for i in range(1, 3):
        t.penup()
        t.goto(-75, 75 - 50 * i)
        t.pendown()
        t.forward(150)

    t.right(90)

    for i in range(1, 3):
        t.penup()
        t.goto(-75 + 50 * i, 75)
        t.pendown()
        t.forward(150)

    t.hideturtle()

def check_win(player):
    for i in range(3):
        if all(board[i, :] == player) or all(board[:, i] == player):
            return True
    if all(board.diagonal() == player) or all(np.fliplr(board).diagonal() == player):
        return True
    return False

def check_draw():
    return np.all(board != 0)

def two():
    game = True
    i = 0
    while game:
        try:
            if i % 2 == 0:
                value = int(input("Player X: Choose a number between 1-9: "))
            else:
                value = int(input("Player O: Choose a number between 1-9: "))
        except ValueError:
            print("Invalid input. Please choose a number between 1 and 9.")
            continue

        if value not in cor:
            print("Invalid input. Please choose a number between 1 and 9.")
            continue

        row, col = (value - 1) // 3, (value - 1) % 3
        if board[row, col] != 0:
            print("Position already taken. Choose another number.")
            continue

        x, y = cor[value]
        if i % 2 == 0:
            cross(x, y)
            board[row, col] = 1
            if check_win(1):
                print("Player X wins!")
                game = False
        else:
            circle(x, y)
            board[row, col] = 2
            if check_win(2):
                print("Player O wins!")
                game = False
        
        if check_draw():
            print("The game ends in a draw!")
            game = False

        i += 1

def comp(level):
    game = True
    while game:
        try:
            value = int(input("Player X: Choose a number between 1-9: "))
        except ValueError:
            print("Invalid input. Please choose a number between 1 and 9.")
            continue

        if value not in cor:
            print("Invalid input. Please choose a number between 1 and 9.")
            continue

        row, col = (value - 1) // 3, (value - 1) % 3
        if board[row, col] != 0:
            print("Position already taken. Choose another number.")
            continue

        x, y = cor[value]
        cross(x, y)
        board[row, col] = 1
        if check_win(1):
            print("Player X wins!")
            game = False
            break

        if check_draw():
            print("The game ends in a draw!")
            game = False
            break

        flat_board = board.flatten()
        value = random.choice(np.where(flat_board == 0)[0]) + 1
        row, col = (value - 1) // 3, (value - 1) % 3
        x, y = cor[value]
        circle(x, y)
        board[row, col] = 2

        if check_win(2):
            print("Player O wins!")
            game = False
            break

        if check_draw():
            print("The game ends in a draw!")
            game = False
            break

draw_grid()

zs = selection()

if zs == "p":
    two()
elif zs == "1":
    comp(1)
elif zs == "2":
    comp(2)
else:
    comp(3)

t.done()