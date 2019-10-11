class myQueue():
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, val):
        while len(self.s1) > 0:
            self.s2.append(self.s1.pop())
        self.s1.append(val)
        while len(self.s2) > 0:
            self.s1.append(self.s2.pop())
        return(0)

    def pop(self):
        return(self.s1.pop())
    # ALT: MAKE POP EXPENSIVE

    # †o push, just append to S1

    # to pop, move all items from S1 to S2
    # return last elem of S1/ first elem of S2
    # move items back from S2 to S1


test = myQueue()

test.push(1)
test.push(2)
test.push(3)
print(test.s1,test.s2)  # [3,2,1] []
print(test.pop())       # 1
print(test.s1,test.s2)  # [3,2] []
print(test.pop())       # 2
print(test.s1,test.s2)  # [3] []
