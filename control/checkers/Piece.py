class Piece:
    def __init__(self, belongsToAgent):
        self.belongsToAgent = belongsToAgent
        self.isKing = False

    def __repr__(self):
        # might change later
        rep = {
            (True,True): 'X',
            (True,False): 'x',
            (False,True): 'O',
            (False, False): 'o'
        }

        return str(rep[self.belongsToAgent, self.isKing])
