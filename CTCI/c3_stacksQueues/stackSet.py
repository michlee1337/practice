class stackSet():
    # set of stacks
    # create new stack if last one > capacity
    # push and pop behave like a single stacks

    #! pop at stack
    def __init__(self, capacity):
        self.capacity = capacity
        self.store = []
        # each item in store is a stack

    def push(self,val):
        if len(self.store) == 0 or len(self.store[-1]) == self.capacity:
            newStack = []
            newStack.append(val)
            self.store.append(newStack)
        else:
            self.store[-1].append(val)
        return(0)

    def pop(self):
        if len(self.store) == 0:
            raise ValueError("Empty store")
        else:
            popped = self.store[-1].pop()
            if len(self.store[-1]) == 0:
                self.store.pop()
            return(popped)

    def popAt(self, s_ind):
        # this would be much easier if i could store
        # not as stacks, but as DLL, and have a
        # hash table/dict lookup table for pointers to head
        # of diff stacks
        if s_ind < len(self.store):
            popped = self.store[s_ind].pop()
            self.store[s_ind].append(None)
            self._shiftBack(s_ind, len(self.store[s_ind])-1)
        return(popped)

    def _shiftBack(self, s_ind, v_ind):
        s0,v0 = s_ind, v_ind
        s1,v1 = self._increment(s_ind,v_ind) # get indexes for next value
        while s1 < len(self.store) and v1 < len(self.store[s1]): # while next value exists
            self.store[s0][v0] =  self.store[s1][v1] # update current value
            # repeat for next value
            s0,v0 = s1,v1
            s1,v1 = self._increment(s0,v0)

        # delete any empty spaces
        if v0 == 0:
            self.store.pop()
        else:
            self.store[s0].pop()
        return(0)

    def _increment(self, s_ind, v_ind):
        # get indexes for next value
        if v_ind == self.capacity-1:
            s_ind += 1
            v_ind = 0
        else:
            v_ind += 1
        return(s_ind, v_ind)

testSS = stackSet(3)

testSS.push(1)
testSS.push(2)
testSS.push(3)
testSS.push(4)
testSS.push(5)
print(testSS.store) # [1,2,3][4,5]
print(testSS.popAt(0)) # 3
print(testSS.store) # [1,2,4][5]
print(testSS.popAt(1)) # 5
print(testSS.store) # [1,2,4]
