class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
    def __str__(self):
        return(str(self.val))

class BST:
    def __init__(self):
        self.root = None
        # consider adding size and height?

    def _traverse(self, cur_node):
        if cur_node != None:
            self._traverse(cur_node.left)
            print(cur_node)
            self._traverse(cur_node.right)

    def traverse(self):
        if self.root != None:
            self._traverse(self.root)
        else:
            print('Empty :(')

    def find(key,node):
        if node is None or node.key == key:
            return(node)
        elif key < node.key:
            return find(key, node.left)
        else:
            return find(key, node.right)

    def _insert(self,val,cur_node):
        if val < cur_node.val:
            if cur_node.left == None:
                cur_node.left = Node(val)
            else:
                self._insert(val, cur_node.left)
        else:
            if cur_node.right == None:
                cur_node.right = Node(val)
            else:
                self._insert(val,cur_node.right)

    def insert(self, val):
        if self.root is None:
            self.root = Node(val)
        else:
            self._insert(val,self.root)

# depth first Search
# pre order




# in order

# post order

# breadth first search

if __name__ == "__main__":
    '''
    print("Testing tree...")
    root = Node('A')
    c1 = Node('B')
    c2 = Node('C')
    root.left = c1
    root.right = c2
    print(root)
    print(root.left, root.right)
    '''
    print("Testing BST...")
    test_BST = BST()
    test_BST.traverse()
    test_BST.insert(9)
    test_BST.insert(3)
    test_BST.insert(2)
    test_BST.insert(7)
    test_BST.traverse()
