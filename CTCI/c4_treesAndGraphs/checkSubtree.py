def checkSubtree(node1,node2):
    # if reached end of tree2, success
    if node2 == None:
        return(True)

    # if reached end of tree1, fail
    elif node1 == None:
        return(False)

    # if same node, check subtrees
    elif node2.val == node1.val:
        if checkSubtree(node1.left, node2.left) or checkSubtree(node1.right, node2.right):
            return(True)

    # else if no subtree found and not ended,
    # check another main tree node
    return(checkSubtree(node1.left, node2) or checkSubtree(node1.right, node2))

class Node():
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None


n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)
n6 = Node(6)

n2.left = n1
n2.right = n4
n4.left = n3
n4.right = n5
n6.right = n6


r4 = Node(4)
r3 = Node(3)
r5 = Node(5)

r4.left = r3
r4.right = r5

print(checkSubtree(n2,r4))
