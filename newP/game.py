import os, time, pygame

from states.title import Title

class Game():
    def __init__(self):
        pygame.init()
        self.GAME_W, self.GAME_H = 1280, 800
        self.SCREEN_WIDTH,self.SCREEN_HEIGHT = 1280, 800
        self.game_canvas = pygame.Surface((self.GAME_W, self.GAME_H))
        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH,self.SCREEN_HEIGHT))
        self.pygame_icon = pygame.image.load("_assets\images\Snake.jpg")
        pygame.display.set_icon(self.pygame_icon)
        self.GameName = pygame.display.set_caption('Just Not Snake')
        self.running, self.playing = True, True
        self.actions = {"left": False, "right": False, "up" : False, "down" : False,   "action1" : False, "action2" : False, "start" : False,
         "up_arrow":False, "down_arrow":False,"right_arrow":False,"left_arrow":False, "leftClick" : False, "rightClick" : False}
        
        self.dt, self.prev_time = 0, 0
        self.state_stack = []
        self.clock = pygame.time.Clock()
        self.FPS = 60
        self.load_assets(20)
        self.load_states()

    def game_loop(self):
        while self.playing:
            self.get_dt()
            self.get_events()
            self.update()
            self.render()


    def get_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False

            if event.type == pygame.KEYDOWN:
                #WASD
                    if event.key == pygame.K_ESCAPE:
                        self.playing = False
                        self.running = False
                    if event.key == pygame.K_a:
                        self.actions['left'] = True
                    if event.key == pygame.K_d:
                        self.actions['right'] = True
                    if event.key == pygame.K_w:
                        self.actions['up'] = True
                    if event.key == pygame.K_s:
                        self.actions['down'] = True
                    if event.key == pygame.K_p:
                        self.actions['action1'] = True
                    if event.key == pygame.K_o:
                        self.actions['action2'] = True    
                    if event.key == pygame.K_RETURN:
                        self.actions['start'] = True  
                #Arrow
                    if event.key == pygame.K_UP:
                        self.actions['up_arrow'] = True
                    if event.key == pygame.K_DOWN:
                        self.actions['down_arrow'] = True
                    if event.key == pygame.K_RIGHT:
                         self.actions['right_arrow'] = True
                    if event.key == pygame.K_LEFT:
                        self.actions['left_arrow'] = True

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    self.actions['left'] = False
                if event.key == pygame.K_d:
                    self.actions['right'] = False
                if event.key == pygame.K_w:
                    self.actions['up'] = False
                if event.key == pygame.K_s:
                    self.actions['down'] = False
                if event.key == pygame.K_p:
                    self.actions['action1'] = False
                if event.key == pygame.K_o:
                    self.actions['action2'] = False
                if event.key == pygame.K_RETURN:
                    self.actions['start'] = False 
                if event.key == pygame.K_UP:
                    self.actions['up_arrow'] = False
                if event.key == pygame.K_DOWN:
                    self.actions['down_arrow'] = False
                if event.key == pygame.K_RIGHT:
                        self.actions['right_arrow'] = False
                if event.key == pygame.K_LEFT:
                    self.actions['left_arrow'] = False 

            if (event.type == pygame.MOUSEBUTTONDOWN):
                self.actions['leftClick'] = True

    def update(self):
         self.state_stack[-1].update(self.dt,self.actions)

    def render(self):
        
        # Render current state to the screen
        self.screen.blit(pygame.transform.scale(self.game_canvas,(self.SCREEN_WIDTH, self.SCREEN_HEIGHT)), (0,0))
        self.state_stack[-1].render(self.game_canvas)
        self.clock.tick(self.FPS)
        pygame.display.flip()
        #pygame.display.update()
    
    def get_dt(self):
        now = time.time()
        self.dt = now - self.prev_time
        self.prev_time = now
    
    def draw_text(self, surface, text, color, x, y):
        text_surface = self.font.render(text, True, color)
        #text_surface.set_colorkey((0,0,0))
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y)
        surface.blit(text_surface, text_rect)
    
    def load_assets(self, fontsize):
        # Create pointers to directories 
        self.assets_dir = os.path.join("_assets")
        self.sprite_dir = os.path.join(self.assets_dir, "sprites")
        self.font_dir = os.path.join(self.assets_dir, "font")
        self.font= pygame.font.Font(os.path.join(self.font_dir, "PressStart2P-Regular.ttf"), fontsize)

    def load_states(self):
            self.title_screen = Title(self)
            self.state_stack.append(self.title_screen)

    def reset_keys(self):
        for action in self.actions:
            self.actions[action] = False
            

if __name__ == "__main__":
    g = Game()
    while g.running:
        g.game_loop()
