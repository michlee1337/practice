from Piece import *
from Board import *
from Agent import *

def createBoard(ll):
    ll = [l.split(" ") for l in ll]
    ret = []
    for l in ll:
        row = []
        for c in l:
            if c == "_":
                row.append(0)
            elif c == "x":
                row.append(Piece(True))
            elif c == "X":
                row.append(Piece(True))
                row[-1].isKing = True
            elif c == "o":
                row.append(Piece(False))
            elif c == "O":
                row.append(Piece(False))
                row[-1].isKing = True
            else:
                raise ValueError("Unrecognized piece")
        ret.append(row)
    return(Board(ret))

board = createBoard(["_ x _ x _ x _ x",
                    "x _ x _ x _ x _",
                    "_ _ _ x _ x _ x",
                    "_ _ _ _ _ _ _ _",
                    "_ o _ o _ _ _ _",
                    "o _ _ _ _ _ o _",
                    "_ o _ _ _ o _ o",
                    "o _ o _ o _ o _"])
board.isAgentTurn = True
a = Agent(3, None)
print(a.move(board))
