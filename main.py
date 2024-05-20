import pygame
import button
import slider
import card
import random
import player as pl
import math

pygame.font.init()
pygame.mixer.init()
# Global constants
WIDTH = 900
HEIGHT = 500
GREEN = (88, 175, 54)
WHITE = (255, 255, 255)
BLUE = (0, 30, 230)
LIGHT_GREEN = (43, 253, 11)
YELLOW = (246, 242, 30)
ARROW_WIDTH = 13 * 6
ARROW_HEIGHT = 20 * 6
MODE_WIDTH = 40 * 6
MODE_HEIGHT = 20 * 6
HOME_WIDTH = 20 * 3
BOT_CARD_WIDTH = 27 * 2
BOT_CARD_HEIGHT = 38 * 2
PLAYER_CARD_WIDTH = 27 * 3
PLAYER_CARD_HEIGHT = 38 * 3
ACTION_WIDTH = 60
ACTION_HEIGHT = 30
PLAYER_TAG_WIDTH = 60
PLAYER_TAG_HEIGHT = 30
USER_TAG_WIDTH = 50 * 2
USER_TAG_HEIGHT = 30 * 2

FPS = 60

screen = pygame.display.set_mode((WIDTH, HEIGHT))
# images
Right_Arrow_img = pygame.transform.scale(pygame.image.load("Buttons/RightArrow.png"), (ARROW_WIDTH, ARROW_HEIGHT))
Left_Arrow_img = pygame.transform.scale(pygame.image.load("Buttons/LeftArrow.png"), (ARROW_WIDTH, ARROW_HEIGHT))
Easy_img = pygame.transform.scale(pygame.image.load("Buttons/Easy.png"), (MODE_WIDTH, MODE_HEIGHT))
Medium_img = pygame.transform.scale(pygame.image.load("Buttons/Medium.png"), (MODE_WIDTH, MODE_HEIGHT))
Hard_img = pygame.transform.scale(pygame.image.load("Buttons/Hard.png"), (MODE_WIDTH, MODE_HEIGHT))
Home_img = pygame.transform.scale(pygame.image.load("Buttons/Home.png"), (HOME_WIDTH, HOME_WIDTH))

Check_img = pygame.transform.scale(pygame.image.load("Buttons/Check.png"), (ACTION_WIDTH, ACTION_HEIGHT))
Call_img = pygame.transform.scale(pygame.image.load("Buttons/Call.png"), (ACTION_WIDTH, ACTION_HEIGHT))
Fold_img = pygame.transform.scale(pygame.image.load("Buttons/Fold.png"), (ACTION_WIDTH, ACTION_HEIGHT))
Raise_img = pygame.transform.scale(pygame.image.load("Buttons/Raise.png"), (ACTION_WIDTH, ACTION_HEIGHT))

Player1_img = pygame.transform.scale(pygame.image.load("Players/Player1.png"), (PLAYER_TAG_WIDTH, PLAYER_TAG_HEIGHT))
Player2_img = pygame.transform.scale(pygame.image.load("Players/Player2.png"), (PLAYER_TAG_WIDTH, PLAYER_TAG_HEIGHT))
Player3_img = pygame.transform.scale(pygame.image.load("Players/Player3.png"), (PLAYER_TAG_WIDTH, PLAYER_TAG_HEIGHT))
Player4_img = pygame.transform.scale(pygame.image.load("Players/Player4.png"), (PLAYER_TAG_WIDTH, PLAYER_TAG_HEIGHT))
USER_TAG_img = pygame.transform.scale(pygame.image.load("Players/You.png"), (USER_TAG_WIDTH, USER_TAG_HEIGHT))

DEALER_TAG_img = pygame.transform.scale(pygame.image.load("Buttons/Dealer.png"), (21, 21))
# Home Screen buttons
btn_Right = button.Button(int(WIDTH / 2 + Easy_img.get_width() * 0.5) + 20, int(HEIGHT / 2 - Easy_img.get_height() / 2),
                          Right_Arrow_img)
btn_Left = button.Button(int(WIDTH / 2 - Easy_img.get_width() / 2) - Right_Arrow_img.get_width() - 20,
                         int(HEIGHT / 2 - Easy_img.get_height() / 2), Left_Arrow_img)
btn_Easy = button.Button(int(WIDTH / 2 - Easy_img.get_width() / 2), int(HEIGHT / 2 - Easy_img.get_height() / 2),
                         Easy_img)
btn_Medium = button.Button(int(WIDTH / 2 - Easy_img.get_width() / 2), int(HEIGHT / 2 - Easy_img.get_height() / 2),
                           Medium_img)
btn_Hard = button.Button(int(WIDTH / 2 - Easy_img.get_width() / 2), int(HEIGHT / 2 - Easy_img.get_height() / 2),
                         Hard_img)

btn_Fold = button.Button(350, 450, Fold_img)
btn_Check = button.Button(420, 450, Check_img)
btn_Call = button.Button(420, 450, Call_img)
btn_Raise = button.Button(490, 450, Raise_img)

# GameplayButtons
btn_Home = button.Button(20, 20, Home_img)

# Fonts
POT_FONT = pygame.font.SysFont("comicsans", 30)
PLAYER_MONEY_FONT = pygame.font.SysFont("arial", 20)
PLAYER_MOVE_FONT = pygame.font.SysFont("calibri", 20)
WINNER_FONT = pygame.font.SysFont("calibri", 40)

