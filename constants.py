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
BLURED_BG = pygame.image.load("game_bg_blured.jpg")

MODE = []
WORDS_PASSED = []

word_len = 5