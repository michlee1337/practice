import math

class HashMap():
    def __init__(self, size):
        self.size = size
        self.map = [[]] * size

    def _getHash(self,char):
        return(ord(char) % self.size)

    def insert(self,char):
        key = self._getHash(char)
        self.map[key].append(char)
        return(0)

    def lookup(self,char):
        key = self._getHash(char)
        for slot in self.map[key]:
            if slot == char:
                return(True)
        return(False)

def isUnique1(str):
    # Idea 1: store each char in a hash map and lookup
    ## terminate if present
    # !! hash maps can have false positives!
    # !! is a false positive acceptable?

    # Expected O(n) time, worst case O(n^2) time
    # O(n) space

    # implementation details
    # since I'm using an array to resolve collisions its worst case O(n^2) time.
    # But its expected O(n) time since average lookup should be O(1) !# review this
    # if i used a binary tree to resolve collisions it would be O(nlgn)

    lookupTable = HashMap(math.ceil(len(str)/0.75)) # optimal size to minimize collisions

    for char in str:
        if (lookupTable.lookup(char)):
            return(False)
        lookupTable.insert(char)
    return(True)


def isUnique2(str):
    # Idea 2: for each char, compare against later chars
    # terminate if duplicate
    # time = (n(n-1))/2 = O(n^2)
    # space = O(1)

    # implementation details
    # null is True
    # when char can be stringified, it will be (special chars, nums)
    for i in range(len(str)):
        for j in range(i+1,len(str)):
            if str[i] == str[j]:
                return(False)
    return(True)

    ## Could a bit vector be useful?

if __name__ == "__main__":
    inputStr = input("unique str?: ")
    print(isUnique1(inputStr))
    print(isUnique2(inputStr))
