from tkinter import Menu
from tkinter.tix import Tree
import pygame, sys
from buttonMenu import Button
from class_game import Game

pygame.init()
pygame.font.init()

class MainMenu():
    def __init__(self):
        self.runningmenu, self.optionRun = True, True
        self.SCREEN = pygame.display.set_mode((1280, 720))
        self.BG = pygame.image.load("assets/Background.png")
        #display menu
        self.centerX = 550
        self.MENU_MOUSE_POS = pygame.mouse.get_pos()
        self.g = Game()
        #Opition
        self.playButton = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(self.centerX, 250), 
                            text_input="PLAY", font=self.get_font(75), base_color="#d7fcd4", hovering_color="White")
        self.optionButton =  Button(image=pygame.image.load("assets/Options Rect.png"), pos=(self.centerX, 400), 
                                text_input="OPTIONS", font=self.get_font(75), base_color="#d7fcd4", hovering_color="White")
        self.quitButton =  Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(self.centerX, 550), 
                                text_input="QUIT", font=self.get_font(75), base_color="#d7fcd4", hovering_color="White")

    def get_font(self, size): # Returns Press-Start-2P in the desired size
        return pygame.font.Font("assets/font.ttf", size)
    
    def play(self):
        self.g.game_loop()
    
    def options(self):
        
        backTomenu = True
        while self.optionRun:
            OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

            self.SCREEN.fill("white")

            OPTIONS_TEXT = self.get_font(45).render("This is the OPTIONS screen.", True, "Black")
            OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 260))
            self.SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

            OPTIONS_BACK = Button(image=None, pos=(640, 460), 
                                text_input="BACK", font=self.get_font(75), base_color="Black", hovering_color="Green")

            OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
            OPTIONS_BACK.update(self.SCREEN)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                        #optionRun = False
                        self.runMenu()

            pygame.display.update()

    def runMenu(self):
        while self.runningmenu:
            self.SCREEN.blit(self.BG, (0, 0))

            MENU_MOUSE_POS = pygame.mouse.get_pos()
            MENU_TEXT = self.get_font(100).render("MAIN MENU", True, "#b68f40")
            MENU_RECT = MENU_TEXT.get_rect(center=(self.centerX, 100))

            PLAY_BUTTON = self.playButton
            OPTIONS_BUTTON =  self.optionButton
            QUIT_BUTTON =  self.quitButton

            self.SCREEN.blit(MENU_TEXT, MENU_RECT)

            lstB = [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]

            for button in lstB:
                
                button.changeColor(MENU_MOUSE_POS)
                button.update(self.SCREEN)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            # Events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                        #running = False
                        self.play()
                        
                    if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                        #running = False
                        self.runningmenu = False
                        self.options()
                        
                    if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                        pygame.quit()
                        sys.exit()

            pygame.display.update()