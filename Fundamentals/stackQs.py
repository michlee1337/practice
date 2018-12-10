#_______Implement a queue using stack______#

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

#_______ implement two stacks in one array ________#
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

#______Stack using queues______#

# first thought, do it on dequeue
class stackWQ():
    def __init__(self):
        self.queue1 = []
        self.queue2 = []

    def enqueue(self,x):
        # if there's anything in q2, add there
        if len(self.queue2) > 0:
            self.queue2.append(x)
            return(0)
        # else add in q1
        self.queue1.append(x)
        return(0)

    def dequeue(self):
        # if queue1 not empty, shift items to queue2 except last
        if self.queue1 != []:
            while len(self.queue1) > 1:
                self.queue2.append(self.queue1.pop(0))
            return(self.queue1.pop(0))
        elif self.queue2 != []:
            while len(self.queue2) > 1:
                self.queue1.append(self.queue2.pop(0))
            return(self.queue2.pop(0))
        return('empty :(')
# enqueue O(1)
# dequeue O(n)
# space O(n)

# optimized dequeue, wasted some space for coding readability

class stackWQ2():
    def __init__(self):
        self.queue1 = []
        self.queue2 = []

    def enqueue(self,x):
        # ensure q1 always in reverse
        # add to q2
        self.queue2.append(x)
        # add anything from q1 into q2
        while len(self.queue1) > 0:
            self.queue2.appned(self.queue1.pop(0))
        # switch q1 and q2
        temp = self.queue1
        self.queue1 = self.queue2
        self.queue2 = temp
        return(0)

    def dequeue(self):
        # if queue1 not empty, shift items to queue2 except last
        if self.queue1 == []:
            return('empty :(')
        else:
            return(self.queue1.pop(0))

#_____stack with operations on the middle_______#

# in O(1) time complexity

# needs pointer to the center
# can't be array, not O(1),
# to move back and forth must be doubly linked list

class Node():
    def __init__(self, val):
        self.val = val
        self.next = None
        self.last = None
    def __str__(self):
        return(str(self.val))

class stackMid():
    def __init__(self):
         self.head = None
         self.mid = None
         self.len = 0

    def traverse(self):
        cur_node = self.head
        while cur_node is not None:
            print(cur_node)
            cur_node = cur_node.next
        return(0)

    def push(self,val):
        # if empty stack
        if self.head is None:
            self.head = Node(val)
            self.mid = self.head
        else:
            # add as new node at the head of DLL
            new_node = Node(val)
            new_node.next = self.head
            self.head.last = new_node
            # update stack head
            self.head = new_node
        self.len += 1
        # update mid if new length is odd
        # thus when DLL is even, will always return the mid further from head
        if self.len != 1 and self.len%2 == 1:
            self.mid = self.mid.last
        return(0)

    def pop(self):
        # move mid if cur length is odd
        # else since mid maintained as further from head, will still be mid after pop
        if self.len % 2 == 1:
            self.mid = self.mid.next
        # store return node
        ret = self.head
        # update head
        self.head = self.head.next
        # clean connections
        self.head.last = None
        ret.next = None
        self.len -= 1
        return(ret)

    def findMid(self):
        return(self.mid)

    def delMid(self):
        # store mid
        ret = self.mid

        # determine which direction new mid will be in based on odd/even
        if self.len % 2 == 0:
            # move mid
            self.mid = self.mid.last
            # update connections
            self.mid.next = self.mid.next.next
            self.mid.next.last = self.mid
        else:
            # move mid
            self.mid = self.mid.next
            # update connections
            self.mid.last = self.mid.last.last
            self.mid.last.next = self.mid
        # clear up old mid's connections
        ret.next = None
        ret.last = None
        self.len -= 1
        return(0)

# implement k stacks in a single array

# initial thought, divide array into k and assign from there

# space efficient (maybe) is to have an extra array which is the top of each stack
# and a var that tracks the index of the next free spot
# stack implemented as linked list
# each item is node that links to next list.


class kStacks():
    def __init__(self, numStacks = 3, arraySize = 10):
        self.stack = [None] * arraySize
        # head locations initialized to -1 to show that it DNE
        self.heads = [-1] * numStacks
        # stores index of next free slot in stack, initialized as 0
        self.free = 0

    def push(self, int1, val):
        # store in free index
        cur_loc = self.stack[self.free]
        cur_loc = Node(val)
        # connect to the head
        # if head is currently none, skip this
        if self.heads[int1] != -1:
            cur_loc.next = self.heads[int1]
        # update the heads
        self.heads[int1] = cur_loc

    def pop(self, int1):
        # check the head of that stack

        # if none, inform
        if self.heads[int1] == -1:
            return('Empty :(')
        # else
        else:
            # store that val
            ret = self.heads[int1]
            # update head to next item
            self.heads[int1] = self.heads[int1].next
            # trim connections
            ret.next = None
            # return val
            return(ret)

if __name__ == "__main__":
    '''
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
    print('stack w q')
    testSQ = stackWQ()
    print(testSQ.dequeue())
    testSQ.enqueue(1)
    testSQ.enqueue(2)
    testSQ.enqueue(3)
    print(testSQ.dequeue())
    print(testSQ.dequeue())
    print(testSQ.dequeue())
    print(testSQ.dequeue())
    print('test mid stack')
    midS = stackMid()
    print('testing everything expcept delMid')
    midS.traverse()
    midS.push(1)
    midS.push(2)
    print('mid',midS.findMid())
    midS.push(3)
    print('mid',midS.findMid())
    midS.push(4)
    midS.push(5)
    print('mid',midS.findMid())
    midS.traverse()
    print(midS.pop())
    print('mid',midS.findMid())
    print(midS.pop())
    print('mid',midS.findMid())
    midS.push(4)
    midS.push(5)
    print('testing delMid')
    midS.traverse()
    print('mid',midS.findMid())
    midS.delMid()
    midS.traverse()
    print('mid',midS.findMid())
    midS.delMid()
    midS.traverse()
    print('mid',midS.findMid())
    print('testing k stacks')
    kStack = kStacks()
    print(kStack)
    print(kStack.heads)
    kStack.push(0,1)
    kStack.push(0,2)
    kStack.push(0,3)
    print(kStack.pop(0))
    kStack.push(1,'a')
    kStack.push(1,'b')
    kStack.push(1,'c')
    print(kStack.pop(1))
    print(kStack.pop(1))
    print(kStack.pop(0))
    '''
