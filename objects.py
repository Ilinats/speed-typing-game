import constants
import pygame, random

class Word(pygame.sprite.Sprite):
    def __init__(self, level):
        super().__init__()
        self._delay = random.randint(200, 500) // level if level else 0
        self._speed = random.random() + level/3
        
        i = random.randint(0, len(constants.MODE)-1)
        
        if(len(constants.WORDS_PASSED) == len(constants.MODE)):
            constants.WORDS_PASSED = []

        while i in constants.WORDS_PASSED:
            i = random.randint(0, len(constants.MODE)-1)
        
        self._word = constants.MODE[i]
        constants.WORDS_PASSED.append(i)
        
        self._y = -45
        self._x = random.randint(25, constants.WIDTH - 20 * len(self._word))
        self._state = 0

        FONT = pygame.font.SysFont("comicsans", 30)
        self._render = []
        self._render.append(FONT.render(self._word, True, constants.BLACK))
        for i in range(1, len(self._word)):
            self._render.append(FONT.render(self._word[0:i], True, constants.GREEN))

    def update(self, letter, state_of_word_in_progress):
        if self._delay:
            self._delay -= 1
            return constants.STATE_WAITING

        if letter != None and self._state == state_of_word_in_progress:
            if letter == self._word[self._state]:
                self._state += 1
            else:
                self._state = 0

        self._y += self._speed
        if self._y > constants.HEIGHT:
            self.kill()
            return constants.STATE_MISSED
        
        word_rect = self._render[0].get_rect(topleft=(self._x, self._y))
    
        # Erase the previous word
        constants.screen.blit(constants.BACKGROUND, word_rect, word_rect)

        # draw in black
        constants.screen.blit(self._render[0], (self._x, self._y))

        if self._state >= len(self._word):
            self.kill()
            constants.screen.blit(constants.BACKGROUND, word_rect, word_rect)
            return constants.STATE_GUESSED
        
        # Draw guessed chars in green
        if self._state:
            constants.screen.blit(self._render[self._state], (self._x, self._y))

        return self._state