#sounds
Fold_sound = pygame.mixer.Sound("Sounds/Fold_sound.mp3")
Check_sound = pygame.mixer.Sound("Sounds/Check_sound.mp3")
Raise_sound = pygame.mixer.Sound("Sounds/Raise_sound.mp3")
Card_flip_sound = pygame.mixer.Sound("Sounds/card_turn_sound.mp3")
Poker_chip_sound = pygame.mixer.Sound("Sounds/Poker_chip_sound.mp3")
Winning_sound= pygame.mixer.Sound("Sounds/Winning_sound.mp3")

# Card deck:
SA = pygame.transform.scale(pygame.image.load("cards/AS.png"), (BOT_CARD_WIDTH, BOT_CARD_HEIGHT))
S2 = pygame.transform.scale(pygame.image.load("cards/2S.png"), (BOT_CARD_WIDTH, BOT_CARD_HEIGHT))
S3 = pygame.transform.scale(pygame.image.load("cards/3S.png"), (BOT_CARD_WIDTH, BOT_CARD_HEIGHT))
S4 = pygame.transform.scale(pygame.image.load("cards/4S.png"), (BOT_CARD_WIDTH, BOT_CARD_HEIGHT))
S5 = pygame.transform.scale(pygame.image.load("cards/5S.png"), (BOT_CARD_WIDTH, BOT_CARD_HEIGHT))
S6 = pygame.transform.scale(pygame.image.load("cards/6S.png"), (BOT_CARD_WIDTH, BOT_CARD_HEIGHT))
S7 = pygame.transform.scale(pygame.image.load("cards/7S.png"), (BOT_CARD_WIDTH, BOT_CARD_HEIGHT))
S8 = pygame.transform.scale(pygame.image.load("cards/8S.png"), (BOT_CARD_WIDTH, BOT_CARD_HEIGHT))
S9 = pygame.transform.scale(pygame.image.load("cards/9S.png"), (BOT_CARD_WIDTH, BOT_CARD_HEIGHT))
S10 = pygame.transform.scale(pygame.image.load("cards/10S.png"), (BOT_CARD_WIDTH, BOT_CARD_HEIGHT))
SJ = pygame.transform.scale(pygame.image.load("cards/JS.png"), (BOT_CARD_WIDTH, BOT_CARD_HEIGHT))
SQ = pygame.transform.scale(pygame.image.load("cards/QS.png"), (BOT_CARD_WIDTH, BOT_CARD_HEIGHT))
SK = pygame.transform.scale(pygame.image.load("cards/KS.png"), (BOT_CARD_WIDTH, BOT_CARD_HEIGHT))
DA = pygame.transform.scale(pygame.image.load("cards/AD.png"), (BOT_CARD_WIDTH, BOT_CARD_HEIGHT))
D2 = pygame.transform.scale(pygame.image.load("cards/2D.png"), (BOT_CARD_WIDTH, BOT_CARD_HEIGHT))
D3 = pygame.transform.scale(pygame.image.load("cards/3D.png"), (BOT_CARD_WIDTH, BOT_CARD_HEIGHT))
D4 = pygame.transform.scale(pygame.image.load("cards/4D.png"), (BOT_CARD_WIDTH, BOT_CARD_HEIGHT))
D5 = pygame.transform.scale(pygame.image.load("cards/5D.png"), (BOT_CARD_WIDTH, BOT_CARD_HEIGHT))
D6 = pygame.transform.scale(pygame.image.load("cards/6D.png"), (BOT_CARD_WIDTH, BOT_CARD_HEIGHT))
D7 = pygame.transform.scale(pygame.image.load("cards/7D.png"), (BOT_CARD_WIDTH, BOT_CARD_HEIGHT))
D8 = pygame.transform.scale(pygame.image.load("cards/8D.png"), (BOT_CARD_WIDTH, BOT_CARD_HEIGHT))
D9 = pygame.transform.scale(pygame.image.load("cards/9D.png"), (BOT_CARD_WIDTH, BOT_CARD_HEIGHT))
D10 = pygame.transform.scale(pygame.image.load("cards/10D.png"), (BOT_CARD_WIDTH, BOT_CARD_HEIGHT))
DJ = pygame.transform.scale(pygame.image.load("cards/JD.png"), (BOT_CARD_WIDTH, BOT_CARD_HEIGHT))
DQ = pygame.transform.scale(pygame.image.load("cards/QD.png"), (BOT_CARD_WIDTH, BOT_CARD_HEIGHT))
DK = pygame.transform.scale(pygame.image.load("cards/KD.png"), (BOT_CARD_WIDTH, BOT_CARD_HEIGHT))
CA = pygame.transform.scale(pygame.image.load("cards/AC.png"), (BOT_CARD_WIDTH, BOT_CARD_HEIGHT))
C2 = pygame.transform.scale(pygame.image.load("cards/2C.png"), (BOT_CARD_WIDTH, BOT_CARD_HEIGHT))
C3 = pygame.transform.scale(pygame.image.load("cards/3C.png"), (BOT_CARD_WIDTH, BOT_CARD_HEIGHT))
C4 = pygame.transform.scale(pygame.image.load("cards/4C.png"), (BOT_CARD_WIDTH, BOT_CARD_HEIGHT))
C5 = pygame.transform.scale(pygame.image.load("cards/5C.png"), (BOT_CARD_WIDTH, BOT_CARD_HEIGHT))
C6 = pygame.transform.scale(pygame.image.load("cards/6C.png"), (BOT_CARD_WIDTH, BOT_CARD_HEIGHT))
C7 = pygame.transform.scale(pygame.image.load("cards/7C.png"), (BOT_CARD_WIDTH, BOT_CARD_HEIGHT))
C8 = pygame.transform.scale(pygame.image.load("cards/8C.png"), (BOT_CARD_WIDTH, BOT_CARD_HEIGHT))
C9 = pygame.transform.scale(pygame.image.load("cards/9C.png"), (BOT_CARD_WIDTH, BOT_CARD_HEIGHT))
C10 = pygame.transform.scale(pygame.image.load("cards/10C.png"), (BOT_CARD_WIDTH, BOT_CARD_HEIGHT))
CJ = pygame.transform.scale(pygame.image.load("cards/JC.png"), (BOT_CARD_WIDTH, BOT_CARD_HEIGHT))
CQ = pygame.transform.scale(pygame.image.load("cards/QC.png"), (BOT_CARD_WIDTH, BOT_CARD_HEIGHT))
CK = pygame.transform.scale(pygame.image.load("cards/KC.png"), (BOT_CARD_WIDTH, BOT_CARD_HEIGHT))
HA = pygame.transform.scale(pygame.image.load("cards/AH.png"), (BOT_CARD_WIDTH, BOT_CARD_HEIGHT))
H2 = pygame.transform.scale(pygame.image.load("cards/2H.png"), (BOT_CARD_WIDTH, BOT_CARD_HEIGHT))
H3 = pygame.transform.scale(pygame.image.load("cards/3H.png"), (BOT_CARD_WIDTH, BOT_CARD_HEIGHT))
H4 = pygame.transform.scale(pygame.image.load("cards/4H.png"), (BOT_CARD_WIDTH, BOT_CARD_HEIGHT))
H5 = pygame.transform.scale(pygame.image.load("cards/5H.png"), (BOT_CARD_WIDTH, BOT_CARD_HEIGHT))
H6 = pygame.transform.scale(pygame.image.load("cards/6H.png"), (BOT_CARD_WIDTH, BOT_CARD_HEIGHT))
H7 = pygame.transform.scale(pygame.image.load("cards/7H.png"), (BOT_CARD_WIDTH, BOT_CARD_HEIGHT))
H8 = pygame.transform.scale(pygame.image.load("cards/8H.png"), (BOT_CARD_WIDTH, BOT_CARD_HEIGHT))
H9 = pygame.transform.scale(pygame.image.load("cards/9H.png"), (BOT_CARD_WIDTH, BOT_CARD_HEIGHT))
H10 = pygame.transform.scale(pygame.image.load("cards/10H.png"), (BOT_CARD_WIDTH, BOT_CARD_HEIGHT))
HJ = pygame.transform.scale(pygame.image.load("cards/JH.png"), (BOT_CARD_WIDTH, BOT_CARD_HEIGHT))
HQ = pygame.transform.scale(pygame.image.load("cards/QH.png"), (BOT_CARD_WIDTH, BOT_CARD_HEIGHT))
HK = pygame.transform.scale(pygame.image.load("cards/KH.png"), (BOT_CARD_WIDTH, BOT_CARD_HEIGHT))
UC = pygame.transform.scale(pygame.image.load("cards/UnknownCard.png"), (BOT_CARD_WIDTH, BOT_CARD_HEIGHT))
UCL = pygame.transform.rotate(UC, 15)
UCR = pygame.transform.rotate(UC, -15)
CARDS_ = [
    [card.Card("A", "H", HA), card.Card("2", "H", H2), card.Card("3", "H", H3), card.Card("4", "H", H4),
     card.Card("5", "H", H5), card.Card("6", "H", H6), card.Card("7", "H", H7), card.Card("8", "H", H8),
     card.Card("9", "H", H9), card.Card("10", "H", H10), card.Card("J", "H", HJ), card.Card("Q", "H", HQ),
     card.Card("K", "H", HK)],
    [card.Card("A", "C", CA), card.Card("2", "C", C2), card.Card("3", "C", C3), card.Card("4", "C", C4),
     card.Card("5", "C", C5), card.Card("6", "C", C6), card.Card("7", "C", C7), card.Card("8", "C", C8),
     card.Card("9", "C", C9), card.Card("10", "C", C10), card.Card("J", "C", CJ), card.Card("Q", "C", CQ),
     card.Card("K", "C", CK)],
    [card.Card("A", "D", DA), card.Card("2", "D", D2), card.Card("3", "D", D3), card.Card("4", "D", D4),
     card.Card("5", "D", D5), card.Card("6", "D", D6), card.Card("7", "D", D7), card.Card("8", "D", D8),
     card.Card("9", "D", D9), card.Card("10", "D", D10), card.Card("J", "D", DJ), card.Card("Q", "D", DQ),
     card.Card("K", "D", DK)],
    [card.Card("A", "S", SA), card.Card("2", "S", S2), card.Card("3", "S", S3), card.Card("4", "S", S4),
     card.Card("5", "S", S5), card.Card("6", "S", S6), card.Card("7", "S", S7), card.Card("8", "S", S8),
     card.Card("9", "S", S9), card.Card("10", "S", S10), card.Card("J", "S", SJ), card.Card("Q", "S", SQ),
     card.Card("K", "S", SK)],
]
temp_CARDS = [[], [], [], []]
for suite in range(4):
    for number in range(13):
        temp_CARDS[suite].append(CARDS_[suite][number])
