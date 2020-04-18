class Graph:
    """ Data Members of the Pseudo-Data Type Graph """
    vertices = 0
    edges = 0
    adjacencyMatrix = [[]]  # A 2-D Matrix representation of a Graph
    cycleLength = 0
    markTable = []

    def __init__(self, vertices, edges):
        """ Parameterized Constructor of the Graph Class """
        self.vertices = vertices
        self.edges = edges
        """ Initializing the entire graph with 0s """
        self.adjacencyMatrix = [[0 for j in range(vertices)] for i in range(vertices)]

        for i in range(vertices):
            for j in range(vertices):
                if i == j:
                    self.adjacencyMatrix[i][j] = 1

                
        self.markTable = [False for i in range(self.vertices)]

    def addEdge(self, emergentNode, terminalNode):
        """ Definition of a function that adds an edge between two nodes on the adjacency matrix """
        self.adjacencyMatrix[emergentNode - 1][terminalNode - 1] = 1
        self.adjacencyMatrix[terminalNode - 1][emergentNode - 1] = 1

    def acceptGraph(self):
        """ Definition of a function that accepts the edges of a graph and calls the addEdge function """
        for i in range(self.edges):
            emergentNode = int(input("Emergent Node: "))
            terminalNode = int(input("Terminal Node: "))
            self.addEdge(emergentNode, terminalNode)

    def printAdjacencyMatrix(self):
        """ Function that simply prints the entire Adjacency Matrix onto the console """
        print(f"{self.adjacencyMatrix}")

    def removeEdge(self, v1, v2):
        if self.adjacencyMatrix[v1][v2] == 0:
            print("No edge between %d and %d" % (v1, v2))
            return
        self.adjacencyMatrix[v1][v2] = 0
        self.adjacencyMatrix[v2][v1] = 0

    def removeAllEdges(self, L):
        for i in range(vertices):
            self.adjacencyMatrix[L][i] = 0
            self.adjacencyMatrix[i][L] = 0

    def containsEdge(self, v1, v2):
        return True if self.adjacencyMatrix[v1][v2] > 0 else False

    
    """check whether the matrix has been reduced to a single vertex"""

    def cop_or_robber(self):
        for i in range(vertices):
            for j in range(vertices):
                if i != j and self.containsEdge(i, j):
                    print(f"Robber win graph!")
                    return 

        print(f"Cop win graph!")
        return

def compare_lists(list1, list2):
    for i in range(vertices):
        if list1[i] == 1 and list2[i] != 1:
            """not a  pitfall"""
            return False
       
    return True
            
vertices = int(input("Number Of Vertices: "))
edges = int(input("Number Of Edges: "))
graph = Graph(vertices, edges)
graph.acceptGraph()

""""check whether there are pitfalls, and if so, remove them"""

for i in range(vertices):
    for j in range(vertices):
        if i != j:
            if(compare_lists(graph.adjacencyMatrix[i], graph.adjacencyMatrix[j])):

                graph.removeAllEdges(i)
                break

graph.cop_or_robber()
            