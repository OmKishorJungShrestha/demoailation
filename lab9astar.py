#lab9 A* algorithm
import heapq

def a_star(graph, start, goal, heuristic):
    # Priority queue to store nodes with their f(n) values (f(n) = g(n) + h(n))
    open_list = []
    heapq.heappush(open_list, (0 + heuristic[start], start))
    
    # Dictionaries to store the actual cost to reach a node and the parent of each node
    g_costs = {start: 0}  # g(n) is the cost from the start node to the current node
    came_from = {start: None}  # To reconstruct the path
    
    while open_list:
        # Pop the node with the lowest f(n) from the priority queue
        _, current_node = heapq.heappop(open_list)
        
        # If the goal is reached, reconstruct the path and return it
        if current_node == goal:
            path = []
            while current_node:
                path.append(current_node)
                current_node = came_from[current_node]
            return path[::-1]  # Reverse the path to get the correct order
        
        # Explore the neighbors of the current node
        for neighbor, cost in graph[current_node]:
            # Calculate g(n) for the neighbor
            tentative_g_cost = g_costs[current_node] + cost
            
            # If this neighbor has not been visited or a shorter path is found
            if neighbor not in g_costs or tentative_g_cost < g_costs[neighbor]:
                g_costs[neighbor] = tentative_g_cost
                f_cost = tentative_g_cost + heuristic[neighbor]
                came_from[neighbor] = current_node
                heapq.heappush(open_list, (f_cost, neighbor))  # Add the neighbor to the open list

    # If the goal is not reached, return None
    return None

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
    'A': 7,  # Heuristic value for node A
    'B': 6,  # Heuristic value for node B
    'C': 4,  # Heuristic value for node C
    'D': 3,  # Heuristic value for node D
    'E': 2,  # Heuristic value for node E
    'F': 1,  # Heuristic value for node F
    'G': 0   # Heuristic value for node G (goal node)
}

# Start node and goal node
start = 'A'
goal = 'G'

# Run the A* algorithm
path = a_star(graph, start, goal, heuristic)

# Display the result
if path:
    print(f"Path found: {' -> '.join(path)}")
else:
    print("No path found")