# list of modes
MODES = [btn_Hard, btn_Medium, btn_Easy]

# Events
PLAY_EASY = pygame.USEREVENT + 1
PLAY_MEDIUM = pygame.USEREVENT + 2
PLAY_HARD = pygame.USEREVENT + 3

# global money amounts
POT_AMT = 0

# players
USER = pl.Player()
BOT0 = pl.Player()
BOT1 = pl.Player()
BOT2 = pl.Player()
BOT3 = pl.Player()

PLAYERS = [BOT0, BOT1, BOT2, BOT3, USER]

is_Raising = False
raise_amt = slider.Slider(150, 2, 500, 600, 320)
has_dealt_cards = False
# counters
RIVER_CARD_COUNT = 0
PLAYERS_FOLDED = 0
CHECK_COUNT = 0
RIVER = []
is_a_tie = False
SMALl_BLIND = 3
player = 3
has_done_small_blind = False
has_done_big_blind = False



def shuffle_cards(thingy):
    shuffled_cards = [
        [],
        [],
        [],
        [],
    ]
    row = 0
    for i in range(4):
        for j in range(13):
            suite = int(random.random() * len(thingy))
            number = int(random.random() * len(thingy[suite]))

            temp = thingy[suite][number]
            shuffled_cards[int(row / 13)].append(temp)
            thingy[suite].remove(thingy[suite][number])
            if len(thingy[suite]) == 0:
                thingy.remove(thingy[suite])

            row += 1
    return shuffled_cards


