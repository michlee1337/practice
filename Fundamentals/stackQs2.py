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
        print(self.heap)
        print('cur ind',i)
        if i <= 0:
            return(0)
        while i//2 >= 0:
            # check with parent, if larger, switch and repeat w new index
            if self.heap[i] < self.heap[(i-1)//2]:
                temp = self.heap[(i-1)//2]
                self.heap[(i-1)//2] = self.heap[i]
                self.heap[i] = temp
                self.bubbleUp((i-1)//2)
            # else, end and return
            else:
                return(0)

    def bubbledown(self,i):
        if i >= self.size:
            return(0)
        while i < self.size:
            if self.heap[i] > self.heap[(i*2)+1]:
                temp = self.heap[i]
                self.heap[i] = self.heap[(i*2)+1]
                self.heap[(i*2)+1] = temp
                self.bubbleUp((i*2)+1)
            elif self.heap[i] > self.heap[(i*2)+2]:
                temp = self.heap[i]
                self.heap[i] = self.heap[(i*2)+2]
                self.heap[(i*2)+2] = temp
                self.bubbleUp((i*2)+2)
            else:
                return(0) 

    def insert(self,x):
        self.heap.append(x)
        self.size += 1
        self.bubbleUp(self.size-1)

    def extract(self):
        ret = self.heap[0]
        self.heap[0] = self.heap.pop()
        seld.size -= 1



class stack_priQ():
    def __init__(self):
        self.heap = MinHeap()

    def push(x):
        self.heap.insert(x)

    def pop():
        self.heap.pop()


if __name__ == "__main__":
    my_heap = MinHeap()
    my_heap.push('7')
    print(my_heap.heap)
    print('______')
    my_heap.push('6')
    print(my_heap.heap)
    print('______')
    my_heap.push('5')
    print(my_heap.heap)
    print('______')
    my_heap.push('4')
    print(my_heap.heap)
    print('______')
    my_heap.push('3')
    print(my_heap.heap)
