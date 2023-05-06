import pygame, random

screen = pygame.display.set_mode((720, 1280))
SCREEN = WIDTH, HEIGHT = 720, 1280
WORD_WIDTH = WIDTH // 4
BLACK = (0, 0, 0)

class Word(pygame.sprite.Sprite):
    def __init__(self, text, speed):
        super().__init__()
        self._letters = list(text)
        self._font = pygame.font.SysFont("Arial", 36)
        self._color = (0, 0, 0)
        self._speed = speed
        self._text = self._letters[::-1]
        self._x = random.randint(0, WIDTH)
        self._y = -25 * len(self._text)

    def update(self):
        self._y += self._speed
        if self._y > HEIGHT:
            self._y = -self._font.size(''.join(self._text))[1] 
            self._x = random.randint(0, WIDTH)


    def draw(self, surface):
        chars = list(self._text)
        char_height = self._font.size(" ")[1]

        for i, char in enumerate(chars):
            char_surface = self._font.render(char, True, self._color)
            char_rect = char_surface.get_rect()
            char_rect.centerx = self._x
            char_rect.bottom = self._y + (i+1)*char_height
            surface.blit(char_surface, char_rect)