import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

def draw_path_on_graph(graph, path, algorithm):
    G = nx.Graph()
    for node, neighbors in graph.items():
        for neighbor in neighbors:
            G.add_edge(node, neighbor)

    # Create a list of edges in the path
    path_edges = [(path[i], path[i+1]) for i in range(len(path)-1)]

    pos = nx.spring_layout(G, seed=42)
    edge_labels = {(node, neighbor): '' for node, neighbors in graph.items() for neighbor in neighbors}
    edge_colors = ['red' if (node, neighbor) in path_edges or (neighbor, node) in path_edges else 'gray' for node, neighbor in G.edges()]

    plt.figure(figsize=(10, 8))
    nx.draw(G, pos, with_labels=True, node_size=2000, node_color='skyblue', font_size=15, font_weight='bold', arrows=True, edge_color=edge_colors)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red', font_size=12)
    plt.title('Graph with BFS Path', fontsize=20)
    plt.savefig(f'graph/path_solution_{algorithm}.png', format='PNG')
    plt.show()