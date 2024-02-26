import heapq
import random
import time
import math

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, source, destination, weight):
        if source not in self.graph:
            self.graph[source] = []
        if destination not in self.graph:
            self.graph[destination] = []

        self.graph[source].append((destination, weight))
        self.graph[destination].append((source, weight))


def prim(graph: Graph, start_vertex) -> []:
    visited = set()
    min_heap = [(0, start_vertex, None)]
    minimum_spanning_tree = []

    while min_heap:
        weight, current_vertex, parent_vertex = heapq.heappop(min_heap)

        if current_vertex not in visited:
            visited.add(current_vertex)

            if parent_vertex is not None:
                minimum_spanning_tree.append((parent_vertex, current_vertex, weight))

            for neighbor, edge_weight in graph.graph[current_vertex]:
                heapq.heappush(min_heap, (edge_weight, neighbor, current_vertex))

    return minimum_spanning_tree


def generate_random_graph(num_edges: int, max_weight: int) -> Graph:
    graph = Graph()

    vertices = list(range(1, num_edges + 1))
    random.shuffle(vertices)

    for i in range(num_edges - 1):
        u = vertices[i]
        v = vertices[i + 1]
        weight = random.randint(1, max_weight)
        graph.add_edge(u, v, weight)

    last_vertex = vertices[-1]
    first_vertex = vertices[0]
    weight = random.randint(1, max_weight)
    graph.add_edge(last_vertex, first_vertex, weight)

    return graph


if __name__ == '__main__':

    start = time.time()
    for testNumber in range(1, 1001):
        graph = generate_random_graph(2 * testNumber, testNumber * 10)

        prim(graph, list(graph.graph.keys())[0])
    end = time.time()
    print(math.ceil(end - start))