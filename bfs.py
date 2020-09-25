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
        
    def path_finder(self, source, destination):
        path_arr = []
        path_arr.append(source)
        candidates = list()
        source.cost = 0
        source.visited = True
        if source.name == destination.name: 
            print("The source is the destination, hence cost is zero and no traversal is needed")
        else:
            candidates.append(source)
            while len(candidates) > 0:
                candidate = candidates.pop()
                for neighbour in candidate.neighbors:
                    if not neighbour.visited:
                        neighbour.cost = candidate.cost + 1
                        neighbour.visited = True        
                        if neighbour.name == destination.name:
                            path_arr.append(neighbour)
                        else:
                            candidates.append(neighbour)
                            path_arr.append(neighbour)
        for i in range(len(path_arr)):
            try:
                #print(path_arr[i].name, path_arr[i].cost, path_arr[i + 1].name, path_arr[i + 1].cost)
                if path_arr[i].cost == i and (path_arr[i] in path_arr[i + 1].neighbors):
                    pass
                else:
                    path_arr.pop(i)
            except:
                pass
            
                
        for i in path_arr:
            print(i.name, " ", end = '')
        print(" ")
        print("To go from {} to {}, we need to make {} steps".format(source.name, destination.name, destination.cost))
    

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
di_maria = GraphNode("Di_Maria")
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

#graph.bfs(messi)
graph.path_finder(messi,ronaldo)
