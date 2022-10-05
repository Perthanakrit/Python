import pygame
import time
import random

pygame.init()
pygame.font.init()

#window
window_x, window_y = 720, 720
screenWIN = pygame.display.set_mode((window_x, window_y))
pygame.display.set_caption("เกมงูที่ไม่ใช่งู")
icon = pygame.image.load('snakeGame\images\Snake.jpg')
pygame.display.set_icon(icon)
bg = pygame.image.load('snakeGame\images\ฺBackground_N.jpg')
bg = pygame.transform.scale(bg, (720, 720))

black = (0, 0, 0)
blue = (0, 0, 255)

#snake1
snake_body_1 = pygame.image.load('snakeGame\images\snake_1.png')
direction = 'RIGHT'
last_rotation = direction
angle = -90
s1_width, s1_height = 55, 45
x_1, y_1 = 200, 400
snake_body_1 = pygame.transform.rotate(pygame.transform.scale(snake_body_1, (s1_width, s1_height)), angle)
snake1_rect = snake_body_1.get_rect()
speed = 2
delta_x, delta_y = speed, 0
score_1 = 0
#snake2
snake_body_2 = pygame.image.load('snakeGame\images\snake_2.png')
direction2 = 'UP'
last_rotation2 = direction2
angle2 = 0
s2_width, s2_height = 50, 40
snake_body_2 = pygame.transform.rotate(pygame.transform.scale(snake_body_2, (s2_width, s2_height)), angle2)
x_2, y_2 = 200, 300
snake2_rect = snake_body_2.get_rect()
speed2 = 2
delta_x_2, delta_y_2 = 0, -speed2
score_2 = 0
#Food
apple = pygame.image.load('snakeGame\images\Apple.png')
apple = pygame.transform.scale(apple, (25, 25))
food_spawn = True
food_x, food_y = random.randint(1, window_x-60), random.randint(1, window_y-60)

def Your_score(score1, score2):
    score_font = pygame.font.SysFont('System Bold', 25)
    value1 = score_font.render("Your Score: " + str(score1), True, black)
    screenWIN.blit(value1, (10, 10))
    value2 = score_font.render("Your Score: " + str(score2), True, blue)
    screenWIN.blit(value2, (600, 10))
    pygame.display.update()

def snake_and_food(color):
    global x_1, y_1, snake_body_1, snake_body_2, x_2, y_2, w, food_x, food_y, score_1, score_2, s1_width, s1_height, s2_width, s2_height

    x_1 += delta_x
    y_1 += delta_y
    screenWIN.blit(bg, (0, 0))
    x_2 += delta_x_2
    y_2 += delta_y_2

    #food and eating
    screenWIN.blit(apple, (food_x, food_y))
    if (10 <= (y_1-food_y) <= 20 or 10 <= (food_y-y_1) <= 20) and (10 <= x_1-food_x <= 30 or 10 <= food_x-x_1 <= 30):
        screenWIN.blit(apple, (food_x, food_y))
        screenWIN.blit(bg, (0, 0))
        food_x, food_y = random.randint(1, window_x - 60), random.randint(1, window_y - 60)
        score_1 += 5

    if (10 <= y_2-food_y <= 20 or 10 <= food_y-y_2 <= 20) and (10 <= x_2-food_x <= 30 or 10 <= food_x-x_2 <= 30):
        screenWIN.blit(apple, (food_x, food_y))
        screenWIN.blit(bg, (0, 0))
        food_x, food_y = random.randint(1, window_x - 60), random.randint(1, window_y - 60)
        score_2 += 5

    screenWIN.blit(snake_body_1, (x_1, y_1))

    if color == 'Blue':
        screenWIN.blit(bg, (0, 0))
    screenWIN.blit(snake_body_2, (x_2, y_2))
    if color == 'Black':
        screenWIN.blit(bg, (0, 0))
        screenWIN.blit(snake_body_1, (x_1, y_1))

    Your_score(score_1, score_2)
    pygame.display.update()

