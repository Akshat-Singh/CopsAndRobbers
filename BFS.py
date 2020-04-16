#=====================================================================
#BFS

from collections import deque, defaultdict

#=============================================================================
# Define class for a graph and it's adjacency list
#=============================================================================

class Graph():
	def __init__(self):
		self.graph = defaultdict(list)

	def adj(self):
		return self.graph 

	def addEdge(self, u, v):
		self.graph[u].append(v)

	def length(self):
		return int(len(self.graph))

#=============================================================================
# Define BFS Algorithm. It consists of two functions: BFS Traveral and BFS Path Reconstruction
#=============================================================================

def BFS(g, graph, home, target):

	def BFS_traversal(g, graph, home):
		# Make a queue and add the first element to it 
		# A list-queue data structure is used, however it is slow as it's time complexity is O(n)
		queue = deque()
		queue.append(home)

		# No. of nodes = num_nodes
		# Visited is a list; it contains Boolean values representing whether a node is visited or not
		# Initialize starting point equivalent in "visited" to 'True'
		num_nodes = g.length()rint(num_nodes)
		visited = [False] * num_nodes
		visited[home] = True

		#distance list 
		dist = [None] * num_nodes
		dist[home] = 0 

		#parent list
		parent = [None] * num_nodes

		while queue:
			current = queue.popleft()
			for i in graph[current]:
				if visited[i] == False:
					visited[i] = True
					queue.append(i)
					parent[i] = current
					dist[i] = dist[current] + 1
				
		return dist, parent

	#===========================================

	dist, parent = BFS_traversal(g, graph, home) # Calling the function that we just defined

	#===========================================

	def BFS_reconstruction(home, target, parent):
		path = []
		length = len(parent)
		i = length - 1
		while(i != None):
			path.append(i)
			i = parent[i]

		path.reverse()

		if path[0] == home:
			return path
		return []
		
	#===========================================

	shortest_path = BFS_reconstruction(home, target, parent) #Calling the function we just defined

	#===========================================

	return shortest_path


#=============================================================================

# Driver Code 

# Undirected Graph
g = Graph() 
g.addEdge(0, 1)
g.addEdge(1, 0)
g.addEdge(0, 2)
g.addEdge(2, 0) 
g.addEdge(1, 2)
g.addEdge(2, 1)  
g.addEdge(2, 3)
g.addEdge(3, 2) 

adjacency_matrix = g.adj()

shortestPath = BFS(g, adjacency_matrix, 0, 3)

print(shortestPath)

