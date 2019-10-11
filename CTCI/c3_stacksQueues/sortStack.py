def sortStack(stack):
    # edge, stack is less than 1 elem long
    if len(stack) < 2:
        return(stack)

    # init temp stack and iteration var
    temp = []
    iterate = True

    while iterate:

        # find out of place element
        oop_val = None

        while len(stack) > 1 and oop_val == None:
            temp.append(stack.pop())
            if stack[-1] < temp[-1]:
                oop_val = stack.pop()

        if oop_val == None: # break if no oop
            iterate = False

        else: # place oop in right place
            while len(temp) > 0 and oop_val < temp[-1]:
                stack.append(temp.pop())
            temp.append(oop_val)

    # pop anything on temp back to stack
    while len(temp) > 0:
        stack.append(temp.pop())
    return(stack)

stack = [1,6,2,9,6,10,3,4,5]

print(sortStack(stack))
