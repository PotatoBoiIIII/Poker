import pygame
import button
import slider
import card
import random
import player as pl

pygame.font.init()


#Global constants
WIDTH = 900
HEIGHT= 500
GREEN=(88, 175, 54)
WHITE=(255,255,255)
ARROW_WIDTH=13*6
ARROW_HEIGHT=20*6
MODE_WIDTH=40*6
MODE_HEIGHT=20*6
HOME_WIDTH=20*3
BOT_CARD_WIDTH=27*3
BOT_CARD_HEIGHT=38*3
PLAYER_CARD_WIDTH=27*4
PLAYER_CARD_HEIGHT=38*4
ACTION_WIDTH=60
ACTION_HEIGHT=30
PLAYER_TAG_WIDTH=60
PLAYER_TAG_HEIGHT=30
USER_TAG_WIDTH=50*2
USER_TAG_HEIGHT=30*2


FPS=60


screen= pygame.display.set_mode((WIDTH, HEIGHT))
#images
Right_Arrow_img=pygame.transform.scale(pygame.image.load("Buttons/RightArrow.png"), (ARROW_WIDTH, ARROW_HEIGHT))
Left_Arrow_img=pygame.transform.scale(pygame.image.load("Buttons/LeftArrow.png"), (ARROW_WIDTH, ARROW_HEIGHT))
Easy_img=pygame.transform.scale(pygame.image.load("Buttons/Easy.png"), (MODE_WIDTH, MODE_HEIGHT))
Medium_img=pygame.transform.scale(pygame.image.load("Buttons/Medium.png"), (MODE_WIDTH, MODE_HEIGHT))
Hard_img=pygame.transform.scale(pygame.image.load("Buttons/Hard.png"), (MODE_WIDTH, MODE_HEIGHT))
Home_img= pygame.transform.scale(pygame.image.load("Buttons/Home.png"), (HOME_WIDTH, HOME_WIDTH))

Check_img = pygame.transform.scale(pygame.image.load("Buttons/Check.png"), (ACTION_WIDTH, ACTION_HEIGHT))
Call_img = pygame.transform.scale(pygame.image.load("Buttons/Call.png"), (ACTION_WIDTH, ACTION_HEIGHT))
Fold_img = pygame.transform.scale(pygame.image.load("Buttons/Fold.png"), (ACTION_WIDTH, ACTION_HEIGHT))
Raise_img = pygame.transform.scale(pygame.image.load("Buttons/Raise.png"), (ACTION_WIDTH, ACTION_HEIGHT))

Player1_img = pygame.transform.scale(pygame.image.load("Players/Player1.png"), (PLAYER_TAG_WIDTH, PLAYER_TAG_HEIGHT))
Player2_img = pygame.transform.scale(pygame.image.load("Players/Player2.png"), (PLAYER_TAG_WIDTH, PLAYER_TAG_HEIGHT))
Player3_img = pygame.transform.scale(pygame.image.load("Players/Player3.png"), (PLAYER_TAG_WIDTH, PLAYER_TAG_HEIGHT))
Player4_img = pygame.transform.scale(pygame.image.load("Players/Player4.png"), (PLAYER_TAG_WIDTH, PLAYER_TAG_HEIGHT))
USER_TAG_img = pygame.transform.scale(pygame.image.load("Players/You.png"), (USER_TAG_WIDTH, USER_TAG_HEIGHT))

#Home Screen buttons
btn_Right=button.Button(int(WIDTH/2+Easy_img.get_width()*0.5)+20, int(HEIGHT/2-Easy_img.get_height()/2), Right_Arrow_img )
btn_Left=button.Button(int(WIDTH/2-Easy_img.get_width()/2)-Right_Arrow_img.get_width()-20, int(HEIGHT/2-Easy_img.get_height()/2), Left_Arrow_img)
btn_Easy=button.Button(int(WIDTH/2-Easy_img.get_width()/2), int(HEIGHT/2-Easy_img.get_height()/2), Easy_img)
btn_Medium=button.Button(int(WIDTH/2-Easy_img.get_width()/2), int(HEIGHT/2-Easy_img.get_height()/2), Medium_img)
btn_Hard=button.Button(int(WIDTH/2-Easy_img.get_width()/2), int(HEIGHT/2-Easy_img.get_height()/2), Hard_img)

