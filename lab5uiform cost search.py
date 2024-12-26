#lab5uiform cost search
import heapq

def uniform_cost_search(graph, start, goal):
    # Priority queue (min-heap), starting with the start node and a cost of 0
    priority_queue = [(0, start)]  # Each element is a tuple (cost, node)
    
    # Dictionary to store the minimum cost to reach each node
    costs = {start: 0}
    
    # Dictionary to store the parent of each node to reconstruct the path later
    came_from = {start: None}
    
    while priority_queue:
        # Pop the node with the least cost from the priority queue
        current_cost, current_node = heapq.heappop(priority_queue)
        
        # If the goal is reached, reconstruct the path and return it
        if current_node == goal:
            path = []
            while current_node:
                path.append(current_node)
                current_node = came_from[current_node]
            return path[::-1], current_cost
        
        # Explore the neighbors of the current node
        if current_cost > costs[current_node]:
            continue
        for neighbor, cost in graph[current_node].items():
            new_cost = costs[current_node] + cost
            
            # If this path to the neighbor is cheaper, add it to the frontier
            if neighbor not in costs or new_cost < costs[neighbor]:
                costs[neighbor] = new_cost
                came_from[neighbor] = current_node
                heapq.heappush(priority_queue, (new_cost, neighbor))
    
    # If no path is found, return None
    return None, float('inf')

# Define a sample graph where nodes have edge costs
# The graph is represented as an adjacency list with costs
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'D': 2, 'E': 5},
    'C': {'A': 4, 'E': 1},
    'D': {'B': 5, 'E': 3, 'F': 1},
    'E': {'B': 5, 'C': 1, 'D': 3, 'F': 2},
    'F': {'D': 1, 'E': 2}
}

# Run the UCS from 'A' to 'F'
path, cost = uniform_cost_search(graph, 'A', 'F')

# Display the result
print(f"Path: {path}, Cost: {cost}")

