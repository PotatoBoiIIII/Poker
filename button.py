import pygame

class Button:
    def __init__(self, x, y, image):
        self.x=x
        self.y=y
        self.image=image
        self.rect=self.image.get_rect()
        self.rect.topleft=(x,y)
        self.clicked=False
    def draw(self, surface):
        action=False
        pos= pygame.mouse.get_pos()
        if self.rect.collidepoint(pos) :
            if pygame.mouse.get_pressed()[0]==1 and self.clicked==False:
                self.clicked=True
                action=True

        surface.blit(self.image, (self.rect.x, self.rect.y))
        if pygame.mouse.get_pressed()[0]==0:
            self.clicked=False
        return action