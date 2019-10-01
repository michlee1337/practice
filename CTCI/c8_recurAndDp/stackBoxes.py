def strictlyLarger(base,top,w,h,d):
    return(base <= 0 or top >= len(w) or w[base] > w[top] and h[base] > h[top] and d[base] > d[top])

def sortByHeight(w,h,d):
    h,w,d = zip(*sorted(zip(h,w,d)))
    return(w,h,d)

def stackBoxes(w,h,d):
    w,h,d = sortByHeight(w,h,d)
    # max height considering the addition of box

    n = len(w) # number of boxes
    stack = [0]

    for box in range(1,n):
        for i,top in enumerate(stack):
            # if it can be inserted without removing boxes
            if strictlyLarger(i-1,box,w,h,d) and strictlyLarger(box,i,w,h,d):
                stack.insert(i, box)
                break
            # if can be inserted by removing some boxes
            elif strictlyLarger(box,i,w,h,d):
                # if box taller than base being replaced
                replacedHeight = sum([h[x] for x in stack[:i-1]])
                if h[box] > replacedHeight:
                    stack = [box] + stack[i:]
                    break
    return(sum([h[i] for i in stack]))

if __name__=="__main__":
    tInput = (([5,4,3,2,1],[1,2,3,4,5],[9,3,5,1,5]),([1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5]),([1,2,3,1,5],[2,3,4,4,5],[1,2,3,4,5]))
    tOutput = (1,15,14)
    for i,t in enumerate(tInput):
        print("Input: {}".format(t))
        tres = stackBoxes(t[0],t[1],t[2])
        print("Output: {}".format(tres))
        if tres != tOutput[i]:
            print("ERROR: expected {},".format(tOutput[i]))