btn_Fold=button.Button(340,440, Fold_img)
btn_Check=button.Button(410, 440, Check_img)
btn_Call=button.Button(410,440,Call_img)
btn_Raise=button.Button(480, 440, Raise_img)
btn_Raise2=button.Button(480, 440, Raise_img)

#GameplayButtons
btn_Home=button.Button(20,20, Home_img)

#Fonts
POT_FONT=pygame.font.SysFont("comicsans", 40)

#Card deck:
SA= pygame.transform.scale(pygame.image.load("cards/AS.png"), (BOT_CARD_WIDTH, BOT_CARD_HEIGHT))
S2= pygame.transform.scale(pygame.image.load("cards/2S.png"), (BOT_CARD_WIDTH, BOT_CARD_HEIGHT))
S3= pygame.transform.scale(pygame.image.load("cards/3S.png"), (BOT_CARD_WIDTH, BOT_CARD_HEIGHT))
S4= pygame.transform.scale(pygame.image.load("cards/4S.png"), (BOT_CARD_WIDTH, BOT_CARD_HEIGHT))
S5= pygame.transform.scale(pygame.image.load("cards/5S.png"), (BOT_CARD_WIDTH, BOT_CARD_HEIGHT))
S6= pygame.transform.scale(pygame.image.load("cards/6S.png"), (BOT_CARD_WIDTH, BOT_CARD_HEIGHT))
S7= pygame.transform.scale(pygame.image.load("cards/7S.png"), (BOT_CARD_WIDTH, BOT_CARD_HEIGHT))
S8= pygame.transform.scale(pygame.image.load("cards/8S.png"), (BOT_CARD_WIDTH, BOT_CARD_HEIGHT))
S9= pygame.transform.scale(pygame.image.load("cards/9S.png"), (BOT_CARD_WIDTH, BOT_CARD_HEIGHT))
S10= pygame.transform.scale(pygame.image.load("cards/10S.png"), (BOT_CARD_WIDTH, BOT_CARD_HEIGHT))
SJ= pygame.transform.scale(pygame.image.load("cards/JS.png"), (BOT_CARD_WIDTH, BOT_CARD_HEIGHT))
SQ= pygame.transform.scale(pygame.image.load("cards/QS.png"), (BOT_CARD_WIDTH, BOT_CARD_HEIGHT))
SK= pygame.transform.scale(pygame.image.load("cards/KS.png"), (BOT_CARD_WIDTH, BOT_CARD_HEIGHT))
DA= pygame.transform.scale(pygame.image.load("cards/AD.png"), (BOT_CARD_WIDTH, BOT_CARD_HEIGHT))
D2= pygame.transform.scale(pygame.image.load("cards/2D.png"), (BOT_CARD_WIDTH, BOT_CARD_HEIGHT))
D3= pygame.transform.scale(pygame.image.load("cards/3D.png"), (BOT_CARD_WIDTH, BOT_CARD_HEIGHT))
D4= pygame.transform.scale(pygame.image.load("cards/4D.png"), (BOT_CARD_WIDTH, BOT_CARD_HEIGHT))
D5= pygame.transform.scale(pygame.image.load("cards/5D.png"), (BOT_CARD_WIDTH, BOT_CARD_HEIGHT))
D6= pygame.transform.scale(pygame.image.load("cards/6D.png"), (BOT_CARD_WIDTH, BOT_CARD_HEIGHT))
D7= pygame.transform.scale(pygame.image.load("cards/7D.png"), (BOT_CARD_WIDTH, BOT_CARD_HEIGHT))
D8= pygame.transform.scale(pygame.image.load("cards/8D.png"), (BOT_CARD_WIDTH, BOT_CARD_HEIGHT))
D9= pygame.transform.scale(pygame.image.load("cards/9D.png"), (BOT_CARD_WIDTH, BOT_CARD_HEIGHT))
D10= pygame.transform.scale(pygame.image.load("cards/10D.png"), (BOT_CARD_WIDTH, BOT_CARD_HEIGHT))
DJ= pygame.transform.scale(pygame.image.load("cards/JD.png"), (BOT_CARD_WIDTH, BOT_CARD_HEIGHT))
DQ= pygame.transform.scale(pygame.image.load("cards/QD.png"), (BOT_CARD_WIDTH, BOT_CARD_HEIGHT))
DK= pygame.transform.scale(pygame.image.load("cards/KD.png"), (BOT_CARD_WIDTH, BOT_CARD_HEIGHT))
CA= pygame.transform.scale(pygame.image.load("cards/AC.png"), (BOT_CARD_WIDTH, BOT_CARD_HEIGHT))
C2= pygame.transform.scale(pygame.image.load("cards/2C.png"), (BOT_CARD_WIDTH, BOT_CARD_HEIGHT))
C3= pygame.transform.scale(pygame.image.load("cards/3C.png"), (BOT_CARD_WIDTH, BOT_CARD_HEIGHT))
C4= pygame.transform.scale(pygame.image.load("cards/4C.png"), (BOT_CARD_WIDTH, BOT_CARD_HEIGHT))
C5= pygame.transform.scale(pygame.image.load("cards/5C.png"), (BOT_CARD_WIDTH, BOT_CARD_HEIGHT))
C6= pygame.transform.scale(pygame.image.load("cards/6C.png"), (BOT_CARD_WIDTH, BOT_CARD_HEIGHT))
C7= pygame.transform.scale(pygame.image.load("cards/7C.png"), (BOT_CARD_WIDTH, BOT_CARD_HEIGHT))
C8= pygame.transform.scale(pygame.image.load("cards/8C.png"), (BOT_CARD_WIDTH, BOT_CARD_HEIGHT))
C9= pygame.transform.scale(pygame.image.load("cards/9C.png"), (BOT_CARD_WIDTH, BOT_CARD_HEIGHT))
C10= pygame.transform.scale(pygame.image.load("cards/10C.png"), (BOT_CARD_WIDTH, BOT_CARD_HEIGHT))
CJ= pygame.transform.scale(pygame.image.load("cards/JC.png"), (BOT_CARD_WIDTH, BOT_CARD_HEIGHT))
CQ= pygame.transform.scale(pygame.image.load("cards/QC.png"), (BOT_CARD_WIDTH, BOT_CARD_HEIGHT))
CK= pygame.transform.scale(pygame.image.load("cards/KC.png"), (BOT_CARD_WIDTH, BOT_CARD_HEIGHT))
HA= pygame.transform.scale(pygame.image.load("cards/AH.png"), (BOT_CARD_WIDTH, BOT_CARD_HEIGHT))
H2= pygame.transform.scale(pygame.image.load("cards/2H.png"), (BOT_CARD_WIDTH, BOT_CARD_HEIGHT))
H3= pygame.transform.scale(pygame.image.load("cards/3H.png"), (BOT_CARD_WIDTH, BOT_CARD_HEIGHT))
H4= pygame.transform.scale(pygame.image.load("cards/4H.png"), (BOT_CARD_WIDTH, BOT_CARD_HEIGHT))
H5= pygame.transform.scale(pygame.image.load("cards/5H.png"), (BOT_CARD_WIDTH, BOT_CARD_HEIGHT))
H6= pygame.transform.scale(pygame.image.load("cards/6H.png"), (BOT_CARD_WIDTH, BOT_CARD_HEIGHT))
H7= pygame.transform.scale(pygame.image.load("cards/7H.png"), (BOT_CARD_WIDTH, BOT_CARD_HEIGHT))
H8= pygame.transform.scale(pygame.image.load("cards/8H.png"), (BOT_CARD_WIDTH, BOT_CARD_HEIGHT))
H9= pygame.transform.scale(pygame.image.load("cards/9H.png"), (BOT_CARD_WIDTH, BOT_CARD_HEIGHT))
H10= pygame.transform.scale(pygame.image.load("cards/10H.png"), (BOT_CARD_WIDTH, BOT_CARD_HEIGHT))
HJ= pygame.transform.scale(pygame.image.load("cards/JH.png"), (BOT_CARD_WIDTH, BOT_CARD_HEIGHT))
HQ= pygame.transform.scale(pygame.image.load("cards/QH.png"), (BOT_CARD_WIDTH, BOT_CARD_HEIGHT))
HK= pygame.transform.scale(pygame.image.load("cards/KH.png"), (BOT_CARD_WIDTH, BOT_CARD_HEIGHT))
global CARDS
CARDS=[
    [card.Card("A", "H", HA), card.Card("2", "H", H2), card.Card("3", "H", H3), card.Card("4", "H", H4), card.Card("5", "H", H5), card.Card("6", "H", H6), card.Card("7", "H", H7), card.Card("8", "H", H8), card.Card("9", "H", H9), card.Card("10", "H", H10), card.Card("J", "H", HJ), card.Card("Q", "H", HQ), card.Card("K", "H", HK) ],
    [card.Card("A", "C", CA), card.Card("2", "C", C2), card.Card("3", "C", C3), card.Card("4", "C", C4), card.Card("5", "C", C5), card.Card("6", "C", C6), card.Card("7", "C", C7), card.Card("8", "C", C8), card.Card("9", "C", C9), card.Card("10", "C", C10), card.Card("J", "C", CJ), card.Card("Q", "C", CQ), card.Card("K", "C", CK) ],
    [card.Card("A", "D", DA), card.Card("2", "D", D2), card.Card("3", "D", D3), card.Card("4", "D", D4), card.Card("5", "D", D5), card.Card("6", "D", D6), card.Card("7", "D", D7), card.Card("8", "D", D8), card.Card("9", "D", D9), card.Card("10", "D", D10), card.Card("J", "D", DJ), card.Card("Q", "D", DQ), card.Card("K", "D", DK) ],
    [card.Card("A", "S", SA), card.Card("2", "S", S2), card.Card("3", "S", S3), card.Card("4", "S", S4), card.Card("5", "S", S5), card.Card("6", "S", S6), card.Card("7", "S", S7), card.Card("8", "S", S8), card.Card("9", "S", S9), card.Card("10", "S", S10), card.Card("J", "S", SJ), card.Card("Q", "S", SQ), card.Card("K", "S", SK) ],
]