cards = []
cards = shuffle_cards(temp_CARDS)
temp_CARDS = [[], [], [], []]
for suite in range(4):
    for number in range(13):
        temp_CARDS[suite].append(CARDS_[suite][number])


def winner_animation(winners):
    winner_text = WINNER_FONT.render("WINNER!", 1, BLUE)
    Winning_sound.play()
    Card_flip_sound.play()
    reveal_cards()
    for i in range(15):
        for winner in winners:
            if winner == 0:
                screen.blit(winner_text, (40, 265))
            if winner == 1:
                screen.blit(winner_text, (270, 136))
            if winner == 2:
                screen.blit(winner_text, (550, 135))
            if winner == 3:
                screen.blit(winner_text, (740, 265))
            if winner == 4:
                screen.blit(winner_text, (400, 400))
        pygame.display.update()
        pygame.time.delay(500)
        Update_Game_Screen()
        reveal_cards()
        pygame.display.update
        pygame.time.delay(500)


def draw_player_highlight():
    if player == 0:
        pygame.draw.circle(screen, LIGHT_GREEN, [80, 215], 90, 90)
    elif player == 1:
        pygame.draw.circle(screen, LIGHT_GREEN, [310, 85], 90, 90)
    elif player == 2:
        pygame.draw.circle(screen, LIGHT_GREEN, [590, 85], 90, 90)
    elif player == 3:
        pygame.draw.circle(screen, LIGHT_GREEN, [780, 215], 90, 90)
    elif player == 4:
        pygame.draw.circle(screen, LIGHT_GREEN, [450, 360], 100, 100)


def reset_game():
    global CHECK_COUNT
    global PLAYERS_FOLDED
    global RIVER
    global RIVER_CARD_COUNT
    global is_a_tie
    global is_Raising
    global POT_AMT
    global PLAYERS
    global cards
    global temp_CARDS
    global has_dealt_cards
    global SMALl_BLIND
    global has_done_small_blind
    global has_done_big_blind
    global player
    SMALl_BLIND = (SMALl_BLIND + 1) % 5
    player = SMALl_BLIND
    has_done_big_blind = False
    has_done_small_blind = False
    has_dealt_cards = False
    CHECK_COUNT = 0
    PLAYERS_FOLDED = 0
    RIVER = []
    RIVER_CARD_COUNT = 0
    is_a_tie = False
    is_Raising = False
    POT_AMT = 0
    for p in PLAYERS:
        p.set_call(0)
        p.set_has_cards(False)
        p.set_folded(False)
        p.set_last_move("")
    cards = shuffle_cards(temp_CARDS)
    temp_CARDS = [[], [], [], []]
    for suite in range(4):
        for number in range(13):
            temp_CARDS[suite].append(CARDS_[suite][number])

def print_dealer_button():
    dealer = SMALl_BLIND-1
    if SMALl_BLIND==0:
        dealer = 4
    if dealer == 0:
        screen.blit(DEALER_TAG_img, (35, 260))
    elif dealer == 1:
        screen.blit(DEALER_TAG_img, (265, 100))
    elif dealer == 2:
        screen.blit(DEALER_TAG_img, (545, 100))
    elif dealer == 3:
        screen.blit(DEALER_TAG_img, (735, 260))
    elif dealer == 4:
        screen.blit(DEALER_TAG_img, (385, 410))
