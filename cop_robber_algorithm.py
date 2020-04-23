def compare_lists(list1, list2, vertices):
    for i in range(vertices):
        if list1[i] == 1 and list2[i] != 1:
            """not a  pitfall"""
            return False
       
    return True

def removeAllEdges(adjacencyMatrix, L, vertices):
    for i in range(vertices):
        adjacencyMatrix[L][i] = 0
        adjacencyMatrix[i][L] = 0

def containsEdge(adjacencyMatrix, v1, v2):
    return True if adjacencyMatrix[v1][v2] > 0 else False

def cop_robber_preliminary(adjacencyMatrix, vertices):
    for i in range(vertices):
        for j in range(vertices):
            if i != j:
                if (compare_lists(adjacencyMatrix[i], adjacencyMatrix[j], vertices)):
                    removeAllEdges(adjacencyMatrix, i, vertices)
                    break

def cop_robber_final(adjacencyMatrix, vertices):
    for i in range(vertices):
        for j in range(vertices):
            if i != j and containsEdge(adjacencyMatrix, i, j):
                """it is a robber win graph"""
                return True

        """it is a cop win graph"""
    return False
            
