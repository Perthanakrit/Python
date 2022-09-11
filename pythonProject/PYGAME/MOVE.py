import pygame

pygame.init()


display = pygame.display.set_mode((1150, 700))

clock = pygame.time.Clock()
FPS = 30

x = 0
y = 350
while True:
    # check exit event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # check user input

    # compute
    display.fill('white')
    pygame.draw.circle(display, 'red', (x, y), 50)

    # wait
    clock.tick(FPS)

    # display to player
    pygame.display.update()

    x += 1
