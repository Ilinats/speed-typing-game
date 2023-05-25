import constants, pygame, images, random
from objects import Word
from button import Button

pygame.init()
pygame.mixer.init()
pygame.mixer.music.set_volume(0.2)
        
# Basic settings
clock = pygame.time.Clock()
FPS = 60

level = 1
words_guessed = 0
lives = 3
state_of_word_in_progress = 0
score = 0
final_score = ''
word_group = pygame.sprite.Group()
FONT = pygame.font.SysFont("comicsans", 45)

word_group.add(Word(0))

constants.screen.fill(constants.WHITE)

def game_loop():
    global level, words_guessed, lives, state_of_word_in_progress, word_group, score, final_score
    constants.screen.blit(constants.BACKGROUND, (0, 0))
    pygame.mixer.music.play()
    
    while True:
        letter = None
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
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
            break
            
        if words_guessed == 10:
            level += 1
            words_guessed = 0
            score += 1
            
        if not has_waiting:
            word_group.add(Word(level))
        
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
    
    score = score*10 + words_guessed
    final_score = str(score)
    score = 0
    level = 1
    words_guessed = 0
    lives = 3
    state_of_word_in_progress = 0

    word_group = pygame.sprite.Group()

    word_group.add(Word(0))
    pygame.mixer.music.stop()
    restart()
        
def restart():
    global final_score
    text = FONT.render('Words guessed: ' + final_score, True, constants.WHITE)
    
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        constants.screen.blit(constants.BLURED_BG, (0, 0))
        
        PLAY_BACK = Button(None, (360, 640), "RESTART")
        rect = text.get_rect(center=(360, 450))
        shadow_rect = rect.move(2,2)
        constants.screen.blit(FONT.render('Words guessed: ' + final_score, True, constants.BLACK), shadow_rect)
        constants.screen.blit(text, rect)

        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()

        clock.tick(FPS)
        pygame.display.update()
        
def options():
    
    constants.screen.blit(constants.BLURED_BG, (0, 0))
    
    while True:

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        LEVEL1 = Button(None, (360, 490), "LEVEL 1")
        LEVEL2 = Button(None, (360, 640), "LEVEL 2")
        LEVEL3 = Button(None, (360, 790), "LEVEL 3")

        for button in [LEVEL1, LEVEL2, LEVEL3]:
            button.changeColor(MENU_MOUSE_POS)
            button.update()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if LEVEL1.checkForInput(MENU_MOUSE_POS):
                    game_loop()
                if LEVEL2.checkForInput(MENU_MOUSE_POS):
                    game_loop()
                if LEVEL3.checkForInput(MENU_MOUSE_POS):
                    game_loop()
                    
        clock.tick(FPS)
        pygame.display.update()
        
def main_menu():
    
    constants.screen.blit(constants.BLURED_BG, (0, 0))
    
    match random.randint(1, 7):
        case 1:
            pygame.mixer.music.load('hell_above.mp3')
        case 2:
            pygame.mixer.music.load('king_for_a_day.mp3')
        case 3:
            pygame.mixer.music.load('bulls_in_the_bronx.mp3')
        case 4:
            pygame.mixer.music.load('tangled_in_the_great_escape.mp3')
        case 5:
            pygame.mixer.music.load('the_first_punch.mp3')
        case 6:
            pygame.mixer.music.load('one_hundred_sleepless_nights.mp3')
        case 7:
            pygame.mixer.music.load('caraphernelia.mp3')
            
    PLAY_BUTTON = Button(None, (360, 490), "PLAY")
    OPTIONS_BUTTON = Button(None, (360, 640), "OPTIONS")
    QUIT_BUTTON = Button(None, (360, 790), "QUIT")
    
    while True:

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    game_loop()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    
        clock.tick(FPS)
        pygame.display.update()
        
main_menu()

pygame.quit()