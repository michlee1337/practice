# Tversky studied Philadelphia 76ers basketball games from 1980-1981
# players estimate

# Basketball
# player has 50-50 chance of scoring
p = 0.5
# player makes 20 shots per game
x = 20
# record the hits and misses of a game
def aGame():
    c = 0
    s = []
    while c < x:
        if random.random() > p:
            s.append(1)
        else:
            s.append(0)
        c += 1
    return(s)
# calculate the probability of a 5-streak within n games
def pGame(n):
    streaks = 0
    for x in range(n):
        g = aGame()
        sumG = [(k, sum(1 for i in g)) for k,g in groupby(g)]
        for i in sumG:
            if i[0] == 1:
                if i[1] >= 5:
                    streaks += 1
    return(streaks/n)
pGame(1000000)
