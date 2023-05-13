import pygame

filled_heart_img = pygame.image.load('filled_heart.png')
empty_heart_img = pygame.image.load('empty_heart2.png')
empty_level_bar = pygame.image.load('empty_bar.png')
full_level_bar = pygame.image.load('full_bar.png')
level1_bar = pygame.image.load('bar1.png')
level2_bar = pygame.image.load('bar2.png')
level3_bar = pygame.image.load('bar3.png')
level4_bar = pygame.image.load('bar4.png')
level5_bar = pygame.image.load('bar5.png')
level6_bar = pygame.image.load('bar6.png')
level7_bar = pygame.image.load('bar7.png')
level8_bar = pygame.image.load('bar8.png')
level9_bar = pygame.image.load('bar9.png')

width = empty_heart_img.get_rect().width
height = empty_heart_img.get_rect().height

width2 = empty_level_bar.get_rect().width
height2 = empty_level_bar.get_rect().height

empty_heart_img = pygame.transform.scale(empty_heart_img, (width//2, height//2))
filled_heart_img = pygame.transform.scale(filled_heart_img, (width//2, height//2))
empty_level_bar = pygame.transform.scale(empty_level_bar, (width2/1.8, height2/1.8))
full_level_bar = pygame.transform.scale(full_level_bar, (width2/1.8, height2/1.8))
level1_bar = pygame.transform.scale(level1_bar, (width2/1.8, height2/1.8))
level2_bar = pygame.transform.scale(level2_bar, (width2/1.8, height2/1.8))
level3_bar = pygame.transform.scale(level3_bar, (width2/1.8, height2/1.8))
level4_bar = pygame.transform.scale(level4_bar, (width2/1.8, height2/1.8))
level5_bar = pygame.transform.scale(level5_bar, (width2/1.8, height2/1.8))
level6_bar = pygame.transform.scale(level6_bar, (width2/1.8, height2/1.8))
level7_bar = pygame.transform.scale(level7_bar, (width2/1.8, height2/1.8))
level8_bar = pygame.transform.scale(level8_bar, (width2/1.8, height2/1.8))
level9_bar = pygame.transform.scale(level9_bar, (width2/1.8, height2/1.8))