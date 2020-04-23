"""compares two rows of the adjacency matrix"""
def compare_lists(list1, list2, vertices):
    for i in range(vertices):
        if list1[i] == 1 and list2[i] != 1:
            """not a  pitfall"""
            return False
       
    return True


"""removes all edges in case the vertex ia  pitfall"""
def removeAllEdges(adjacencyMatrix, L, vertices):
    for i in range(vertices):
        adjacencyMatrix[L][i] = 0
        adjacencyMatrix[i][L] = 0

"""checks whether an edge exists between two vertices"""
def containsEdge(adjacencyMatrix, v1, v2):
    return True if adjacencyMatrix[v1][v2] > 0 else False

"""checks whether a pitfall exists and removes all edges if it does"""
def cop_robber_preliminary(adjacencyMatrix, vertices):
    counter = 0
    while counter != vertices:
        for i in range(vertices):
            for j in range(vertices):
                if i != j:
                    if (compare_lists(adjacencyMatrix[i], adjacencyMatrix[j], vertices)):
                        removeAllEdges(adjacencyMatrix, i, vertices)
                        break

        counter = counter + 1
"""checks whether it is a cop win graph or robber win graph"""
"""returns True if it is a robber win graph, and False if it a cop win graph"""
def cop_robber_final(adjacencyMatrix, vertices):
    for i in range(vertices):
        for j in range(vertices):
            if i != j and containsEdge(adjacencyMatrix, i, j):
                """it is a robber win graph"""
                return True

    """it is a cop win graph"""
    return False
