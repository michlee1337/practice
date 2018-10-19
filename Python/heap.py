# making a binary max heap

# math definition
# a[k] <= a[2*k+1]
# a[k] <= a[2*k+2]

#mapping heap parents to kids
# root node = 0
# parent = (index-2)/2
# left child = index*2 +1
# right child = index*2 + 2


def maxH(A):
    sorted = []
    while len(A) > 1: #while the list is not 1 item
        for i in range(1,len(A)-1): # for each item in list
            ind = i
            print('____')
            print("sorting", A, "; index: ",ind)

            while ind > 0: # as long as not root node
                #print("child = ",A[ind],"parent = ", A[(ind-1)//2])
                if A[ind] > A[(ind-1)//2]: # if child > parent
                    print('swap on', ind)
                    temp = A[ind]
                    A[ind] = A[(ind-1)//2]
                    A[(ind-1)//2] = temp
                else:
                    print('no swap')
                ind = ind//2
        sorted.append(A[0])
        print("sorted =",sorted)
        A = A[1:len(A)]
    return(sorted)

print(maxH([3,1,2,17,99,-7,2]))



'''
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
        return(1)
    def insert(self, x): # when inserting new node
        self.heapList.append(x)
        self.currentSize = self.currentSize + 1
        self.bubbleUp(self.currentSize) # put it in the right place
        return(1)
    def maxH(A):
        sorted = []
        for i in range(1,len(A)):
            bubbleUp(A[i],i)
            sorted.append(A.pop)
        return(sorted)

A = heap()

A.heapList = [5,8,3,1,9]

A.maxH()



hi = heap()
print(hi)


'''
