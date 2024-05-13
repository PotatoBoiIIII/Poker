import pygame

class Player:
    def __init__(self):
        self.folded=False
        self.money = 1000
        self.call = 0
        self.isRaising=False
        self.has_cards=False
        self.last_move = ""
    def set_money(self, change):
        self.money+=change
    def set_folded(self, folded):
        self.folded=folded

    def set_call(self, amt):
        self.call=amt
    def set_isRaising(self, isRaising):
        self.isRaising=isRaising
    def set_cards(self, card1, card2):
        self.card1=card1
        self.card2=card2
    def set_has_cards(self, has_cards):
        self.has_cards=has_cards
    def set_last_move(self, last_move):
        self.last_move=last_move