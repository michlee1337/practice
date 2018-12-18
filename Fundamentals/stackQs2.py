# implement stack through min heap priority q

class MinHeap():
    def __init__(self):
        self.heap = []
        self.size = 0

    # parent: (i-1)//2
    # left child: (i*2)+1
    # right Child: (i*2)+2]

    def bubbleUp(self,i):
        # while parent exists for this index
        while i//2 > 0:
            # check with parent, if larger, switch and repeat w new index
            if self.heap[i] > self.heap[(i-1)//2]:
                temp = self.heap[(i-1)//2]
                self.heap[(i-1)//2] = self.heap[i]
                self.heap[i] = temp
                bubbleUp(self,(i-1)//2)
            # else, end and return
            else:
                return(0)

    def push(self,x):
        self.heap.append(x)
        self.size += 1
        self.bubbleUp(self.size)
