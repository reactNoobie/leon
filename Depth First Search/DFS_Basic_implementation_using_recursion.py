class GraphNode:
    def __init__(self,name):
        self.name = name
        self.visited = False
        self.cost = 0
        self.edges = []
        self.parent = None
        
    def add_edge(self,edge):
        self.edges.append(edge)
        
    def print(self):
        print("****************************************")
        print("Node:")
        print("name:", self.name)
        print("cost:", self.cost)
        print("visited:", self.visited)
        print("number of neighbors:", len(self.edges))
        print("neighbors:", end="")
        for neighbor in self.edges:
            print("(" + neighbor.name + ")", end=" ")
        print("\n****************************************")
        
class Graph:
    def __init__(self):
        self.nodes = []
        self.result_array = []
        self.first_traversal = False
   
    def add_node(self,node):
        self.nodes.append(node)
    
    def dfs_recur(self, source):
        if self.first_traversal == False:
            source.cost = 0
            print("**************Initiating DFS with", source.name, "as head**************")
            self.first_traversal = True
        print("Current Candidate = ", source.name, "with edges", [edge.name for edge in source.edges])
        if source.visited == False:
            source.visited = True
            self.result_array.append(source.name)
            for edge in source.edges:
                if edge.visited == False:
                    print("current edge =", edge.name)
                    edge.parent = source
                    edge.cost = source.cost + 1
                    graph.dfs_recur(edge)
                else:
                    print(edge.name, "has been visited previously")

"""*************************************************Driver code BELOW*************************************************"""
graph = Graph()

messi = GraphNode("Messi")
ronaldo = GraphNode("Ronaldo")
di_maria = GraphNode("Di Maria")
neymar = GraphNode("Neymar")
ramos = GraphNode("Ramos")
bale = GraphNode("Bale")
willian = GraphNode("Willian")
silva = GraphNode("Silva")

graph.add_node(messi)
graph.add_node(ronaldo)
graph.add_node(di_maria)
graph.add_node(neymar)
graph.add_node(ramos)
graph.add_node(bale)
graph.add_node(willian)
graph.add_node(silva)

messi.add_edge(neymar) 
messi.add_edge(di_maria)
#messi.print()

# connect ronaldo with friends
ronaldo.add_edge(di_maria)
ronaldo.add_edge(ramos)
# ronaldo.print()

# connect di maria with friends
di_maria.add_edge(messi)
di_maria.add_edge(ronaldo)
di_maria.add_edge(neymar)
# di_maria.print()

# connect neymar with friends
neymar.add_edge(messi)
neymar.add_edge(willian)
neymar.add_edge(di_maria)
# neymar.print()
willian.add_edge(silva)
willian.add_edge(neymar)

silva.add_edge(neymar)

# connect ramos with friends
ramos.add_edge(ronaldo)
# ramos.print()

graph.dfs_recur(messi)
print(" ")
print("DFS RESULT ARRAY BELOW")
print(graph.result_array)

for node in graph.nodes:
    node.print()