def eightQueens():
    return(doEightQueens(8,[]))

def board(placement):
    return(placement)

def placable(row,col,placements):
    for place in placements:
        rcomp, ccomp = place
        # no need to check row since the recursion decreases by row
        if ccomp == col or rcomp-ccomp == row-col or rcomp+ccomp == row+col:
            return(False)
    return(True)

def doEightQueens(rem,placements):
    if rem == 0:
        print(board(placements))
    else:
        # always place by rows, removes redundant perms + stuff to check
        for col in range(8):
            # find a place for this queen
            if placable(rem-1,col,placements):
                doEightQueens(rem-1, placements + [(rem-1,col)])
    return(placements)

if __name__=="__main__":
    eightQueens()