def set_calls(player, amt):
    global PLAYERS
    if player == 0:
        for i in range(1, 5):
            PLAYERS[i].set_call(PLAYERS[i].call + amt)
    else:
        for i in range(player):
            PLAYERS[i].set_call(PLAYERS[i].call + amt)
        for j in range(player + 1, 5):
            PLAYERS[j].set_call(PLAYERS[j].call + amt)


def increment_player():
    global player
    if player == 4:
        player = 0
    else:
        player += 1


def check_Checks():
    global CHECK_COUNT
    if CHECK_COUNT == 5 - PLAYERS_FOLDED:
        CHECK_COUNT = 0
        return True
    else:
        return False


def handle_isRaising():
    global is_Raising
    global POT_AMT
    global PLAYERS
    global CHECK_COUNT
    value = raise_amt.draw(screen, POT_FONT)
    if btn_Raise.draw(screen):
        PLAYERS[-1].set_last_move("Raised $" + str(value))
        POT_AMT += value + PLAYERS[-1].call
        PLAYERS[-1].isRaising = False
        PLAYERS[-1].set_money(-(value + PLAYERS[-1].call))
        PLAYERS[-1].set_call(0)
        is_Raising = False
        CHECK_COUNT = 1
        set_calls(4, value)
        Poker_chip_sound.play()
        increment_player()


def handle_bot_move():
    global POT_AMT
    global PLAYERS_FOLDED
    global CHECK_COUNT
    global PLAYERS
    if not has_done_small_blind:
        small_blind()
        return "Raise"
    elif not has_done_big_blind:
        big_blind()
        return "Raise"
    action = int(random.random() * 10)
    if action < 2:
        PLAYERS[player].set_folded(True)
        PLAYERS[player].set_has_cards(False)
        fold_text = PLAYER_MOVE_FONT.render("Folded", 1, BLUE)
        PLAYERS_FOLDED += 1
        PLAYERS[player].set_last_move("Folded")
        increment_player()
        return "Fold"
    elif action < 9:
        if PLAYERS[player].call == 0:
            PLAYERS[player].set_last_move("Checked")
            CHECK_COUNT += 1
            Check_sound.play()
            increment_player()
            return "Check"
        else:
            PLAYERS[player].set_last_move("Called $" + str(PLAYERS[player].call))
            POT_AMT += PLAYERS[player].call
            PLAYERS[player].set_money(-PLAYERS[player].call)
            PLAYERS[player].set_call(0)
            Poker_chip_sound.play()
            CHECK_COUNT += 1
            increment_player()
            return "Call"
    elif action < 10:
        bet = 9999999999
        while PLAYERS[player].money - bet - PLAYERS[player].call < 0:
            bet = int(1.01 ** (random.random() * 145))
        PLAYERS[player].set_last_move("Raised $" + str(bet))
        POT_AMT += bet + PLAYERS[player].call
        CHECK_COUNT = 1
        PLAYERS[player].set_money(-(bet + PLAYERS[player].call))
        set_calls(player, bet)
        PLAYERS[player].set_call(0)
        Poker_chip_sound.play()
        increment_player()
        return "Raise"


def print_dealt_cards():
    if has_dealt_cards:
        if PLAYERS[0].has_cards:
            screen.blit(UCL, (40, 140))
            screen.blit(UCR, (60, 140))
        if PLAYERS[1].has_cards:
            screen.blit(UCL, (270, 10))
            screen.blit(UCR, (290, 10))
        if PLAYERS[2].has_cards:
            screen.blit(UCL, (550, 10))
            screen.blit(UCR, (570, 10))
        if PLAYERS[3].has_cards:
            screen.blit(UCL, (730, 140))
            screen.blit(UCR, (750, 140))
        if PLAYERS[4].has_cards:
            PLAYERS[4].card1.print_Card(screen, 405, 275)
            PLAYERS[4].card2.print_Card(screen, 445, 275)


def reveal_cards():
    if not PLAYERS[0].folded:
        PLAYERS[0].card1.print_Card(screen, 30, 130)
        PLAYERS[0].card2.print_Card(screen, 70, 130)
        PLAYERS[0].set_has_cards(False)
    if not PLAYERS[1].folded:
        PLAYERS[1].card1.print_Card(screen, 260, 5)
        PLAYERS[1].card2.print_Card(screen, 300, 5)
        PLAYERS[1].set_has_cards(False)
    if not PLAYERS[2].folded:
        PLAYERS[2].card1.print_Card(screen, 540, 5)
        PLAYERS[2].card2.print_Card(screen, 580, 5)
        PLAYERS[2].set_has_cards(False)
    if not PLAYERS[3].folded:
        PLAYERS[3].card1.print_Card(screen, 720, 130)
        PLAYERS[3].card2.print_Card(screen, 760, 130)
        PLAYERS[3].set_has_cards(False)
    pygame.display.update()


def small_blind():
    global PLAYERS
    global POT_AMT
    global CHECK_COUNT
    global has_done_small_blind
    has_done_small_blind = True
    PLAYERS[SMALl_BLIND].set_last_move("Small Blind $2")
    POT_AMT += 2
    CHECK_COUNT = 1
    PLAYERS[SMALl_BLIND].set_money(-2)
    set_calls(SMALl_BLIND, 2)
    PLAYERS[SMALl_BLIND].set_call(0)
    increment_player()


