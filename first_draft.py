import pygame
import random
import numpy as np

WIDTH=1000
HEIGHT=800

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Poker")

global pot_amt
pot_amt=0

class card:
    def __init__(self, number, suite):
        self.number=number
        self.suite=suite
        if number =="J":
            self.value=11
        elif number=="Q":
            self.value=12
        elif number=="K":
            self.value=13
        elif number=="A":
            self.value=14
        else:
            self.value=int(number)
global cards
cards= [
    [card("A", "\u2665"), card("2", "\u2665"), card("3", "\u2665"), card("4", "\u2665"), card("5", "\u2665"), card("6", "\u2665"), card("7", "\u2665"), card("8", "\u2665"), card("9", "\u2665"), card("10", "\u2665"), card("J", "\u2665"), card("Q", "\u2665"), card("K", "\u2665"), ],
    [card("A", "\u2663"), card("2", "\u2663"), card("3", "\u2663"), card("4", "\u2663"), card("5", "\u2663"), card("6", "\u2663"), card("7", "\u2663"), card("8", "\u2663"), card("9", "\u2663"), card("10", "\u2663"), card("J", "\u2663"), card("Q", "\u2663"), card("K", "\u2663"), ],
    [card("A", "\u2666"), card("2", "\u2666"), card("3", "\u2666"), card("4", "\u2666"), card("5", "\u2666"), card("6", "\u2666"), card("7", "\u2666"), card("8", "\u2666"), card("9", "\u2666"), card("10", "\u2666"), card("J", "\u2666"), card("Q", "\u2666"), card("K", "\u2666"), ],
    [card("A", "\u2660"), card("2", "\u2660"), card("3", "\u2660"), card("4", "\u2660"), card("5", "\u2660"), card("6", "\u2660"), card("7", "\u2660"), card("8", "\u2660"), card("9", "\u2660"), card("10", "\u2660"), card("J", "\u2660"), card("Q", "\u2660"), card("K", "\u2660"), ],

]
def printCard(card, row, column):
    #frame=LabelFrame(root, padx=50, pady=100, borderwidth=5, relief=RAISED, fg="red", )
    if card.suite=="\u2665"or card.suite=="\u2666":
        card = Label(root, text=str(card.number) + " of " + card.suite, borderwidth=3, relief=RAISED, padx=20, pady=40, fg='red')
    else:
        card=Label(root, text=str(card.number)+" of "+card.suite, borderwidth=3, relief=RAISED, padx=20, pady=40)
    #frame.pack()
    card.grid(row=row, column=column)

def revealCard():
    printCard(getRandCard(cards), 0, 1)
    global btn_check
    btn_check['state']=DISABLED
    global btn_raise
    btn_raise['state']=DISABLED
def getRandCard(cards):
    suite=random.randint(0,len(cards)-1)
    number=random.randint(0, len(cards[suite])-1)
    temp=cards[suite][number]
    del cards[suite][number]
    return temp

def bet():
    bet=bet_amt.get()
    btn_bet.destroy()
    bet_amt.destroy()
    global pot_amt
    pot_amt+=bet
    pot=Label(root, text="you bet $"+str(pot_amt))
    pot.grid(row=3, column=0)
    btn_check['state']=NORMAL
    btn_raise['state']=NORMAL

def Raise():
    global btn_check
    btn_check['state']=DISABLED
    global btn_raise
    btn_raise['state']=DISABLED
    global bet_amt
    bet_amt=Scale(root, from_=0, to=500)
    bet_amt.grid(row=0, column=5)
    global btn_bet
    btn_bet=Button(root, text="bet", command=bet)
    btn_bet.grid(row=2, column=4)

deck=LabelFrame(root, padx=30,pady=42)
test=Label(deck,  text="???")
test.grid()
deck.grid(row=0, column=0)
printCard(getRandCard(cards), 1, 0)
printCard(getRandCard(cards),1, 1)
btn_check=Button(root, text="check", command=revealCard)
btn_check.grid(row=2, column=0)
btn_raise=Button(root, text="raise", command=Raise)
btn_raise.grid(row=2, column=1)


