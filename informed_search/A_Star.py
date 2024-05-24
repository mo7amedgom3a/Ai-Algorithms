# AStarSearch.py

import heapq
from informed_search.heuristic import heuristic

def a_star_search(graph, start, goal, heuristic_values):
    # Priority queue to store (f_cost, current_node, path, g_cost)
    priority_queue = []
    heapq.heappush(priority_queue, (heuristic(start, goal, heuristic_values), start, [start], 0))
    visited = set()
    path_costs = {start: 0}

    while priority_queue:
        f_cost, current_node, path, g_cost = heapq.heappop(priority_queue)

        if current_node == goal:
            return path

        visited.add(current_node)

        for neighbor, weight in graph[current_node].items():
            if neighbor in visited:
                continue

            new_g_cost = g_cost + weight
            new_f_cost = new_g_cost + heuristic(neighbor, goal, heuristic_values)
            
            if neighbor not in path_costs or new_g_cost < path_costs[neighbor]:
                path_costs[neighbor] = new_g_cost
                new_path = path + [neighbor]
                heapq.heappush(priority_queue, (new_f_cost, neighbor, new_path, new_g_cost))

    return None
