import pygame
import time
import random

pygame.init()
pygame.font.init()
pygame.mixer.init()

windown_x, windown_y = 720, 720
screenWIN = pygame.display.set_mode((windown_x, windown_y))
pygame.display.set_caption("Snake Game")
icon = pygame.image.load('Snake.jpg')
pygame.display.set_icon(icon)
bg = pygame.image.load('background_N.jpg')
bg = pygame.transform.scale(bg, (720, 720))

#snake1
snake_body_1 = pygame.image.load('snake_1.png')
snake_body_2 = pygame.image.load('snake_2.png')
direction = 'RIGHT'
last_rotation = direction
angle = -90
snake_body_1 = pygame.transform.rotate(pygame.transform.scale(snake_body_1, (50, 40)), angle)
x_1, y_1 = 200, 400
speed = 1.5
delta_x, delta_y = speed, 0


def snake_action():
    global x_1, y_1, snake_body_1, snake_body_2
    x_1 += delta_x
    y_1 += delta_y
    print(x_1, y_1)
    screenWIN.blit(bg, (0, 0))
    screenWIN.blit(snake_body_1, (x_1, y_1))
    pygame.display.update()

def game_over(win):
    text = pygame.font.SysFont('System Bold', 50)
    text_surface = text.render('WINNER is '+win+'Snake', True, (255, 0, 0))
    screenWIN.blit(text_surface, (200, 360))
    pygame.display.flip()
    time.sleep(3)
    pygame.quit()
    quit()

def snake_1():
    global x_1, y_1, snake_body_1, delta_x, delta_y, angle, last_rotation, direction
    if event.key == pygame.K_DOWN:
        last_rotation = 'DOWN'
    elif event.key == pygame.K_UP:
        last_rotation = 'UP'
    elif event.key == pygame.K_RIGHT:
        last_rotation = 'RIGHT'
    elif event.key == pygame.K_LEFT:
        last_rotation = 'LEFT'

    # Move
    if last_rotation == 'UP':
        if direction == 'RIGHT':
            angle = 90
            snake_body_1 = pygame.transform.rotate(snake_body_1, angle)
        elif direction == 'LEFT':
            angle = -90
            snake_body_1 = pygame.transform.rotate(snake_body_1, angle)
        elif direction == 'DOWN':
            angle = 180
            snake_body_1 = pygame.transform.rotate(snake_body_1, angle)
        delta_x = 0
        delta_y = -speed

    elif last_rotation == 'DOWN':
        if direction == 'RIGHT':
            angle = -90
            snake_body_1 = pygame.transform.rotate(snake_body_1, angle)
        elif direction == 'LEFT':
            angle = 90
            snake_body_1 = pygame.transform.rotate(snake_body_1, angle)
        elif direction == 'UP':
            angle = 180
            snake_body_1 = pygame.transform.rotate(snake_body_1, angle)
        delta_x = 0
        delta_y = speed
    elif last_rotation == 'RIGHT':
        if direction == 'UP':
            angle = -90
            snake_body_1 = pygame.transform.rotate(snake_body_1, angle)
        elif direction == 'LEFT':
            angle = 180
            snake_body_1 = pygame.transform.rotate(snake_body_1, angle)
        elif direction == 'DOWN':
            angle = 90
            snake_body_1 = pygame.transform.rotate(snake_body_1, angle)
        delta_x = speed
        delta_y = 0
    elif last_rotation == 'LEFT':
        if direction == 'UP':
            angle = 90
            snake_body_1 = pygame.transform.rotate(snake_body_1, angle)
        elif direction == 'DOWN':
            angle = -90
            snake_body_1 = pygame.transform.rotate(snake_body_1, angle)
        elif direction == 'RIGHT':
            angle = 180
            snake_body_1 = pygame.transform.rotate(snake_body_1, angle)
        delta_x = -speed
        delta_y = 0
    direction = last_rotation

running = True
FPS = 60
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            quit()
        if event.type == pygame.KEYDOWN:
            snake_1()
            snake_action()

    if not pygame.event.get():
        snake_action()

    clock.tick(FPS)
