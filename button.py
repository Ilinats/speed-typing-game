import constants, pygame

class Button():
	def __init__(self, image, pos, text_input):
		self._image = image
		self._x_pos = pos[0]
		self._y_pos = pos[1]
		self._font = pygame.font.SysFont("comicsans", 45)
		self._base_color, self._hovering_color = constants.WHITE, constants.GREEN
		self._text_input = text_input
		self._text = self._font.render(self._text_input, True, self._base_color)
		self._shadow_color = constants.BLACK
		if self._image is None:
			self._image = self._text
		self._rect = self._image.get_rect(center=(self._x_pos, self._y_pos))
		self._text_rect = self._text.get_rect(center=(self._x_pos, self._y_pos))
		self._shadow_rect = self._text_rect.move(2, 2)

	def update(self):
		if self._image is not None:
			constants.screen.blit(self._image, self._rect)
   
		constants.screen.blit(self._font.render(self._text_input, True, self._shadow_color), self._shadow_rect)
		constants.screen.blit(self._text, self._text_rect)

	def checkForInput(self, position):
		if position[0] in range(self._rect.left, self._rect.right) and position[1] in range(self._rect.top, self._rect.bottom):
			return True
		return False

	def changeColor(self, position):
		if position[0] in range(self._rect.left, self._rect.right) and position[1] in range(self._rect.top, self._rect.bottom):
			self._text = self._font.render(self._text_input, True, self._hovering_color)
		else:
			self._text = self._font.render(self._text_input, True, self._base_color)