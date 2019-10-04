from queue import *

# O(n) time: finding the nodes takes O(n) time,
# and the rest takes O(h) time where h is height of the tree

# O(lgn) space: search queue will be O(lgn) (at least the root will be on a diff level)
# and the rest are constant space pointers

def firstCommonAncestor(root, node1, node2):
    # find the nodes and their depths in the tree
    pointer_1, pointer_2 = findNodeLevels(root, [node1,node2])

    # make their depths equal
    while (pointer_2[1] - pointer_1[1]) > 0:
        pointer_2 = (pointer_2[0].parent, pointer_2[1]-1)

    while (pointer_1[1] - pointer_2[1]) > 0:
        pointer_1 = (pointer_1[0].parent, pointer_1[1]-1)

    pointer_1 = pointer_1[0] # getting rid of level counts for cleaner code
    pointer_2 = pointer_2[0]

    # traverse up ancestor paths until common
    while pointer_1 != pointer_2: # no need for a out of bounds check because root must be a common ancestor
        pointer_1 = pointer_1.parent
        pointer_2 = pointer_2.parent

    return(pointer_1)

def findNodeLevels(root, nodes):
    pointers = [None for _ in nodes]

    searchQueue = Queue()
    searchQueue.put((root,0))

    while None in pointers:
        if searchQueue.empty():
            raise ValueError("Nodes given are not in tree!")
        else:
            node, level = searchQueue.get()
            for child in node.children:
                for node_ind, node in enumerate(nodes):
                    if child == node:
                        pointers[node_ind] = (child, level)
                searchQueue.put((child,level+1))
    return(pointers)

class Node():
    def __init__(self,val):
        self.val = val
        self.children = []
        self.parent = None

    def addChildren(self,children):
        self.children = children
        for node in self.children:
            node.parent = self

if __name__ == "__main__":
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n5 = Node(5)
    n6 = Node(6)
    n7 = Node(7)

    n1.addChildren([n2,n3,n4])
    n2.addChildren([n5])
    n4.addChildren([n6,n7])

    print(firstCommonAncestor(n1,n6,n7).val)
