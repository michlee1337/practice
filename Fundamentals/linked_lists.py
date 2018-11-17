'''
Linked lists
(oft compared to arrays)

Advantages
- saves memory: only allocates memory required for vals to be stored
- nodes can be anywhere in memory: as long as refs are updated, each node can be flexibly moved to diff address

Disadvantages
- linear look up time: arrays are constant

'''

# initialize

class Node:
# first node (header) can be treated as the address of the linked list

    # initialize
    def __init__(self,val):
        self.val = val
        self.next = None # initialize to none

    # traverse: print all values from start to end of linked list
    def traverse(self):
        node = self
        while node != None:
            print(node.val)
            node = node.next

node1 = Node(12)
node2 = Node(7)

node1.next = node2

# print(node1)
# node1.traverse()

'''
Doubly Linked list

Advatages
- traverse in both dir
- constant time in accessing (insert/delete) end node

Disadvantages
- each node requires 1 extra unit of space
- all operations require extra pointer to be maintained
'''

class DoublyNode:
    def __init__(self,var):
        self.val = var
        self.next = None
        self.last = None
    def traverse(self,forward = True):
        node = self
        while node != None:
            print(node.val)
            if forward == True:
                node = node.next
            else:
                node = node.last

def connectNodes(node1,node2):
    node1.next = node2
    node2.last = node1

nodly1 = DoublyNode(31)
nodly2 = DoublyNode(7)

connectNodes(nodly1,nodly2)

print(nodly1)
nodly1.traverse()
nodly2.traverse(forward=False)
#nodly1.traverse()
# Challenges
#
