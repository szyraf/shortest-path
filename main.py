from shortest_path import dijkstra, bellman_ford, get_path
from visualize import visualize
from graph_examples import create_dijkstra_example, create_bellman_ford_example


def print_result(algorithm_name: str, distances: dict, predecessors: dict, start: int, target: int):
    print(f'\n{algorithm_name} Results:')
    print(f'Distance to vertex {target}: {distances[target]}')
    path = get_path(predecessors, target)
    print(f'Path to vertex {target}: {" -> ".join(map(str, path))}')


def main():
    print("Example 1: Simple graph (Dijkstra's Algorithm)")
    graph1 = create_dijkstra_example()
    start_vertex = 0
    target_vertex = 4

    distances, predecessors = dijkstra(graph1, start_vertex)
    print(distances)
    print(predecessors)
    print_result('Dijkstra', distances, predecessors, start_vertex, target_vertex)

    print('\nExample 2: Graph with negative weights (Bellman-Ford Algorithm)')
    graph2 = create_bellman_ford_example()

    distances, predecessors, no_negative_cycle = bellman_ford(graph2, start_vertex)

    if no_negative_cycle:
        print_result('Bellman-Ford', distances, predecessors, start_vertex, target_vertex)
    else:
        print('Negative cycle detected!')

    print('\nGenerating graph visualizations...')

    visualize()


if __name__ == '__main__':
    main()
