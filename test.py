import random
import cowsay 

class card:
    
    def __init__(self, value, suite):
        self.value=value
        self.suite=suite
        if value=="A":
            self.number=11
        elif value=="J" or value=="Q" or value=="K":
            self.number=10
        else:
            try:
                self.number=int(value)
            except ValueError:
                self.number=0
    def printCard(self):
        if self.value=="10":
            print(" ", end="")
            for i in range(8):
                print("-", end="")
            print()
            print("|        |")
            print("|        |")
            print(f"|{self.value} of {self.suite} |")
            print("|        |")
            print("|        |")
            print(" ", end="")
            for i in range(8):
                print("-", end="")
            print()
        else:
            print(" ", end="")
            for i in range(8):
                print("-", end="")
            print()
            print("|        |")
            print("|        |")
            print(f"| {self.value} of {self.suite} |")
            print("|        |")
            print("|        |")
            print(" ", end="")
            for i in range(8):
                print("-", end="")
            print()
    def printTwoCards(self, ocard):
        if self.value=="10":
            print(" ", end="")
            for i in range(8):
                print("-", end="")
            print("   ", end="")
            for i in range(8):
                print("-", end="")
            print()
            print("|        | |        |")
            print("|        | |        |")
            print(f"|{self.value} of {self.suite} | | {ocard.value} of {ocard.suite} |")
            print("|        | |        |") 
            print("|        | |        |")
            print(" ", end="")
            for i in range(8):
                print("-", end="")
            print("   ", end="")
            for i in range(8):
                print("-", end="")
            
            print()
        else:
            print(" ", end="")
            for i in range(8):
                print("-", end="")
            print("   ", end="")
            for i in range(8):
                print("-", end="")
            print()
            print("|        | |        |")
            print("|        | |        |")
            print(f"| {self.value} of {self.suite} | | {ocard.value} of {ocard.suite} |")
            print("|        | |        |") 
            print("|        | |        |")
            print(" ", end="")
            for i in range(8):
                print("-", end="")
            print("   ", end="")
            for i in range(8):
                print("-", end="")
            
            print()
def randCard(cards):
    x=random.randint(0,3)
    y=random.randint(0,len(cards[x])-1)
    temp=cards[x][y]
    del cards[x][y]
    return temp
        
def askMove():
    while True:
        try:
            x = input("Do you want to hit or stand?\n")
            x=x.strip().lower()
            if x=="hit":
                return True
            elif x=="stand":
                return False
            
        except ValueError:
            print("That is not a valid input! Please try again.")
            continue
        print("That is not a valid input! Please try again.")
def askWager(money):
    while True:
        try:
            wager=input("How much would you like to wager? Please enter a whole number.\n$")
            wager=int(wager)
            if wager<0:
                print("That is not a valid input! Please try again.")
            elif wager-(int(wager))!=0:
                print("That is not a valid input! Please try again.")
            elif wager>money:
                print("That is not a valid input! Please try again.")
            else:
                return wager
        except ValueError:
            print("That is not a valid input! Please try again.")
def getSum(cards):
    sum=0
    for card in cards:
        sum+=card.number
    return sum
def askPlay():
    while True:
        try:
            x=input("Would you like to play? (y/n)\n")
            x=x.strip().lower()
            if x=="y" or x=="yes":
                return True
            elif x=="n"or x=="no":
                return False
            else:
                print("That is not a valid input! Please try again.")
        except ValueError:
            print("That is not a valid input! Please try again.")
def printRules():
    print("You enter the Dinosaur Casino with $1000 to play blackjack. A t-rex greets you at the entrance. ")
    cowsay.trex("Welcome!")
    print("Before we begin, you must know that Aces are worth 11 unless you have an ace and go over 21. Then they are automatically converted to be worth 1.")
    
def checkAce(cards):
    for card in cards:
        if card.number==11:
            return True
    return False
