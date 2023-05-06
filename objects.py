import pygame, random

screen = pygame.display.set_mode((720, 1280))
SCREEN = WIDTH, HEIGHT = 720, 1280
WORD_WIDTH = WIDTH // 4
BLACK = (0, 0, 0)

class Word(pygame.sprite.Sprite):
    def __init__(self, word, speed):
        font = pygame.font.SysFont("Arial", 36)
        self.text = font.render(word, True, BLACK)
        self.rect = self.text.get_rect()
        self.rect.x = random.randrange(0, WIDTH - self.rect.width)
        self.rect.y = -self.rect.height
        self.speed = speed

    def movement(self):
        self.rect.y += self.speed
        if self.rect.y > HEIGHT:
            self.rect.x = random.randrange(0, WIDTH - self.rect.width)
            self.rect.y = -self.rect.height
        screen.blit(self.text, self.rect)