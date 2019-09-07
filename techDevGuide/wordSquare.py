def isWordSquare(w_list):
    # O(n^2) time where n is number of words
    # O(1) space
    n = len(w_list)
    for i in range(n):
        for j in range(n):
            if w_list[j][i] != w_list[i][j]:
                return(False)
    return(True)

# helper: test all permutations
# to keep params clean
def getWordSquares(w_list, n, square = [], perms = []):

    # base case: if square full, append if word square
    if len(square) == n:
        if isWordSquare(square):
            perms.append(square)
        return(perms)

    # base case: if w_list depleted, return perms
    if len(w_list) == 0:
        return(perms)

    # recursive step: add all perms for current pos and call for rest
    else:
        for i in range(len(w_list)):
            perms = getWordSquares(w_list[:i]+w_list[i+1:], n, square + [w_list[i]], perms)
        return(perms)

def wordSquares(w_list):
    if len(w_list) < 1:
        return("need list")
    return(getWordSquares(w_list, len(w_list[0])))

if __name__=="__main__":
    w_list = input("word list: ").split()
    print(w_list)
    print(wordSquares(w_list))
