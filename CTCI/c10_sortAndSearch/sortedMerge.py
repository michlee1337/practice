def sortedMerge(A,B):
    # time: O(n+m)
    # space: O(1)

    # init pointers
    pA, pB = 0,0

    # while A is not exhauted
    while pB < len(B):
        if A[pA] == None or B[pB] < A[pA]:
            A.insert(pA,B[pB])
            A.pop()
            pB += 1
        else:
            pA += 1

    return(A)

if __name__=="__main__":
    tIn = (([1,4,6,7,18,None,None,None],[0,5,20]),([],[]))
    tOut = ([0,1,4,5,6,7,18,20],[])
    for i,_ in enumerate(tIn):
        tRes = sortedMerge(tIn[i][0],tIn[i][1])
        print(tRes)
        if tRes != tOut[i]:
            print("problem!", tIn[i])
