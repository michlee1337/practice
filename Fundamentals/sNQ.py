# Python is a garbage collecter lang (Java too). Most games never use garb coll langs

class Node:
    def __init__(self):
        self.val = None
        self.next = None

class Stack:
    def __init__(self):
        self.head = None
        self.size = 0
        # don't need a max size since doing linked list imp

    def push(self, val):
        newN = Node()
        newN.val = val
        next_node = self.head
        self.head = newN
        self.head.next = next_node
        self.size += 1

    def pop(self):
        if self.head == None:
            return(None)
        else:
            top_node = self.head
            self.head = self.head.next
            self.size -= 1
            return(top_node.val)

    def peek(self):
        if self.head:
            return(self.head.val)
        else:
            return(None)

    def size(self):
        return(self.size)

    def __str__(self):
        curr_node = self.head
        return_str = ''
        while curr_node != None:
            return_str += str(curr_node.val) + ' '
            curr_node = curr_node.next
        return(return_str)

# test case!
# call every method
# call every method in every state - edge cases - you can think of
if __name__ == "__main__":
    print('hi')
    test_stack = Stack()
    test_stack.push('a')
    test_stack.push('b')
    test_stack.push('c')
    print(test_stack)
    topN = test_stack.pop()
    print('top: ', str(topN))
    print(test_stack)
