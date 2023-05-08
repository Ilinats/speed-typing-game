import pygame
from objects import Word

pygame.init()

# Basic settings
screen = pygame.display.set_mode((720, 1280))
background_color = (255, 255, 255)
clock = pygame.time.Clock()
FPS = 60

level = 1
current_words = []
lives = 3
state_of_word = 0

word_group = pygame.sprite.Group()

for i in range (0, 100):
    word = Word(3, i+1)
    word_group.add(word)

running = True

while running:
    screen.fill(background_color)
    letter = None

    # For exiting
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            else: 
                letter = event.unicode
                print(letter)
    
    for word in word_group:
        result = word.update(letter, state_of_word)
        
        if result == -4:
            lives -= 1
            current_words.remove(word)
            break
        elif result == -3:
            current_words.remove(word)
        elif word not in current_words and result == -2:
            current_words.append(word)
            
        #print(current_words)
            
    if lives == 0:
        running = False

    clock.tick(FPS)
    pygame.display.update()

pygame.quit()