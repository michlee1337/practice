# implement stack through min heap priority q

class MinHeap():
    def __init__(self):
        self.heap = []

    def parent(self,i):
        return(self[(i-1)//2])

    def leftChild(self,i):
        return(self[(i*2)+1])

    def rightChild(self,i):
        return(self[(i*2)+2])

    def _push(cur_node, x):
        if cur_node.left is None:
            cur_node.left = Node(self.count, x)
            self.count += 1
            return(0)
        elif cur_node.right is None:
            cur_node.right = Node(self.count, x)
            return(0)
        else:
            cur_node = cur_node.left

    def push(self,x):
        # if empty tree, insert at root
        if self.root is None:
            self.root = Node(self.count, x)
            self.count += 1
            return(0)
        # find next empty slot
        _push(self.root,x)
        # check children




        if self.root == None:
            self
