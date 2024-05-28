import main
import player
river = [main.CARDS_[0][4], main.CARDS_[3][12], main.CARDS_[0][6], main.CARDS_[2][5], main.CARDS_[2][9] ]

bot = player.Player()
bot.set_cards(main.CARDS_[3][11], main.CARDS_[3][2])

print(main.check_hand(river, bot.card1, bot.card2))