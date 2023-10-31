import pygame
from pygame.locals import *
import os

# Game Initialization
pygame.init()

# Center the Game Application
os.environ['SDL_VIDEO_CENTERED'] = '1'

# Game Resolution
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))


# Text Renderer
def text_format(message, textFont, textSize, textColor):
	newFont = pygame.font.Font(textFont, textSize)
	newText = newFont.render(message, 0, textColor)
	return newText


# Colors
white = (255, 255, 255)
black = (0, 0, 0)
gray = (50, 50, 50)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)

# Game Fonts
font = "Retro.ttf"

# Game Framerate
clock = pygame.time.Clock()
FPS = 30


# Main Menu
def main_menu():

	menu = True
	while menu:

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
			if event.type == pygame.MOUSEBUTTONDOWN:
				mouse = pygame.mouse.get_pos()
				if 340 <= mouse[0] <= 450 and 370 <= mouse[1] <= 415:
					pygame.quit()
				if 325 <= mouse[0] <= 470 and 310 <= mouse[1] <= 355:
					options()

		# Main Menu UI
		screen.fill((23, 145, 135))
		title = text_format("Tic Tac Toe", font, 90, (247, 125, 10))
		mouse = pygame.mouse.get_pos()
		if 325 <= mouse[0] <= 470 and 310 <= mouse[1] <= 355:
			text_start = text_format("START", font, 75, white)
		else:
			text_start = text_format("START", font, 75, black)
		if 340 <= mouse[0] <= 450 and 370 <= mouse[1] <= 415:
			text_quit = text_format("QUIT", font, 75, white)
		else:
			text_quit = text_format("QUIT", font, 75, black)

		title_rect = title.get_rect()
		start_rect = text_start.get_rect()
		quit_rect = text_quit.get_rect()

		# Main Menu Text
		screen.blit(title, (screen_width / 2 - (title_rect[2] / 2), 120))
		screen.blit(text_start, (screen_width / 2 - (start_rect[2] / 2), 300))
		screen.blit(text_quit, (screen_width / 2 - (quit_rect[2] / 2), 360))

		pygame.display.update()
		pygame.display.set_caption("TIC TAC TOE")
		pygame.display.update()


def options():
	op = True
	while op:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
			if event.type == pygame.MOUSEBUTTONDOWN:
				mouse = pygame.mouse.get_pos()

				if 220 <= mouse[0] <= 575 and 210 <= mouse[1] <= 245:
					import pvp.py
				if 195 <= mouse[0] <= 600 and 270 <= mouse[1] <= 305:
					difficulty()

# OPTION UI
#Changes made here
		screen.fill((23, 145, 135))
		options = text_format("OPTIONS", font, 90, (247, 125, 10))
		mouse = pygame.mouse.get_pos()

		if 220 <= mouse[0] <= 575 and 210 <= mouse[1] <= 245:
			pvp_option = text_format("PLAYER VS PLAYER", font, 60, white)
		else:
			pvp_option = text_format("PLAYER VS PLAYER", font, 60, black)
		if 195 <= mouse[0] <= 600 and 270 <= mouse[1] <= 305:
			pvc_option = text_format("PLAYER VS COMPUTER", font, 60, white)
		else:
			pvc_option = text_format("PLAYER VS COMPUTER", font, 60, black)

		options_rect = options.get_rect()
		pvp_rect = pvp_option.get_rect()
		pvc_rect = pvc_option.get_rect()

		# OPTION Text
		screen.blit(options, (screen_width / 2 - (options_rect[2] / 2), 80))
		screen.blit(pvp_option, (screen_width / 2 - (pvp_rect[2] / 2), 200))
		screen.blit(pvc_option, (screen_width / 2 - (pvc_rect[2] / 2), 260))

		pygame.display.update()

		pygame.display.update()


def difficulty():
	diff = True
	while diff:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
			if event.type == pygame.MOUSEBUTTONDOWN:
				mouse = pygame.mouse.get_pos()

				if 350 <= mouse[0] <= 445 and 210 <= mouse[1] <= 245:
					import pvc_easy.py
				if 330 <= mouse[0] <= 465 and 270 <= mouse[1] <= 305:
					import pvc_medium.py
				if 350 <= mouse[0] <= 445 and 330 <= mouse[1] <= 365:
					import pvc_hard.py

#Difficulty UI
		screen.fill((23, 145, 135))
		difficulty = text_format("DIFFICULTY", font, 90, (247, 125, 10))
		mouse = pygame.mouse.get_pos()

		if 350 <= mouse[0] <= 445 and 210 <= mouse[1] <= 245:
			easy_option = text_format("EASY", font, 60, white)
		else:
			easy_option = text_format("EASY", font, 60, black)
		if 330 <= mouse[0] <= 465 and 270 <= mouse[1] <= 305:
			medium_option = text_format("MEDIUM", font, 60, white)
		else:
			medium_option = text_format("MEDIUM", font, 60, black)
		if 350 <= mouse[0] <= 445 and 330 <= mouse[1] <= 365:
			hard_option = text_format("HARD", font, 60, white)
		else:
			hard_option = text_format("HARD", font, 60, black)

		difficulty_rect = difficulty.get_rect()
		easy_rect = easy_option.get_rect()
		medium_rect = medium_option.get_rect()
		hard_rect = hard_option.get_rect()

		# OPTION Text
		screen.blit(difficulty,
		            (screen_width / 2 - (difficulty_rect[2] / 2), 80))
		screen.blit(easy_option, (screen_width / 2 - (easy_rect[2] / 2), 200))
		screen.blit(medium_option,
		            (screen_width / 2 - (medium_rect[2] / 2), 260))
		screen.blit(hard_option, (screen_width / 2 - (hard_rect[2] / 2), 320))

		pygame.display.update()


#Initialize the Game
main_menu()
pygame.quit()
quit()
