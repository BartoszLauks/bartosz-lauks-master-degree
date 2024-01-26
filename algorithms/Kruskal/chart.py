import random
import sys
import time

from matplotlib import pyplot as plt

try:
    from userKruskal import kruskal
except Exception as e:
    print(sys.argv[1], "ERROR IMPORT")
    sys.exit()


class Graph:
    def __init__(self):
        self.graph = []

    def add_edge(self, source, destination, weight):
        self.graph.append((source, destination, weight))


def kruskal_origin(graph: Graph):
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
    x = []
    t1 = []
    t2 = []
    i = 0
    for testNumber in range(0, 11):
        i += 1
        #print(i)
        graphLenNode = 2 ** testNumber
        #print(graphLenNode)
        x.append(graphLenNode)
        graph = generate_random_graph(graphLenNode, graphLenNode)

        start = time.time()
        # #print(graph.graph)
        kruskal_origin(graph)
        #print('origin: ', float((time.time() - start)))
        t1.append(float(time.time() - start))

        start = time.time()
        kruskal(graph)
        #print('Kruskal: ', time.time() - start)
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
    plt.title('Kruskal Algorithm')
    #plt.show()
    plt.savefig('chart.png')
