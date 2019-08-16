# biggest piece has nothing on top => move to final
# inductive step: move everything except bottom to "other" stack

def towersOfHanoi(numDiscs):
    # assumption: all the disks start on stack1 and we need to move it to stack3
    stack1 = [x for x in range(numDiscs,0,-1)]
    stack2 = []
    stack3 = []
    if len(stack1)  == 1:
        print("move ",stack1[0], "to stack3")
        stack3.append(stack1.pop())
        # swicth stack1 and stack2 so stack1 is always the one we focus on
        print("swap stack1 stack2")
        stack1, stack2 = stack2, stack1
    else:
        towersOfHanoi(numDiscs-1)
        print("move ",stack1[0], "to stack3")
        stack3.append(stack1.pop())
        #progression.append((stack1,stack2,stack3))
    return(1)

if __name__=="__main__":
    num = int(input("num discs: "))
    print(towersOfHanoi(num))
