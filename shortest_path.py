from typing import Dict, List, Optional, Tuple
from math import inf
from graph import Graph
from heapq import heappush, heappop


def dijkstra(graph: Graph, start: int) -> Tuple[Dict[int, float], Dict[int, Optional[int]]]:
    distances = {vertex: inf for vertex in graph.get_vertices()}
    distances[start] = 0
    predecessors = {vertex: None for vertex in graph.get_vertices()}
    priority_queue = [(0, start)]
    visited = set()

    while priority_queue:
        current_distance, current_vertex = heappop(priority_queue)

        if current_vertex in visited:
            continue

        visited.add(current_vertex)

        for neighbor, weight in graph.get_neighbors(current_vertex):
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                predecessors[neighbor] = current_vertex
                heappush(priority_queue, (distance, neighbor))

    return distances, predecessors


def bellman_ford(graph: Graph, start: int) -> Tuple[Dict[int, float], Dict[int, Optional[int]], bool]:
    distances = {vertex: inf for vertex in graph.get_vertices()}
    distances[start] = 0
    predecessors = {vertex: None for vertex in graph.get_vertices()}

    for _ in range(len(graph.get_vertices()) - 1):
        for vertex in graph.get_vertices():
            for neighbor, weight in graph.get_neighbors(vertex):
                if distances[vertex] + weight < distances[neighbor]:
                    distances[neighbor] = distances[vertex] + weight
                    predecessors[neighbor] = vertex

    for vertex in graph.get_vertices():
        for neighbor, weight in graph.get_neighbors(vertex):
            if distances[vertex] + weight < distances[neighbor]:
                return distances, predecessors, False

    return distances, predecessors, True


def get_path(predecessors: Dict[int, Optional[int]], target: int) -> List[int]:
    path = []
    current = target

    while current is not None:
        path.append(current)
        current = predecessors[current]

    return path[::-1]
