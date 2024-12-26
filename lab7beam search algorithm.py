#lab7beam search algorithm
import heapq

def beam_search(graph, start, goal, heuristic, beam_width):
    # Priority queue initialized with the start node and its heuristic value
    frontier = [(heuristic[start], start)]
    visited = set([start])  # Set to track visited nodes
    came_from = {start: None}  # Dictionary to track the predecessors of nodes

    while frontier:
        # Sort the frontier based on the heuristic value
        frontier = sorted(frontier, key=lambda x: x[0])
        
        # Limit the number of nodes in the frontier based on the beam width
        frontier = frontier[:beam_width]
        
        next_frontier = []

        # Explore each node in the frontier
        for _, current_node in frontier:
            if current_node == goal:
                # Reconstruct the path if the goal is reached
                path = []
                while current_node is not None:
                    path.append(current_node)
                    current_node = came_from[current_node]
                return path[::-1]

            # Add the neighbors of the current node to the next frontier
            for neighbor in graph[current_node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    came_from[neighbor] = current_node  # Set the current node as the predecessor of the neighbor
                    next_frontier.append((heuristic[neighbor], neighbor))
        
        # Update the frontier for the next iteration
        frontier = next_frontier

    return None  # Return None if no path is found

# Graph structure with alphabetic nodes
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F', 'G'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E'],
    'G': ['C']
}

# Heuristic values: estimated cost from each node to the goal ('G')
heuristic = {
    'A': 4,
    'B': 3,
    'C': 2,
    'D': 3,
    'E': 2,
    'F': 1,
    'G': 0  # Goal node
}

# Start and goal nodes
start = 'A'
goal = 'G'

# Define the beam width
beam_width = 2

# Run the Beam Search from start to goal
path = beam_search(graph, start, goal, heuristic, beam_width)

# Display the result
print(f"Path: {path}")
