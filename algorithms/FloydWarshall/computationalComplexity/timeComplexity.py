import random
import time
import math


class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, source, destination, weight):
        if source not in self.graph:
            self.graph[source] = {}
        self.graph[source][destination] = weight


def floyd_warshall(graph: Graph, start_edge: int) -> {}:
    dist = {}

    for vertex in graph.graph:
        if vertex == start_edge:
            dist[start_edge] = 0
        elif start_edge in graph.graph and vertex in graph.graph[start_edge]:
            dist[vertex] = graph.graph[start_edge][vertex]
        else:
            dist[vertex] = float('inf')

    for k in graph.graph:
        for i in graph.graph:
            for j in graph.graph:
                if i in graph.graph[k] and j in graph.graph[i]:
                    if dist[i] != float('inf') and dist[i] + graph.graph[i][j] < dist[j]:
                        dist[j] = dist[i] + graph.graph[i][j]

    # Set unreachable graph to None
    for vertex in graph.graph:
        if dist[vertex] == float('inf'):
            del dist[vertex]

    return dist


def generate_random_graph(size: int, min_weight: int, max_weight: int) -> Graph:
    graph = Graph()

    for i in range(size):
        for j in range(i + 1, size):
            weight = random.randint(min_weight, max_weight)
            graph.add_edge(i, j, weight)

    return graph


if __name__ == '__main__':
    start = time.time()
    for testNumber in range(1, 81):
        graph = generate_random_graph(2 * testNumber, testNumber * 2 * -1, testNumber * 2)
        floyd_warshall(graph, list(graph.graph.keys())[0])
    end = time.time()
    print(math.ceil(end - start))
