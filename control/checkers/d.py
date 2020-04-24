# helper: check if a piece is edible
def edible(state, piece, rn, cn, rd, cd):
    exists = state[rn][cn] != 0
    opponent = state[rn][cn].belongsToAgent != piece.belongsToAgent
    unprotected = state[rn+rd][cn+cd] == 0
    return exists and opponent and unprotected

# helper: update state after eating
def eat(state,r,c,rn,cn,rd,cd):
    nstate = copy.deepcopy(state) # references begone!
    nstate[rn][cn] = 0 # eat
    nstate[r][c], nstate[rn+rd][cn+cd] = 0, nstate[r][c] # move
    return(nstate)

if edible(state, piece, rn, cn, rd, cd):
    nstate = eat(state,r,c,rn,cn,rd,cd):
    recurseStates = self._doCaptureMoves(nstate,piece, rn+rd, cn+cd, True) # must make all jumps possible
    nstates += recurseStates

'''        else:
            for rd,cd in dirs:
                rn = r+rd
                cn = c+cd
                if edible(state, piece, rn, cn, rd, cd):
                    nstate = eat(state,r,c,rn,cn,rd,cd):
                    recurseStates = self._doCaptureMoves(nstate,piece, rn+rd, cn+cd, True) # must make all jumps possible
                    nstates += recurseStates
'''
