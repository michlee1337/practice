# helper to modularize
def insertAll(str, char):
    inserted = []
    for i in range(len(str) + 1):
        inserted.append(str[:i] + char + str[i:])
    return(inserted)

def permUniq(str):
    # trivial base: permutation of one char is the char
    if len(str) == 1:
        return([str])

    # iterative step: insert char into all positions in all unique permutations
    else:
        perm_wo = permUniq(str[1:])
        perm_w = []

        for perm in perm_wo:
            perm_w += insertAll(perm,str[0])
        return(perm_wo + perm_w + [str[0]])

if __name__=="__main__":
    str = input("your str: ")
    print(permUniq(str))
