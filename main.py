import pygame, random
from objects import Word

pygame.init()

# Basic settings
screen = pygame.display.set_mode((720, 1280))
background_color = (255, 255, 255)
clock = pygame.time.Clock()
FPS = 60

# Creating a word group
word_group = pygame.sprite.Group()

# List of test words
word_list = ["Test", "Ne znam", "Neshto", "Drugo"]

# Adding the words form the list
for i, word in enumerate(word_list):
    delay = i * 60  # delay each word by 1 second
    word_obj = Word(word, 5, delay)
    word_group.add(word_obj)

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
    for word in word_group:
        word.draw(screen)
    
    clock.tick(FPS)
    pygame.display.update()
                
pygame.quit()