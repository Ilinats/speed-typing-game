import pygame
from objects import Word

pygame.init()

# Basic settings
screen = pygame.display.set_mode((720, 1280))
background_color = (255, 255, 255)
clock = pygame.time.Clock()
FPS = 60

level = 1

word_group = pygame.sprite.Group()

word1 = Word(1)
word2 = Word(2)
word_group.add(word1)
word_group.add(word2)

running = True

while running:
    screen.fill(background_color)

    # For exiting
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
    
    word_group.update()

    clock.tick(FPS)
    pygame.display.update()

pygame.quit()