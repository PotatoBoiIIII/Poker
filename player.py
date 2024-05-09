import pygame

class Player:
    def __init__(self):
        self.folded=False
        self.money = 1000
        self.call = 0
        self.isRaising=False
    def set_money(self, change):
        self.money+=change
    def set_folded(self, folded):
        self.folded=folded

    def set_call(self, amt):
        self.call=amt
    def set_isRaising(self, isRaising):
        self.isRaising=isRaising