def game_over(win, textColor):
    text = pygame.font.SysFont('System Bold', 50)
    text_surface = text.render('WINNER is '+win+'Snake', True, textColor, (255, 255, 255))
    screenWIN.blit(text_surface, (170, 360))
    pygame.display.update()
    pygame.display.flip()
    time.sleep(4)
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
            angle = 90
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

def snake_2():
    global x_2, y_2, snake_body_2, delta_x_2, delta_y_2, angle2, last_rotation2, direction2
    if event.key == pygame.K_s:
        last_rotation2 = 'DOWN'
    elif event.key == pygame.K_w:
        last_rotation2 = 'UP'
    elif event.key == pygame.K_d:
        last_rotation2 = 'RIGHT'
    elif event.key == pygame.K_a:
        last_rotation2 = 'LEFT'

    # Move
    if last_rotation2 == 'UP':
        if direction2 == 'RIGHT':
            angle2 = 90
            snake_body_2 = pygame.transform.rotate(snake_body_2, angle2)
        elif direction2 == 'LEFT':
            angle2 = -90
            snake_body_2 = pygame.transform.rotate(snake_body_2, angle2)
        elif direction2 == 'DOWN':
            angle2 = 180
            snake_body_2 = pygame.transform.rotate(snake_body_2, angle2)
        delta_x_2 = 0
        delta_y_2 = -speed2

    elif last_rotation2 == 'DOWN':
        if direction2 == 'RIGHT':
            angle2 = -90
            snake_body_2 = pygame.transform.rotate(snake_body_2, angle2)
        elif direction2 == 'LEFT':
            angle2 = 90
            snake_body_2 = pygame.transform.rotate(snake_body_2, angle2)
        elif direction2 == 'UP':
            angle2 = 180
            snake_body_2 = pygame.transform.rotate(snake_body_2, angle2)
        delta_x_2 = 0
        delta_y_2 = speed2
    elif last_rotation2 == 'RIGHT':
        if direction2 == 'UP':
            angle2 = -90
            snake_body_2 = pygame.transform.rotate(snake_body_2, angle2)
        elif direction2 == 'LEFT':
            angle2 = 180
            snake_body_2 = pygame.transform.rotate(snake_body_2, angle2)
        elif direction2 == 'DOWN':
            angle2 = 90
            snake_body_2 = pygame.transform.rotate(snake_body_2, angle2)
        delta_x_2 = speed2
        delta_y_2 = 0
    elif last_rotation2 == 'LEFT':
        if direction2 == 'UP':
            angle2 = 90
            snake_body_2 = pygame.transform.rotate(snake_body_2, angle2)
        elif direction2 == 'DOWN':
            angle2 = -90
            snake_body_2 = pygame.transform.rotate(snake_body_2, angle2)
        elif direction2 == 'RIGHT':
            angle2 = 180
            snake_body_2 = pygame.transform.rotate(snake_body_2, angle2)
        delta_x_2 = -speed2
        delta_y_2 = 0
    direction2 = last_rotation2

w = ''
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
            snake_2()
            snake_and_food(w)
#Food
    if not pygame.event.get():
        snake_and_food(w)
#GAME OVER
    if x_1 > window_x-30 or x_1 < 0 or y_1 > window_y-30 or y_1 < 0:
        w = 'Blue'
        game_over(w, blue)
    elif x_2 > window_x-37 or x_2 < 0 or y_2 > window_y-37 or y_2 < 0:
        w = 'Black'
        game_over(w, black)

    if (0 < x_1-x_2 < 10 or 0 < x_2-x_1 < 20) and (0 < y_1-y_2 < 10 or 0 < y_2-y_1 < 20):
        if score_1 > score_2:
            w = 'Black'
            snake_and_food(w)
            game_over(w, black)
        elif score_1 < score_2:
            w = 'Blue'
            snake_and_food(w)
            game_over(w, blue)

    clock.tick(FPS)
