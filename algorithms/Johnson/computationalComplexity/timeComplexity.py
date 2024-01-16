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


def remove_inf(dict):
    for key, value in list(dict.items()):
        if isinstance(value, dict):
            remove_inf(value)
        elif value == float('inf'):
            del dict[key]


def bellman_ford(graph: Graph, source):
    distance = {node: float('inf') for node in graph.graph}
    distance[source] = 0

    for node in graph.graph:
        if node != source and node not in distance:
            distance[node] = float('inf')

    for _ in range(len(graph.graph) - 1):
        for node in graph.graph:
            if distance[node] == float('inf'):
                continue
            for neighbor, weight in graph.graph.get(node, []):
                if distance[node] + weight < distance.get(neighbor, float('inf')):
                    distance[neighbor] = distance[node] + weight

    return distance


def reweight_edges(graph: Graph, distances):
    for u in graph.graph:
        for i, (v, weight) in enumerate(graph.graph[u]):
            graph.graph[u][i] = (v, weight + distances[u] - distances[v])


def dijkstra(graph: Graph, source, distances):
    distance = {node: float('inf') for node in graph.graph}
    distance[source] = 0
    visited = set()

    while len(visited) < len(graph.graph):
        current_node = min((node for node in graph.graph if node not in visited), key=lambda x: distance[x])
        visited.add(current_node)

        for neighbor, weight in graph.graph.get(current_node, []):
            if distance[current_node] + weight < distance.get(neighbor, float('inf')):
                distance[neighbor] = distance[current_node] + weight
    distance = {node: dist - distances[source] + distances[node] for node, dist in distance.items()}

    return distance


def johnson(graph: Graph):
    new_node = 'NEW_NODE'
    graph.graph[new_node] = [(node, 0) for node in graph.graph]

    distances = bellman_ford(graph, new_node)

    if any(distances[node] == float('inf') for node in distances):
        return None

    reweight_edges(graph, distances)

    del graph.graph[new_node]

    shortest_paths = {}
    for node in graph.graph:
        shortest_paths[node] = dijkstra(graph, node, distances)

    # remove_inf_origin(shortest_paths)

    if shortest_paths is None:
        return {}

    return shortest_paths


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
        graph = generate_random_graph(5 * testNumber, 0, testNumber * 5)
        johnson(graph)
    end = time.time()
    print(math.ceil(end - start))