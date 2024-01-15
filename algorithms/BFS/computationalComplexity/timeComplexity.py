import random
import time
from collections import deque


class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)


def bfs(graph: Graph, start: int) -> []:
    visited = []
    queue = deque([start])

    while queue:
        current_node = queue.popleft()

        if current_node not in visited:
            visited.append(current_node)
            queue.extend(neighbor for neighbor in graph.graph.get(current_node, []) if neighbor not in visited)

    return visited


if __name__ == '__main__':

    start = time.time()
    for test in range(1, 500):
        graphLenNode = test * 10
        graph = Graph()

        for createGraph in range(1, graphLenNode):
            graph.add_edge(random.randint(0, 100), random.randint(0, 100))

        bfs(graph, 0)
    end = time.time()
    print(round(end - start, 2))
