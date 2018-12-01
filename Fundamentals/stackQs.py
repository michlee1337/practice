'''
Implement a queue using stack
'''

class qWithStack():
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self,x):
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

testQ = qWithStack()
print(testQ.enqueue(1))
testQ.enqueue(2)
testQ.enqueue(3)
print(testQ.dequeue())

if __name__ is "__main__":
    testQ = qWithStack
    testQ.enqueue(1)
    testQ.enqueue(2)
    testQ.enqueue(3)
    testQ.dequeue()
    # have an empty stack

    # each insert,

# cut the minimum n times
