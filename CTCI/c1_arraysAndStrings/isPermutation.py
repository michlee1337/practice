import math

class HashMap():
    def __init__(self,size):
        self.capacity = 0
        self.size = size
        self.map = [[]] * size

    def _hash(self,char):
        return(ord(char)%self.size)

    def insert(self,char):
        self.map[self._hash(char)].append(char)
        self.capacity += 1
        return(self._hash(char))

    def lookup(self,char):
        for val in self.map[self._hash(char)]:
            if val == char:
                return(True)
        return(False)

    def delete(self, char):
        key = self._hash(char)
        for val in self.map[key]:
            if val == char:
                self.map[key].remove(char)
                self.capacity -= 1
                return(True)
        return(False)

def isPermutataion(strA, strB):
    # O(n + m) time
    # O(n) space
    lookupTable = HashMap(math.ceil(len(strA)/0.75))
    for char in strA:
        lookupTable.insert(char)

    for char in strB:
        if not (lookupTable.delete(char)):
            return(False)
    return(lookupTable.capacity == 0)

# ideas
# brute force: check each in second str: O(nm)
# sort second string then search: O(mlgm+ nlgm)

if __name__=="__main__":
    inputStrA = input("string 1: ")
    inputStrB = input("string 2: ")
    print(isPermutataion(inputStrA,inputStrB))
