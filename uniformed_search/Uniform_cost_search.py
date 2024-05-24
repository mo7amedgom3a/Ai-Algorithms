def ucs(graph, start, goal):
    priority_queue = [(0, start, [start])]  # (total_cost, current_node, path)
    visited = set()

    while priority_queue:
        total_cost, current_node, path = priority_queue.pop(0)

        if current_node == goal:
            return path

        visited.add(current_node)

        for neighbor, weight in graph[current_node].items():
            if neighbor not in visited:
                new_cost = total_cost + weight
                new_path = path + [neighbor]
                priority_queue.append((new_cost, neighbor, new_path))
                priority_queue.sort()  # Sort the priority queue based on total cost

    return None
