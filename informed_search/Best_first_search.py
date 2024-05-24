import heapq
from informed_search.heuristic import heuristic

def best_first_search(graph, start, goal, heuristic_values):
    """
    Find the shortest path from the start node to the goal node using Best First Search.
    :param graph: The graph represented as an adjacency dictionary with edge weights.
    :param start: The start node.
    :param goal: The goal node.
    :param heuristic_values: A dictionary containing heuristic values for each node.
    """
    priority_queue = []
    heapq.heappush(priority_queue, (heuristic(start, goal, heuristic_values), start, [start]))
    visited = set()

    while priority_queue:
        _, current_node, path = heapq.heappop(priority_queue)

        if current_node == goal:
            return path

        visited.add(current_node)

        for neighbor, _ in graph[current_node].items():
            if neighbor not in visited:
                new_path = path + [neighbor]
                heapq.heappush(priority_queue, (heuristic(neighbor, goal, heuristic_values), neighbor, new_path))

    return None
