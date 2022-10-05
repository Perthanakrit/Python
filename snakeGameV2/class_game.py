import pygame
import time
import random
from Character import *

pygame.init()
pygame.font.init()

class Game():
    def __init__(self):
        pygame.init()
        self.running, self.playing = True, False
        self.stop_game = False
        self.window_w, self.window_h = 1080, 760
        self.window = pygame.display.set_mode((self.window_w, self.window_h))
        self.display = pygame.Surface((self.window_w, self.window_h))
        self.caption = 'Snake Game'
        self.icon = pygame.image.load('Snake.jpg')
        self.bg = pygame.image.load('background_N.jpg')
        self.bg = pygame.transform.scale(self.bg, (1080, 760))
        self.font_name = 'System Bold'
        self.White = (255, 255, 255)
        self.Black = (0, 0, 0)
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False
        # Function Menu
        self.curr_menu, self.ply_menu, self.ply_options = MainMenu(self), start_menu(self), Options(self)
        self.FPS = 60
        self.clock = pygame.time.Clock()
        self.xsnake_1, self.ysnake_1 = 200, 400
        self.xsnake_2, self.ysnake_2 = 300, 500
        self.snake, self.snake2 = SNAKE_1(self.xsnake_1, self.ysnake_1), SNAKE_2(self.xsnake_2, self.ysnake_2)

    def game_loop(self):
        while self.playing:
            self.check_events()
            # self.draw_text('Thanks', 20, self.window_w / 2, self.window_h / 2)
            self.window.blit(self.bg, (0, 0))
            # snake_1
            if not pygame.event.get():
                self.snake.draw()
            self.window.blit(self.snake.snake_body_1, (self.snake.x, self.snake.y))
            # snake_2
            self.window.blit(self.snake2.snake_body_2, (self.xsnake_2, self.ysnake_2))
            # return to Menu
            if self.stop_game:
                self.exit_screen()

            self.clock.tick(self.FPS)
            pygame.display.update()

    def check_events(self):
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                self.running, self.playing = False, False
                self.curr_menu.run_display, self.ply_menu.run_startMenu, self.ply_options.run_Options = False, False, False
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
                if ev.key == pygame.K_w:
                    pass

    def reset_key(self):
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False
        self.snake.direction = 'right'

    def reset_game(self):
        self.snake.direction = 'right'
        self.snake.x, self.snake.y = self.xsnake_1, self.ysnake_1

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
            font = pygame.font.SysFont('System Bold', 50)
            text = font.render('Y to return to The Menu' + '\n' + 'N to continue', True, (255, 255, 255))
            textrect = text.get_rect()
            textrect.center = (self.window_w / 2, self.window_h / 2)
            self.window.fill((0, 0, 0), None)
            self.window.blit(text, textrect)
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_y:
                        pause = False
                        self.playing = False
                        self.curr_menu.run_display = True
                        self.reset_game()
                        self.stop_game = False
                    if e.key == pygame.K_n:
                        pause = False
                        self.playing = True
                        self.stop_game = False
            pygame.display.update()
