def isPalindrome(str):
    # O(n) time
    # arguably O(1) space
    # O(min of n or c) space
    lookupTable = {}
    for c in str:
        if c == " ":
            pass
        elif c in lookupTable:
            lookupTable[c] = (lookupTable[c] + 1) % 2
        else:
            lookupTable[c] = 1
    return(sum(lookupTable.values()) == 1)

if __name__ == "__main__":
    inputStr = input("your str: ")
    print(isPalindrome(inputStr))
