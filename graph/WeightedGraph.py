#!/usr/bin/env python3
def create_weighted_graph():
    """
    Create a weighted graph
    :return: graph
    """
    graph = {
        'A': {'B': 1, 'C': 4},
        'B': {'D': 2, 'E': 5},
        'C': {'F': 3, 'G': 6},
        'D': {},
        'E': {},
        'F': {},
        'G': {}
    }
    return graph
"""
        A
       / \
       1   4
       /     \
      B       C
     / \     / \
    2   5   3   6
    D   E   F   G
"""