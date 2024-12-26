#4.iteratitive depth limit search:
def dls(graph, start, depth_limit, visited=None, depth=0):
    if visited is None:
        visited = set()
    
    # Check if the depth limit has been reached
    if depth > depth_limit:
        return visited
    
    # Mark the current node as visited
    visited.add(start)
    print(f"{'  ' * depth}{start} (Depth: {depth})")  # Print node with depth indentation

    # Recurse for each neighbor if not visited and within depth limit
    for next_node in graph[start] - visited:
        dls(graph, next_node, depth_limit, visited, depth + 1)
    
    return visited

def iddfs(graph, start, goal, max_depth):
    for depth in range(max_depth + 1):
        print(f"Searching with depth limit: {depth}")
        visited = set()
        result = dls(graph, start, depth, visited)
        
        if goal in visited:
            print(f"Goal {goal} found at depth {depth}")
            return visited
    
    print(f"Goal {goal} not found within depth limit {max_depth}")
    return visited

# Example graph
graph = {
    'A': set(['B', 'C']),
    'B': set(['A', 'D', 'E']),
    'C': set(['A', 'F', 'G']),
    'D': set(['B', 'E']),
    'E': set(['B', 'F', 'I']),
    'F': set(['E', 'C']),
    'G': set(['C']),
    'H': set(['D']),
    'I': set(['E'])
}

# Perform Iterative Deepening DFS from node 'E' with a goal 'G' and max depth of 3
iddfs(graph, 'E', 'G', max_depth=3)

