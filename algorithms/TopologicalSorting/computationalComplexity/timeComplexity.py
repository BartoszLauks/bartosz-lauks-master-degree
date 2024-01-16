import random
import time
import math

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, source, destination):
        if source not in self.graph:
            self.graph[source] = []
        self.graph[source].append(destination)
        if destination not in self.graph:
            self.graph[destination] = []


def topological_sort(graph: Graph) -> []:
    def topological_sort_util(v, visited, stack):
        visited[v] = True
        for neighbor in graph.graph.get(v, []):
            if not visited[neighbor]:
                topological_sort_util(neighbor, visited, stack)
        stack.append(v)

    visited = {v: False for v in graph.graph}
    stack = []

    for vertex in graph.graph:
        if not visited[vertex]:
            topological_sort_util(vertex, visited, stack)

    return stack[::-1]


if __name__ == '__main__':

    start = time.time()
    for testNumber in range(1, 501):
        graphLenNode = testNumber * 10

        graph = Graph()

        for createGraph in range(1, graphLenNode):
            graph.add_edge(random.randint(0, 10 * testNumber), random.randint(0, 10 * testNumber))

        topological_sort(graph)
    end = time.time()
    print(math.ceil(end - start))