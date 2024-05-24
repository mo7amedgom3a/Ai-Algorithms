def create_unweighted_graph():
    """
    Create a unweighted graph
    :return: graph
    """
    graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F', 'G'],
        'D': [],
        'E': [],
        'F': [],
        'G': []
    }
    return graph

"""
      A
     / \
    B   C
   / \  / \
   D  E F  G
"""