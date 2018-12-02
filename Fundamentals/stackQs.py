'''
Implement a queue using stack
'''

# best for time in general + enqueue
# enqueue = O(1)
# dequeue = O(n)
# space = 2n
class qWithStack1():
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self,x):
        self.stack1.append(x)
        return(0)

    def dequeue(self):
        # if nothing stored
        if len(self.stack1) == 0 and len(self.stack2) == 0:
            return('empty :()')
        # moving items from one stack to another inverses the order
        # move items into s2 only if s2 is empty
        # else you'll be putting newer items above older
        if len(self.stack2) == 0:
            while len(self.stack1) > 0:
                self.stack2.append(self.stack1.pop())
        return(self.stack2.pop())

if __name__ == "__main__":
    testQ = qWithStack1()
    print(testQ.dequeue())
    testQ.enqueue(1)
    testQ.enqueue('bat')
    testQ.enqueue(2)
    testQ.enqueue(3)
    print(testQ.dequeue())
    print(testQ.dequeue())
    print(testQ.dequeue())
    print(testQ.dequeue())
    print(testQ.dequeue())

# NOTE: test edge cases
# NOTE: describe complexity
# NOTE: consider optimizing: enqueue, dequeue, space

# ALT solutions

# optimized dequeue
class qWithStack2():
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self,x):
        # if stack 1 is empty
        # add to stack 1

        if len(self.stack2) == 0:
            self.stack1.append(x)
            return(0)
        else:
            self.stack2.append(x)
            return(0)

    def dequeue(self):
        if len(self.stack2) == 0:
            while len(self.stack1) > 0:
                self.stack2.append(self.stack1.pop())
            return(self.stack2.pop())
        else:
            while len(self.stack2) > 0:
                self.stack1.append(self.stack2.pop())
            return(self.stack1.pop())
