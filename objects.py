import pygame
import random

SCREEN = WIDTH, HEIGHT = 720, 1280
WORD_WIDTH = WIDTH // 4
BLACK = (0, 0, 0)

class Word(pygame.sprite.Sprite):
    def __init__(self, text, speed, delay, spacing, positions, word_group):
        super().__init__()
        self._delay = delay
        self._letters = list(text)
        self._font = pygame.font.SysFont("Arial", 36)
        self._color = (0, 0, 0)
        self._speed = speed
        self._for_position = text
        self._text = self._letters[::-1]
        self._x = random.randint(25, WIDTH-25)
        self._y = -45 * len(text) - spacing
        self._spacing = spacing
        self.rect = pygame.Rect(self._x, self._y, WORD_WIDTH, len(text) * WORD_WIDTH)
        self._positions = positions
        self.current_letter = self._letters[0]
        self._word_group = word_group  # add word group attribute
        self._word_group.add(self)  # add self to word group

    def update(self):
        if self._delay > 0:
            self._delay -= 1
        else:
            self._y += self._speed
            if self._y > HEIGHT:
                self.kill()
                return

            for i, pos in enumerate(self._positions):
                if self.rect.colliderect(pygame.Rect(self._x, pos, WORD_WIDTH, len(self._for_position) * WORD_WIDTH)):
                    self._y = pos - len(self._for_position) * WORD_WIDTH - self._spacing
                    self.rect = pygame.Rect(self._x, self._y, WORD_WIDTH, len(self._for_position) * WORD_WIDTH)
                    break

            if self._delay == 0 and self._letters:
                self.current_letter = self._letters[0]
                self._letters.pop(0)
                self._text = self._letters[::-1]

            # Update position of the word
            self.rect.y = self._y
       
    def draw(self, surface):
        self.image = pygame.Surface((WORD_WIDTH, len(self._text) * WORD_WIDTH), pygame.SRCALPHA)
        self.image.fill((255, 255, 255, 0))
        chars = list(self._text)
        char_height = self._font.size(" ")[1]

        for i, char in enumerate(chars):
            char_surface = self._font.render(char, True, self._color)
            char_rect = char_surface.get_rect()
            char_rect.centerx = self.rect.width / 2
            char_rect.bottom = (i + 1) * char_height
            self.image.blit(char_surface, char_rect)

        surface.blit(self.image, self.rect)

            
    def check_letter(self, letter):
        if self._text and letter == self._text[-1]:
            self._text.pop()
            if not self._text:
                self.kill()
            return True
        return False
