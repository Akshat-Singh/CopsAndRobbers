""" Header Files used to visualize graphs """
import networkx as nx
import matplotlib.pyplot as mpl

""" Creating an object of the networkX library """
visualGraph = nx.Graph()


class Graph:
    """ Data Members of the Pseudo-Data Type Graph """
    vertices = 0
    edges = 0
    adjacencyMatrix = [[]]  # A 2-D Matrix representation of a Graph

    """ Parameterized Constructor of the Graph Class """
    def __init__(self, vertices, edges):
        self.vertices = vertices
        self.edges = edges
        """ Initializing the entire graph with 0s """
        self.adjacencyMatrix = [[0 for j in range(vertices)] for i in range(vertices)]

    """ Definition of a function that adds an edge between two nodes on the adjacency matrix """
    def addEdge(self, emergentNode, terminalNode):
        self.adjacencyMatrix[emergentNode - 1][terminalNode - 1] = 1
        self.adjacencyMatrix[terminalNode - 1][emergentNode - 1] = 1

    """ Definition of a function that accepts the edges of a graph and calls the addEdge function """
    def acceptGraph(self):
        for i in range(self.edges):
            emergentNode = int(input("Emergent Node: "))
            terminalNode = int(input("Terminal Node: "))
            self.addEdge(emergentNode, terminalNode)

    """ Function that simply prints the entire Adjacency Matrix onto the console """
    def printAdjacencyMatrix(self):
        print(f"{self.adjacencyMatrix}")

    """ Definition of a function that uses matplotlib and networkx to visualize a graph """
    def visualizeGraph(self):
        for i in range(self.vertices):
            for j in range(self.vertices):
                if self.adjacencyMatrix[i][j] == 1:
                    visualGraph.add_edge(i, j)

        nx.draw(visualGraph)
        mpl.show()


""" Driver Code """


def main():
    towns = int(input("Number Of Vertices: "))
    roads = int(input("Number Of Edges: "))
    graph = Graph(towns, roads)
    graph.acceptGraph()
    graph.visualizeGraph()


if __name__ == '__main__':
    main()
