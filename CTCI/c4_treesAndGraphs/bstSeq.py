def bstSeq(root):
    if root == None:
        return([[]])
    if root.left == None and root.right == None:
        return([[root.val]])

    # each seq is
    # root + left + right + rest
    # root + right + left + rest

    # left and right can have many sequences
    seq = []

    seq_left = bstSeq(root.left)
    seq_right = bstSeq(root.right)
    print(seq_left,seq_right)

    for l in seq_left:
        for r in seq_right:
            seq.append([root.val] + l + r)
            if l != [] and r != []:
                seq.append([root.val] + r + l)

    return(seq)

class Node():
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

if __name__=="__main__":
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n5 = Node(5)
    n6 = Node(6)
    n7 = Node(7)
    n2.left = n1
    n2.right = n3
    n3.right = n4
    n4.right = n5
    n1.left = n6
    n1.right = n7
    print(bstSeq(n2))
