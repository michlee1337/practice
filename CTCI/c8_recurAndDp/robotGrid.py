def robotGrid(grid, r, c):
    # assume I'm given a grid of T and F
    # O(rc) space
    # O(rc) time
    # can probably optimize this
    # can you look ahead in the grid???

    # check path
    row = r -1
    while row > 0:
        col = c -1
        while col > 0:
            # set last cell ## could probs do this better
            if (r-1 == row and c-1 == col):
                grid[row][col] = True
            elif (grid[row][col]):
                grid[row][col] = (grid[row][col+1] or grid[row+1][col])
            col -= 1
        row -= 1

    # walk path
    i,j = [0,0]
    path = []

    while (i != r-1 or j != c-1):
        if j != c-1 and grid[i][j+1]:
             path.append("r")
             j += 1
        elif i != r-1 and grid[i+1][j]:
            path.append("d")
            i += 1
        else:
            return(False)
    return(path)

if __name__=="__main__":
    row = int(input("num rows: "))
    grid = []
    for i in range(row):
        a_row = input("grid row: ").split(" ")
        a_row = [x == "true" for x in a_row]
        grid.append(a_row)
    print(grid)
    print(robotGrid(grid, len(grid), len(grid[0])))
