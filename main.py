import constants, pygame, images, random, words, pickle, os
from collections import OrderedDict
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
username = ''
rankings = {}
word_group = pygame.sprite.Group()
FONT = pygame.font.SysFont("comicsans", 45)

constants.screen.fill(constants.WHITE)

def game_loop(word_level):
    global level, words_guessed, lives, state_of_word_in_progress, word_group, score, final_score, username
    constants.screen.blit(constants.BACKGROUND, (0, 0))
    pygame.mixer.music.play()
    constants.MODE = word_level
    word_group.add(Word(0))
    
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
    global final_score, username, rankings
    text = FONT.render('Words guessed: ' + final_score, True, constants.WHITE)
    
    rankings[username] = int(final_score)
        
    print(rankings)
        
    rankings = OrderedDict(sorted(rankings.items(), key=lambda x: x[1], reverse=True))
    
    if len(rankings) > 10:
       rankings.popitem()
        
    with open('rankings.pkl', 'wb') as output_file:
        pickle.dump(dict(rankings), output_file)
        
    username = ''
    
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
                    game_loop(words.LEVEL_1)
                if LEVEL2.checkForInput(MENU_MOUSE_POS):
                    game_loop(words.LEVEL_2)
                if LEVEL3.checkForInput(MENU_MOUSE_POS):
                    game_loop(words.LEVEL_3)
                    
        clock.tick(FPS)
        pygame.display.update()
        
def ranking():
    global rankings, FONT
    constants.screen.blit(constants.BLURED_BG, (0, 0))

    table_width = 600
    table_height = 400
    table_x = (constants.WIDTH - table_width) // 2
    table_y = (constants.HEIGHT - table_height) // 2
    column_width = table_width // 3
    row_height = 50

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    main_menu()

        headers = ["Rank", "Name", "Score"]
        for idx, header in enumerate(headers):
            header_surface = FONT.render(header, True, constants.WHITE)
            header_x = table_x + idx * column_width
            header_y = table_y
            constants.screen.blit(header_surface, (header_x, header_y))

        for idx, (name, score) in enumerate(rankings.items()):
            rank_surface = FONT.render(str(idx + 1), True, constants.WHITE)
            name_surface = FONT.render(name, True, constants.WHITE)
            score_surface = FONT.render(str(score), True, constants.WHITE)

            row_x = table_x
            row_y = table_y + (idx + 1) * row_height

            constants.screen.blit(rank_surface, (row_x, row_y))
            constants.screen.blit(name_surface, (row_x + column_width, row_y))
            constants.screen.blit(score_surface, (row_x + 2 * column_width, row_y))

        clock.tick(FPS)
        pygame.display.update()
        
def enter_name():
    global username
    input_box_x = (constants.WIDTH - 300) // 2
    input_box_y = (constants.HEIGHT - 40) // 2
    input_box = pygame.Rect(input_box_x, input_box_y, 300, 40)
    font = pygame.font.SysFont("comicsans", 30)

    constants.screen.blit(constants.BLURED_BG, (0, 0))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return username
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                if event.key == pygame.K_RETURN:
                    options()
                if event.key == pygame.K_BACKSPACE:
                    username = username[:-1]
                elif len(username) < 16:
                    username += event.unicode

        constants.screen.blit(constants.BLURED_BG, (0, 0))
        pygame.draw.rect(constants.screen, constants.BLACK, input_box, 3)
        
        text_surface = font .render(username, True, (255, 255, 255))
        text_x = input_box.x + (input_box.width - text_surface.get_width()) // 2
        text_y = input_box.y + (input_box.height - text_surface.get_height()) // 2
        rect = text_surface.get_rect(center=(360, 640))
        shadow_rect = rect.move(1,1)
        constants.screen.blit(font.render(username, True, constants.BLACK), shadow_rect)
        constants.screen.blit(text_surface, (text_x, text_y))

        pygame.display.update()
        clock.tick(FPS)

def main_menu():
    global rankings
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
            
    PLAY_BUTTON = Button(None, (360, 520), "PLAY")
    RANK_BUTTON = Button(None, (360, 640), "RANKING")
    QUIT_BUTTON = Button(None, (360, 760), "QUIT")
    
    if os.path.exists('rankings.pkl'):
        with open('rankings.pkl', 'rb') as input_file:
            try:
                rankings = pickle.load(input_file)
                print("\n")
            except (FileNotFoundError, EOFError):
                rankings = {}
    else:
        rankings = {}
    
    while True:

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        for button in [PLAY_BUTTON, RANK_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    enter_name()
                if RANK_BUTTON.checkForInput(MENU_MOUSE_POS):
                    ranking()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    
        clock.tick(FPS)
        pygame.display.update()
        
main_menu()

pygame.quit()