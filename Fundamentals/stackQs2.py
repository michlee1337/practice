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
            print('check')
            # check with parent, if larger, switch and repeat w new index
            if self.heap[i] < self.heap[(i-1)//2]:
                print('switched')
                print(self.heap[i], self.heap[(i-1)//2])
                temp = self.heap[(i-1)//2]
                self.heap[(i-1)//2] = self.heap[i]
                self.heap[i] = temp
                self.bubbleUp((i-1)//2)
            # else, end and return
            else:
                return(0)

    def push(self,x):
        self.heap.append(x)
        self.size += 1
        self.bubbleUp(self.size-1)
print(0//2)
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
