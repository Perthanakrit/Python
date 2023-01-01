import pygame ,os,time
from states.state import State
from _assets.Character import *
from Button import Button


class PauseMenu(State):
    def __init__(self, game, winnerName, winnerColor):
        self.game = game
        self.winner = [winnerName, winnerColor]
        State.__init__(self, game)
        #Button.__init__(self, game)
        # Set the menu
        self.menu_img = pygame.image.load(os.path.join(self.game.assets_dir, "images", "Pause.jpg"))
        self.menu_img = pygame.transform.scale(self.menu_img, (game.SCREEN_WIDTH * 1.8,game.SCREEN_HEIGHT*1.2))
        self.menu_rect = self.menu_img.get_rect()
        self.menu_rect.center = (self.game.GAME_W*.85, self.game.GAME_H*.4)
        self.PLAY_BUTTON = Button(image=pygame.image.load("_assets/Play Rect.png"), pos=(100, 100), 
                            text_input="Restart", font= self.game.font, base_color="#d7fcd4", hovering_color="White")
        #
        self.restartText_x, self.restartText_y = self.game.GAME_W/2, self.game.GAME_H - 320 
        self.exitText_x, self.exitText_y = self.game.GAME_W/2, self.game.GAME_H - 260 
        #
        self.menu_options = {0 :"Restart", 1 : "Exit"}
        self.index = 0
        self.cursor_img = pygame.image.load(os.path.join(self.game.assets_dir, "images", "Apple.png"))
        self.cursor_img = pygame.transform.scale(self.cursor_img,(46,46))
        self.cursor_rect = self.cursor_img.get_rect()
        self.cursor_pos_y = (self.menu_rect.y + self.game.GAME_W/2) - 30
        self.cursor_rect.x, self.cursor_rect.y = self.game.GAME_W/2 -190, self.cursor_pos_y 

    def update(self, delta_time, actions):  
        self.update_cursor(actions)      
        if actions["start"]:
            self.transition_state(self.game)
        if actions["action2"]:
            self.exit_state()
        self.game.reset_keys()

    def render(self, display):
        # render the gameworld behind the menu, which is right before the pause menu on the stack
        #self.game.state_stack[-2].render(display)
        self.prev_state.render(display)
        #display.blit(self.menu_img, self.menu_rect)
        display.blit(self.menu_img, (0, 0))
        
        self.game.load_assets(45)
        self.game.draw_text(display, "Game Over ", (255,255,255), self.game.GAME_W/2, self.game.GAME_H - 600)
        self.game.draw_text(display, "Snake "+self.winner[0]+" is winner",self.winner[1] , self.game.GAME_W/2, self.game.GAME_H - 500)
        display.blit(self.cursor_img, self.cursor_rect)
        self.game.load_assets(39)
        self.game.draw_text(display, "Restart", (255,255,255), self.restartText_x, self.restartText_y)
        self.game.draw_text(display, "Exit",(255,255,255) , self.exitText_x, self.exitText_y)
        
        self.PLAY_BUTTON = Button(image=pygame.image.load("_assets/Play Rect.png"), pos=(100, 100), 
                            text_input="Restart", font= self.game.font, base_color="#d7fcd4", hovering_color="black")
              
    def update_cursor(self, actions):
        if actions['down'] or actions['down_arrow']:
            self.index = (self.index + 1) % len(self.menu_options)
        elif actions['up'] or actions['up_arrow']:
            self.index = (self.index - 1) % len(self.menu_options)
        self.cursor_rect.y = self.cursor_pos_y + (self.index *(self.exitText_y - self.restartText_y))

    def transition_state(self,game):
        if self.menu_options[self.index] == "Restart": 
            while len(self.game.state_stack) > 1:
                self.game.state_stack.pop()
        
        elif self.menu_options[self.index] == "Exit": 
            game.playing = False
            game.running = False
            #pygame.quit()
        #display.blit(self.cursor_img, self.cursor_rect)