def bubBub(L):
    # make it happen
    swap = True

    # if change made in last iteration, continue
    while swap == True:
        # set the var for a reiteration to False
        swap = False

        # compare and swap for each item in L
        for i in range(len(L)-1):
            if L[i] > L[i+1]:
                temp = L[i]
                L[i] = L[i+1]
                L[i+1] = temp
                # if swap occurs, set var for reiteration to true
                swap = True
    return(L)

#test
print(bubBub([7,74,3,774,5,1,3,2]))
