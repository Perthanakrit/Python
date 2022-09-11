import pygame

pygame.init()

screenWIN = pygame.display.set_mode((720, 720))
pygame.display.set_caption("Snake Game")
one_body = pygame.image.load('snake_1.png')
bg = pygame.image.load('background_N.jpg')
bg = pygame.transform.scale(bg, (720, 720))
one_body = pygame.transform.rotate(pygame.transform.scale(one_body, (20, 20)), -45)
x, y = 200, 400
delta_x, delta_y = 0, 0
def player():
    global x, y
    x += delta_x
    y += delta_y

    screenWIN.blit(bg, (0, 0))
    one_body_rect = one_body.get_rect()
    screenWIN.blit(one_body, (x, y))
    print(x, y)
    pygame.display.update()


def game_over():
    pass
clock = pygame.time.Clock()
FPS = 60

running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            quit()


            player()
    if not pygame.event.get():
        player()
    clock.tick(FPS)



