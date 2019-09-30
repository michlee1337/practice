def ditch(w,h,d):
    # for each box, know which boxes can be stacked on top
    # for each of those boxes, what is the max height achievable

    # for each box
    # find the optimal box to stack on top
    # so best one stack starting from box i
    # b est two stack starting from box i

    n = len(w) # number of boxes

    # initiate memo to the heights of the boxes
    heightsByBase = [h[i] for i in range(n)]

    # iterate through all possible stack heights
    for _ in range(1,n):
        updatedMemo = heightsByBase

        for base in range(n):
            # could sort boxes by height first to allow for early termination
            for top in range(n): # small optimization: don't check self
                if strictlyLarger(base,top,w,h,d):
                    if updatedMemo[base] < heightsByBase[base] + h[top]:
                        print(top,base)
                        updatedMemo[base] = heightsByBase[base] + h[top]

        heightsByBase = updatedMemo

    return(heightsByBase)

def strictlyLarger(base,top,w,h,d):
    return(base <= 0 or top >= len(w) or w[base] > w[top] and h[base] > h[top] and d[base] > d[top])



def stackBoxes(w,h,d):
    # max height considering the addition of box

    n = len(w) # number of boxes
    stack = [0] # probably unecessary but for now
    stackHeight = h[0]

    for box in range(1,n):
        for i,top in enumerate(stack):
            # if it can be inerted below top with no negations
            if strictlyLarger(i-1,box,w,h,d) and strictlyLarger(box,i,w,h,d):
                #print("insert", box, i)
                stack.insert(i, box)
                stackHeight += h[box]
                #print(stack)
                break
            # if can be inserted with negation:
            elif strictlyLarger(box,i,w,h,d):
                # if box taller than base being replaced
                replacedHeight = sum([h[x] for x in stack[:i-1]])
                if h[box] > replacedHeight:
                    #print("insert", box)
                    stack = [box] + stack[i:]
                    #print(stack)
                    stackHeight += h[box] - replacedHeight
                    break
    print(stackHeight)
    return(stack)



    # each box can potentially be added anywhere in the stack (could go bottom to top, since that maintains the most height)
    # if box can be inserted without deletions, add and continue
    # if box can be added in middle and negates base: if new stack is taller, replace stack

if __name__=="__main__":
    #tInput = (([0],[0],[0]),([1,2,3],[1,2,3],[1,2,3]))
    tInput = (([5,4,3,2,1],[1,2,3,4,5],[9,3,5,1,5]),([1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5]),([1,2,3,1,5],[2,3,4,4,5],[1,2,3,4,5]))
    for t in tInput:
        print(stackBoxes(t[0],t[1],t[2]))
