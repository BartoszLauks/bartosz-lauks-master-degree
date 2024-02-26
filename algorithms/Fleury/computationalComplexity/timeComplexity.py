import math
import random
import time


class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, source, destination):
        self.graph.setdefault(source, []).append(destination)
        self.graph.setdefault(destination, []).append(source)


def is_bridge(graph, u, v):
    visited = set()
    dfs_stack = [u]
    visited.add(u)

    while dfs_stack:
        current = dfs_stack.pop()
        for neighbor in graph[current]:
            if neighbor == v:
                continue
            if neighbor not in visited:
                dfs_stack.append(neighbor)
                visited.add(neighbor)

    return v not in visited


def fleury(graph):
    odd_degree_nodes = [node for node, neighbors in graph.graph.items() if len(neighbors) % 2 == 1]
    if len(odd_degree_nodes) not in [0, 2]:
        return {}

    current_node = list(graph.graph.keys())[0] if len(odd_degree_nodes) == 0 else odd_degree_nodes[0]
    circuit = []

    while graph.graph:
        neighbors = graph.graph[current_node]

        if not neighbors:
            break

        edge_to_remove = None

        for neighbor in list(neighbors):
            if is_bridge(graph.graph, current_node, neighbor):
                continue

            edge_to_remove = (current_node, neighbor)
            break

        if edge_to_remove is None:
            edge_to_remove = (current_node, neighbors[0])

        graph.graph[edge_to_remove[0]].remove(edge_to_remove[1])
        graph.graph[edge_to_remove[1]].remove(edge_to_remove[0])

        if not graph.graph[current_node]:
            del graph.graph[current_node]

        circuit.append(edge_to_remove)
        current_node = edge_to_remove[1]

    return circuit


def generate_random_graph(num_vertices: int, num_edges: int):
    graph = Graph()

    for _ in range(num_edges):
        u = random.randint(0, num_vertices - 1)
        v = random.randint(0, num_vertices - 1)
        graph.add_edge(u, v)

    return graph


if __name__ == '__main__':
    start = time.time()
    for testNumber in range(1, 501):
        graph = generate_random_graph(testNumber, testNumber)
        fleury(graph)
    end = time.time()
    print(math.ceil(end - start))