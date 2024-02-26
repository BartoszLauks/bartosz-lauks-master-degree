import heapq
import random
import sys
import time

from matplotlib import pyplot as plt

try:
    from userDijkstra import dijkstra
except Exception as e:
    print(sys.argv[1], "ERROR IMPORT")
    sys.exit()


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


def dijkstra_origin(graph: Graph, start):
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
    x = []
    t1 = []
    t2 = []
    i = 0
    for testNumber in range(1, 50):
        i += 1
        #print(i)
        graphLenNode = testNumber ** 2
        #print(graphLenNode)
        x.append(graphLenNode)
        graph = generate_random_graph(graphLenNode, graphLenNode)

        start = time.time()
        # #print(graph.graph)
        dijkstra_origin(graph, list(graph.graph.keys())[0])
        #print('origin: ', float((time.time() - start)))
        t1.append(float(time.time() - start))

        start = time.time()
        dijkstra(graph, list(graph.graph.keys())[0])
        #print('BFS: ', time.time() - start)
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
    plt.title('Dijkstra Algorithm')
    #plt.show()
    plt.savefig('chart.png')