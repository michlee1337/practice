def searchRotated(arr,n,v):
    return(doSearchRotated(arr,0,n,v))

def doSearchRotated(arr,s,e,v):
    mid = (e+s)//2
    if e <= s:
        return(None)
    elif arr[mid] == v:
        return(mid)
    elif v < arr[mid]:
        if v > arr[s]:
            return(doSearchRotated(arr,s,mid,v))
        else:
            return(doSearchRotated(arr,mid,e,v))
    else:
        #breakpoint()
        if v < arr[e]:
            return(doSearchRotated(arr,mid,e,v))
        else:
            return(doSearchRotated(arr,s,mid,v))

if __name__=="__main__":
    tInput = (([15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14],5),([],1))
    tOutput = (8,None)
    for i,t in enumerate(tInput):
        t = searchRotated(t[0],len(t[0])-1,t[1])
        print(t)
        if t != tOutput[i]:
            print("ERROR, expected", tOutput[i])