#list of modes
global MODES
MODES=[btn_Hard, btn_Medium, btn_Easy]

#Events
PLAY_EASY = pygame.USEREVENT+1
PLAY_MEDIUM = pygame.USEREVENT+2
PLAY_HARD = pygame.USEREVENT+3

#global money amounts
global POT_AMT
POT_AMT = 0
global CALL_AMT
CALL_AMT=6


#players
global USER
USER = pl.Player()
global BOT0
BOT0 = pl.Player()
global BOT1
BOT1 = pl.Player()
global BOT2
BOT2 = pl.Player()
global BOT3
BOT3 = pl.Player()
global PLAYERS
PLAYERS = [BOT0, BOT1, BOT2, BOT3, USER]
global player
player=4
global is_Raising
is_Raising=False
raise_amt = slider.Slider(150, CALL_AMT, PLAYERS[-1].money, 600, 320)



def handle_isRaising():
    Pot_amt=POT_AMT
    Call_amt=CALL_AMT
    thingy=btn_Raise2.draw(screen)
    value=raise_amt.draw(screen, POT_FONT)
    if thingy:
        Pot_amt+=value
        Call_amt=value
        PLAYERS[-1].isRaising=False
        PLAYERS[-1].money-=value
        is_Raising=False


def handle_buttons():
    if btn_Fold.draw(screen):
        PLAYERS[-1].set_folded(True)
        player+=1
    elif CALL_AMT==0:
        if btn_Check.draw(screen):
            player+=1
    elif btn_Call.draw(screen):
        POT_AMT+=CALL_AMT
        PLAYERS[-1].set_money(PLAYERS[-1].money-CALL_AMT)
        player+=1
    elif btn_Raise.draw(screen):
        PLAYERS[-1].set_isRaising(True)

