""" Header Files used to visualize graphs """
import matplotlib.pyplot as mpl
import networkx as nx


class Graph:
    """ Data Members of the Pseudo-Data Type Graph """
    vertices = 0
    edges = 0
    undirectedAdjacencyMatrix = [[]]  # A 2-D Matrix representation of a Graph
    directedAdjacencyMatrix = [[]]
    cycleLength = 0
    markTable = []

    def __init__(self, vertices, edges):
        """ Parameterized Constructor of the Graph Class """
        self.vertices = vertices
        self.edges = edges
        """ Initializing the entire graph with 0s """
        self.directedAdjacencyMatrix = [[0 for j in range(vertices)] for i in range(vertices)]
        self.undirectedAdjacencyMatrix = [[0 for j in range(vertices)] for i in range(vertices)]
        self.markTable = [False for i in range(self.vertices)]

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

    def visualizeGraph(self):
        """ Definition of a function that uses matplotlib and networkx to visualize a graph """

        """ Creating an object of the networkX library """
        visualGraph = nx.Graph()

        for i in range(self.vertices):
            for j in range(self.vertices):
                if self.undirectedAdjacencyMatrix[i][j] == 1:
                    visualGraph.add_edge(i, j)

        nx.draw(visualGraph)
        mpl.show()

    def returnDirectedAdjacencyMatrix(self):
        return self.directedAdjacencyMatrix

    def returnUndirectedAdjacencyMatrix(self):
        return self.undirectedAdjacencyMatrix


def run():
    """ Driver Code """
    graphFile = open("data/level1.txt", "r")
    fileData = graphFile.readlines()
    towns, roads = map(int, fileData[0].split())
    graph = Graph(towns, roads)
    graph.acceptGraph(fileData)
    graph.visualizeGraph()

