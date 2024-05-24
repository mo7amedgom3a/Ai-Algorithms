import networkx as nx
import matplotlib.pyplot as plt

def visualize_graph(graph):
    """
    Visualize the graph
    :param graph: graph
    :return: None
    """
    G = nx.DiGraph()

    for node, edges in graph.items():
        for adjacent_node, weight in edges.items():
            G.add_edge(node, adjacent_node, weight=weight)

    pos = nx.spring_layout(G, seed=42)  # Fixed seed for reproducible layout
    edge_labels = nx.get_edge_attributes(G, 'weight')
    
    plt.figure(figsize=(10, 8))
    
    nx.draw(G, pos, with_labels=True, node_size=2000, node_color='skyblue', font_size=15, font_weight='bold', arrows=True, edge_color='gray')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red', font_size=12)

    plt.title('Weighted Graph Visualization', fontsize=20)
    plt.savefig('graph/weighted_graph.png', format='PNG')