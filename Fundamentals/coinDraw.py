# given a stack of coins and two players, each player alternates to select either the top or bottom coin.
# find the maximal ammount a player can win given that both players make optimum choices.

'''
class coinStack(size=10):
    def __init__():
        self.coins = []

    def takeTop(self):
        return(self.coins.pop(0))

    def takeBottom(self):
        return(self.coins.pop())

class player():
    def __init__():
        self.coins = []
        self.points = 0

    def takeMax(self,coinStack):
        self.coins.append(max(coinStack))
        self.points += max(coinStack)
        return(0)
'''

# find nth fib number cause coins is too complicated

# recursive
def fib(n):
    if n == 1 or n == 2:
        return(1)
    return(fib(n-1)+ fib(n-2))

# memoized
def fib1(n, memo):
    if memo[n-1] is not None:
        return(memo[n-1])
    elif n == 1 or n == 2:
        result = 1
    else:
        result = fib1(n-1,memo)+fib1(n-2,memo)
    memo[n-1] = result
    return(result)

# bottom up
def fib2(n):
    memo = [None] * n
    memo[0] = 1
    memo[1] = 1
    for i in range(2,n):
        memo[i] = (memo[i-1]+memo[i-2])
    return(memo[n-1])


memo = [None] * 16
print(fib(16))
print(fib1(16,memo))
print(fib2(16))

# find best move given coin stack: recurse
def maxSum(coinStack):
    # base case
    if len(coinStack) <= 2:
        return(max(coinStack))
    else:
        return(max(coinStack[0] + min(maxSum(coinStack[2:]),maxSum(coinStack[1:-1])),
        coinStack[-1] + min(maxSum(coinStack[1:-1]),maxSum(coinStack[:-2]))))


print(maxSum([1]))
print(maxSum([1,2]))
print(maxSum([1,2,3]))
print(maxSum([1,2,3,4,5,6,7,8,9,1,4,2]))

test = [1,2,3]
sum([1,2,3,4,5,6,7,8,9,1,4,2])
52-29
