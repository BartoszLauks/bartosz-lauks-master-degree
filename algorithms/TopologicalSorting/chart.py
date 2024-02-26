import random
import sys
import time

from matplotlib import pyplot as plt

try:
    from userTopologicalSorting import topological_sort
except Exception as e:
    print(sys.argv[1], "ERROR IMPORT")
    sys.exit()


class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, source, destination):
        if source not in self.graph:
            self.graph[source] = []
        self.graph[source].append(destination)
        if destination not in self.graph:
            self.graph[destination] = []


def topological_sort_original(graph: Graph) -> []:
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


def create_dag_graph(size):
    g = Graph()
    vertices = list(range(1, size + 1))

    for vertex in vertices:
        possible_destinations = [v for v in vertices if v > vertex]
        num_destinations = random.randint(0, min(len(possible_destinations), size // 2))
        destinations = random.sample(possible_destinations, num_destinations)

        for destination in destinations:
            g.add_edge(vertex, destination)

    return g


if __name__ == '__main__':
    x = []
    t1 = []
    t2 = []
    #i = 0
    for testNumber in range(1, 60):
        #i += 1
        #print(i)
        graphLenNode = testNumber ** 2
        #print(graphLenNode)
        x.append(graphLenNode)
        graph = create_dag_graph(graphLenNode)

        start = time.time()
        ##print(graph.graph)
        topological_sort_original(graph)
        #print('origin: ', float((time.time() - start)))
        t1.append(float(time.time() - start))

        start = time.time()
        topological_sort_original(graph)
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
    plt.title('Topological sorting Algorithm')
    #plt.show()
    plt.savefig('chart.png')
