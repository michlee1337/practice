def maxStrawberries(maxLimit,numBush,bushes):
    dp = [[0]+([None] * (maxLimit)) for _ in range(numBush)]
    return(solveMaxStrawberries(maxLimit,numBush-1,bushes,dp))

def solveMaxStrawberries(maxLimit, bushIndex, bushes, dp):
    if bushIndex < 0:
        return(0)

    maxWithout = solveMaxStrawberries(maxLimit, bushIndex-1, bushes, dp)
    maxWithNL = bushes[bushIndex] + solveMaxStrawberries(maxLimit-bushes[bushIndex], bushIndex-2, bushes, dp)

    if (maxWithNL) <= maxLimit:
        maxWith = maxWithNL
    else:
        maxWith = 0
    if maxWithout >= maxWith:
        dp[bushIndex][maxLimit] = maxWithout
    else:
        dp[bushIndex][maxLimit] = maxWith

    return(dp[bushIndex][maxLimit])

if __name__=="__main__":
    print(maxStrawberries(100,5,[50,10,20,30,40]))
