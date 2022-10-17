import pygame

pygame.init()
pygame.font.init()

class SNAKE_1:
    def __init__(self, x, y):
        self.snake_body_1 = pygame.image.load('assets\images\snake_1.png')
        self.snake_body_1 = pygame.transform.rotate(pygame.transform.scale(self.snake_body_1, (40, 40)), -90)
        self.snake_1_rect = self.snake_body_1.get_rect()
        self.snake_1_rect.center = (self.snake_body_1.get_width() / 2, self.snake_body_1.get_height() / 2)
        self.name = 'black'
        self.black = (0, 0, 0)
        
        self.speed = 2
        self.x, self.y = x, y
        self.snake1_center = self.snake_1_rect.center
        self.direction = 'right'
        self.alive = True
        self.recent = self.direction

        self.score = 0;

    def draw(self):
        
        if self.recent == 'left':
            if self.direction == 'up':
                self.x -= self.speed
                self.snake_body_1 = pygame.transform.rotate(self.snake_body_1, -90)
            elif self.direction == 'down':
                self.snake_body_1 = pygame.transform.rotate(self.snake_body_1, 90)
            elif self.direction == 'right':
                self.snake_body_1 = pygame.transform.rotate(self.snake_body_1, -180)
            self.x -= self.speed
        elif self.recent == 'right':
            if self.direction == 'up':
                self.snake_body_1 = pygame.transform.rotate(self.snake_body_1, 90)
            elif self.direction == 'left':
                self.snake_body_1 = pygame.transform.rotate(self.snake_body_1, 180)
            elif self.direction == 'down':
                self.snake_body_1 = pygame.transform.rotate(self.snake_body_1, -90)
            self.x += self.speed
        elif self.recent == 'up':
            if self.direction == 'down':
                self.snake_body_1 = pygame.transform.rotate(self.snake_body_1, 180)
            elif self.direction == 'left':
                self.snake_body_1 = pygame.transform.rotate(self.snake_body_1, 90)
            elif self.direction == 'right':
                self.snake_body_1 = pygame.transform.rotate(self.snake_body_1, -90)
            self.y -= self.speed
        elif self.recent == 'down':
            if self.direction == 'up':
                self.snake_body_1 = pygame.transform.rotate(self.snake_body_1, 180)
            elif self.direction == 'left':
                self.snake_body_1 = pygame.transform.rotate(self.snake_body_1, -90)
            elif self.direction == 'right':
                self.snake_body_1 = pygame.transform.rotate(self.snake_body_1, 90)
            self.y += self.speed
        self.recent = self.direction

class SNAKE_2:
    def __init__(self, x, y):
        self.snake_body_2 = pygame.image.load('assets\images\snake_2.png')
        self.snake_body_2 = pygame.transform.rotate(pygame.transform.scale(self.snake_body_2, (40, 40)), -90)
        self.snake_2_rect = self.snake_body_2.get_rect()
        self.snake_2_rect.center = (self.snake_body_2.get_width() / 2, self.snake_body_2.get_height() / 2)
        self.name = 'blue'
        self.blue = (0, 0, 255)
        self.speed = 2
        self.x, self.y = x, y
        self.snake2_center = self.snake_2_rect.center
        self.direction = 'right'
        self.alive = True
        self.recent = self.direction
        
        self.score = 0;

    def draw(self):
        if self.recent == 'left':
            if self.direction == 'up':
                self.x -= self.speed
                self.snake_body_2 = pygame.transform.rotate(self.snake_body_2, -90)
            elif self.direction == 'down':
                self.snake_body_2 = pygame.transform.rotate(self.snake_body_2, 90)
            elif self.direction == 'right':
                self.snake_body_2 = pygame.transform.rotate(self.snake_body_2, -180)
            self.x -= self.speed
        elif self.recent == 'right':
            if self.direction == 'up':
                self.snake_body_2 = pygame.transform.rotate(self.snake_body_2, 90)
            elif self.direction == 'left':
                self.snake_body_2 = pygame.transform.rotate(self.snake_body_2, 180)
            elif self.direction == 'down':
                self.snake_body_2 = pygame.transform.rotate(self.snake_body_2, -90)
            self.x += self.speed
        elif self.recent == 'up':
            if self.direction == 'down':
                self.snake_body_2 = pygame.transform.rotate(self.snake_body_2, 180)
            elif self.direction == 'left':
                self.snake_body_2 = pygame.transform.rotate(self.snake_body_2, 90)
            elif self.direction == 'right':
                self.snake_body_2 = pygame.transform.rotate(self.snake_body_2, -90)
            self.y -= self.speed
        elif self.recent == 'down':
            if self.direction == 'up':
                self.snake_body_2 = pygame.transform.rotate(self.snake_body_2, 180)
            elif self.direction == 'left':
                self.snake_body_2 = pygame.transform.rotate(self.snake_body_2, -90)
            elif self.direction == 'right':
                self.snake_body_2 = pygame.transform.rotate(self.snake_body_2, 90)
            self.y += self.speed
        self.recent = self.direction