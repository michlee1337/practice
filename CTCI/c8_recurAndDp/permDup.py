# helper to modularize
def insertAll(str, char):
    inserted = []
    for i in range(len(str) + 1):
        # if current char is a duplicate, only count insertions after i
        if (i > 0 and str[i-1] == char):
            inserted = []
        inserted.append(str[:i] + char + str[i:])
    return(inserted)

def permDup(str):
    # trivial base: permutation of one char is the char
    if len(str) == 1:
        return([str])

    # iterative step: insert char into all positions in all unique permutations
    else:
        perm_wo = permDup(str[1:])
        perm_w = []

        for perm in perm_wo:
            perm_w += insertAll(perm,str[0])
        return(perm_w)

if __name__=="__main__":
    str = input("your str: ")
    print(permDup(str))
