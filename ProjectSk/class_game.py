
from turtle import right
import pygame
import time
import random
from Character import *
from main import *


class Game():
    def __init__(self):
        pygame.init()
        #self.running = True
        self.running, self.playing = True, True
        self.runMainGame = False
        self.stop_game = False
        self.window_w, self.window_h = 1080, 760
        self.window = pygame.display.set_mode((self.window_w, self.window_h))
        self.display = pygame.Surface((self.window_w, self.window_h))
        self.caption = 'Snake Game'
        self.icon = pygame.image.load('assets\images\Snake.jpg')
        self.bg = pygame.image.load('assets\images\ฺBackground_N.jpg')
        self.bg = pygame.transform.scale(self.bg, (1080, 760))
        self.font_name = 'System Bold'
        self.White = (255, 255, 255)
        self.Black = (0, 0, 0)
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False
        # Function Menu
        self.runningmenu = play()
        self.Menu = main_menu(True)
        #self.ms = menuSystem.mainmenu(self.runningmenu)
        #self.curr_menu, self.ply_menu, self.ply_options = MainMenu(self), start_menu(self), Options(self)
        self.FPS = 60
        self.clock = pygame.time.Clock()
        self.xsnake_1, self.ysnake_1 = 200, 400
        self.xsnake_2, self.ysnake_2 = 300, 500
        self.snake, self.snake2 = SNAKE_1(self.xsnake_1, self.ysnake_1), SNAKE_2(self.xsnake_2, self.ysnake_2)
        #Food 
        self.food = pygame.image.load('assets\images\Apple.png')
        self.food_x_pos, self.food_y_pos = random.randint(1, self.window_w-60), random.randint(1, self.window_h-60)
        #food_x, food_y = random.randint(1, window_x-60), random.randint(1, window_y-60)
        self.apple = pygame.transform.scale(self.food, (25, 25))

    def GameManager(self):
        while self.playing:    
            print(self.runningmenu)
            if (self.runningmenu == False):
                self.game_loop()
                self.Menu = main_menu(False)
            else:
                self.Menu
                

    def game_loop(self):         
        self.check_events()
        # self.draw_text('Thanks', 20, self.window_w / 2, self.window_h / 2)
        self.window.blit(self.bg, (0, 0))
        # snake_1
        if not pygame.event.get():
            self.snake.draw()
            self.snake2.draw()
            
        self.window.blit(self.snake.snake_body_1, (self.snake.x, self.snake.y))
        # snake_2
        
        self.window.blit(self.snake2.snake_body_2, (self.snake2.x, self.snake2.y))
        # return to Menu
        if self.stop_game:
            self.exit_screen()

    #GAME OVER
        if((self.snake.x > self.window_w or self.snake.x < -40)  or (self.snake.y > self.window_h or self.snake.y < -40)):
            self.gameOver(self.snake2.name, self.snake2.blue)
        elif((self.snake2.x > self.window_w or self.snake2.x < -40)  or (self.snake2.y > self.window_h or self.snake2.y < -40)):
            self.gameOver(self.snake.name, self.snake.black)
    #Spwanin Food
        self.spwan_food()

        self.clock.tick(self.FPS)
        pygame.display.update()

    def check_events(self):
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                # self.running 
                self.playing = False
                #self.curr_menu.run_display, self.ply_menu.run_startMenu, self.ply_options.run_Options = False, False, False
                quit()
            if ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_RETURN:  # Enter key
                    self.START_KEY = True
                if ev.key == pygame.K_BACKSPACE:
                    self.BACK_KEY = True
                if ev.key == pygame.K_ESCAPE:
                    self.stop_game = True
                    self.BACK_KEY = True
                if ev.key == pygame.K_UP:
                    self.UP_KEY = True
                    self.snake.direction = 'up'
                elif ev.key == pygame.K_DOWN:
                    self.DOWN_KEY = True
                    self.snake.direction = 'down'
                elif ev.key == pygame.K_LEFT:
                    self.snake.direction = 'left'
                elif ev.key == pygame.K_RIGHT:
                    self.snake.direction = 'right'
                #
                if ev.key == pygame.K_w:
                    self.snake2.direction = 'up'                  
                elif ev.key == pygame.K_s:
                    self.snake2.direction = 'down'                 
                elif ev.key == pygame.K_a:
                    self.snake2.direction = 'left'                   
                elif ev.key == pygame.K_d:
                    self.snake2.direction = 'right'
                    

    def reset_key(self):
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False
        self.snake.direction = 'right'
        self.snake2.direction = 'right'

    def reset_game(self):
        self.snake.direction = 'right'
        self.snake2.direction = 'right'
        self.snake.x, self.snake.y = self.xsnake_1, self.ysnake_1
        self.snake2.x, self.snake2.y =self.xsnake_2, self.ysnake_2

    def draw_text(self, text, size, x, y):
        font = pygame.font.SysFont(self.font_name, size)
        text_surface = font.render(text, True, self.White)
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y)
        self.display.blit(text_surface, text_rect)

    def exit_screen(self):
        pause = True
        while pause:
            self.playing = False
            #mS.main_menu(True)
            
            font = pygame.font.SysFont('System Bold', 50)
            text = font.render('Y to return to The Menu' , True, (255, 255, 255))
            textrect = text.get_rect()
            textrect.center = (self.window_w / 2, self.window_h / 2)
            self.window.fill((0, 0, 0), None)
            self.window.blit(text, textrect)

            textN = font.render('N to continue', True, (255, 255, 255))
            textNrect = textN.get_rect()
            textNrect.center = (self.window_w / 2, (self.window_h / 2)+50)
            
            self.window.blit(textN, textNrect)

            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_y:
                        pause = False
                        self.playing = False
                        main_menu(True)
                        #self.curr_menu.run_display = True
                        self.reset_game()
                        self.stop_game = False
                    if e.key == pygame.K_n:
                        pause = False
                        self.playing = True
                        self.stop_game = False
            pygame.display.update()

    def gameOver(self,win, textColor):
        text = pygame.font.SysFont('System Bold', 50)
        text_surface = text.render('WINNER is '+win+'Snake', True, textColor, (255, 255, 255))
        self.window.blit(text_surface, (170, 360))
        pygame.display.update()
        pygame.display.flip()
        time.sleep(4)
        #pygame.quit()
        #quit()
    
    def spwan_food(self):
        self.window.blit(self.apple, (self.food_x_pos, self.food_y_pos))
        if (10 <= (self.snake.y -self.food_y_pos) <= 20 or 10 <= (self.food_y_pos-self.snake.y) <= 20) and (10 <= self.snake.x-self.food_x_pos <= 30 or 10 <= self.food_x_pos-self.food_x_pos <= 30):
            self.window.blit(self.apple, (self.food_x_pos, self.food_y_pos))
            self.window.blit(self.bg, (0, 0))
            self.food_x_pos, self.food_y_pos = random.randint(1, self.window_w - 60), random.randint(1, self.window_h - 60)
            #score_1 += 5

        if (10 <= self.snake2.y -self.food_y_pos <= 20 or 10 <= self.food_y_pos-self.snake2.y <= 20) and (10 <= self.snake2.x-self.food_x_pos <= 30 or 10 <= self.food_x_pos-self.snake2.x <= 30):
            self.window.blit(self.apple, (self.food_x_pos, self.food_y_pos))
            self.window.blit(self.bg, (0, 0))
            self.food_x_pos, self.food_y_pos = random.randint(1, self.window_w - 60), random.randint(1, self.window_h - 60)
            #score_2 += 5

    def MainMenu(self):
        self.Menu


if __name__ == "__main__":
    g = Game()
    while g.running:
        g.GameManager()
#c1.game_loop()