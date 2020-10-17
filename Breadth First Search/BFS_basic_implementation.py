class Graph:
    def __init__(self):
        self.nodes = []
        self.array = []
        
    def add_node(self, node):
        self.nodes.append(node)
    
    def bfs(self, head):
        candidates = []
        print("*****************************starting BFS Search with source =", head.name, "************************************")
        print("**********************************************************************************************************")
        head.visited = True
        head.cost = 0
        candidates.append(head)
        while len(candidates) > 0:
            candidate = candidates.pop(0)
            print("Currently checking node", candidate.name)
            print(" ")
            for neighbour in candidate.neighbours:
                if not neighbour.visited:
                    print("Visiting node =", neighbour.name)
                    print(" ")
                    neighbour.cost = candidate.cost + 1
                    neighbour.visited = True
                    candidates.append(neighbour)
                    self.array.append("To traverse to node {}, we need to make {} steps".format(neighbour.name, neighbour.cost))
                else:
                    print("we have already visited node", neighbour.name)
        print("END OF BFS, use function print_traversal_cost to get log of the steps we need to take to visit each node.")
        print("********************************************************************************************************** ")
        print(" ")
                    
                    
    def print_traversal_cost(self):
        for i in self.array:
            print(i)
    
    def print(self):
        print("*******Name of the candidates to be considered throughout the BFS Search*******")
        for node in self.nodes:
            print(node.name, " ", end = '')
        print(" ")
        print("*********************************************************************************")
        print(" ")
        print(" ")

            
class GraphNode:
    def __init__(self, name):
        self.name = name
        self.neighbours = []
        self.cost = -1
        self.visited = False
    
    def add_neighbour(self, neighbour):
        self.neighbours.append(neighbour)


#declaring a graph

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
messi.add_neighbour(di_maria) 
messi.add_neighbour(neymar)
# messi.print()

# connect ronaldo with friends
ronaldo.add_neighbour(di_maria)
ronaldo.add_neighbour(ramos)
# ronaldo.print()

# connect di maria with friends
di_maria.add_neighbour(messi)
di_maria.add_neighbour(ronaldo)
di_maria.add_neighbour(neymar)
# di_maria.print()

# connect neymar with friends
neymar.add_neighbour(messi)
neymar.add_neighbour(di_maria)
# neymar.print()

# connect ramos with friends
ramos.add_neighbour(ronaldo)
# ramos.print()

graph.print()
graph.bfs(messi)
graph.print_traversal_cost()
                
                
