'''
Implement a queue using stack
'''

# best for enqueue
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

# NOTE: test edge cases
# NOTE: describe complexity
# NOTE: consider optimizing: enqueue, dequeue, space

# ALT solutions

# optimized dequeue
# enqueue O(n)
# dequeue O(1)
# space O(2n)
class qWithStack2():
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self,x):
        # if stack2 has items, reset it to stack 1
        while len(self.stack2) > 0:
            self.stack1.append(self.stack2.pop())

        # add new item to stack 1
        self.stack1.append(x)

        # invert stack1 into stack2
        while len(self.stack1) > 0:
                self.stack2.append(self.stack1.pop())
        return(0)

    def dequeue(self):
        if len(self.stack2) == 0:
            return('empty :(')
        return(self.stack2.pop())

class specialStack():
    # implement push pop isEmpty isFull getMin in O(1):
    def __init__(self, max = 100):
        self.stack = []
        self.minStack = []
        self.len = 0
        self.max = max

    def push(self,x):
        # append
        self.stack.append(x)
        # update min
        if len(self.minStack) == 0 or x < self.minStack[-1]:
            self.minStack.append(x)
        else:
            self.minStack.append(self.minStack[-1])
        # update length
        self.len += 1
        return(0)

    def pop(self):
        # update length
        self.len -= 1
        # update minStack
        self.minStack.pop()
        # return last item in stack
        return(self.stack.pop())


    def isEmpty(self):
        return(self.len == 0)

    def isFull(self):
        return(self.len >= (self.max-1))

    def getMin(self):
        return(self.minStack[-1])

# implement two stacks in one array
class twoStacks():
    # one stack from start to end, other stack from end to start
    # marker to denote difference
    def __init__(self):
        self.list = ['marker']

    def push1(self,x):
        # add to start of stack
        self.list.insert(0,x)

    def push2(self,x):
        # add to end of stack
        self.list.append(x)

    def pop1(self):
        # pop from start of list as long as it is not the marker
        if self.list[0] != 'marker':
            return(self.list.pop(0))
        # else inform empty
        return('empty :(')

    def pop2(self):
        #pop from end of list as long as it is not the marker
        if self.list[-1] != 'marker':
            return(self.list.pop())
        # else inform empty
        return('empty :(')

if __name__ == "__main__":
    print('testing method 1')
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
    print('testing method 2')
    testQ = qWithStack2()
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
    print('testing special stack')
    testS = specialStack(5)
    print(testS.isEmpty())
    print(testS.isFull())
    testS.push(10)
    testS.push(9)
    testS.push(5)
    testS.push(2)
    testS.push(19)
    print(testS.isEmpty())
    print(testS.isFull())
    print(testS.getMin())
    print(testS.pop())
    print('test double stack')
    testDS = twoStacks()
    testDS.push1('a')
    testDS.push2(1)
    testDS.push1('b')
    testDS.push2(2)
    testDS.push2(3)
    print(testDS.pop1())
    print(testDS.pop1())
    print(testDS.pop1())
    print(testDS.pop2())
    print(testDS.pop2())
    print(testDS.pop2())