defaultCards = [
    [card("A", "\u2665"), card("2", "\u2665"), card("3", "\u2665"), card("4", "\u2665"), card("5", "\u2665"), card("6", "\u2665"), card("7", "\u2665"), card("8", "\u2665"), card("9", "\u2665"), card("10", "\u2665"), card("J", "\u2665"), card("Q", "\u2665"), card("K", "\u2665"), ],
    [card("A", "\u2666"), card("2", "\u2666"), card("3", "\u2666"), card("4", "\u2666"), card("5", "\u2666"), card("6", "\u2666"), card("7", "\u2666"), card("8", "\u2666"), card("9", "\u2666"), card("10", "\u2666"), card("J", "\u2666"), card("Q", "\u2666"), card("K", "\u2666"), ],
    [card("A", "\u2663"), card("2", "\u2663"), card("3", "\u2663"), card("4", "\u2663"), card("5", "\u2663"), card("6", "\u2663"), card("7", "\u2663"), card("8", "\u2663"), card("9", "\u2663"), card("10", "\u2663"), card("J", "\u2663"), card("Q", "\u2663"), card("K", "\u2663"), ],
    [card("A","\U00002660"), card("2","\U00002660"), card("3","\U00002660"), card("4","\U00002660"), card("5","\U00002660"), card("6","\U00002660"), card("7","\U00002660"), card("8","\U00002660"), card("9","\U00002660"), card("10","\U00002660"), card("J","\U00002660"), card("Q","\U00002660"), card("K","\U00002660"), ],
    ]

def main():
    cards=defaultCards
    money=1000
    broke=False
    uCard=card("?","?")
    printRules()
    while(money>0):
        
        print(f"You have ${money}")
        if not askPlay():
            print(f"You left the casino with ${money}")
            break
        wager=askWager(money)
        dCards=[randCard(cards), randCard(cards)]
        pCards=[randCard(cards), randCard(cards)]
        print("The dealers cards are: ")
        print("---------------------------")
        uCard.printTwoCards(dCards[1])
        print("----------------------------")
        while True:
            print("Your cards are:")
            for i in range(0,len(pCards)-1, 2):
                pCards[i].printTwoCards(pCards[i+1])
            if len(pCards)%2==1:
                pCards[-1].printCard()
            print("---------------------------")
            if askMove():
                pCards.append(randCard(cards))
                if getSum(pCards)>21:
                    print(f"You got a {pCards[-1].value}")
                    if checkAce(pCards):
                        continue
                    print("You bust!")
                    money-=wager
                    break
                else:
                    continue
            else:
                dSum=getSum(dCards)
                pSum = getSum(pCards)
                dBusted=False
                while dSum<=15 and dSum <= pSum :
                    dCards.append(randCard(cards))
                    dSum+=dCards[-1].number
                    print("The dealer hit and now has a sum of "+str(dSum)+"!")
                    
                    if dSum>21:
                        print("The dealer bust! You win!")
                        print("The dealer's cards were:")
                        for i in range(0,len(dCards)-1, 2):
                            dCards[i].printTwoCards(dCards[i+1])
                        if len(dCards)%2==1:
                            dCards[-1].printCard()
                        print("---------------------------")
                        dBusted=True
                        money+=wager
                        break
                if dSum > pSum and not dBusted:
                    money-=wager
                    print("You lost! ")
                    wager=0
                    print("The dealer's cards were:")
                    for i in range(0,len(dCards)-1, 2):
                        dCards[i].printTwoCards(dCards[i+1])
                    if len(dCards)%2==1:
                        dCards[-1].printCard()
                    print("---------------------------")
                    break
                elif dSum==pSum:
                    print(f"The dealer's cards added up to {dSum}")
                    print("You tied!")
                    wager=0
                    print("The dealer's cards were:")
                    for i in range(0,len(dCards)-1, 2):
                        dCards[i].printTwoCards(dCards[i+1])
                    if len(dCards)%2==1:
                        dCards[-1].printCard()
                    print("---------------------------")
                    break
                elif pSum>dSum:
                    print("The dealer's cards were:")
                    for i in range(0,len(dCards)-1, 2):
                        dCards[i].printTwoCards(dCards[i+1])
                    if len(dCards)%2==1:
                        dCards[-1].printCard()
                    print("---------------------------")
                    money+=wager
                    wager=0
                    print("You win!")
                    break
                else:
                    break
    if money==0:
        print("You lost all your money. Come again soon!")
        
        
    
    
    
main()