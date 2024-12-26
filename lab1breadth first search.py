#breadth first search
def bfs(graph, start):
    """Perform Breadth-First Search (BFS) on a graph using a list as the queue."""
    visited = set()
    queue = [start]  # Using a list instead of deque
    order = []

    while queue:
        node = queue.pop(0)  # Popping from the front of the list
        if node not in visited:
            visited.add(node)
            order.append(node)
            
            # Append neighbors to the queue
            for neighbor in graph.get(node, []):
                if neighbor not in visited:
                    queue.append(neighbor)

    return order

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}
start_node = 'A'
print("BFS Traversal Order:", bfs(graph, start_node))

