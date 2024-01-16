import heapq
import random
import time
import math

class Graph:
    def __init__(self):
        self.graph = {}

    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []

    def add_edge(self, source, destination, weight):
        self.add_vertex(source)
        self.add_vertex(destination)
        self.graph[source].append((destination, weight))
        self.graph[destination].append((source, weight))


def dijkstra(graph: Graph, start):
    min_heap = [(0, start)]
    visited = set()

    distances = {vertex: float('infinity') for vertex in graph.graph}
    distances[start] = 0

    while min_heap:
        current_distance, current_vertex = heapq.heappop(min_heap)

        if current_vertex in visited:
            continue

        visited.add(current_vertex)

        for neighbor, weight in graph.graph[current_vertex]:
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(min_heap, (distance, neighbor))

    return distances


def generate_random_graph(size: int, max_weight: int) -> Graph:
    graph = Graph()

    for i in range(size):
        graph.add_vertex(i)

    for i in range(size):
        for j in range(i + 1, size):
            weight = random.randint(1, max_weight)
            graph.add_edge(i, j, weight)

    return graph


if __name__ == '__main__':

    start = time.time()
    for testNumber in range(1, 201):
        graph = generate_random_graph(2 * testNumber, testNumber)

        dijkstra(graph, 0)
    end = time.time()
    print(math.ceil(end - start))
