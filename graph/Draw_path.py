import matplotlib.pyplot as plt
import networkx as nx

def draw_path_on_graph(graph, path, algorithm, start_node=None):
    G = nx.Graph()
    for node, neighbors in graph.items():
        for neighbor in neighbors:
            G.add_edge(node, neighbor)

    pos = nx.spring_layout(G, seed=42)
    edge_labels = {(node, neighbor): '' for node, neighbors in graph.items() for neighbor in neighbors}

    path_edges = [(path[i], path[i + 1]) for i in range(len(path) - 1)]
        
    edge_colors = ['red' if (node, neighbor) in path_edges or (neighbor, node) in path_edges else 'gray' for node, neighbor in G.edges()]

    # Sort edges so that edges starting with start_node are drawn first
    edges = G.edges()
    edges = sorted(edges, key=lambda edge: edge[0] != start_node)

    plt.figure(figsize=(10, 8))
    nx.draw_networkx_edges(G, pos, edgelist=edges, edge_color=edge_colors)
    nx.draw_networkx_nodes(G, pos, node_size=2000, node_color='skyblue')
    nx.draw_networkx_labels(G, pos, font_size=15, font_weight='bold')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red', font_size=12)

    if start_node:
        nx.draw_networkx_nodes(G, pos, nodelist=[start_node], node_color='green', node_size=2000)

    plt.title(f'Graph with {algorithm} Path', fontsize=20)
    plt.savefig(f'graph/path_solution_{algorithm}.png', format='PNG')
    plt.show()