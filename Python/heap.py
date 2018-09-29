# making a binary max heap

# math definition
# a[k] <= a[2*k+1]
# a[k] <= a[2*k+2]

#mapping heap parents to kids
# root node = 0
# parent = (index-2)/2
# left child = index*2 +1
# right child = index*2 + 2

class heap:
    def __init(self):
        self.heapList = []
        self.currentSize = 0
    def getLeftChild(currentIndex):
        return(2*currentIndex+1)
    def getRightChild(currentIndex):
        return(2*currentIndex+2)
    def getParent(currentIndex):
        return((currentIndex-1)//2)
    def bubbleUp(self, currentIndex):
        while i/2 > 0: # as long as not root node
            if self.heapList[i] > self.heapList[getParent(i)]: # if child > parent
                temp = self.heapList[i] # swap
                self.heapList[i] = self.heapList[getParent(i)]
                self.heapList[getParent(i)] = temp
            i = i//2
    def insert(self, x): # when inserting new node
        self.heapList.append(x)
        self.currentSize = self.currentSize + 1
        self.bubbleUp(self.currentSize) # put it in the right place

print(2//2)
