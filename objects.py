import constants
import pygame, random, string


curr_chars = "asjkl"


class Word(pygame.sprite.Sprite):
    def __init__(self, level):
        super().__init__()
        self._delay = random.randint(200, 500) // level
        self._speed = 0.5 * level
        self._word = "".join(
            (random.choice(curr_chars))
            for x in range(random.randint(2, len(curr_chars)))
        )
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

        self._y += self._speed
        if self._y > constants.HEIGHT:
            self.kill()
            return constants.STATE_MISSED

        # draw in black
        constants.screen.blit(self._render[0], (self._x, self._y))

        if letter != None and self._state == state_of_word_in_progress:
            if letter == self._word[self._state]:
                self._state += 1
            else:
                self._state = 0

        if self._state >= len(self._word):
            self.kill()
            return constants.STATE_GUESSED

        # Draw guessed chars in green
        if self._state:
            constants.screen.blit(self._render[self._state], (self._x, self._y))

        return self._state
