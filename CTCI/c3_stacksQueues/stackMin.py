class stackMin():
    def __init__(self):
        self.store = []
        self.minimums = [None]

    def push(self,val):
        # add value to stack
        self.store.append(val)

        # update min
        if self.min() == None or val <= self.min():
            self.minimums.append(val)
        return(0)

    def pop(self):
        if len(self.store) == 0:
            raise ValueError("No elements in stack!")
        else:
            # pop element
            val = self.store.pop()

            # update min
            if self.min() == val:
                self.minimums.pop()
        return(val)

    def min(self):
        return(self.minimums[-1])

stack = stackMin()

stack.push(2)
stack.push(8)
stack.push(7)
stack.push(6)
stack.push(1)
stack.push(5)
print(stack.min(), stack.store[-1]) # 1 5
print(stack.pop()) # 5
print(stack.min(), stack.store[-1]) # 1 1
print(stack.pop()) # 1
print(stack.min(), stack.store[-1]) # 2 6
