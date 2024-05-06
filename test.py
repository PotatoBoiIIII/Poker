import pygame
import button
import slider

screen=pygame.display.set_mode((800,800))
pygame.font.init()
number_font=pygame.font.SysFont("comicsans", 15)
img= pygame.transform.scale(pygame.image.load("Assets/spaceship_red.png"), (50,50))
img2=pygame.transform.scale(pygame.image.load("images/pixil-frame-0.png"), (27*3, 38*3))

run=True
while run:
    screen.fill((0,0,0))
    screen.blit(img2, (100,100))

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False









    pygame.display.update()

pygame.quit()