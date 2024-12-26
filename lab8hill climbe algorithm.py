#lab8hill climbe algorithm
def hill_climbing(graph, start, goal, heuristic):
    # Initialize the current node and its cost (heuristic value)
    current_node = start
    current_cost = heuristic[current_node]
    path = [current_node]

    while current_node != goal:
        # Get the neighbors of the current node
        neighbors = graph.get(current_node, [])
        
        # If there are no neighbors, stop the search
        if not neighbors:
            break
        
        # Sort the neighbors based on their heuristic value in descending order
        neighbors.sort(key=lambda x: heuristic[x[0]])
        
        # Get the best neighbor with the highest heuristic value
        next_node, cost = neighbors[0]
        next_cost = heuristic[next_node]
        
        # If the next node does not improve the heuristic, stop (stuck at a local maximum)
        if next_cost >= current_cost:
            break
        
        # Move to the next node
        current_node = next_node
        current_cost = next_cost
        path.append(current_node)

    # If the goal is reached, return the path, otherwise return None
    return path if current_node == goal else None

# Define the graph with nodes, neighbors, and edge costs
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2), ('E', 5)],
    'C': [('F', 3)],
    'D': [('G', 6)],
    'E': [('G', 2)],
    'F': [('G', 1)],
    'G': []
}

# Define the heuristic values for each node
heuristic = {
    'A': 7,
    'B': 6,
    'C': 4,
    'D': 3,
    'E': 2,
    'F': 1,
    'G': 0
}

# Start node and goal node
start = 'A'
goal = 'G'

# Run the hill climbing algorithm
path = hill_climbing(graph, start, goal, heuristic)

# Display the result
if path:
    print(f"Path found: {' -> '.join(path)}")
else:
    print("No path found or stuck in local optimum")


