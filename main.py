import pygame
from objects import Word

pygame.init()
screen = pygame.display.set_mode((720, 1280))
background_color = (255, 255, 255)
clock = pygame.time.Clock()
FPS = 60

test = Word("test", 10)

running = True

while running:
    screen.fill(background_color)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
                
    test.movement()
    
    clock.tick(FPS)
    pygame.display.update()
                
pygame.quit()