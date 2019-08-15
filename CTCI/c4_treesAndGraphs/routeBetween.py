class Node():
    def __init__(self, val, neighbours = []):
        self.val = val
        self.neighbours = neighbours
        self.visited = None

class Graph():
    def __init__(self):
        self.nodes = []
        self.count = 0
    def addNode(self):
        self.nodes.append(Node(self.count))
        self.count += 1

def routeBetween(node1, node2):
    nodeQ = [(node1,1),(node2,2)]
    # while the graph is not fully traversed
    while len(nodeQ) != 0:
        curNode, path = nodeQ.pop(0)
        # base
        if (curNode.visited and curNode.visited != path):
            return(True)
        # iterate
        elif not curNode.visited:
            nodeQ += [(n, path) for n in curNode.neighbours]
            curNode.visited = path
    return(False)

if __name__ == "__main__":
    graph = Graph()
    num_nodes = int(input("num nodes: "))
    for _ in range(num_nodes):
        graph.addNode()
    for i in range(num_nodes):
        neighbours = [int(x) for x in input("neighbours seperated by space: ").split()]
        graph.nodes[i].neighbours = [graph.nodes[j] for j in neighbours]
    start, end = [int(x) for x in input("start and end ind of route: ").split()]
