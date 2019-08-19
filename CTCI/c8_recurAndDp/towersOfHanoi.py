# reasoning: this took way too long
# base case: biggest piece has nothing on top => move to final
# inductive step: move everything except bottom to "other" stack

# helper function, so I don't mess with the params of the main function
def moveDiscToTower(towerList, disc, from_ind, to_ind, other_ind):
    # recursive step: if there's stuff blocking the disc I want to move
    # move those discs to the "other" stack
    if towerList[from_ind][-1] != disc:
        towerList = moveDiscToTower(towerList, disc-1, from_ind, other_ind, to_ind)

    # move my disc!
    print("move", disc, "from", from_ind, "to", to_ind)
    towerList[to_ind].append(towerList[from_ind].pop())

    # put any existing smaller discs back on top of moved disc
    ### this is to always keep the "other" stack clear to accomadate the next move
    if disc-1 > 0:
        towerList = moveDiscToTower(towerList, disc-1, other_ind, to_ind, from_ind)
    return(towerList)


def towersOfHanoi(towerList):
    # towerList MUST include three stacks
    ### each disc is indicated my a number
    ### 1 is the smallest disc, n is the largest
    ### each tower is represented as a stack, with the last index being the top element
    movedTowerList = moveDiscToTower(towerList, len(towerList[0]), 0, 2, 1)
    return(movedTowerList)

if __name__=="__main__":
    num = int(input("num discs: "))
    # initialize towers
    towerList = [[x for x in range(num,0,-1)], [], []]
    print("solving: ", towerList)
    print(towersOfHanoi(towerList))
