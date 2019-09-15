class Node():
    def __init__(self,val):
        self.val = val
        self.next = None

def removeDups(root):
    # assuming singly linked list
    seen = {}
    seen[root.val] = True
    node = root
    while node.next != None:
        # if dup, remove
        if node.next.val in seen:
            node.next = node.next.next
        else:
            seen[node.next.val] = True
            node = node.next
    return(root)

def removeDupsConstantSpace(root):
    # for each node
    while root.next != None:
        # for each subsequent node
        node = root.next
        while node.next != None:
            # if dup, remove
            if node.next.val == root.val:
                node.next = node.next.next
            node = node.next
        root = root.next
    return(root)

# for testing
def printLL(root):
    list = []
    while root != None:
        list.append(root.val)
        root = root.next
    print(list)
    return(0)

if __name__=="__main__":
    root = Node(0)
    node = root
    for i in range(1,5):
        node.next = Node(i)
        node = node.next
    printLL(root)
    removeDupsConstantSpace(root)
    printLL(root)

    root1 = Node(0)
    node1 = root1
    for i in [1,2,3,4,5,3,6,4,4,7,8]:
        node1.next = Node(i)
        node1 = node1.next
    printLL(root1)
    removeDupsConstantSpace(root1)
    printLL(root1)
