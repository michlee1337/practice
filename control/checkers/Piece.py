class Piece:
    '''
    A checkers piece.

    Attributes
        - belongsToAgent <Boolean>: True if the piece belongs to Agent
        - isKing <Boolean>: True if the piece is a King.

    Methods
        - crown: makes the piece a King piece.
        - getDirs: returns the directions that the piece can move.
    '''

    def __init__(self, belongsToAgent, isKing=False):
        self.belongsToAgent = belongsToAgent
        self.isKing = isKing

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
