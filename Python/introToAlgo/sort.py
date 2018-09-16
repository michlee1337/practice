# EXP: explanation
# N: note
# temp: delete when done


# insertion sort
def insertSort(L):
    # EXP: for each card (not including first)
    for i in range(1,len(L)): # EXP: for each card in deck (except first)
        swap = True
        currPos = i # EXP: take the card, remember position of card
        while currPos > 0 and swap == True: # EXP: compare it with all cards before it (backwards sequence) until either you reach the end or there was no swap on last iteration
            swap = False
            if L[currPos] < L[currPos-1]: # EXP: if smaller than card directly before it, swap positions
                temp = L[currPos]
                L[currPos] = L[currPos-1]
                L[currPos-1] = temp
                swap = True
            currPos -= 1
    return(L)

# insertSort([5,0,3,2,1])

# bubble sort
def bubBub(L):
    swap = True # EXP: make it happen

    while swap == True: # EXP: if change made in last iteration, continue
        swap = False
        for i in range(len(L)-1): # EXP: compare and swap for each item in L
            if L[i] > L[i+1]:
                temp = L[i]
                L[i] = L[i+1]
                L[i+1] = temp

                swap = True # EXP: if swap occurs, reiterate
    return(L)

# print(bubBub([7,74,3,774,5,1,3,2]))
