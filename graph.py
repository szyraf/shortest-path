from collections import defaultdict
from typing import Dict, List, Set, Tuple, Optional
from math import inf


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.vertices = set()

    def add_edge(self, source: int, destination: int, weight: int) -> None:
        self.graph[source].append((destination, weight))
        self.vertices.add(source)
        self.vertices.add(destination)

    def get_neighbors(self, vertex: int) -> List[Tuple[int, int]]:
        return self.graph[vertex]

    def get_vertices(self) -> Set[int]:
        return self.vertices
