def tripleStep(t_steps):
    # O(n) time: max number of iterations is n-4
    ## each iteration is constant work
    ## everything else in the func is constant work
    # O(1) space: only store 3 ints at a time, so constant

    # initialize number of ways to take 1, 2, and 3 steps
    numWays = [1,2,4]

    # handle edge case
    if t_steps <= 3:
        return(numWays[t_steps-1])

    # iterative
    for i in range(3,t_steps):
        ways_i = numWays[-1] + numWays[-2] + numWays[-3]
        numWays = numWays[1:] + [ways_i]
    return(numWays[-1])

if __name__ == "__main__":
    inputInt = int(input("num steps: "))
    print(tripleStep(inputInt))
