# 3     >    2    >   8    >    10    >    4      >     7
#            h                   r
# increment head until .next is > partition
# # increment runner until .next is < partition
# # move runner.next to head.next

def partition(root,partition):
    # init head pointer to dummy and move to just before a val more than/ eq partition
    dummy = Node("#")
    dummy.next = root
    head = dummy

    while head.next != None and head.next.val < partition:
        head = head.next

    # init runner to check through rest of list
    runner = head.next
    while runner.next != None:
        # move nodes less than partition to head pointer
        if runner.next.val < partition:
            nodeToMove = runner.next
            runner.next = nodeToMove.next
            nodeToMove.next = head.next
            head.next = nodeToMove
        # else, just increment
        else:
            runner = runner.next

    return(dummy.next)

class Node():
    def __init__(self,val):
        self.val = val
        self.next = None

def printLL(root):
    print('_____')
    print(root.val)
    while root.next:
        print(root.next.val)
        root = root.next
    return(0)

n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)
n6 = Node(6)
n7 = Node(7)

n2.next = n1
n1.next = n6
n6.next = n3
n3.next = n4
n4.next = n5
n5.next = n7

printLL(n2)

r = partition(n2,5)
printLL(r)
