#2.depth first search
def dfs(graph, start, visited=None):
    """Perform Depth-First Search (DFS) on a graph using sets for neighbors."""
    if visited is None:
        visited = set()  # Initialize visited set if it's not provided

    visited.add(start)  # Mark the current node as visited
    print(start)  # Print the current node

    # Recursively visit all unvisited neighbors
    for next in graph[start] - visited:
        dfs(graph, next, visited)  # Recursively call DFS for the unvisited neighbor

    return visited  

graph = {
    'A': set(['B', 'C']),
    'B': set(['A', 'D', 'E']),
    'C': set(['D', 'F','G']),
    'D': set(['B', 'E']),
    'E': set(['B', 'F', 'I']),
    'F': set(['E', 'C']),
    'G': set(['C']),  # New node 'G'
    'H': set(['D']),  # New node 'H'
    'I': set(['E'])   # New node 'I'
}

dfs(graph, 'E')
