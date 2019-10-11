def delMid(node):
    # assuming it is a middle node

    # move next val to current val
    #         n
    # a > b > c > d, del b
    # a > c > d >

    if node == None or node.next = None:
        return(-1)

    while node.next:
        node.val = node.next.val
        if node.next.next == None:
            node.next = None
        else:
            node = node.next
    return(0)

class Node():
    def __init__(self,val):
        self.val = val
        self.next = None

def printLL(root):
    print("_______")
    print(root.val)
    while root.next:
        root = root.next
        print(root.val)
    return(0)

n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)
n6 = Node(6)

n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n6

printLL(n1)
delMid(n2)
printLL(n1)
