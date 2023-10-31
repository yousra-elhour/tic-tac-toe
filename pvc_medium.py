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
o_radius = 30
o_width = 10
x_width = 10
space = 25
# colors
bg_color = (23, 145, 135)
line_color = (58, 188, 177)
o_color = (255, 255, 255)
x_color = (0, 0, 0)

# screen
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('TIC TAC TOE')
screen.fill(bg_color)

# console board
board = np.zeros((b_rows, b_cols))

# ---------
# VARIABLES
# ---------

ai = 2
user = 1
player = random.choice([user, ai])

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
                pygame.draw.circle(screen, o_color,
                                   (int(col * square_size + square_size // 2),
                                    int(row * square_size + square_size // 2)),
                                   o_radius, o_width)
            elif board[row][col] == 2:
                pygame.draw.line(screen, x_color,
                                 (col * square_size + space,
                                  row * square_size + square_size - space),
                                 (col * square_size + square_size - space,
                                  row * square_size + space), x_width)
                pygame.draw.line(
                    screen, x_color,
                    (col * square_size + space, row * square_size + space),
                    (col * square_size + square_size - space,
                     row * square_size + square_size - space), x_width)


def mark_square(row, col, player):
    board[row][col] = player


def available_square(row, col):
    return board[row][col] == 0

def available_towin(row, col):
  return board[row][col] == ai

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

    # desc diagonal win chek
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
        color = o_color
    elif player == 2:
        color = x_color

    pygame.draw.line(screen, color, (posX, 15), (posX, height - 15),
                     line_width)


def draw_horizontal_winning_line(row, player):
    posY = row * square_size + square_size // 2

    if player == 1:
        color = o_color
    elif player == 2:
        color = x_color

    pygame.draw.line(screen, color, (15, posY), (width - 15, posY),
                     win_line_width)


def draw_asc_diagonal(player):
    if player == 1:
        color = o_color
    elif player == 2:
        color = x_color

    pygame.draw.line(screen, color, (15, height - 15), (width - 15, 15),
                     win_line_width)


def draw_desc_diagonal(player):
    if player == 1:
        color = o_color
    elif player == 2:
        color = x_color

    pygame.draw.line(screen, color, (15, 15), (width - 15, height - 15),
                     win_line_width)


def restart():
    screen.fill(bg_color)
    draw_lines()
    for row in range(b_rows):
        for col in range(b_cols):
            board[row][col] = 0
    game_over = False



draw_lines()

# ---------
# VARIABLES
# ---------
player = random.randint(1, 2)
if player == 1:
  ai = 2
  user = 1
  
elif player == 2:
  ai = 2
  user = 1
  

#random_value
ai_row = random.randint(0, 2)
ai_col = random.randint(0, 2)

#medium difficulty ai value
aimd_row = 0
aimd_col = 0

game_over = False
winningMoveDone = False

# mainloop
while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
            sys.exit()
        
      if player == user:
        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:

            print("player = " + str(player) + " user = " + str(user), "ai = " + str(ai))

            mouseX = event.pos[0]  # x
            mouseY = event.pos[1]  # y

            clicked_row = int(mouseY // square_size)
            clicked_col = int(mouseX // square_size)

            
            print("someone is about to play")
            if available_square(clicked_row, clicked_col):
              mark_square(clicked_row, clicked_col, user)
              player = ai
            if check_win(user):
              game_over = True
              print("game stopped")

            print("user has played")
            draw_figures() 
            
      elif player == ai and not game_over:
        if winningMoveDone == False:     
          if (board[0][0] == ai and board[1][0] == ai and winningMoveDone == False):
            aimd_row = 2
            if available_square(aimd_row, 0):
              mark_square(aimd_row, 0, ai)
              winningMoveDone = True  
              print("col winning move 1")            
          if (board[2][0] == ai and board[1][0] == ai and winningMoveDone == False):
            aimd_row = 0
            if available_square(aimd_row, 0):
              mark_square(aimd_row, 0, ai)
              winningMoveDone = True
              print("col winning move 2")   
          if (board[0][0] == ai and board[2][0] == ai and winningMoveDone == False):
            aimd_row = 1
            if available_square(aimd_row, 0):
              mark_square(aimd_row, 0, ai)
              winningMoveDone = True
              print("col winning move 3")
          if (board[1][1] == ai and board[1][2] == ai and winningMoveDone == False):
            aimd_col = 2
            if available_square(1, aimd_col):
              mark_square(1, aimd_col, ai)
              winningMoveDone = True
              print("col winning move 3")

          if (board[0][1] == ai and board[1][1] == ai and winningMoveDone == False):
            aimd_row = 2
            if available_square(aimd_row, 1):
              mark_square(aimd_row, 1, ai)
              winningMoveDone = True  
              print("col winning move 1")            
          if (board[2][0] == ai and board[1][1] == ai and winningMoveDone == False):
            aimd_row = 0
            if available_square(aimd_row, 1):
              mark_square(aimd_row, 1, ai)
              winningMoveDone = True
              print("col winning move 2")   
          if (board[0][1] == ai and board[2][1] == ai and winningMoveDone == False):
            aimd_row = 1
            if available_square(aimd_row, 1):
              mark_square(aimd_row, 1, ai)
              winningMoveDone = True
              print("col winning move 3")   

          if (board[0][2] == ai and board[1][2] == ai and winningMoveDone == False):
            aimd_row = 2
            if available_square(aimd_row, 2):
              mark_square(aimd_row, 2, ai)
              winningMoveDone = True  
              print("col winning move 1")            
          if (board[2][2] == ai and board[1][2] == ai and winningMoveDone == False):
            aimd_row = 2
            if available_square(aimd_row, 2):
              mark_square(aimd_row, 2, ai)
              winningMoveDone = True
              print("col winning move 2")   
          if (board[0][2] == ai and board[2][2] == ai and winningMoveDone == False):
            aimd_row = 1
            if available_square(aimd_row, 2):
              mark_square(aimd_row, 2, ai)
              winningMoveDone = True
              print("col winning move 3")


          
          if board[0][1] == ai and board[0][2] == ai and winningMoveDone == False:
            aimd_col = 0
            if available_square(0, aimd_col):
              mark_square(0, aimd_col, ai)
              winningMoveDone = True
              print("row winning move 1")   
          if board[0][0] == ai and board[0][2] == ai and winningMoveDone == False:
            aimd_col = 1
            if available_square(0, aimd_col):
              mark_square(0, aimd_col, ai)
              winningMoveDone = True
              print("row winning move 2")   
          if board[0][0] == ai and board[0][1] == ai and winningMoveDone == False:
            aimd_col = 2
            if available_square(0, aimd_col):
              mark_square(0, aimd_col, ai)
              winningMoveDone = True
              print("row winning move 3")   

          if board[1][1] == ai and board[1][2] == ai and winningMoveDone == False:
            aimd_col = 0
            if available_square(1, aimd_col):
              mark_square(1, aimd_col, ai)
              winningMoveDone = True
              print("row winning move 1")   
          if board[1][0] == ai and board[1][2] == ai and winningMoveDone == False:
            aimd_col = 1
            if available_square(1, aimd_col):
              mark_square(1, aimd_col, ai)
              winningMoveDone = True
              print("row winning move 2")   
          if board[1][0] == ai and board[1][1] == ai and winningMoveDone == False:
            aimd_col = 2
            if available_square(1, aimd_col):
              mark_square(1, aimd_col, ai)
              winningMoveDone = True
              print("row winning move 3")  


          if board[2][1] == ai and board[2][2] == ai and winningMoveDone == False:
            aimd_col = 0
            if available_square(2, aimd_col):
              mark_square(2, aimd_col, ai)
              winningMoveDone = True
              print("row winning move 1")   
          if board[2][0] == ai and board[2][2] == ai and winningMoveDone == False:
            aimd_col = 1
            if available_square(2, aimd_col):
              mark_square(2, aimd_col, ai)
              winningMoveDone = True
              print("row winning move 2")   
          if board[2][0] == ai and board[2][1] == ai and winningMoveDone == False:
            aimd_col = 2
            if available_square(2, aimd_col):
              mark_square(2, aimd_col, ai)
              winningMoveDone = True
              print("row winning move 3") 

          if board[2][2] == ai and board[1][2] == ai and winningMoveDone == False:
            aimd_col = 2
            if available_square(0, aimd_col):
              mark_square(0, aimd_col, ai)
              winningMoveDone = True
              print("row winning move 3")    

              
          if board[2][0] == ai and board[1][1] == ai and winningMoveDone == False:
            if available_square(0, 2):
              mark_square(0, 2, ai)
              winningMoveDone = True
              print("diag winning move 1")   
          
          if board[0][2] == ai and board[1][1] == ai and winningMoveDone == False:
            if available_square(2, 0):
              mark_square(2, 0, ai)
              winningMoveDone = True
              print(" diag winning move 2")   

          if board[2][0] == ai and board[0][2] == ai and winningMoveDone == False:
            if available_square(1, 1):
              mark_square(1, 1, ai)
              winningMoveDone = True
              print("diag winning move 3")   

          if board[0][0] == ai and board[1][1] == ai and winningMoveDone == False:
            if available_square(2, 2):
              mark_square(2, 2, ai)
              winningMoveDone = True
              print("diag winning move 4")   
          
          if board[2][2] == ai and board[1][1] == ai and winningMoveDone == False:
            if available_square(0, 0):
              mark_square(0, 0, ai)
              winningMoveDone = True
              print("diag winning move 5")   

          if board[0][0] == ai and board[2][2] == ai and winningMoveDone == False:
            if available_square(1, 1):
              mark_square(1, 1, ai)
              winningMoveDone = True
              print("diag winning move 6")   

        

          if winningMoveDone == False:
            print("no winning move")
            randomMoveDone = False
            while(randomMoveDone == False):
              ai_row = random.randint(0, 2)
              ai_col = random.randint(0, 2)
              if(available_square(ai_row, ai_col)):
                mark_square(ai_row, ai_col, ai)
                randomMoveDone = True

        print("ai has played")

        draw_figures() 
        player = user

        if check_win(ai):
          game_over= True
          print("game stopped")
          
            
            

          
      print(board)
      result = checkWinner() 
      if game_over == True:
        if ai == result:
            victory = "The winner is: ai, too bad"
        elif user == result:
            victory = "The winner is: YOU! good job"  
        print(victory)  

      if is_board_full() == True:
        print("Its a tie")

      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_r:
          restart()


    pygame.display.update()
