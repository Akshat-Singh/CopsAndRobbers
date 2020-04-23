class Graph:
    """ Data Members of the Pseudo-Data Type Graph """
    vertices = 0
    edges = 0
    undirectedAdjacencyMatrix = [[]]  # A 2-D Matrix representation of a Graph
    directedAdjacencyMatrix = [[]]
    cycleLength = 0

    def __init__(self, vertices, edges):
        """ Parameterized Constructor of the Graph Class """
        self.vertices = vertices
        self.edges = edges
        """ Initializing the entire graph with 0s """
        self.directedAdjacencyMatrix = [[0 for j in range(vertices)] for i in range(vertices)]
        self.undirectedAdjacencyMatrix = [[0 for j in range(vertices)] for i in range(vertices)]

        """ Ensuring that every node has an edge to itself """
        for i in range(self.vertices):
            self.undirectedAdjacencyMatrix[i][i] = 1

    def addEdge(self, emergentNode, terminalNode):
        """ Definition of a function that adds an edge between two nodes on the adjacency matrix """
        self.undirectedAdjacencyMatrix[emergentNode - 1][terminalNode - 1] = 1
        self.undirectedAdjacencyMatrix[terminalNode - 1][emergentNode - 1] = 1
        self.directedAdjacencyMatrix[emergentNode - 1][terminalNode - 1] = 1

    def acceptGraph(self, attributes):
        """ Definition of a function that accepts the edges of a graph and calls the addEdge function """
        for i in range(1, self.edges + 1):
            emergentNode, terminalNode = map(int, attributes[i].split())
            self.addEdge(emergentNode, terminalNode)

    def returnDirectedAdjacencyMatrix(self):
        return self.directedAdjacencyMatrix

    def returnUndirectedAdjacencyMatrix(self):
        return self.undirectedAdjacencyMatrix

    def matrixLength(self):
        return self.vertices


def testrun():
    """ Driver Code """
    graphFile = open("data/level1.txt", "r")
    fileData = graphFile.readlines()
    towns, roads = map(int, fileData[0].split())
    graph = Graph(towns, roads)
    graph.acceptGraph(fileData)
