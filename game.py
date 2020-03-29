""" Header Files used to visualize graphs """
import networkx as nx
import matplotlib.pyplot as mpl

""" Creating an object of the networkX library """
visualGraph = nx.Graph()


class Graph:
    """ Data Members of the Pseudo-Data Type Graph """
    vertices = 0
    edges = 0
    graph = [[]]  # A 2-D Matrix representation of a Graph

    """ Parameterized Constructor of the Graph Class """
    
    def __init__(self, vertices, edges):
        self.vertices = vertices
        self.edges = edges
        self.graph = [[0 for j in range(vertices)] for i in range(vertices)]  # Initializing the entire graph with 0s

    def addEdge(self, emergentNode, terminalNode):
        self.graph[emergentNode - 1][terminalNode - 1] = 1
        self.graph[terminalNode - 1][emergentNode - 1] = 1

    def acceptGraph(self):
        for i in range(self.edges):
            emergentNode = int(input("Emergent Node: "))
            terminalNode = int(input("Terminal Node: "))
            self.addEdge(emergentNode, terminalNode)

    def printAdjacencyMatrix(self):
        print(f"{self.graph}")

    def visualizeGraph(self):
        for i in range(self.vertices):
            for j in range(self.vertices):
                if self.graph[i][j] == 1:
                    visualGraph.add_edge(i, j)

        nx.draw(visualGraph)
        mpl.show()


def main():
    towns = int(input("Number Of Vertices: "))
    roads = int(input("Number Of Edges: "))
    graph = Graph(towns, roads)
    graph.acceptGraph()
    graph.visualizeGraph()


if __name__ == '__main__':
    main()
