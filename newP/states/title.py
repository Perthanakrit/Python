import pygame 
from states.state import State
from states.game_world import Game_World 

class Title(State):
    def __init__(self,game):
        State.__init__(self, game)
        self.bg = pygame.image.load("_assets/images/BgMenu.jpg")
        self.bg = pygame.transform.scale(self.bg,(1280,800))
        self.MENU_MOUSE_POS = pygame.mouse.get_pos()
        self.PLAY_BUTTON = Button(image=pygame.image.load("_assets/Play Rect.png"), pos=(1280/2, 800/2), 
                            text_input="PLAY", font= self.game.font, base_color="#12E8FF", hovering_color="White")
        

    def update(self, delta_time, actions):
        if actions["leftClick"] and self.PLAY_BUTTON.checkForInput(self.MENU_MOUSE_POS):
            new_state = Game_World(self.game)
            new_state.enter_state()
        self.game.reset_keys()
        '''for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.PLAY_BUTTON.checkForInput(self.MENU_MOUSE_POS):
                    new_state = Game_World(self.game)
                    new_state.enter_state()'''
    def render(self, display):
        display.blit(self.bg, (0, 0))
        self.MENU_MOUSE_POS = pygame.mouse.get_pos()
        self.game.load_assets(50)
        self.game.draw_text(display, "Not Just Snake", (255,255,255), self.game.GAME_W/2, self.game.GAME_H - 600)
        self.PLAY_BUTTON 

        for button in [self.PLAY_BUTTON]:
            button.changeColor(self.MENU_MOUSE_POS)
            button.update(display)

        

class Button():
	def __init__(self, image, pos, text_input, font, base_color, hovering_color):
		self.image = image
		self.x_pos = pos[0]
		self.y_pos = pos[1]
		self.font = font
		self.base_color, self.hovering_color = base_color, hovering_color
		self.text_input = text_input
		self.text = self.font.render(self.text_input, True, self.base_color)
		if self.image is None:
			self.image = self.text
		self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
		self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

	def update(self, screen):
		if self.image is not None:
			screen.blit(self.image, self.rect)
		screen.blit(self.text, self.text_rect)

	def checkForInput(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			return True
		return False

	def changeColor(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			self.text = self.font.render(self.text_input, True, self.hovering_color)
		else:
			self.text = self.font.render(self.text_input, True, self.base_color)
