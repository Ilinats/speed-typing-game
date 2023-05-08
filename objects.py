import pygame, random, string

SCREEN = WIDTH, HEIGHT = 720, 1280
screen = pygame.display.set_mode((WIDTH, HEIGHT))
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

curr_chars = 'asjkl'


class Word(pygame.sprite.Sprite):
    def __init__(self, level, word_counter):
        super().__init__()
        self._delay = 300 // level + 100 * word_counter
        self._speed = 1 * level
        self._word = ''.join((random.choice(curr_chars)) for x in range(random.randint(2, len(curr_chars))))
        self._font = pygame.font.SysFont('comicsans', 30)
        self._text = self._font.render(self._word, True, BLACK)
        self._y = -45
        self._x = random.randint(25, WIDTH - 20 * len(self._word))
        self._letter_position = 0
        self._coloredtextstr = ''
        self._coloredtext = self._font.render(self._coloredtextstr, True, GREEN)
        self._state = 0
        self._current_color = BLACK
        self._first = -1

    def update(self, letter, state_of_word):
        if self._delay:
            self._delay -= 1
            self._first = 1
        else:  
            if self._first:
                self._state = -2
                self._coloredtext = self._font.render(self._coloredtextstr, True, BLACK)
                self._first = 0
                
            self._y += self._speed
            if self._y > HEIGHT:
                if self._current_color != GREEN:
                    self._state = -4
                else:
                    self._state = -3
                self.kill()
                
        screen.blit(self._text, (self._x, self._y))
        screen.blit(self._coloredtext, (self._x, self._y))
        
        if letter != None:
            # if state_of_word != self._letter_position:
            #     self._state = 0
                
            if self._letter_position < len(self._word):
                if letter == self._word[self._letter_position]:
                    self._text = self._font.render(self._word, True, BLACK)
                    
                    self._coloredtextstr += self._word[self._letter_position]
                    self._coloredtext = self._font.render(self._coloredtextstr, True, GREEN)
                    self._current_color = GREEN
                    
                    if self._letter_position + 1 == len(self._word):
                        self.kill()
                        
                    self._letter_position += 1
                    
                else: 
                    self._coloredtext = self._font.render(self._word, True, RED)
                    self._current_color = RED
                    self._letter_position = 0
                    self._coloredtextstr = ''
                    
            else: 
                self._letter_position = 0
                
        return self._state