def compare_cards(card1, card2):
    if card1.value>card2.value:
        return 1
    elif card1.value<card2.value:

        return -1
    elif card1.value==card2.value:
        if card1.suite=="H":
            return 1
        elif card1.suite=="C" and card2.suite!="H":
            return 1
        elif card1.suite =="D" and card2.suite=="S":
            return 1
        else:
            return -1

def sort_cards(cards):
    for i in range(len(cards)-1):
        for j in range(len(cards)-i-1):
            if compare_cards(cards[j],cards[j+1])==1:
                temp =cards[j]
                cards[j]=cards[j+1]
                cards[j+1]=temp
    return cards
def check_straight_flush(cards):
    for i in range(len(cards)-4):
        if cards[i].suite == cards[i+1].suite and cards[i].suite == cards[i+2].suite and cards[i].suite == cards[i+3].suite and cards[i].suite == cards[i+4].suite and cards[i].value== cards[i+1].value+1 and cards[i].value== cards[i+2].value+1 and cards[i].value== cards[i+3].value+1 and cards[i].value== cards[i+4].value+1:
            cards[i].value
    return -1
def check_four_of_a_kind(cards):
    for i in range(len(cards)-3):
        if cards[i].value==cards[i+1].value and cards[i].value==cards[i+2].value and cards[i].value==cards[i+3].value:
            return cards[i].value
    return -1

