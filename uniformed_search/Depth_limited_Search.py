def dls_recursive(graph, start, goal, depth_limit, visited=None, path=None):
    """
    Recursive implementation of Depth Limited Search
    """
    if visited is None:
        visited = set()
    if path is None:
        path = []

    if start == goal:
        path.append(start)
        return path

    if depth_limit <= 0:
        return None

    visited.add(start)
    path.append(start)

    for neighbor in graph[start]:
        if neighbor not in visited:
            result = dls_recursive(graph, neighbor, goal, depth_limit - 1, visited, path)
            if result:
                return result

    path.pop()  # Backtrack if no path found from this node
    return None

def dls(graph, start, goal, depth_limit):
    return dls_recursive(graph, start, goal, depth_limit, visited=set(), path=[])
