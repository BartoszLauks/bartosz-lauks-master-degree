import random
import time
import math

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)


def dfs(graph: Graph, start: int, visited=None) -> []:
    if visited is None:
        visited = []
    visited.append(start)

    for neighbor in graph.graph.get(start, []):
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

    return visited


if __name__ == '__main__':

    start = time.time()
    for testNumber in range(1, 501):
        graphLenNode = testNumber * 10
        graph = Graph()

        for createGraph in range(1, graphLenNode):
            graph.add_edge(random.randint(0, 100), random.randint(0, 100))

        dfs(graph, 0)
    end = time.time()
    print(math.ceil(end - start))
