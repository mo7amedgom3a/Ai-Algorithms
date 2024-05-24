
from collections import deque
heuristic_values = {
        'A': 10,
        'B': 8,
        'C': 5,
        'D': 7,
        'E': 3,
        'F': 0
}


def heuristic(node, goal, heuristic_values):
    """
    Returns the heuristic estimate of the cost to reach the goal from the given node.
    :param node: The current node.
    :param goal: The goal node.
    :param heuristic_values: A dictionary containing heuristic values for each node.
    :return: The heuristic cost estimate from the node to the goal.
    """
    return heuristic_values.get(node, 0)

def calculate_path_cost(graph, start, end):
    """
    Calculate the actual cost to get from the start node to the end node.
    :param graph: The graph represented as an adjacency dictionary with edge weights.
    :param start: The start node.
    :param end: The end node.
    :return: The actual cost to reach the end node from the start node.
    """
    
    # Priority queue to store (cost, current_node, path)
    priority_queue = deque([(0, start, [])])
    visited = set()

    while priority_queue:
        total_cost, current_node, path = priority_queue.popleft()

        if current_node in visited:
            continue

        path = path + [current_node]
        visited.add(current_node)

        if current_node == end:
            return total_cost

        for neighbor, weight in graph[current_node].items():
            if neighbor not in visited:
                priority_queue.append((total_cost + weight, neighbor, path))
                priority_queue = deque(sorted(priority_queue, key=lambda x: x[0]))

    return float('inf')  # If there is no path
