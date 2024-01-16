import random
import time
import math


class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, source, destination, weight):
        if source not in self.graph:
            self.graph[source] = []
        self.graph[source].append((destination, weight))


def bellman_ford_origin(graph: Graph, start_vertex: int) -> {}:
    distances = {vertex: float('infinity') for vertex in graph.graph}
    distances[start_vertex] = 0

    for _ in range(len(graph.graph) - 1):
        for current_vertex in graph.graph:
            if current_vertex in distances:
                for neighbor, weight in graph.graph[current_vertex]:
                    if distances[current_vertex] + weight < distances.get(neighbor, float('infinity')):
                        distances[neighbor] = distances[current_vertex] + weight

    for current_vertex in graph.graph:
        if current_vertex in distances:
            for neighbor, weight in graph.graph[current_vertex]:
                if distances[current_vertex] + weight < distances[neighbor]:
                    return {}

    return distances


def generate_random_graph(size, min_weight, max_weight):
    graph = Graph()
    vertices = list(range(1, size + 1))

    for u in vertices:
        for v in vertices:
            if u != v:
                weight = random.randint(min_weight, max_weight)
                graph.add_edge(u, v, weight)

    return graph


if __name__ == '__main__':

    start = time.time()
    for testNumber in range(1, 31):
        graph = generate_random_graph(5 * testNumber, testNumber * 5, testNumber * 5)
        bellman_ford_origin(graph, list(graph.graph.keys())[0])
    end = time.time()
    print(math.ceil(end - start))
