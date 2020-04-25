from Piece import *
from Board import *

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


if __name__=="__main__":
    # _____ TEST NEXT BOARD GENERATION _____
    # def need a better way of testing
    MoveParent = createBoard(["_ x _ x _ x _ x",
                                "x _ x _ x _ x _",
                                "_ _ _ x _ x _ x",
                                "_ _ _ _ _ _ _ _",
                                "_ o _ o _ _ _ _",
                                "o _ _ _ _ _ o _",
                                "_ o _ _ _ o _ o",
                                "o _ o _ o _ o _"])

    # playerMoveChild = createBoard(["_ x _ x _ x _ x",
    #                                 "x _ x _ x _ x _",
    #                                 "_ _ _ x _ x _ x",
    #                                 "o _ _ _ _ _ _ _",
    #                                 "_ _ _ o _ _ _ _",
    #                                 "o _ _ _ _ _ o _",
    #                                 "_ o _ _ _ o _ o",
    #                                 "o _ o _ o _ o _"])
    #
    # AgentMoveChild = createBoard(["_ x _ x _ x _ x",
    #                                 "x _ x _ x _ x _",
    #                                 "_ _ _ x _ x _ _",
    #                                 "_ _ _ _ _ _ x _",
    #                                 "_ o _ o _ _ _ _",
    #                                 "o _ _ _ _ _ o _",
    #                                 "_ o _ _ _ o _ o",
    #                                 "o _ o _ o _ o _"])
    #

    captureParent = createBoard(["_ x _ _ _ _ _ x",
                                "x _ x _ x _ x _",
                                "_ _ _ _ _ x _ x",
                                "_ _ x _ _ _ _ _",
                                "_ o _ o _ _ _ _",
                                "_ _ _ _ _ _ o _",
                                "_ o _ _ _ o _ o",
                                "o _ _ _ o _ o _"])


    #assert playerMoveChild in MoveParent.next_boards()

    #MoveParent.isAgentTurn = True
    #assert agentMoveChild in MoveParent.next_boards()
    #print(captureParent.next_boards())

    captureParent.isAgentTurn = True
    print(captureParent.next_boards())




'''
"_ x _ x _ x _ x",
"x _ x _ x _ x _",
"_ _ _ x _ x _ x",
"_ _ _ _ _ _ _ _",
"_ o _ o _ _ _ _",
"o _ _ _ _ _ o _",
"_ o _ _ _ o _ o",
"o _ o _ o _ o _"
____

"_ x _ x _ x _ x",
"_ _ x _ x _ x _",
"_ x _ x _ x _ x",
"_ _ _ _ _ _ _ _",
"_ o _ o _ _ _ _",
"o _ _ _ _ _ o _",
"_ o _ _ _ o _ o",
"o _ o _ o _ o _"



'''
