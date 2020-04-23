# =====================================================================
# BFS

from collections import deque


def BFS(g, home, target):
    matrix = g.returnUndirectedAdjacencyMatrix()  # Extract the matrix from the graph

    def BFS_traversal(g, matrix, home):

        # Make a queue and add the first element to it
        queue = deque()
        queue.append(home)


        # No. of nodes = num_nodes
        # Visited is a list; it contains Boolean values representing whether a node is visited or not
        # Initialize starting point equivalent in "visited" to 'True'
        num_nodes = g.matrixLength()
        visited = [False] * num_nodes
        visited[home] = True
        
        # parent list
        parent = [None] * num_nodes

        while queue:
            current = queue.popleft()
            for i in range(len(matrix[current])):
                if matrix[current][i] == 1:
                    if not visited[i]:
                        visited[i] = True
                        queue.append(i)
                        parent[i] = current
                        
        return parent

    # ===========================================

    parent = BFS_traversal(g, matrix, home)  # Calling the function that we just defined

    # ===========================================

    def BFS_reconstruction(home, target, parent):
        path = []
        length = len(parent)
        i = target
        while i is not None:
            path.append(i)
            i = parent[i]

        path.reverse()

        if path[0] == home:
            return path
        return []

    shortest_path = BFS_reconstruction(home, target, parent)  # Calling the function we just defined

    return shortest_path[1]
