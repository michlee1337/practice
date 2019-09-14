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
        l_height = nodeHeight(node.left)
        r_height = nodeHeight(node.right)
        if (abs(l_height - r_height) > 1):
            raise ValueError('Tree Unbalanced')
        else:
            return(max(l_height,r_height)+1)

def checkBalanced(node):
    #base case: if leaf, return true
    try:
        nodeHeight(node)
        return(True)
    except:
        return(False)

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
