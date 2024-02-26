import random
import sys
import time

from matplotlib import pyplot as plt

try:
    from userFloydWarshall import floyd_warshall
except Exception as e:
    print(sys.argv[1], "ERROR IMPORT")
    sys.exit()


class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, source, destination, weight):
        if source not in self.graph:
            self.graph[source] = {}
        self.graph[source][destination] = weight


def floyd_warshall_origin(graph: Graph, start_edge: int) -> {}:
    dist = {}

    for vertex in graph.graph:
        if vertex == start_edge:
            dist[start_edge] = 0
        elif start_edge in graph.graph and vertex in graph.graph[start_edge]:
            dist[vertex] = graph.graph[start_edge][vertex]
        else:
            dist[vertex] = float('inf')

    for k in graph.graph:
        for i in graph.graph:
            for j in graph.graph:
                if i in graph.graph[k] and j in graph.graph[i]:
                    if dist[i] != float('inf') and dist[i] + graph.graph[i][j] < dist[j]:
                        dist[j] = dist[i] + graph.graph[i][j]

    # Set unreachable graph to None
    for vertex in graph.graph:
        if dist[vertex] == float('inf'):
            del dist[vertex]

    return dist


def generate_random_graph(size: int, min_weight: int, max_weight: int) -> Graph:
    graph = Graph()

    for i in range(size):
        for j in range(i + 1, size):
            weight = random.randint(min_weight, max_weight)
            graph.add_edge(i, j, weight)

    return graph


if __name__ == '__main__':
    x = []
    t1 = []
    t2 = []
    #i = 0
    for testNumber in range(1, 22):
        #i += 1
        #print(i)
        graphLenNode = testNumber ** 2 + 1
        #print(graphLenNode)
        x.append(graphLenNode)
        graph = generate_random_graph(graphLenNode, 0, graphLenNode)

        start = time.time()
        # #print(graph.graph)
        floyd_warshall_origin(graph, list(graph.graph.keys())[0])
        #print('origin: ', float((time.time() - start)))
        t1.append(float(time.time() - start))

        start = time.time()
        floyd_warshall(graph, list(graph.graph.keys())[0])
        #print('FloydWarshall: ', time.time() - start)
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
    plt.title('Floyd Warshall Algorithm')
    #plt.show()
    plt.savefig('chart.png')