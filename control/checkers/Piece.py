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

    def crown(self):
        self.isKing = True
        return(0)

    def getDirs(self):
        if self.isKing:
            return [(1,-1),(1,1),(-1,-1),(-1,1)]
        elif self.belongsToAgent:
            return [(1,-1),(1,1)]
        else:
            return [(-1,-1),(-1,1)]
