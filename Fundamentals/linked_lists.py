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
        return(0)

def connectNodes(arr):
    for i in range(len(arr[0:-1])):
        arr[i].next = arr[i+1]
    return(0)

# by index
def delNode(node,int):
    # only works for singly linked lists
    if int == 0:
        node.next = None
    else:
        for i in range(int-1):
            node = node.next
        if node.next.next != None:
            node.next = node.next.next
        else:
            node.next = None
    return(0)

# testing
'''
n1 = Node('a')
n2 = Node('b')
n3 = Node('c')
n4 = Node('d')

connectNodes([n1,n2,n3,n4])

print('b4')
n1.traverse()

print('after')
delNode(n1,1)
n1.traverse()
'''

#_________________DOUBLY LINKED LISTS___________
'''
Doubly Linked list

Advantages
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
        return(0)

def connectDNodes(arr):
    arr[0].next = arr[1]
    for i in range(1,len(arr)-1):
        arr[i].next = arr[i+1]
        arr[i].last = arr[i-1]
    arr[len(arr)-1].last = arr[len(arr)-2]
    return(0)


'''
nodly1 = DoublyNode('a')
nodly2 = DoublyNode('b')
nodly3 = DoublyNode('c')
nodly4 = DoublyNode('d')
connectDNodes([nodly1,nodly2,nodly3,nodly4])


#testing
nodly1.traverse()
nodly4.traverse(False)
'''

#___________________CHALLENGES________________
''' remove duplicates from linked list '''

def delDuples(node1):
    # counting vars
    vals = []
    node = node1
    count = 0

    while node != None: # until the end of the linked list
        # check if val has been seen before
        # if it has, delete it
        if node.val in vals:
            delNode(node1,count)
            count -= 1
        # else add value to the log and move on
        else:
            vals.append(node.val)
        count+=1
        node = node.next
    return(0)
'''
# Testing

d1 = Node('a')
d2 = Node('a')
d3 = Node('c')
d4 = Node('a')
d5 = Node('e')

connectNodes([d1,d2,d3,d4,d5])

print('b4')
d1.traverse()

print('after')
delDuples(d1)
d1.traverse()
'''

'''
get kth to last element from a linked list

this would probs be easier with a doubly linked list.
or if we knew the length of a linked list through a linked list class
lets do doubly
'''

def remKNode(nodeEnd,k):
    node = nodeEnd
    for i in range(k):
        node = node.last
        print(node.val,node.last.val)
        print(node.next)
    # could make a helper func here but maybe later
    # check if we got to right place
    print(node.val,node.next.val, node.last.val)
    node.next.last = node.last
    node.last.next = node.next

nodly1 = DoublyNode('a')
nodly2 = DoublyNode('b')
nodly3 = DoublyNode('c')
nodly4 = DoublyNode('d')
connectDNodes([nodly1,nodly2,nodly3,nodly4])

#testing that the doubly linked list is working

#remKNode(nodly4,1)

# delete a node from linked list

# add two linked lists from left to right

# add two linked lists from right to left
