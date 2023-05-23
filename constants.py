import pygame

STATE_WAITING = -1
STATE_GUESSED = -2
STATE_MISSED = -3

SCREEN = WIDTH, HEIGHT = 720, 1280
screen = pygame.display.set_mode((WIDTH, HEIGHT))
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BACKGROUND = pygame.image.load("game_bg.jpg")

MODE_1 = 'asdfjkl'
MODE_2 = 'asdfjklghtreiouyvn'
MODE_3 = 'qwertyuiopasdfghjklzxcvbnm'

word_len = 5