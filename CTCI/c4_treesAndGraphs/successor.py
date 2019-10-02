class Node():
    def __init__(self, val, left = None, right = None, parent = None):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent

    def attach(self, node):
        if self.val < node.val:
            self.right = node
        else:
            self.left = node
        node.parent = self
        return(self)

def successor(node):
    # check if right child
    # else, check parent first rightward parent
    if node.right:
        return(node.right.val)

    parent = node.parent

    while parent:
        if parent.left == node:
            return(parent.val)
        node = parent
        parent = node.parent

    return(None)

if __name__=="__main__":
    root = Node(3)
    child1 = Node(1)
    child2 = Node(4)
    root.attach(child1)
    root.attach(child2)
    child3 = Node(0)
    child4 = Node(2)
    child5 = Node(5)
    child1.attach(child3)
    child1.attach(child4)
    child2.attach(child5)

    print(successor(root))
    print(successor(child1))
    print(successor(child2))
    print(successor(child3))
    print(successor(child4))
    print(successor(child5))
