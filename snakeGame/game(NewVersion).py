import pygame
import time
import random

pygame.init()
pygame.font.init()

window_x, window_y = 1080, 760
screenWIN = pygame.display.set_mode((window_x, window_y))
pygame.display.set_caption("เกมงูไม่ใช่เกมงู")
icon = pygame.image.load('snakeGame\Snake.jpg')
pygame.display.set_icon(icon)
bg = pygame.image.load('snakeGame\ฺBackground_N.jpg')
bg = pygame.transform.scale(bg, (1080, 760))
# FOOD
apple = pygame.image.load('snakeGame\Apple.png')
apple = pygame.transform.scale(apple, (25, 25))
apple_rect = apple.get_rect()
apple_rect.center = (apple.get_width()/2, apple.get_height()/2)
# snake1
snake_body_1 = pygame.image.load('snakeGame\snake_1.png')
snake_body_1 = pygame.transform.rotate(pygame.transform.scale(snake_body_1, (40, 40)), -90)
snake_1_rect = snake_body_1.get_rect()
snake_1_rect.center = (snake_body_1.get_width() / 2, snake_body_1.get_height() / 2)
# snake2
snake_body_2 = pygame.image.load('snakeGame\snake_2.png')
snake_body_2 = pygame.transform.rotate(pygame.transform.scale(snake_body_2, (40, 40)), -90)
snake_2_rect = snake_body_2.get_rect()
snake_2_rect.center = (snake_body_2.get_width() / 2, snake_body_2.get_height() / 2)

