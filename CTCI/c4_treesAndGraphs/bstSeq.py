# ugh still broken

class Solution():
    def bstSeq(self, root):
        if root == None:
            return([[]])
        if root.left == None and root.right == None:
            return([[root.val]])

        seq_left = self.bstSeq(root.left)
        seq_right = self.bstSeq(root.right)

        if len(seq_left) == 0 and len(seq_right) == 0:
            return([[root.val]])

        for l in seq_left:
            for r in seq_right:
                weaves = self.doWeave(l,r,[root.val],[])
        return(weaves)

    def doWeave(self,l1,l2,prefix,weaves):
        if len(l1) == 0 or len(l2) == 0:
            weaves.append(prefix + l1 + l2)
        if len(l1) != 0:
            weaves = self.doWeave(l1[1:],l2, prefix + [l1[0]], weaves)

        if len(l2) != 0:
            weaves = self.doWeave(l1,l2[1:], prefix + [l2[0]], weaves)

        return(weaves)

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
    n1.left = n2
    n1.right = n3
    n2.left = n4
    n2.right = n5
    n3.left = n6
    test = Solution()
    print(test.bstSeq(n1))
