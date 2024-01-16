import random
import time
import math

class Graph:
    def __init__(self):
        self.graph = []

    def add_edge(self, source, destination, weight):
        self.graph.append((source, destination, weight))


def kruskal(graph: Graph):
    all_vertices = set()
    for edge in graph.graph:
        all_vertices.add(edge[0])
        all_vertices.add(edge[1])

    num_vertices = len(all_vertices)

    graph.graph = sorted(graph.graph, key=lambda x: x[2])

    parent = [i for i in range(num_vertices)]

    def find_set(v):
        if parent[v] == v:
            return v
        return find_set(parent[v])

    def union_sets(u, v):
        root_u = find_set(u)
        root_v = find_set(v)
        parent[root_u] = root_v

    min_spanning_tree = []

    for edge in graph.graph:
        u, v, w = edge
        if find_set(u) != find_set(v):
            min_spanning_tree.append((u, v, w))
            union_sets(u, v)

    return min_spanning_tree


def generate_random_graph(size: int, max_weight: int) -> Graph:
    graph = Graph()

    for i in range(size):
        for j in range(i + 1, size):
            weight = random.randint(1, max_weight)
            graph.add_edge(i, j, weight)

    return graph


if __name__ == '__main__':

    start = time.time()
    for testNumber in range(1, 101):
        graph = generate_random_graph(testNumber * 2, testNumber * 10)

        kruskal(graph)
    end = time.time()
    print(math.ceil(end - start))
