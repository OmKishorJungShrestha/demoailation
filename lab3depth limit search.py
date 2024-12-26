#lab3depth limit search
def dls(graph, start, depth_limit, visited=None, depth=0):
    """Perform Depth-Limited Search (DLS) on a graph with a specified depth limit."""
    if visited is None:
        visited = set()  # Initialize visited set if it's not provided

    # If the depth limit is reached or exceeded, stop the search
    if depth > depth_limit:
        return visited

    visited.add(start)  # Mark the current node as visited
    print(f"{' ' * depth}{start}(Depth:{depth})")  # Indent and print the current node with its depth

    
    # Visit neighbors in the custom defined order
    for next_node in graph[start] - visited:
        
            dls(graph, next_node, depth_limit, visited, depth + 1)  # Recursively call DLS for the unvisited neighbor

    return visited  # Return the visited set to propagate it back

# Define the graph with sets for adjacency lists
graph = {
    'A': set(['B', 'C']),
    'B': set(['A', 'D', 'E']),
    'C': set(['D', 'F', 'G']),
    'D': set(['B', 'E']),
    'E': set(['B', 'F', 'I']),
    'F': set(['E', 'C']),
    'G': set(['C']),  # New node 'G'
    'H': set(['D']),  # New node 'H'
    'I': set(['E'])   # New node 'I'
}

# Call Depth-Limited Search (DLS) starting from node 'E' with a depth limit of 3
dls(graph, 'E', depth_limit=2)