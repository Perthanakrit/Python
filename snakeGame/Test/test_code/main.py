from class_game import Game
import pygame

g = Game()

while g.running:
    # g.playing = True
    pygame.display.set_caption(g.caption)
    pygame.display.set_icon(g.icon)

    '''g.curr_menu.display_menu()
    g.ply_menu.player_display()
    g.ply_options.player_display()'''
    g.game_loop()