def big_blind():
    global PLAYERS
    global POT_AMT
    global CHECK_COUNT
    global has_done_big_blind
    has_done_big_blind = True
    PLAYERS[(SMALl_BLIND + 1) % 5].set_last_move("big Blind $4")
    POT_AMT += 4
    CHECK_COUNT = 1
    PLAYERS[(SMALl_BLIND + 1) % 5].set_money(-4)
    set_calls((SMALl_BLIND + 1) % 5, 2)
    PLAYERS[(SMALl_BLIND + 1) % 5].set_call(0)
    increment_player()


def deal_cards():
    global PLAYERS
    global has_dealt_cards
    has_dealt_cards = True
    i = 0
    Card_flip_sound.play()
    for plyr in PLAYERS:
        plyr.set_cards(cards[0][i], cards[0][i + 1])
        plyr.set_has_cards(True)
        i += 2


def deal_flop():
    global RIVER_CARD_COUNT
    global CHECK_COUNT
    global cards
    RIVER_CARD_COUNT += 3
    RIVER.append(cards[0][10])
    RIVER.append(cards[0][11])
    RIVER.append(cards[0][12])
    cards.remove(cards[0])
    CHECK_COUNT = 0
    Card_flip_sound.play()


def print_River():
    i = 300
    j = 190
    for card in RIVER:
        card.print_Card(screen, i, j)
        i += BOT_CARD_WIDTH + 10


def handle_buttons():
    global POT_AMT
    global player
    global PLAYERS
    global is_Raising
    global CHECK_COUNT
    global PLAYERS_FOLDED
    if btn_Fold.draw(screen):
        PLAYERS[-1].set_folded(True)
        PLAYERS_FOLDED += 1
        PLAYERS[-1].set_last_move("Folded")
        Fold_sound.play()
        increment_player()
    if PLAYERS[-1].call == 0:
        if btn_Check.draw(screen):
            PLAYERS[-1].set_last_move("Checked")
            CHECK_COUNT += 1
            Check_sound.play()
            increment_player()
    else:
        if btn_Call.draw(screen):
            PLAYERS[-1].set_last_move("Called $" + str(PLAYERS[-1].call))
            POT_AMT += PLAYERS[-1].call
            PLAYERS[-1].set_money(-PLAYERS[-1].call)
            PLAYERS[-1].set_call(0)
            CHECK_COUNT += 1
            Poker_chip_sound.play()
            increment_player()
    if btn_Raise.draw(screen):
        Raise_sound.play()
        PLAYERS[-1].set_isRaising(True)
        is_Raising = True


def compare_cards(card1, card2):
    if card1.value > card2.value:
        return 1
    elif card1.value < card2.value:

        return -1
    elif card1.value == card2.value:
        if card1.suite == "H":
            return 1
        elif card1.suite == "C" and card2.suite != "H":
            return 1
        elif card1.suite == "D" and card2.suite == "S":
            return 1
        else:
            return -1


def sort_cards(cards):
    for i in range(len(cards) - 1):
        for j in range(len(cards) - i - 1):
            if compare_cards(cards[j], cards[j + 1]) == 1:
                temp = cards[j]
                cards[j] = cards[j + 1]
                cards[j + 1] = temp
    return cards


def check_straight_flush(cards):
    for i in range(len(cards) - 4):
        if cards[i].suite == cards[i + 1].suite and cards[i].suite == cards[i + 2].suite and cards[i].suite == cards[
            i + 3].suite and cards[i].suite == cards[i + 4].suite and cards[i].value == cards[i + 1].value + 1 and \
                cards[i].value == cards[i + 2].value + 1 and cards[i].value == cards[i + 3].value + 1 and cards[
            i].value == cards[i + 4].value + 1:
            cards[i].value
    return -1


def check_flush(cards):
    spade_count = 0
    heart_count = 0
    diamond_count = 0
    clubs_count = 0
    spade_index=0
    heart_index =0
    diamond_index = 0
    clubs_index =0
    for card in cards:
        if card.suite == "S":
            spade_count+=1
            if card.value >spade_index:
                spade_index=card.value
        elif card.suite=="H":
            heart_count+=1
            if card.value >heart_index:
                heart_index=card.value
        elif card.suite == "D":
            diamond_count+=1
            if card.value >diamond_index:
                diamond_index=card.value
        elif card.suite == "C":
            clubs_count+=1
            if card.value >clubs_index:
                clubs_index=card.value
    if spade_count>=5:
        return spade_index
    elif heart_count>=5:
        return heart_index
    elif diamond_count>=5:
        return diamond_index
    elif clubs_count>=5:
        return clubs_index
    else:
        return-1


def check_straight(cards):
    for i in range(len(cards) - 4):
        if cards[i].value == cards[i + 1].value - 1 and cards[i].value == cards[i + 2].value - 2 and cards[i].value == \
                cards[i + 3].value - 3 and cards[i].value == cards[i + 4].value - 4:
            return cards[i].value
    return -1


def check_four_of_a_kind(cards):
    for i in range(len(cards) - 3):
        if cards[i].value == cards[i + 1].value and cards[i].value == cards[i + 2].value and cards[i].value == cards[
            i + 3].value:
            return cards[i].value
    return -1


