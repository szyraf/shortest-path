import networkx as nx
import matplotlib.pyplot as plt
from graph import Graph
from graph_examples import create_dijkstra_example, create_bellman_ford_example


def create_graph_visualization(graph: Graph, title: str, filename: str):
    G = nx.DiGraph()

    for source in graph.graph:
        for dest, weight in graph.graph[source]:
            G.add_edge(source, dest, weight=weight)

    pos = nx.spring_layout(G, k=2, iterations=50)

    plt.figure(figsize=(10, 8))
    plt.title(title)

    nx.draw_networkx_nodes(G, pos, node_color='lightblue', node_size=500, alpha=0.8)
    nx.draw_networkx_labels(G, pos)

    edge_labels = nx.get_edge_attributes(G, 'weight')
    for (src, dst), label in edge_labels.items():
        x_src, y_src = pos[src]
        x_dst, y_dst = pos[dst]
        x_label = (x_src + x_dst) / 2
        y_label = (y_src + y_dst) / 2 + 0.04  

        plt.text(x_label, y_label, str(label), fontsize=10, bbox=dict(facecolor='white', edgecolor='none', pad=1.0))
    nx.draw_networkx_edges(G, pos, edge_color='gray', arrowsize=20)

    plt.axis('off')
    plt.savefig(filename, format='png', dpi=300, bbox_inches='tight')
    plt.close()


def visualize():
    # Create and visualize first graph (Dijkstra example)
    graph1 = create_dijkstra_example()
    create_graph_visualization(
        graph1,
        "Graf z nieujemnymi wagami (Algorytm Dijkstry)",
        'dijkstra_graph.png',
    )

    # Create and visualize second graph (Bellman-Ford example)
    graph2 = create_bellman_ford_example()
    create_graph_visualization(
        graph2,
        'Graf z ujemnymi wagami (Algorytm Bellmana-Forda)',
        'bellman_ford_graph.png',
    )
