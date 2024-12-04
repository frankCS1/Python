graph = {
  'X': ['M', 'P'],
  'M': ['L', 'R', 'A'],
  'L': ['C', 'J'],
  'R': ['M', 'N'],
  'A': [],
  'P': ['B'],
  'B': ['P', 'F'],
  'F': [], #To keep empty because it already has been completed
  'C': [],
  'J': [],
  'N': [] #These are the ends of the nodes
}
#This is the list of elements
visited = set() #This keeps track of already completed nodes of graph.

def dfs(visited, graph, node):  #Function for dfs 
    if node not in visited:
        print(node)
        visited.add(node) #Saves the unvisited nodes to the list 
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

print("Result of DFS: ")
dfs(visited, graph, 'X') #This prints the DFS graph


def bfs(graph, start):
    visited = set()
    queue = [start]  # Starts a queue with the start node
    visited.add(start)

    while queue:
        node = queue.pop(0)  
        print(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append(neighbor)  #Appends the neighbour
                visited.add(neighbor) #Adds the neighbour to the visted list

print("\nResult of BFS: ")
bfs(graph, 'X') #This prints the BFS graph
