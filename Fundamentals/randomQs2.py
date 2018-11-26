# find the first common parent of two nodes in the tree
class Node():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
    def __str__(self):
        return(str(self.val))

class binTree():
    def __init__(self):
        self.root = None

    def _insert(self,cur_node, val):
        if val < cur_node.val:
            if cur_node.left is None:
                cur_node.left = Node(val)
                return(0)
            else:
                self._insert(cur_node.left, val)
        if val > cur_node.val:
            if cur_node.right is None:
                cur_node.right = Node(val)
            else:
                self._insert(cur_node.right, val)

    def insert(self,val):
        if self.root is None:
            self.root = Node(val)
        else:
            self._insert(self.root, val)

    def bfs(self,cur_node,val):
        search_q = [cur_node]
        if cur_node is not None:
            while len(search_q > 0):
                cur_node = search_q.pop(0)
                if cur_node.val == val:
                    return(cur_node)
                if cur_node.left is not None:
                    search_q.append(cur_node.left)
                if cur_node.right is not None:
                    search_q.append(cur_node.right)
        else:
            return('not here')

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
                    lineT += ('     ')
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
                    next_level.append(node.left)

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

def fill_tree(tree, num_elems=10,max_int=10):
    from random import randint
    for i in range(num_elems):
        cur_elem = randint(0,max_int)
        tree.insert(cur_elem)
    return(tree)

test = binTree()
fill_tree(test)
print(test.root.right)
test.draw()
