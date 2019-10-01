from anytree import Node, RenderTree
from collections import deque
from queue import *

def listOfDepths(root):
    # dictionary of linked lists by depth
    ## defaultdict(list) << could be used, but for accuracy will approximate linked list w deque instead
    # init with root
    listsByDepth = {}

    # breadth first search, but remembering levels
    searchQueue = Queue()
    # init with (root,0)
    searchQueue.put((root,0))

    while not searchQueue.empty():
        print(searchQueue.qsize())
        curNode, curDepth = searchQueue.get()
        print(curNode.name)
        # add children (node,depth+1)
        for child in curNode.children:
            searchQueue.put((child,curDepth+1))

        # evaluate self: append node to lists[depth]
        listsByDepth.setdefault(curDepth, deque()).append(curNode.name)
    return(listsByDepth)

if __name__=="__main__":
    udo = Node("Udo")
    marc = Node("Marc", parent=udo)
    lian = Node("Lian", parent=marc)
    dan = Node("Dan", parent=udo)
    jet = Node("Jet", parent=dan)
    jan = Node("Jan", parent=dan)
    joe = Node("Joe", parent=dan)
    for pre, fill, node in RenderTree(udo):
        print("%s%s" % (pre, node.name))
    depthLists = listOfDepths(udo)
    print(depthLists)
