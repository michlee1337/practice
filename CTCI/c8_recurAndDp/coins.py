def coins(cents):
    return(doCoins(cents,[25,10,5,1]))


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




if __name__ == "__main__":
    test_in = (0,1,2,3,4,5,6,7,8,9,10)
    #test_out = (0,1,4)
    for t in test_in:
        print(coins(t))
