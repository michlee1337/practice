from Piece import *
import copy

class Board:
    '''
    Attributes:
        - state
        - isAgentTurn

    '''
    def __init__(self, state=None, isAgentTurn=False):
        if state is None:
            self.state = [
                [ 0, Piece(True), 0, Piece(True), 0, Piece(True), 0, Piece(True)],
            	[ Piece(True), 0, Piece(True), 0, Piece(True), 0, Piece(True), 0],
            	[ 0, Piece(True), 0, Piece(True), 0, Piece(True), 0, Piece(True)],
            	[ 0, 0, 0, 0, 0, 0, 0, 0],
            	[ 0, 0, 0, 0, 0, 0, 0, 0],
            	[Piece(False), 0,Piece(False), 0,Piece(False), 0,Piece(False), 0],
            	[ 0,Piece(False), 0,Piece(False), 0,Piece(False), 0,Piece(False)],
            	[Piece(False), 0,Piece(False), 0,Piece(False), 0,Piece(False), 0]
            	]
        else:
            self.state = state
        self.isAgentTurn = isAgentTurn

    # pretty print state, for debugging and display
    def __repr__(self):
        res = "_____\n"
        for row in self.state:
            res += ' '.join(map(str, row))
            res += '\n'
        res += "_____\n"
        res = res.replace('0','_')
        return res

    def customState(self,state):
        '''
        Accepts lists of integers as input and converts
        to lists of pieces.
        '''
        transform = {
            0: 0,
            1: Piece(True),
            2: Piece(True, True),
            -1: Piece(False),
            -2: Piece(False,True)
        }
        self.state = [[transform[v] for v in row] for row in state]
        return(0)

    def next_boards(self):
        # for each piece
        nstates = []
        captureStates = []
        simpleStates = []

        # EXT: unnecessary work, could fix
        for r,row in enumerate(self.state):
            for c,piece in enumerate(row):
                if piece != 0 and self.isAgentTurn == piece.belongsToAgent:
                    captureStates += self._doCaptureMoves(self.state, piece, r, c)
                    simpleStates += self._doSimpleMoves(self.state, piece, r, c)

        # if capture possible, must capture.
        if len(captureStates) != 0:
            return [Board(s, not self.isAgentTurn) for s in captureStates]
        else:
            return [Board(s, not self.isAgentTurn) for s in simpleStates]

    def noPieces(self, ofAgent):
        for row in self.state:
            for p in row:
                if p != 0 and p.belongsToAgent == ofAgent:
                    return(False)
        return(True)

    def _doCaptureMoves(self, state, piece, r, c, captured=False):
        '''
        Recursive function.
        Must make all jumps possible.
        '''

        # helper: capture whatever is possible, return result
        def omnom(state,piece,r,c,rn,cn,rd,cd):
            # out of bounds
            if rn+rd>7 or cn+cd>7 or rn+rd < 0 or cn+cd < 0:
                return([])
            if state[rn][cn] != 0 and state[rn][cn].belongsToAgent != piece.belongsToAgent and state[rn+rd][cn+cd] == 0:
                nstate = copy.deepcopy(state) # references begone!
                nstate[rn][cn] = 0 # eat
                nstate[r][c], nstate[rn+rd][cn+cd] = 0, nstate[r][c] # move
                if nstate[rn+rd][cn+cd].belongsToAgent and rn+rd == 7:
                    nstate[rn+rd][cn+cd].crown() # become king
                    return([nstate])
                elif not nstate[rn+rd][cn+cd].belongsToAgent and rn+rd == 0:
                    nstate[rn+rd][cn+cd].crown() # become king
                    return([nstate])
                else:
                    return self._doCaptureMoves(nstate,piece, rn+rd, cn+cd, True) # recurse to complete all captures
            return []

        nstates = []

        # handle kings
        for rd,cd in piece.getDirs():
            if piece.isKing:
                #for k in range(1,min(rowDist[rd], colDist[cd]),1):
                for k in range(1, 8):
                    rn = r+rd*k
                    cn = c+cd*k
                    nstates += omnom(state,piece,r,c,rn,cn,rd,cd)
            else:
                rn = r+rd
                cn = c+cd
                nstates += omnom(state,piece,r,c,rn,cn,rd,cd)

        # base case: if no more captures possible but have captured before, return self
        if len(nstates) == 0 and captured:
            return([state])

        return(nstates)

    def _doSimpleMoves(self, state, piece, r, c):
        # moves based on whose piece it is
        # EXT: haha i really need to abstract this out

        nstates = []
        for rd,cd in piece.getDirs():
            rn = r+rd
            cn = c+cd
            # EXT: a board cell should be an object and blank/ piece are subclasses
            if rn >= 0 and cn >= 0 and rn<=7 and cn<=7 and state[rn][cn] == 0:
                nstate = copy.deepcopy(state) # references begone!
                nstate[r][c], nstate[rn][cn] = nstate[rn][cn], nstate[r][c]
                if piece.belongsToAgent and rn == 7:
                    piece.crown()
                elif not piece.belongsToAgent and rn == 0:
                    piece.crown()
                nstates.append(nstate)
        return(nstates)
