# 1: limited length, set starting index of each stack
# 2: first second third index starts each stack, each entry stores a value and a pointer to the next val
# 3: flexible storage: keep first index pointer, when max cap exceeded, reshuffle storage

class threeStack():
    def __init__(self,size):
        self.storage = [None]*size
        self.tops = [0,size//3,2*(size//3)]
        for i in self.tops:
            self.storage[i] = ["END"]

    def addTo(self,val,stack):
        # check next space
        if self.storage[self.tops[stack]+1] == None:
            self.storage[self.tops[stack]+1] == val
            self.tops[stack] += 1

        ## # else try reassigning
        ## try reassignStack(stack)

        # else raise error
        else:
            raise ValueError('Stack is full!')
        return(0)
