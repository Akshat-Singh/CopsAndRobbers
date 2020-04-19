# Python Program to count
# cycles of length n
# in a given graph.

# Number of vertices
V = 5
import networkx as nx
import matplotlib.pyplot as mpl

def DFS(graph, marked, n, vert, start, count):
    # mark the vertex vert as visited
    marked[vert] = True

    # if the path of length (n-1) is found
    if n == 0:

        # mark vert as un-visited to make
        # it usable again.
        marked[vert] = False

        # Check if vertex vert can end with
        # vertex start
        if graph[vert][start] == 1:
            count = count + 1
            return count
        else:
            return count

            # For searching every possible path of
    # length (n-1)
    for i in range(V):
        if marked[i] == False and graph[vert][i] == 1:
            # DFS for searching path by decreasing
            # length by 1
            count = DFS(graph, marked, n - 1, i, start, count)

            # marking vert as unvisited to make it
    # usable again.
    marked[vert] = False
    return count


# Counts cycles of length
# N in an undirected
# and connected graph.
def countCycles(graph, n):
    # all vertex are marked un-visited initially.
    marked = [False] * V

    # Searching for cycle by using v-n+1 vertices
    count = 0
    for i in range(V - (n - 1)):
        count = DFS(graph, marked, n - 1, i, i, count)

        # ith vertex is marked as visited and
        # will not be visited again.
        marked[i] = True

    return int(count / 2)


# main :
graph = [[0, 1, 0, 1, 0],
         [1, 0, 1, 0, 1],
         [0, 1, 0, 1, 0],
         [1, 0, 1, 0, 1],
         [0, 1, 0, 1, 0]]
visualGraph = nx.Graph()
for i in range(5):
    for j in range(5):
        if graph[i][j] == 1:
            visualGraph.add_edge(i, j)

nx.draw(visualGraph)
mpl.show()

n = 4
print("Total cycles of length ", n, " are ", countCycles(graph, n))
