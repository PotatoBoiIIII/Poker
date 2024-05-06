import pygame
import button
WIDTH=800
HEIGHT=800

start_img=pygame.transform.scale(pygame.image.load("Assets/spaceship_red.png"), (50,50))
exit_img=pygame.transform.scale(pygame.image.load("Assets/spaceship_yellow.png"), (50,50))

screen= pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("BUTTONS")



start_button=button.Button(100, 200, start_img)
exit_button=button.Button(400,200, exit_img)

run=True

while run:
    screen.fill((202,228, 241))
    if start_button.draw(screen):
        print("start")
    if exit_button.draw(screen):
        run=False
    for event in pygame.event.get():

        if event.type ==pygame.QUIT:
            run=False

    pygame.display.update()

pygame.quit()
