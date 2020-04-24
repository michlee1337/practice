from Piece import *
import copy

class Board:
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
        self.val = 0

    # pretty print state, for debugging and display
    def __repr__(self):
        res = "_____\n"
        for row in self.state:
            res += ' '.join(map(str, row))
            res += '\n'
        res += "_____\n"
        res = res.replace('0','_')
        return res

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

    def noPieces(self, forAgent):
        for row in self.state:
            for p in row:
                if p != 0 and p.belongsToAgent != forAgent:
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
            if rn+rd>7 or cn+cd>7:
                return([])
            if state[rn][cn] != 0 and state[rn][cn].belongsToAgent != piece.belongsToAgent and state[rn+rd][cn+cd] == 0:
                nstate = copy.deepcopy(state) # references begone!
                nstate[rn][cn] = 0 # eat
                nstate[r][c], nstate[rn+rd][cn+cd] = 0, nstate[r][c] # move
                return self._doCaptureMoves(nstate,piece, rn+rd, cn+cd, True) # must make all jumps possible
            return []

        # EXT: better direction abstraction
        rowDist = {-1: r, 1: 7-r}
        colDist = {-1: c, 1: 7-c}

        if piece.isKing:
            dirs = [(1,-1),(1,1),(-1,-1),(-1,1)] # left up, right up, left down, right down
        elif piece.belongsToAgent:
            dirs = [(1,-1),(1,1)]
        else:
            dirs = [(-1,-1),(-1,1)]

        nstates = []

        # handle kings
        for rd,cd in dirs:
            if piece.isKing:
                for k in range(1,min(rowDist[rd], colDist[c]),1):
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
        print("MOVING PIECE: ",r,c)
        # moves based on whose piece it is
        # EXT: haha i really need to abstract this out
        dirs = {
            False: [(-1,-1),(-1,1)],
            True: [(1,-1),(1,1)]
        }
        nstates = []
        for rd,cd in dirs[piece.belongsToAgent]:
            rn = r+rd
            cn = c+cd
            print("Trying move to: ",rn,cn)
            # EXT: a board cell should be an object and blank/ piece are subclasses
            if rn >= 0 and cn >= 0 and rn<=7 and cn<=7 and state[rn][cn] == 0:
                print("Accepted move to: ",rn,cn)
                nstate = copy.deepcopy(state) # references begone!
                nstate[r][c], nstate[rn][cn] = nstate[rn][cn], nstate[r][c]
                nstates.append(nstate)
        return(nstates)
