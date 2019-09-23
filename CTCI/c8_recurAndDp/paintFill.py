def paintFill(screen, x, y, color):
    return(doPaintFill(screen, x, y, screen[x][y], color))

def doPaintFill(screen, x, y, old, new):
    if len(screen) > x and len(screen[0]) > y and screen[x][y] == old:
        screen[x][y] = new
        screen = doPaintFill(screen, x-1, y, old, new)
        screen = doPaintFill(screen, x+1, y, old, new)
        screen = doPaintFill(screen, x, y-1, old, new)
        screen = doPaintFill(screen, x, y+1, old, new)
    return(screen)

if __name__=="__main__":
    testInput = (([[1,1,1,1,0],[1,1,0,0,1],[1,0,0,0,0],[1,0,0,1,1]],2,3,2),([[1,0,1,1,0],[1,1,0,0,1],[0,1,1,1,1],[1,0,0,1,1]],2,0,2))
    testOutput = ([[1,1,1,1,0],[1,1,2,2,1],[1,2,2,2,2],[1,2,2,1,1]],[[1,0,1,1,0],[1,1,0,0,1],[2,1,1,1,1],[1,0,0,1,1]])
    for i,t in enumerate(testInput):
        screen = paintFill(t[0], t[1], t[2], t[3])
        print(screen)
        if screen != testOutput[i]:
            print("error: expected", testOutput[i])
