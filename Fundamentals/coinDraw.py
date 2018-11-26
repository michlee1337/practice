# given a stack of coins and two players, each player alternates to select either the top or bottom coin.
# find the maximal ammount a player can win given that both players make optimum choices.

class coinStack(size=10):
    def __init__():
        self.coins = []

    def takeTop(self):
        return(self.coins.pop(0))

    def takeBottom(self):
        return(self.coins.pop())

class player():
    def __init__():
        self.coins = []
        self.points = 0

    def takeMax(self,coinStack):
        self.coins.append(max(coinStack))
        self.points += max(coinStack)
        return(0)

def bestMove(coinStack, p1,p2):
    # for each coin
    imStack = []
    for coin in coinStack:
        bestSums = []
        # for each item starting from this coin
        for i in len(coinStack):
            imStack.append(coin)
            lastMove = False
            while len(imStack) > 0:
                if lastMove:
                    p2.takeMax(imStack)
                    lastMove = False
                else:
                    p1.takeMax(imStack)
                    lastMove = True
            imStack.append(coinStack.pop())



p1 = player()
p2 = player()

coinStack = [1,2,8]
