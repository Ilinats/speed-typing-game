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
word_list = ["Test"]

# Adding the words from the list
word_positions = []
spacing = 100

for i, word in enumerate(word_list):
    delay = i * 60  # Delay each word by 1 second
    word_obj = Word(word, 5, delay, spacing, word_positions, word_group)  # pass word_group
    word_positions.append(word_obj.rect.y)

running = True
current_word = None

while running:
    screen.fill(background_color)

    # For exiting
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            elif current_word and chr(event.key) == current_word.current_letter:
                current_word.remove_letter()
                if current_word.is_word_complete():
                    current_word = None
                else:
                    current_word.current_letter = current_word._letters[0] 

    if not current_word and len(word_group.sprites()) > 0:
        current_word = word_group.sprites()[0]

    word_group.update()
    for word in word_group:
        word.draw(screen)
        
    clock.tick(FPS)
    pygame.display.update()

pygame.quit()
