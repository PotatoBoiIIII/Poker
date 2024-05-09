import pygame
class Card:
    def __init__(self, number, suite, img):
        self.img=img
        self.suite=suite
        self.number=number
        if self.number=="A":
            self.value=14
        elif self.number=="J":
            self.value=11
        elif self.number=="Q":
            self.value=12
        elif self.number=="K":
            self.value=13
        else:
            self.value=int(self.number)

    def print_Card(self, screen, x, y):
        screen.blit(self.img, (x,y))