def check_full_house(cards):
    found_two = 0
    found_three = 0
    first_two_index = 0
    second_two_index = 0
    three_index = 0
    i = 0
    while i < len(cards) - 1:
        if cards[i].value == cards[i + 1].value:
            found_two += 1
            if found_two == 1:
                first_two_index = cards[i].value
            else:
                second_two_index = cards[i].value
            i += 1
        if i < len(cards) - 1:
            if cards[i + 1].value == cards[i].value and cards[i - 1].value == cards[i].value:
                if found_two == 1:
                    first_two_index == 0
                else:
                    second_two_index == 0
                found_two -= 1
                three_index = cards[i].value
                found_three += 1
                i += 1
        i += 1

    if found_two == 1 and found_three == 1:
        return (0, three_index, first_two_index)
    else:
        return (-1, 0, 0)


def check_doubles_triples(cards):
    found_two = 0
    found_three = 0
    first_two_index = 0
    second_two_index = 0
    three_index = 0
    i = 0
    while i < len(cards) - 1:
        if cards[i].value == cards[i + 1].value:
            found_two += 1
            if found_two == 1:
                first_two_index = cards[i].value
            else:
                second_two_index = cards[i].value
            i += 1
        if i < len(cards) - 1:
            if cards[i + 1].value == cards[i].value and cards[i - 1].value == cards[i].value:
                if found_two == 1:
                    first_two_index == 0
                else:
                    second_two_index == 0
                found_two -= 1
                three_index = cards[i].value
                found_three += 1
                i += 1
        i += 1

    if found_two == 1 and found_three == 1:
        return (45, three_index, first_two_index)
    elif found_three == 1:
        return (30, three_index, 0)
    elif found_two == 2:
        return (15, first_two_index, second_two_index)
    elif found_two == 1:
        return (0, first_two_index, 0)
    else:
        return (-1, 0, 0)


def check_hand(river, card1, card2):
    cards = []
    temp_cards = []
    for i in range(len(river)):
        temp_cards.append(river[i])
    temp_cards.append(card1)
    temp_cards.append(card2)
    cards = sort_cards(temp_cards)
    if check_straight_flush(cards) != -1:
        if cards[-1].value == 14:
            return 200
        return 180 + check_straight_flush(cards)
    elif check_four_of_a_kind(cards) != -1:
        return 160 + check_four_of_a_kind(cards)
    elif check_full_house(cards)[0] != -1:
        return 140 + check_full_house(cards)[1]
    elif check_flush(cards) != -1:
        return 120 + check_flush(cards)
    elif check_straight(cards) != -1:
        return 100 + check_straight(cards)
    elif check_doubles_triples(cards)[0] != -1:
        x = check_doubles_triples(cards)
        return 40 + x[0] + x[1]
    else:
        if card1.value > card2.value:
            return card1.value
        else:
            return card2.value


def check_win():
    global is_a_tie
    global cards
    global PLAYERS
    if PLAYERS_FOLDED == 4:
        for i in range(len(PLAYERS)):
            if not PLAYERS[i].folded:
                PLAYERS[i].set_money(POT_AMT)
                winner = [i]
                winner_animation(winner)
                return i
    elif RIVER_CARD_COUNT == 5:
        max_score = -100
        first_place = -1
        tied_with = -1
        for i in range(len(PLAYERS)):
            if PLAYERS[i].folded == False:
                score = check_hand(RIVER, PLAYERS[i].card1, PLAYERS[i].card2)
                if score > max_score:
                    max_score = score
                    first_place = i
                elif score == max_score:
                    tied_with = i
                    is_a_tie = True
        if is_a_tie:
            first_place_card = PLAYERS[first_place].card1
            tied_with_card = PLAYERS[tied_with].card1
            if PLAYERS[first_place].card1.value > PLAYERS[first_place].card2.value:
                first_place_card = PLAYERS[first_place].card1
            elif PLAYERS[first_place].card1.value < PLAYERS[first_place].card2.value:
                first_place_card = PLAYERS[first_place].card2
            elif PLAYERS[first_place].card1.value == PLAYERS[first_place].card2.value:
                PLAYERS[first_place].set_money(int(POT_AMT / 2))
                PLAYERS[tied_with].set_money(int(POT_AMT / 2))
                winner = [first_place, tied_with]
                winner_animation(winner)
                return first_place
            if PLAYERS[tied_with].card1.value > PLAYERS[tied_with].card2.value:
                tied_with_card = PLAYERS[tied_with].card1
            elif PLAYERS[tied_with].card1.value < PLAYERS[tied_with].card2.value:
                tied_with_card = PLAYERS[tied_with].card2
            if first_place_card.value > tied_with_card.value:
                PLAYERS[first_place].set_money(POT_AMT)
                is_a_tie = False
                winner = [first_place]
                winner_animation(winner)
                return first_place
            elif tied_with_card.value > first_place_card.value:
                PLAYERS[tied_with].set_money(POT_AMT)
                is_a_tie = False
                winner = [tied_with]
                winner_animation(winner)
                return tied_with
            else:
                PLAYERS[first_place].set_money(int(POT_AMT / 2))
                PLAYERS[tied_with].set_money(int(POT_AMT / 2))
                winner = [first_place, tied_with]
                winner_animation(winner)
                return first_place


        else:
            PLAYERS[first_place].set_money(POT_AMT)
            winner = [first_place]
            winner_animation(winner)
            return first_place
    else:
        return -1


