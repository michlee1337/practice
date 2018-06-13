# trying to porgram solution to TedEd cat army riddle
# 2, 10, 14
# +5 +7 square root

def listmultiples(x1,x2):
    m = []
    for i in range(10):
        n = []
        for j in range (10):
            n.append((x1**i)*(x2**j))

        m.append(n)
    return m

def less60(a):
    less = []
    for x in range(len(a)):
        for y in range(len(a[x])):
            if a[x][y] < 60:
                less.append(a[x][y])
    less.sort()
    return less


def addx(a,x):
    tab = [a]
    for reps in range(10):
        temp = []
        for i in range(len(a)):
            temp.append(a[i] + x)
        tab.append(temp)
    return tab
