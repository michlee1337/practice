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

    def _find(self,val,cur_node):
        if cur_node is None:
            print('val not here')
        elif cur_node.val == val:
            # note: i should build in a more valuable measure of location. depth perhaps?)
            print('found as parent of:', cur_node.left,'and', cur_node.right)
        elif val < cur_node.val:
            return self._find(val, cur_node.left)
        else:
            return self._find(val, cur_node.right)

    def find(self,val):
        if self.root is None:
            print('tree empty')
        else:
            return(self._find(val,self.root))

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

    def maxDepth(self,cur):
        max = 0
        if cur.left is None and cur.right is None:
            return(max)
        pass


    def draw(self):
        # check max spacing and add padding
        next_level = [self.root]
        not_empty = True
        while not_empty:
            not_empty = False
            cur_level = next_level
            next_level = []
            lineT = ''
            lineB = ''
            for node in cur_level: # for each node in past level
                if node is None:
                    lineT += ('  |  ')
                    lineB += ('     ')
                else:
                    lineT += ('  |  ')
                    lineB += ('  ' + str(node.val) + '  ')
                    not_empty = True

                if node is None or node.left is None:
                    next_level.append(None)
                else:
                    next_level.append(node.left)

                if node is None or node.right is None:
                    next_level.append(None)
                else:
                    next_level.append(node.right)

            print(lineT)
            print(lineB)
        return(0)

    def commParent(self,val1,val2):
        loc = self._find(val1)
        if loc is None:
            return('not in tree')
        while loc is not None:
            try1 = self.bfs(loc,val2)
            # should remove checked nodes
            if try1 is not None:
                return(loc.parent())
            parent = loc.parent()
            if parent.left() == loc:
                loc = parent.right()
            else:
                loc = parent.left()
                # oops infinite
                # should probably do this recursively w a modified dfs
        pass

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
    print("Testing BST...")
    test_BST = BST()
    print("An empty tree")
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
    my_tree.find('d')
    my_tree.find('coconut')
    '''
    print("Testing BST...")
    test_BST = BST()
    fill_tree(test_BST)
    print("in order")
    test_BST.traverse()
    print('testing draw')
    test_BST.draw()
