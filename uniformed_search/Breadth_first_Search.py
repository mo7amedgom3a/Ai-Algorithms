from collections import deque
def bfs_recursive(graph, start, goal, visited=None, queue=None):
    if visited is None:
        visited = set()
    if queue is None:
        queue = deque([(start, [start])])

    if not queue:
        return None

    node, path = queue.popleft()
    if node == goal:
        return path
    # if the node is not visited add it to the visited set
    if node not in visited:
        visited.add(node)
        # expand the node and add the neighbors to the queue
        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append((neighbor, path + [neighbor]))
    # recursively call the function until the queue is empty
    return bfs_recursive(graph, start, goal, visited, queue)

def bfs(graph, start, goal):
    return bfs_recursive(graph, start, goal, visited=None, queue=None)

