# blackjack

# define cards class (number, suit)

class card:
    def __init__(self, number, suit):
        self.number = number
        self.suit = suit

class player:
    def __init__(self,name):
        self.name = name
        self.cards = []
        self.total = 0

# create deck
deck = []
for i in ['diamonds','clubs','hearts','spades']:
    for j in range(1,14):
        deck.append(card(j,i))

# shuffle function
from random import shuffle
shuffle(deck)

# draw card function
def draw(p1):
    card = deck.pop()
    p1.cards.append(card)
    p1.total += card.number

# deal function
def deal(pList):
    for i in pList:
        draw(i)
        draw(i)

# check who won function
def whoWon(ps):
    dummy = player('dumdum')
    winner = dummy
    for i in ps:
        print(winner.name)
        if i.total > winner.total:
            winner = i
    print(winner.name)
    return(winner)
Ann = player('Ann')
Bnn = player('Bnn')
deal([Ann,Bnn])
print(Ann.total,Bnn.total)
whoWon([Ann,Bnn])

# main code for gameplay
