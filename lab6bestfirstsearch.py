#lab6best first search:
import heapq

def best_first_search(graph, start, goal, heuristic):
    # Priority queue initialized with the start node and its heuristic
    priority_queue = []
    heapq.heappush(priority_queue, (heuristic[start], start))
    visited = set()
    came_from = {start: None}

    while priority_queue:
        current_priority, current_node = heapq.heappop(priority_queue)

        if current_node == goal:
            # Reconstruct the path from goal to start
            path = []
            while current_node:
                path.append(current_node)
                current_node = came_from[current_node]
            return path[::-1]

        visited.add(current_node)

        # Explore neighbors of the current node
        for neighbor in graph[current_node]:
            if neighbor not in visited:
                heapq.heappush(priority_queue, (heuristic[neighbor], neighbor))
            if neighbor not in came_from:
                came_from[neighbor] = current_node

    return None

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

# Run the search from start to goal
path = best_first_search(graph, start, goal, heuristic)

# Display the result
print(f"Path: {path}")





'''
graph = {
    (0, 0): [(0, 1), (1, 0)],
    (0, 1): [(0, 0), (1, 1)],
    (1, 0): [(0, 0), (1, 1)],
    (1, 1): [(0, 1), (1, 0)]
}

# Heuristic values: estimated cost from each node to the goal
heuristic = {
    (0, 0): 2,
    (0, 1): 1,
    (1, 0): 1,
    (1, 1): 0  # Goal node
}


'''