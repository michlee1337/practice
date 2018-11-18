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

    def _traverseIn(self, cur_node):
        if cur_node is not None:
            self._traverseIn(cur_node.left)
            print(cur_node)
            self._traverseIn(cur_node.right)

    def _traversePre(self, cur_node):
        if cur_node is not None:
            print(cur_node)
            self._traversePre(cur_node.left)
            self._traversePre(cur_node.right)

    def _traversePost(self, cur_node):
        if cur_node is not None:
            self._traversePost(cur_node.left)
            self._traversePost(cur_node.right)
            print(cur_node)

    def _traverseBreadth(self, cur_node):
        if cur_node is not None:
            from collections import deque
            queue = deque()
            queue.append(cur_node)
            while len(queue) > 0:
                cur_node = queue.popleft()
                print(cur_node)
                if cur_node.left is not None:
                    queue.append(cur_node.left)
                if cur_node.right is not None:
                    queue.append(cur_node.right)

    def traverse(self, order="in"):
        if self.root is not None:
            if order == "in":
                self._traverseIn(self.root)
            elif order == "pre":
                self._traversePre(self.root)
            elif order == "post":
                self._traversePost(self.root)
            elif order == "breadth":
                self._traverseBreadth(self.root)
            else:
                print("I don't understand")
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

def fill_tree(tree, num_elems=10,max_int=10):
    from random import randint
    for i in range(num_elems):
        cur_elem = randint(0,max_int)
        tree.insert(cur_elem)
    return(tree)

def perf_tree(tree):
    elems = ['a','b','c','d','e','f','g','h','i']
    for i in elems:
        tree.insert(i)

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
    print("TAn empty tree")
    test_BST.traverse()
    fill_tree(test_BST)
    print("in order")
    test_BST.traverse()
    print("pre order")
    test_BST.traverse("pre")
    print("post order")
    test_BST.traverse("post")
    print("breadth")
    my_tree = BST()
    perf_tree(my_tree)
    my_tree.traverse("breadth")
    my_tree.traverse("banana")
