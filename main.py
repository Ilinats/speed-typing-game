import constants, pygame
from objects import Word

pygame.init()

# Basic settings
clock = pygame.time.Clock()
FPS = 60

level = 1
words_guessed = 0
lives = 3
state_of_word_in_progress = 0

word_group = pygame.sprite.Group()

word_group.add(Word(0))

constants.screen.fill(constants.WHITE)

running = True

while running:
    letter = None
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            else:
                letter = event.unicode
                print(letter)

    has_waiting = False
    
    current_max_hit_state = 0
    for word in word_group:
        result = word.update(letter, state_of_word_in_progress)
        match result:
            case constants.STATE_WAITING:
                has_waiting = True
            case constants.STATE_GUESSED:
                words_guessed += 1
                word_group.remove(word)
            case constants.STATE_MISSED:
                lives -= 1
                word_group.remove(word)
            case _:
                if result > current_max_hit_state:
                    current_max_hit_state = result
                    
    state_of_word_in_progress = current_max_hit_state
            
    if not lives:
        running = False
    
    if not has_waiting:
        word_group.add(Word(level))
        
    if words_guessed >= 10:
        level += 1
        words_guessed = 0
        

    clock.tick(FPS)
    pygame.display.update()

pygame.quit()
