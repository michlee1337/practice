def sortedNoSize(listy,x):
    # find upper bound
    e_ind = 1
    while listy[e_ind] != -1 or listy[e_ind]>x:
        e_ind *= 2
    #return(listy[e_ind],e_ind)
    return(binSearch(listy,x,0,e_ind))

def binSearch(listy,x,start,end):
    mid = start + ((end-start)//2)
    if listy[mid] == x:
        return(mid)
    elif listy[mid] == -1 or listy[mid] > x:
        return(binSearch(listy,x,start,mid))
    else:
        return(binSearch(listy,x,mid,end))

if __name__=="__main__":
    t_in = (([0,1,2,3,4,5,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],5),([0,1,2,-1,-1,-1,-1,-1,-1],0),([0,1,2,-1,-1,-1,-1,-1,-1],1))
    t_out = (5,0,1)
    for i,t in enumerate(t_in):
        test = sortedNoSize(t[0],t[1])
        print(test)
        if test != t_out[i]:
            print("ERROR, expected", t_out[i])
