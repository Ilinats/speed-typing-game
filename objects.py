import pygame, random

screen = pygame.display.set_mode((720, 1280))
SCREEN = WIDTH, HEIGHT = 720, 1280
WORD_WIDTH = WIDTH // 4
BLACK = (0, 0, 0)

import pygame, random

screen = pygame.display.set_mode((720, 1280))
SCREEN = WIDTH, HEIGHT = 720, 1280
WORD_WIDTH = WIDTH // 4
BLACK = (0, 0, 0)

class Word(pygame.sprite.Sprite):
    def __init__(self, text, speed, delay, spacing, positions):
        super().__init__()
        self._delay = delay
        self._letters = list(text)
        self._font = pygame.font.SysFont("Arial", 36)
        self._color = (0, 0, 0)
        self._speed = speed
        self._for_position = text
        self._text = self._letters[::-1]
        self._x = random.randint(25, WIDTH-25)
        self._y = -45 * len(text)
        self._spacing = spacing  # spacing between words
        self.rect = pygame.Rect(self._x, self._y, WORD_WIDTH, len(text) * WORD_WIDTH)
        self._positions = positions

    def update(self):
        if self._delay > 0:
            self._delay -= 1
        else:
            self._y += self._speed
            if self._y > HEIGHT:
                self.kill()

                # Checks for overlapping with other words
                for i, pos in enumerate(self._positions):
                    if self.rect.colliderect(pygame.Rect(self._x, pos, WORD_WIDTH, len(self._for_position) * WORD_WIDTH)):
                        self._y = pos - len(self._for_position) * WORD_WIDTH - self._spacing

                self.rect = pygame.Rect(self._x, self._y, WORD_WIDTH, len(self._for_position) * WORD_WIDTH)

    def draw(self, surface):
        chars = list(self._text)
        char_height = self._font.size(" ")[1]

        for i, char in enumerate(chars):
            char_surface = self._font.render(char, True, self._color)
            char_rect = char_surface.get_rect()
            char_rect.centerx = self._x
            char_rect.bottom = self._y + (i+1)*char_height
            surface.blit(char_surface, char_rect)