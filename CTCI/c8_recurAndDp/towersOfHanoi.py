# biggest piece has nothing on top => move to final
# inductive step: move everything except bottom to "other" stack

def moveDiscToTower(towerList, disc, from_ind, to_ind, other_ind):
    # towerList must include three stacks
    # move disc to tower
    #print("called",towerList, disc,from_ind,to_ind,other_ind)

    # base case: if the disc is at the top of the tower and the destination tower top is bigger, move it
    if towerList[from_ind][-1] == disc and (len(towerList[to_ind]) == 0 or towerList[to_ind][-1] > disc):
        #print('base')
        print("move", disc, "from", from_ind, "to", to_ind)
        towerList[to_ind].append(towerList[from_ind].pop())

        # move all discs smaller than disc back on top of disc
        if disc-1 > 0:
            #print('moving items on top')
            moveDiscToTower(towerList, disc-1, other_ind, to_ind, from_ind)

    else:
        # move all items on top of disc to other stack
        #print('moving top items')
        moveDiscToTower(towerList, disc-1, from_ind, other_ind, to_ind)
        # move all discs smaller than disc-1 (if any) back on top of disc-1
        if disc-2 > 0:
        #    print('moving items on top')
            moveDiscToTower(towerList, disc-2, to_ind, other_ind, from_ind)
        # move self to right pos
        #print('moving self')
        moveDiscToTower(towerList, disc, from_ind, to_ind, other_ind)

    #print("resolved",towerList, disc,from_ind,to_ind,other_ind)
    return(towerList)


def towersOfHanoi(towerList):
    # each disc is indicated my a number
    # 1 is the smallest disc, n is the largest
    # each tower is represented as a stack, with the last index being the top element
    movedTowerList = moveDiscToTower(towerList, len(towerList), 0, 2, 1)
    return(movedTowerList)

if __name__=="__main__":
    num = int(input("num discs: "))
    # initialize towers
    towerList = [[x for x in range(num,0,-1)], [], []]
    print(towersOfHanoi(towerList))
