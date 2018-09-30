# blackjack

# define cards class (number, suit)

class card:
    def __init__(self, number, suit):
        self.number = number
        self.suit = suit

class player:
    def __init__(self):
        self.cards = []

hi = card(7,'heart')

# create deck
deck = []
for i in ['diamonds','clubs','hearts','spades']:
    for j in range(13):
        deck.append(card(j,i))
print(deck[1].suit)

# shuffle function
from random import shuffle
shuffle(deck)
print(deck[1].suit)

# draw card function
def draw(player):
    player.cards.append(deck.pop())

# deal function
def deal(players,deck):
    for i in players():
        draw(players[i])
        draw(players[i])

# stay function

# check who won function

# main code for gameplay
