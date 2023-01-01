import pygame, sys
from buttonMenu import Button

from NewMenuSystem import MainMenu

pygame.init()
pygame.font.init()

menu = MainMenu()

#SCREEN = pygame.display.set_mode((1280, 720))
#BG = pygame.image.load("assets/Background.png")
pygame.display.set_caption("GameName")
#SCREEN.blit(BG, (0, 0))
menu.runMenu()



 