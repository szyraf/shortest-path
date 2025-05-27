from shortest_path import dijkstra, bellman_ford, get_path
from visualize import visualize
from graph_examples import create_dijkstra_example, create_bellman_ford_example


def print_result(algorithm_name: str, distances: dict, predecessors: dict, start: int, target: int):
    print(f'\n{algorithm_name} Wyniki:')
    print(f'Dystans do wierzchołka {target}: {distances[target]}')
    path = get_path(predecessors, target)
    print(f'Ścieżka do wierzchołka {target}: {" -> ".join(map(str, path))}')


def main():
    print("Przykład pierwszy: Prosty graf (Algorytm Dijkstry)")
    graph1 = create_dijkstra_example()
    start_vertex = 0
    target_vertex = 4

    distances, predecessors = dijkstra(graph1, start_vertex)
    print(distances)
    print(predecessors)
    print_result('Dijkstra', distances, predecessors, start_vertex, target_vertex)

    print('\nPrzykład drugi: Graf z ujemnymi wagami (Algorytm Bellmana-Forda)')
    graph2 = create_bellman_ford_example()

    distances, predecessors, no_negative_cycle = bellman_ford(graph2, start_vertex)

    if no_negative_cycle:
        print_result('Bellman-Ford', distances, predecessors, start_vertex, target_vertex)
    else:
        print('Ujemny cykl')


    visualize()


if __name__ == '__main__':
    main()