def Check_Home():
    if btn_Home.draw(screen):
        return True
    return False


def Update_Game_Screen():
    screen.fill(GREEN)
    if not PLAYERS[player % 5].folded:
        draw_player_highlight()
    screen.blit(Player1_img, (50, int(HEIGHT / 2)))
    screen.blit(Player2_img, (280, 120))
    screen.blit(Player3_img, (WIDTH - 280 - 60, 120))
    screen.blit(Player4_img, (WIDTH - 150, int(HEIGHT / 2)))
    screen.blit(USER_TAG_img, (WIDTH / 2 - (USER_TAG_WIDTH / 2), 370))
    print_River()
    pot_text = POT_FONT.render("Pot: $" + str(POT_AMT), 1, WHITE)
    player_move_text0 = PLAYER_MOVE_FONT.render(PLAYERS[0].last_move, 1, BLUE)
    player_move_text1 = PLAYER_MOVE_FONT.render(PLAYERS[1].last_move, 1, BLUE)
    player_move_text2 = PLAYER_MOVE_FONT.render(PLAYERS[2].last_move, 1, BLUE)
    player_move_text3 = PLAYER_MOVE_FONT.render(PLAYERS[3].last_move, 1, BLUE)
    player_move_text4 = PLAYER_MOVE_FONT.render(PLAYERS[4].last_move, 1, BLUE)

    money_text0 = PLAYER_MONEY_FONT.render("$" + str(PLAYERS[0].money), 1, WHITE)
    money_text1 = PLAYER_MONEY_FONT.render("$" + str(PLAYERS[1].money), 1, WHITE)
    money_text2 = PLAYER_MONEY_FONT.render("$" + str(PLAYERS[2].money), 1, WHITE)
    money_text3 = PLAYER_MONEY_FONT.render("$" + str(PLAYERS[3].money), 1, WHITE)
    money_text4 = PLAYER_MONEY_FONT.render("$" + str(PLAYERS[4].money), 1, WHITE)

    screen.blit(money_text0, (60, 225))
    screen.blit(money_text1, (290, 95))
    screen.blit(money_text2, (570, 95))
    screen.blit(money_text3, (760, 225))
    screen.blit(money_text4, (430, 350))

    screen.blit(player_move_text0, (50, 280))
    screen.blit(player_move_text1, (280, 150))
    screen.blit(player_move_text2, (560, 150))
    screen.blit(player_move_text3, (750, 280))
    screen.blit(player_move_text4, (400, 430))
    screen.blit(pot_text, (700, 50))

    print_dealt_cards()
    print_dealer_button()

    # btn_Home.draw(screen)


def Play_Easy():
    global PLAYERS
    global POT_AMT
    global cards
    global RIVER_CARD_COUNT
    global RIVER
    global player
    Update_Game_Screen()
    if not has_dealt_cards:
        deal_cards()

    elif player == 4 and not PLAYERS[-1].folded:
        if not has_done_small_blind:
            small_blind()
            Poker_chip_sound.play()
        elif not has_done_big_blind:
            big_blind()
            Poker_chip_sound.play()
        elif is_Raising:
            handle_isRaising()
        else:
            handle_buttons()
    else:

        if PLAYERS[player].folded:
            increment_player()
        else:
            move = handle_bot_move()
            pygame.display.update()
            pygame.time.delay(1000)
            if move == "Fold":
                Fold_sound.play()
                pygame.time.delay(1000)
            elif move == "Check":
                Check_sound.play()
            elif move == "Raise" or move == "Call":
                Poker_chip_sound.play()
    if len(RIVER) == 0 and CHECK_COUNT == 5 - PLAYERS_FOLDED:
        deal_flop()
    if check_win() != -1:
        reset_game()
    if check_Checks():
        player = SMALl_BLIND
        RIVER.append(cards[0][0])
        cards[0].remove(cards[0][0])
        RIVER_CARD_COUNT += 1
        Card_flip_sound.play()

    pygame.display.update()


def update_home_screen():
    screen.fill(GREEN)
    btn_Right.draw(screen)
    btn_Left.draw(screen)
    MODES[-1].draw(screen)
    pygame.display.update()


def handle_Arrows(modes):
    if btn_Left.draw(screen):

        temp = modes[0]
        for i in range(0, len(modes) - 1):
            modes[i] = modes[i + 1]
        modes[-1] = temp
    if btn_Right.draw(screen):

        temp = modes[-1]
        for i in range(len(modes) - 1, 0, -1):
            modes[i] = modes[i - 1]
        modes[0] = temp

    MODES = modes


def pick_mode():
    top_mode = MODES[-1]

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
    run = True
    Is_Playing = False

    while run:

        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == PLAY_EASY:
                pygame.event.post(pygame.event.Event(PLAY_EASY))

                Is_Playing = True
                Play_Easy()
            elif event.type == PLAY_MEDIUM:
                pygame.event.post(pygame.event.Event(PLAY_EASY))
                Play_Easy()
                Is_Playing = True
                print("Medium")
            elif event.type == PLAY_HARD:
                pygame.event.post(pygame.event.Event(PLAY_EASY))

                Is_Playing = True
                Play_Easy()

        if not Is_Playing:
            handle_Arrows(MODES)
            pick_mode()

            update_home_screen()
    pygame.quit()


main()
