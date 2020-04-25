from Piece import *
from Board import *
from Game import *

if __name__== "__main__":
    res = {}
    for d in range(1,3): # avoiding highest difficulty because it takes too long
        for h in range(0,3):
            res[(d,h)] = 0
            for k in range(10):
                g = Game(difficulty=d,heuristic=h,DEBUG=True)
                g.play()
                res[(d,h)] += g.winner
    print(res)
