class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

# brute
def nodeHeight(node):
    # base case: if none, return 0
    if node == None:
        return 0
    else:
        return(max(nodeHeight(node.left),nodeHeight(node.right))+1)

def checkBalanced(node):
    #base case: if leaf, return true
    if node.left == None and node.right == None:
        return(True)
    # else, check if self and children are balanced
    if node.left and not checkBalanced(node.left):
        print(node.left.val)
        return(False)
    if node.right and not checkBalanced(node.right):
        print(node.right.val)
        return(False)
    print(node.val, abs(nodeHeight(node.left) - nodeHeight(node.right)))
    return(abs(nodeHeight(node.left) - nodeHeight(node.right)) <= 1)

if __name__=="__main__":
    root1 = Node(0)
    root1.left = Node(1)
    root1.right = Node(2)
    root1.left.left = Node(3)
    root1.left.right = Node(4)
    print(checkBalanced(root1))
    root1 = Node(0)
    root1.left = Node(1)
    root1.right = Node(2)
    root1.left.left = Node(3)
    root1.left.right = Node(4)
    root1.left.right.right = Node(5)
    print(checkBalanced(root1))
