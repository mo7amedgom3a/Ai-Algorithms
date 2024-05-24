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
        for adjacent_node in edges:
            G.add_edge(node, adjacent_node)

    pos = nx.spring_layout(G, seed=42)  # Fixed seed for reproducible layout
    
    plt.figure(figsize=(10, 8))
    
    nx.draw(G, pos, with_labels=True, node_size=2000, node_color='skyblue', font_size=15, font_weight='bold', arrows=True, edge_color='gray')

    plt.title('Unweighted Graph Visualization', fontsize=20)
    plt.savefig('graph/unweighted_graph.png', format='PNG')