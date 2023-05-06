import pygame, random

screen = pygame.display.set_mode((720, 1280))
SCREEN = WIDTH, HEIGHT = 720, 1280
WORD_WIDTH = WIDTH // 4
BLACK = (0, 0, 0)

class Word(pygame.sprite.Sprite):
    def __init__(self, text, speed, delay):
        super().__init__()
        self._delay = delay
        self._letters = list(text)
        self._font = pygame.font.SysFont("Arial", 36)
        self._color = (0, 0, 0)
        self._speed = speed
        self._for_postion = text
        self._text = self._letters[::-1]
        self._x = random.randint(0, WIDTH)
        self._y = -45 * len(text)

    def update(self):
        if self._delay > 0:
            self._delay -= 1
        else:
            self._y += self._speed
            if self._y > HEIGHT:
                self._y = -45 * len(self._for_postion)  # start at bottom
                self._x = random.randint(0, WIDTH)
                self._delay = random.randint(0, 120)

    def draw(self, surface):
        chars = list(self._text)
        char_height = self._font.size(" ")[1]

        for i, char in enumerate(chars):
            char_surface = self._font.render(char, True, self._color)
            char_rect = char_surface.get_rect()
            char_rect.centerx = self._x
            char_rect.bottom = self._y + (i+1)*char_height
            surface.blit(char_surface, char_rect)