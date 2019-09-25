def coins(cents):
    #return(doCoins(cents,[25,10,5,1]))
    if cents <= 0:
        return("error: value must be more than 0")
    return(doCoinsDP(cents,[1,5,10,25]))

def doCoins(cents,coins):
    ways = 0
    # base
    if cents == 0:
        return(1)
    # recurse
    else:
        for i,coin in enumerate(coins):
            if cents >= coin:
                ways += doCoins(cents-coin,coins[i:])
    return(ways)


# BROKEN: need to fix
def doCoinsDP(cents,coins):
    # memo[i] keeps count of the number of ways to have i cents
    # 0 is initialized to 1
    memo = [1] + [0 for _ in range(cents)]

    # build memo up by coin
    for i, coin in enumerate(coins):
        updated = memo
        # update ways for each value using current coin
        for val in range(1,cents+1):
            # ways with
            if val >= coin:
                updated[val] += memo[val-coin]
        memo = updated
    return(memo[-1])





if __name__ == "__main__":
    test_in = (0,1,2,3,4,5,6,7,8,9,10)
    #test_in = [7]
    #test_out = (0,1,4)
    for t in test_in:
        print(t, ": ", coins(t), doCoins(t,[25,10,5,1]))