def check_doubles_triples(cards):
    found_two=0
    found_three= 0
    first_two_index=0
    second_two_index=0
    three_index=0
    for i in range(len(cards)-1):
        if cards[i].value == cards[i+1].value:
            found_two +=1
            if found_two ==1:
                first_two_index = cards[i].value
            else:
                second_two_index = cards[i].value
            i+=2
        if i<len(cards)-2:
            if cards[i+2].value == cards[i].value :
                first_two_index=0
                three_index=cards[i].value
                found_two-=1
                found_three+=1
                i+=1
    if found_two==1 and found_three==1:
        return (45, three_index, first_two_index)
    elif found_three ==1:
        return (30, three_index, 0)
    elif found_two ==2:
        return (15, first_two_index, second_two_index)
    elif found_two ==1:
        return(0,first_two_index,0)
    else:
        return -1




def check_hand(river, card1, card2):
    river.append(card1)
    river.append(card2)
    cards=[]
    cards=sort_cards(river)
    if check_straight_flush(cards)!=-1:
            if cards[-1].value == 14:
                return 200
            return 180+check_straight_flush(cards)
    elif check_four_of_a_kind(cards)!=-1:
        return 160+check_four_of_a_kind(cards)
    elif check_doubles_triples(cards)!=-1:
        x= check_doubles_triples(cards)
        return 100+x[0]+x[1]
    else:
        if card1.value>card2.value:
            return card1.value
        else:
            return card2.value
def shuffle_cards(cards):
    shuffled_cards=[
        [],
        [],
        [],
        [],
    ]
    row=0
    for i in range(4):
        for j in range(13):
            suite = int(random.random()*len(cards))
            number = int(random.random()*len(cards[suite]))

            temp = cards[suite][number]
            shuffled_cards[int(row/13)].append(temp)
            cards[suite].remove(cards[suite][number])
            if len(cards[suite])==0:
                cards.remove(CARDS[suite])

            row += 1

    return shuffled_cards


