import constants, pygame, images
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
    
    match lives:
        case 1:
            constants.screen.blit(images.filled_heart_img, (0,0))
            constants.screen.blit(images.empty_heart_img, (50,0))
            constants.screen.blit(images.empty_heart_img, (100,0))
        case 2:
            constants.screen.blit(images.filled_heart_img, (0,0))
            constants.screen.blit(images.filled_heart_img, (50,0))
            constants.screen.blit(images.empty_heart_img, (100,0))
        case 3:
            constants.screen.blit(images.filled_heart_img, (0,0))
            constants.screen.blit(images.filled_heart_img, (50,0))
            constants.screen.blit(images.filled_heart_img, (100,0))
            
    match words_guessed:
        case 0:
            constants.screen.blit(images.empty_level_bar, (555,0))
        case 1:
            constants.screen.blit(images.level1_bar, (555,0))
        case 2:
            constants.screen.blit(images.level2_bar, (555,0))
        case 3:
            constants.screen.blit(images.level3_bar, (555,0))
        case 4:
            constants.screen.blit(images.level4_bar, (555,0))
        case 5:
            constants.screen.blit(images.level5_bar, (555,0))
        case 6:
            constants.screen.blit(images.level6_bar, (555,0))
        case 7:
            constants.screen.blit(images.level7_bar, (555,0))
        case 8:
            constants.screen.blit(images.level8_bar, (555,0))
        case 9:
            constants.screen.blit(images.level9_bar, (555,0))
        case 10:
            constants.screen.blit(images.full_level_bar, (555,0))
        
    
    clock.tick(FPS)
    pygame.display.update()

pygame.quit()
