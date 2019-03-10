##
## Binary Search Tree
## 
class Node:
    def __init__(self, val):
        self.l_child = None
        self.r_child = None
        self.parent = None
        self.data = val

def insert(root, node):
    """inserts a node into a tree rooted at root, returns the root"""
    if root is None:
        root = node
    else:
        if root.data > node.data:
            if root.l_child is None:
                root.l_child = node
                node.parent = root
            else:
                insert(root.l_child, node)
        else:
            if root.r_child is None:
                root.r_child = node
                node.parent = root
            else:
                insert(root.r_child,node)
    return root

def search(root, value):
    """searches a tree rooted at root for a node with data = value, returns the node if found, None otherwise"""
    # Your code goes here
    if root.data == value:
        return root
    elif (root.r_child is not None) and (root.data > value):
        search(root.r_child,value)
    elif (root.l_child is not None) and (root.data < value):
        search(root.l_child,value)
    else:
        return None
    
    
def search_data(root, value): 
    node = search(root, value)
    if node: 
        return node.data
    else: 
        return node


def delete(root, value):
    """if a node with data = value is present in the tree rooted at root, deletes that node and returns the root"""
    node = search(root,value)

    # if leaf node
    if node:
        if (node.l_child is None) and (node.r_child is None):
            # delete parent to child link
            if node.parent:
                if node.parent.r_child == node:
                    node.parent.r_child = None
                else:
                    node.parent.l_child = None
                # delete node links
                node.parent = None

        # if only right child
        if (node.l_child is None):
            if node.parent:
                # link parent to right child
                if node.parent.r_child == node:
                    node.parent.r_child = node.r_child
                else:
                    node.parent.l_child = node.r_child
                # link right child to parent
                node.r_child.parent = node.parent
            # delete node links
            node.parent = None
            node.r_child = None

        # if only left child
        if (node.r_child is None):
            if node.parent:
                # link parent to right child
                if node.parent.r_child == node:
                    node.parent.r_child = node.l_child
                else:
                    node.parent.l_child = node.l_child
                # link left child to parent
                node.l_child.parent = node.parent
            # delete node links
            node.parent = None
            node.l_child = None

            # if two children
            # find min in right subtree
            minInRight = node.r_child
            while minInRight.l_child is not None:
                minInRight = minInRight.l_child
            # link parent to minInRight
            if node.parent:
                if node.parent.r_child == node:
                    node.parent.r_child = node.minInRight
                else:
                    node.parent.l_child = node.minInRight
                # link minInRight to parent and left child
                minInRight.parent = node.parent
            minInRight.l_child = node.l_child
            # delete node links
            node.parent = None
            node.l_child = None 
            node.r_child = None
    return(root) 




    
def inorder(root): 
    """returns a list of all data in the tree rooted at root produced using an in order traversal"""
    # Your code goes here
    return (inorder(root.l_child) + [root.data] + inorder(root.r_child)) if root else []

    
def to_string(root): 
    """returns a string with the relevant binary tree structure associated with the BST with the given root """
    if not root: 
        return 'Nil'
    else: 
        r = to_string(root.r_child) if root.r_child else 'Nil'
        l = to_string(root.l_child) if root.l_child else 'Nil'
        return 'Node(' + str(root.data) + ' L: ' + l + ' R: ' + r + ')'
###
### Simple List Code
###

def list_insert(lst, value): 
    """inserts value into lst in sorted order"""
    ind = 0
    for i in range(len(lst)): 
        if lst[i] > value: 
            lst.insert(i,value)
            return lst
    lst.append(value)
    return lst
            
def list_delete(lst, value): 
    """ deletes first instance of value from lst if it present"""
    i = 0
    while i < (len(lst)):
        if lst[i] == value:
            del lst[i]
        i += 1
    return(lst)
    
def list_search(lst, value): 
    """ searches lst for value and returns value if present, None if it is not present"""
    i = 0
    while i < (len(lst)):
        if lst[i] == value:
            return(lst[i])
        i += 1
    return(None)   
    
###
### Testing Code
###

import random
bst = None
lst = []

for x in [Node(random.randint(0,100)) for _ in range(50)]:
    if not bst: 
        bst = x
    else: 
        insert(bst, x)
        list_insert(lst, x.data)    

for x in [random.randint(0,100) for _ in range(50)]: 
    bst = delete(bst, x)
    list_delete(lst,x)

print(inorder(bst))
print(lst)

'''

for x in [random.randint(0,100) for _ in range(50)]: 
    print(x, search_data(bst, x), list_search(lst, x))
    
print(inorder(bst))
print(lst)
'''