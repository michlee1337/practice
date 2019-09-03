class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

    def bfs(self):
        '''
        print bfs from node given
        '''
        queue = [self]
        while queue:
            node = queue.pop(0)
            print(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return(0)


class Solution:
    def minTree(list):
        '''
        takes in a list of integeers in increasing order and returns
        the root of a min height binary search tree consisting of the values
        '''
        # base case: length of list is 0, return None
        if len(list) == 0:
            return(None)
        else:
            m_ind = len(list)//2
            root = Node(list[m_ind])
            root.left = Solution.minTree(list[:m_ind])
            root.right = Solution.minTree(list[m_ind+1:])
            return(root)

if __name__=="__main__":
    list = [int(x) for x in input("ordered list of values: ").split()]
    print(list)
    tree = Solution.minTree(list)
    tree.bfs()
