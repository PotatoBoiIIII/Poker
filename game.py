import pygame
screen = pygame.display.set_mode((500,500))


run=True
while run:
    screen.fill((255,255,255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False
    pygame.display.update()
pygame.quit()


        

