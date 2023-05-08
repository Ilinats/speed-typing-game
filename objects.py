import pygame, random, string

SCREEN = WIDTH, HEIGHT = 720, 1280
screen = pygame.display.set_mode((WIDTH, HEIGHT))
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

curr_chars = 'asjkl'

class Word(pygame.sprite.Sprite):
    def __init__(self, level):
        super().__init__()
        self._delay = 300 // level
        self._speed = 1 * level
        self._word = ''.join((random.choice(curr_chars)) for x in range(random.randint(2, len(curr_chars))))
        self._font = pygame.font.SysFont('comicsans', 30)
        self._text = self._font.render(self._word, True, BLACK)
        self._y = -45
        self._x = random.randint(25, WIDTH - 20 * len(self._word))
        self._letter_position = 0

    def update(self):
        if self._delay:
            self._delay -= 1
        else:    
            self._y += self._speed
            if self._y > HEIGHT:
                self.kill()
                
        screen.blit(self._text, (self._x, self._y))
        
    def check_character(self, letter):
        if self._letter_position < len(self._word):
            if letter == self._word[self._letter_position]:
                self._text = self._font.render(self._word[self._letter_position] , True, GREEN)
                
                if self._letter_position + 1 == len(self._word):
                    self.kill()
                    
                self._letter_position += 1
                
            else: 
                self._text = self._font.render(self._word, True, RED)
                self._letter_position = 0
                
        else: 
            self._letter_position = 0