class SNAKE_1:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 2
        self.snake1_center = snake_1_rect.center
        self.direction = 'right'
        self.alive = True
        self.recent = self.direction

    def snake_move(self):
        # Key
        if event.key == pygame.K_DOWN:
            self.direction = 'down'
        elif event.key == pygame.K_UP:
            self.direction = 'up'
        elif event.key == pygame.K_LEFT:
            self.direction = 'left'
        elif event.key == pygame.K_RIGHT:
            self.direction = 'right'

    def draw(self, screenWIN):
        global snake_body_1
        # direction
        if self.recent == 'left':
            if self.direction == 'up':
                self.x -= self.speed
                snake_body_1 = pygame.transform.rotate(snake_body_1, -90)
            elif self.direction == 'down':
                snake_body_1 = pygame.transform.rotate(snake_body_1, 90)
            elif self.direction == 'right':
                snake_body_1 = pygame.transform.rotate(snake_body_1, -180)
            self.x -= self.speed
        elif self.recent == 'right':
            if self.direction == 'up':
                snake_body_1 = pygame.transform.rotate(snake_body_1, 90)
            elif self.direction == 'left':
                snake_body_1 = pygame.transform.rotate(snake_body_1, 180)
            elif self.direction == 'down':
                snake_body_1 = pygame.transform.rotate(snake_body_1, -90)
            self.x += self.speed
        elif self.recent == 'up':
            if self.direction == 'down':
                snake_body_1 = pygame.transform.rotate(snake_body_1, 180)
            elif self.direction == 'left':
                snake_body_1 = pygame.transform.rotate(snake_body_1, 90)
            elif self.direction == 'right':
                snake_body_1 = pygame.transform.rotate(snake_body_1, -90)
            self.y -= self.speed
        elif self.recent == 'down':
            if self.direction == 'up':
                snake_body_1 = pygame.transform.rotate(snake_body_1, 180)
            elif self.direction == 'left':
                snake_body_1 = pygame.transform.rotate(snake_body_1, -90)
            elif self.direction == 'right':
                snake_body_1 = pygame.transform.rotate(snake_body_1, 90)
            self.y += self.speed

        self.recent = self.direction
        # draw
        print(self.x, self.y)
        screenWIN.blit(snake_body_1, (self.x, self.y), snake_1_rect)
        #pygame.draw.rect(screenWIN, (255, 0, 0), pygame.Rect(self.x, self.y, 10, 10))
        if self.x > window_x - (FPS // self.speed) or self.x < -5 or self.y > window_y - \
                (FPS // self.speed) or self.y < -5:
            self.alive = False

    def restart_game(self):
        if event.key == pygame.K_r:
            player_1.alive = True
            player_1.x, player_1.y = 200, 300
            player_1.direction = 'right'


player_1 = SNAKE_1(200, 300)


class SNAKE_2:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 0
        self.direction = 'right'
        self.alive = True
        self.recent = self.direction

    def snake_move(self):
        # Key
        if event.key == pygame.K_DOWN:
            self.direction = 'down'
        elif event.key == pygame.K_UP:
            self.direction = 'up'
        elif event.key == pygame.K_LEFT:
            self.direction = 'left'
        elif event.key == pygame.K_RIGHT:
            self.direction = 'right'
    def draw(self, screenWIN):
        global snake_body_2
        # direction
        if self.recent == 'left':
            if self.direction == 'up':
                self.x -= self.speed
                snake_body_2 = pygame.transform.rotate(snake_body_2, -90)
            elif self.direction == 'down':
                snake_body_2 = pygame.transform.rotate(snake_body_2, 90)
            elif self.direction == 'right':
                snake_body_2 = pygame.transform.rotate(snake_body_2, -180)
            self.x -= self.speed
        elif self.recent == 'right':
            if self.direction == 'up':
                snake_body_2 = pygame.transform.rotate(snake_body_2, 90)
            elif self.direction == 'left':
                snake_body_2 = pygame.transform.rotate(snake_body_2, 180)
            elif self.direction == 'down':
                snake_body_2 = pygame.transform.rotate(snake_body_2, -90)
            self.x += self.speed
        elif self.recent == 'up':
            if self.direction == 'down':
                snake_body_2 = pygame.transform.rotate(snake_body_2, 180)
            elif self.direction == 'left':
                snake_body_2 = pygame.transform.rotate(snake_body_2, 90)
            elif self.direction == 'right':
                snake_body_2 = pygame.transform.rotate(snake_body_2, -90)
            self.y -= self.speed
        elif self.recent == 'down':
            if self.direction == 'up':
                snake_body_2 = pygame.transform.rotate(snake_body_2, 180)
            elif self.direction == 'left':
                snake_body_2 = pygame.transform.rotate(snake_body_2, -90)
            elif self.direction == 'right':
                snake_body_2 = pygame.transform.rotate(snake_body_2, 90)
            self.y += self.speed

        self.recent = self.direction
        # draw
        print(self.x, self.y)
        screenWIN.blit(snake_body_2, (self.x, self.y), snake_2_rect)
        # pygame.draw.rect(screenWIN, (255, 0, 0), pygame.Rect(self.x, self.y, 10, 10))
        '''if self.x > window_x - (FPS // self.speed) or self.x < -5 or self.y > window_y - \
                (FPS // self.speed) or self.y < -5:
            self.alive = False'''

player_2 = SNAKE_2(200,500)

class FooD:
    def __init__(self):
        self.food_spawn = True
        self.food_x, self.food_y = random.randint(1, window_x - 60), random.randint(1, window_y - 60)
        self.food_center = apple_rect

    def draw(self):
        if (10 < player_1.x - self.food_x < 30 or 10 < self.food_x - player_1.y < 30) and \
                (10 < self.food_y - player_1.y < 20 or 5 < player_1.y - self.food_y < 20):
            self.food_spawn = False

        if not self.food_spawn:
            self.food_x, self.food_y = random.randint(1, window_x - 60), random.randint(1, window_y - 60)
            self.food_spawn = True

        print('Food', self.food_x, self.food_y)
        screenWIN.blit(apple, (self.food_x, self.food_y))


spwan_food = FooD()


def draw_game():
    screenWIN.blit(bg, (0, 0))
    # Spawn food
    # Draw plater
    player_1.draw(screenWIN)
    player_2.draw(screenWIN)
    spwan_food.draw()
    #
    if player_1.alive == False:
        font = pygame.font.SysFont('System Bold', 50)
        text = font.render('Click R to Restart', True, (255, 255, 255))
        textrect = text.get_rect()
        textrect.center = (window_x // 2, window_y // 2)
        screenWIN.fill((0, 0, 0), None)
        screenWIN.blit(text, textrect)
        pygame.display.update()
        time.sleep(5)

    pygame.display.update()


def main_game():
    pass

running = True
FPS = 60
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            quit()
        if event.type == pygame.KEYDOWN:
            player_1.snake_move()
            player_1.restart_game()
    if not pygame.event.get():
        draw_game()

    clock.tick(FPS)

