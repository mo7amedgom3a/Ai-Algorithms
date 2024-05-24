def dfs_recursive(graph, start, goal, visited=None, path=None):
    """
    Recursive implementation of Depth First Search
    """
    if visited is None:
        visited = set()
    if path is None:
        path = []

    if start == goal:
        path.append(start)
        return path

    visited.add(start)
    path.append(start)

    for neighbor in graph[start]:
        if neighbor not in visited:
            result = dfs_recursive(graph, neighbor, goal, visited, path)
            if result:
                return result

    path.pop()  # Backtrack if no path found from this node
    return None

def dfs(graph, start, goal):
    return dfs_recursive(graph, start, goal, visited=set(), path=[])