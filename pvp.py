# modules
import pygame, sys
import numpy as np
import random

#initializes pygame
pygame.init()

# constants
width = 300
height = 300
line_width = 15
win_line_width = 15
b_rows = 3
b_cols = 3
square_size = 100
circle_radius = 30
circle_width = 10
cross_width = 10
space = 25
# colors
bg_color = (23, 145, 135)
line_color = (58, 188, 177)
circle_color = (255, 255, 255)
cross_color = (0, 0, 0)

# screen
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('TIC TAC TOE')
screen.fill(bg_color)

# console board
board = np.zeros((b_rows, b_cols))


# functions
def draw_lines():
    # 1 hl
    pygame.draw.line(screen, line_color, (0, square_size),
                     (width, square_size), line_width)
    # 2 hl
    pygame.draw.line(screen, line_color, (0, 2 * square_size),
                     (width, 2 * square_size), line_width)

    # 1 vl
    pygame.draw.line(screen, line_color, (square_size, 0),
                     (square_size, height), line_width)
    # 2 vl
    pygame.draw.line(screen, line_color, (2 * square_size, 0),
                     (2 * square_size, height), line_width)

#shapes inside the tictactoe
def draw_figures():
    for row in range(b_rows):
        for col in range(b_cols):
            if board[row][col] == 1:
                pygame.draw.circle(screen, circle_color,
                                   (int(col * square_size + square_size // 2),
                                    int(row * square_size + square_size // 2)),
                                   circle_radius, circle_width)
            elif board[row][col] == 2:
                pygame.draw.line(screen, cross_color,
                                 (col * square_size + space,
                                  row * square_size + square_size - space),
                                 (col * square_size + square_size - space,
                                  row * square_size + space), cross_width)
                pygame.draw.line(
                    screen, cross_color,
                    (col * square_size + space, row * square_size + space),
                    (col * square_size + square_size - space,
                     row * square_size + square_size - space), cross_width)


def mark_square(row, col, player):
    board[row][col] = player


def available_square(row, col):
    return board[row][col] == 0


def is_board_full():
    for row in range(b_rows):
        for col in range(b_cols):
            if board[row][col] == 0:
                return False

    return True


def check_win(player):
    # vertical win check
    for col in range(b_cols):
        if board[0][col] == player and board[1][col] == player and board[2][
                col] == player:
            draw_vertical_winning_line(col, player)
            return True

    # horizontal win check
    for row in range(b_rows):
        if board[row][0] == player and board[row][1] == player and board[row][
                2] == player:
            draw_horizontal_winning_line(row, player)
            return True

    # asc diagonal win check
    if board[2][0] == player and board[1][1] == player and board[0][
            2] == player:
        draw_asc_diagonal(player)
        return True

    # desc diagonal win check
    if board[0][0] == player and board[1][1] == player and board[2][
            2] == player:
        draw_desc_diagonal(player)
        return True

    return False

def equals3(a,b,c):
  return (a == b and b == c and a != 0)

def checkWinner():
  winner = None

  #horizantal
  for i in range(3):
    if(equals3(board[i][0], board[i][1], board[i][2])):
      winner = board[i][0]
  #vertical
  for i in range(3):
    if(equals3(board[0][i], board[1][i], board[2][i])):
      winner = board[0][i]
  #diagonal
  if (equals3(board[0][0], board[1][1], board[2][2])):
    winner = board[0][0]
  
  if (equals3(board[2][0], board[1][1], board[0][2])):
    winner = board[2][0]

  if winner == None and is_board_full():
    tie = "tie"
    return tie
  else:
    return winner


# winnning lines
def draw_vertical_winning_line(col, player):
    posX = col * square_size + square_size // 2

    if player == 1:
        color = circle_color
    elif player == 2:
        color = cross_color

    pygame.draw.line(screen, color, (posX, 15), (posX, height - 15),
                     line_width)


def draw_horizontal_winning_line(row, player):
    posY = row * square_size + square_size // 2

    if player == 1:
        color = circle_color
    elif player == 2:
        color = cross_color

    pygame.draw.line(screen, color, (15, posY), (width - 15, posY),
                     win_line_width)


def draw_asc_diagonal(player):
    if player == 1:
        color = circle_color
    elif player == 2:
        color = cross_color

    pygame.draw.line(screen, color, (15, height - 15), (width - 15, 15),
                     win_line_width)


def draw_desc_diagonal(player):
    if player == 1:
        color = circle_color
    elif player == 2:
        color = cross_color

    pygame.draw.line(screen, color, (15, 15), (width - 15, height - 15),
                     win_line_width)


def restart():
    screen.fill(bg_color)
    draw_lines()
    player = 1
    for row in range(b_rows):
        for col in range(b_cols):
            board[row][col] = 0
    game_over = False


draw_lines()

# variables
player = random.randint(1,2)
game_over = False

# mainloop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:

            mouseX = event.pos[0]  # x
            mouseY = event.pos[1]  # y

            clicked_row = int(mouseY // square_size)
            clicked_col = int(mouseX // square_size)

            if available_square(clicked_row, clicked_col):
                mark_square(clicked_row, clicked_col, player)
                if check_win(player):
                    game_over = True
                    
                player = player % 2 + 1
                draw_figures()
                print(board)
                
        
        if game_over == True:
            print("The winner is: player", str(int(checkWinner())))
             

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                restart()


    pygame.display.update()
