class Graph:
    def __init__(self):
        self.nodes = []

    def add_node(self, node):
        self.nodes.append(node)

    def bfs(self, source):
        print("--------------Running BFS---------------")
        candidates = list()
        source.cost = 0
        source.visited = True
        candidates.append(source)
        while len(candidates) > 0:
            candidate = candidates.pop(0)
            print("Current candidate:", candidate.name)
            for neighbor in candidate.neighbors:
                print("Considering", candidate.name + "'s neighbor", neighbor.name)
                if not neighbor.visited:
                    neighbor.cost = candidate.cost + 1
                    neighbor.visited = True
                    candidates.append(neighbor)
                    print("Added", neighbor.name, "to candidates. Cost:", neighbor.cost)
                else:
                    print(neighbor.name, "already visited! Skipping...")
            print("----------------------------------------")
        print("---------------End of BFS---------------")

    def print(self):
        for node in self.nodes:
            node.print()

class GraphNode:
    def __init__(self, name="NAME"):
        self.name = name
        self.neighbors = []
        self.cost = -1
        self.visited = False

    def add_neighbor(self, neighbor):
        self.neighbors.append(neighbor)

    def print(self):
        print("****************************************")
        print("Node:")
        print("name:", self.name)
        print("cost:", self.cost)
        print("visited:", self.visited)
        print("number of neighbors:", len(self.neighbors))
        print("neighbors:", end="")
        for neighbor in self.neighbors:
            print("(" + neighbor.name + ")", end=" ")
        print("\n****************************************")


# declare a graph
graph = Graph()

# declare the graph nodes
messi = GraphNode("Messi")
ronaldo = GraphNode("Ronaldo")
di_maria = GraphNode("Di Maria")
neymar = GraphNode("Neymar")
ramos = GraphNode("Ramos")
bale = GraphNode("Bale")

# insert the nodes into the graph
graph.add_node(messi)
graph.add_node(ronaldo)
graph.add_node(di_maria)
graph.add_node(neymar)
graph.add_node(ramos)
graph.add_node(bale)

# connect messi with friends
messi.add_neighbor(di_maria) 
messi.add_neighbor(neymar)
# messi.print()

# connect ronaldo with friends
ronaldo.add_neighbor(di_maria)
ronaldo.add_neighbor(ramos)
# ronaldo.print()

# connect di maria with friends
di_maria.add_neighbor(messi)
di_maria.add_neighbor(ronaldo)
di_maria.add_neighbor(neymar)
# di_maria.print()

# connect neymar with friends
neymar.add_neighbor(messi)
neymar.add_neighbor(di_maria)
# neymar.print()

# connect ramos with friends
ramos.add_neighbor(ronaldo)
# ramos.print()

# bale has no friends
# bale.print()

graph.bfs(messi)
graph.print()