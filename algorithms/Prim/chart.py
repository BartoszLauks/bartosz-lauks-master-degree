import heapq
import random
import sys
import time
from string import ascii_uppercase

from matplotlib import pyplot as plt

try:
    from userPrim import prim
except Exception as e:
    print(sys.argv[1], "ERROR IMPORT")
    sys.exit()

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, source, destination, weight):
        if source not in self.graph:
            self.graph[source] = []
        if destination not in self.graph:
            self.graph[destination] = []

        self.graph[source].append((destination, weight))
        self.graph[destination].append((source, weight))


def prim_original(graph: Graph, start_vertex) -> []:
    visited = set()
    min_heap = [(0, start_vertex, None)]
    minimum_spanning_tree = []

    while min_heap:
        weight, current_vertex, parent_vertex = heapq.heappop(min_heap)

        if current_vertex not in visited:
            visited.add(current_vertex)

            if parent_vertex is not None:
                minimum_spanning_tree.append((parent_vertex, current_vertex, weight))

            for neighbor, edge_weight in graph.graph[current_vertex]:
                heapq.heappush(min_heap, (edge_weight, neighbor, current_vertex))

    return minimum_spanning_tree


def generate_random_graph(vertices, max_weight):
    graph = Graph()

    # Add edges to form a connected graph without bridges
    for i in range(1, vertices):
        source = i
        destination = random.randint(0, i - 1)
        weight = random.randint(1, max_weight)
        graph.add_edge(source, destination, weight)

    return graph


if __name__ == '__main__':
    x = []
    t1 = []
    t2 = []
    #i = 0
    for testNumber in range(1, 20):
        #i += 1
        #print(i)
        graphLenNode = 2 ** testNumber
        #print(graphLenNode)
        x.append(graphLenNode)
        graph = generate_random_graph(graphLenNode, graphLenNode)

        start = time.time()
        ##print(graph.graph)
        prim_original(graph, list(graph.graph.keys())[0])
        #print('origin: ', float((time.time() - start)))
        t1.append(float(time.time() - start))

        start = time.time()
        prim(graph, list(graph.graph.keys())[0])
        #print('Prim: ', time.time() - start)
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
    plt.title('Prim Algorithm')
    #plt.show()
    plt.savefig('chart.png')