def Check_Home():

    if btn_Home.draw(screen):

        return True
    return False
def Update_Game_Screen(cards, score, player):
    screen.fill(GREEN)
    #cards[0][0].print_Card(screen, 100,100)
    #cards[0][1].print_Card(screen, 300,100)
    #cards[0][2].print_Card(screen, 500,100)
    #cards[0][3].print_Card(screen, 100,300)
    #cards[0][4].print_Card(screen, 300,300)
    score_text = POT_FONT.render(str(score), 1, WHITE)
    screen.blit(score_text, (50, 50))
    screen.blit(Player1_img, ( 50, int(HEIGHT/2)))
    screen.blit(Player2_img, (280, 120))
    screen.blit(Player3_img, (WIDTH-280-60, 120))
    screen.blit(Player4_img, (WIDTH-150, int(HEIGHT/2)))
    screen.blit(USER_TAG_img, (WIDTH/2-(USER_TAG_WIDTH/2), 370))
    if player == 4 and not PLAYERS[-1].isRaising:
        handle_buttons()
        btn_Fold.draw(screen)
        btn_Raise.draw(screen)
        if PLAYERS[4].call ==0:
            btn_Check.draw(screen)
        else:
            btn_Call.draw(screen)
    elif player==4 and PLAYERS[-1].isRaising:
        handle_isRaising()
    #btn_Home.draw(screen)
    pygame.display.update()

def Play_Easy(cards, player):
    river = []
    river.append(cards[0][0])
    river.append(cards[0][1])
    river.append(cards[0][2])
    handle_buttons()


    score = check_hand(river, cards[0][3], cards[0][4])



    Update_Game_Screen(cards, score, player)
def update_home_screen():
    screen.fill(GREEN)
    btn_Right.draw(screen)
    btn_Left.draw(screen)
    MODES[-1].draw(screen)
    pygame.display.update()

def handle_Arrows(modes):

    if btn_Left.draw(screen):

        temp=modes[0]
        for i in range(0, len(modes)-1):
            modes[i]=modes[i+1]
        modes[-1]=temp
    if btn_Right.draw(screen):

        temp=modes[-1]
        for i in range(len(modes)-1,0, -1):
            modes[i]=modes[i-1]
        modes[0]=temp

    MODES=modes
def pick_mode():
    top_mode=MODES[-1]

    if top_mode.draw(screen):
        if top_mode == btn_Easy:
            pygame.event.post(pygame.event.Event(PLAY_EASY))
            return 1
        elif top_mode == btn_Medium:
            pygame.event.post(pygame.event.Event(PLAY_MEDIUM))
            return 2
        elif top_mode == btn_Hard:
            pygame.event.post(pygame.event.Event(PLAY_HARD))
            return 3





def main():
    clock = pygame.time.Clock()
    run=True
    Is_Playing = False
    temp_cards=[]
    temp_cards=CARDS
    cards = []
    cards=shuffle_cards(temp_cards)
    temp_cards=[]


    player = int(random.random()*len(PLAYERS))
    player=4

    while run:

        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:

                run=False
            if event.type==PLAY_EASY:
                pygame.event.post(pygame.event.Event(PLAY_EASY))

                Is_Playing=True
                Play_Easy(cards, player)
            elif event.type==PLAY_MEDIUM:
                pygame.event.post(pygame.event.Event(PLAY_MEDIUM))
                if Check_Home():
                    pygame.event.clear()
                    Is_Playing=False
                    main()
                Is_Playing = True
                print("Medium")
            elif event.type==PLAY_HARD:
                pygame.event.post(pygame.event.Event(PLAY_HARD))
                if Check_Home():
                    pygame.event.clear()
                    Is_Playing=False
                    main()
                Is_Playing = True
                print("hard")



        if not Is_Playing:
            handle_Arrows(MODES)
            pick_mode()

            update_home_screen()
    pygame.quit()




main()


