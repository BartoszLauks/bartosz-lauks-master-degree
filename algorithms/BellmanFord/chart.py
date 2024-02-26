import random
import sys
import time

from matplotlib import pyplot as plt

try:
    from userBellmanFord import bellman_ford
except Exception as e:
    print(sys.argv[1], "ERROR IMPORT")
    sys.exit()

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, source, destination, weight):
        if source not in self.graph:
            self.graph[source] = []
        self.graph[source].append((destination, weight))


def bellman_ford_origin(graph: Graph, start_vertex: int) -> {}:
    # Step 1: Initialize distances
    distances = {vertex: float('infinity') for vertex in graph.graph}
    distances[start_vertex] = 0

    # Step 2: Relax graph repeatedly
    for _ in range(len(graph.graph) - 1):
        for current_vertex in graph.graph:
            if current_vertex in distances:
                for neighbor, weight in graph.graph[current_vertex]:
                    if distances[current_vertex] + weight < distances.get(neighbor, float('infinity')):
                        distances[neighbor] = distances[current_vertex] + weight

    # Step 3: Check for negative cycles
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
    x = []
    t1 = []
    t2 = []
    #i = 0
    for testNumber in range(1, 23):
        #i += 1
        #print(i)
        graphLenNode = testNumber ** 2 + 1
        #print(graphLenNode)
        x.append(graphLenNode)
        graph = generate_random_graph(graphLenNode, 0, graphLenNode)

        start = time.time()
        # #print(graph.graph)
        bellman_ford_origin(graph, list(graph.graph.keys())[0])
        #print('origin: ', float((time.time() - start)))
        t1.append(float(time.time() - start))

        start = time.time()
        bellman_ford(graph, list(graph.graph.keys())[0])
        #print('Topological sorting: ', time.time() - start)
        t2.append(time.time() - start)

    #print(x)
    #print(t1)
    #print(t2)
    plt.plot(x, t1, label='Server Implementation')
    plt.plot(x, t2, '-.', label='User implementation')

    plt.xlabel("Graph size")
    plt.ylabel("Time (float)")
    plt.grid()
    plt.legend()
    plt.title('Bellman Ford Algorithm')
    #plt.show()
    plt.savefig('chart.png')