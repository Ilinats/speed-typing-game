import pygame, random, string

SCREEN = WIDTH, HEIGHT = 720, 1280
screen = pygame.display.set_mode((WIDTH, HEIGHT))
BLACK = (0, 0, 0)

curr_chars = 'asjkl'

class Word(pygame.sprite.Sprite):
    def __init__(self, level):
        super().__init__()
        self._level = level
        self._y = -45
        self._x = random.randint(25, WIDTH - 25)
        self._delay = 300 // self._level
        self._speed = 1 * self._level
        word = ''.join((random.choice(curr_chars)) for x in range(len(curr_chars)))
        self._font = pygame.font.SysFont('comicsans', 30)
        self._text = self._font.render(word, True, BLACK)
        #self._should_delay = 1

    def update(self):
        if self._delay:
            self._delay -= 1
        else:    
            self._y += self._speed
            if self._y > HEIGHT:
                self.kill()
                
        screen.blit(self._text, (self._x, self._y))