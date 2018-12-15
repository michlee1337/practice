# implement stack through min heap priority q

# define node first
class node():
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.left = None
        self.right = None

class minHeap():
    # heap defined by root
    def __init__(self):
        self.root = None
        self.count = 0

    def push(self,x):
        if
