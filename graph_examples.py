from graph import Graph


def create_dijkstra_example() -> Graph:
    graph = Graph()
    graph.add_edge(0, 1, 7)
    graph.add_edge(0, 2, 2)
    graph.add_edge(1, 3, 3)
    graph.add_edge(2, 3, 2)
    graph.add_edge(3, 4, 4)
    graph.add_edge(1, 4, 15) 
    graph.add_edge(2, 5, 3)
    graph.add_edge(5, 4, 2)
    return graph


def create_bellman_ford_example() -> Graph:
    graph = Graph()
    graph.add_edge(0, 1, 4)
    graph.add_edge(0, 2, 5)
    graph.add_edge(1, 2, -3)
    graph.add_edge(1, 3, 6)
    graph.add_edge(2, 3, 2)
    graph.add_edge(2, 4, 4)
    graph.add_edge(3, 4, -2)
    graph.add_edge(4, 1, 3) 
    return graph
