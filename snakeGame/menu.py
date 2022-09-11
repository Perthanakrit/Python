import pygame


class Menu:
    def __init__(self, class_game):
        self.game = class_game
        self.mid_w, self.mid_h = self.game.window_w/2, self.game.window_h/2
        self.run_display = True
        self.cursor_rect = pygame.Rect(0, 0, 20, 20)
        self.offset = -100
        self.run_startMenu = False
        self.run_Options = False

    def draw_cursor(self):
        self.game.draw_text('>', 15, self.cursor_rect.x, self.cursor_rect.y)

    def bitl_screen(self):
        self.game.window.blit(self.game.display, (0, 0))
        pygame.display.update()
        self.game.reset_key()


class MainMenu(Menu):
    def __init__(self, class_game):
        Menu.__init__(self, class_game)
        self.state = 'Start'
        self.start_x, self.start_y = self.mid_w, self.mid_h + 30
        self.option_x, self.option_y = self.mid_w, self.mid_h + 80
        self.cursor_rect.midtop = (self.start_x + self.offset, self.start_y)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display.fill(self.game.Black)
            self.game.draw_text('Main Menu', 100, self.game.window_w/2, self.game.window_h/2 - 100)
            self.game.draw_text('Start Game', 50, self.start_x, self.start_y)
            self.game.draw_text('Options', 50, self.option_x, self.option_y)
            self.draw_cursor()
            self.bitl_screen()

    def move_cursor(self):
        if self.game.DOWN_KEY:
            if self.state == 'Start':
                self.cursor_rect.midtop = (self.option_x + self.offset, self.option_y)
                self.state = 'Options'
            elif self.state == 'Options':
                self.cursor_rect.midtop = (self.start_x + self.offset, self.start_y)
                self.state = 'Start'
        elif self.game.UP_KEY:
            if self.state == 'Start':
                self.cursor_rect.midtop = (self.option_x + self.offset, self.option_y)
                self.state = 'Options'
            elif self.state == 'Options':
                self.cursor_rect.midtop = (self.start_x + self.offset, self.start_y)
                self.state = 'Start'
        print(self.state)


    def check_input(self):
        self.move_cursor()
        if self.game.START_KEY:
            if self.state == 'Start':
                self.run_startMenu = True
                self.run_Options = False
            elif self.state == 'Options':
                self.run_Options = True
                self.run_startMenu = False
            self.run_display = False


class start_menu(Menu):
    def __init__(self, class_game):
        Menu.__init__(self, class_game)
        self.state = '1 player'
        self.one_player_x, self.one_player_y = self.mid_w, self.mid_h + 30
        self.two_player_x, self.two_player_y = self.mid_w, self.mid_h + 80
        self.cursor_rect.midtop = (self.one_player_x + self.offset, self.one_player_y)
        self.onOroff = False

    def player_display(self):
        while self.run_startMenu:
            self.game.check_events()
            self.check_input()
            self.game.display.fill(self.game.Black)
            self.game.draw_text('1 player', 50, self.one_player_x, self.one_player_y)
            self.game.draw_text('2 player', 50, self.two_player_x, self.two_player_y)
            self.draw_cursor()
            self.bitl_screen()

    def move_cursor(self):
        if self.game.DOWN_KEY:
            if self.onOroff:
                pass
            if self.state == '1 player':
                self.cursor_rect.midtop = (self.two_player_x + self.offset, self.two_player_y)
                self.state = '2 player'
            elif self.state == '2 player':
                self.cursor_rect.midtop = (self.one_player_x + self.offset, self.one_player_y)
                self.state = '1 player'

        elif self.game.UP_KEY:
            if self.state == '1 player':
                self.cursor_rect.midtop = (self.two_player_x + self.offset, self.two_player_y)
                self.state = '2 player'
            elif self.state == '2 player':
                self.cursor_rect.midtop = (self.one_player_x + self.offset, self.one_player_y)
                self.state = '1 player'

    def onlineORoffline(self):
        self.game.draw_text('Online', 40, self.one_player_x, self.one_player_y+40)
        self.game.draw_text('Offline', 40, self.two_player_x, self.two_player_y+60)
        self.draw_cursor()
        self.bitl_screen()

    def check_input(self):
        self.move_cursor()
        if self.game.START_KEY:
            if self.state == '1 player':
                self.game.playing = True
                self.game.stop_game = False
                self.run_startMenu = False
            elif self.state == '2 player':
                self.onlineORoffline()
                self.onOroff = True
        elif self.game.BACK_KEY:
            self.run_startMenu = False

class Options(Menu):
    def __init__(self, class_game):
        Menu.__init__(self, class_game)
        self.one_player_x, self.one_player_y = self.mid_w, self.mid_h + 30
        self.two_player_x, self.two_player_y = self.mid_w, self.mid_h + 80
        self.cursor_rect.midtop = (self.one_player_x + self.offset, self.one_player_y)

    def player_display(self):
        while self.run_Options:
            self.game.display.fill(self.game.Black)
            self.game.draw_text('SFX', 50, self.one_player_x, self.one_player_y)
            self.game.draw_text('Music', 50, self.two_player_x, self.two_player_y)
            self.draw_cursor()
            self.bitl_screen()

