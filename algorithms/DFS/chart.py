import sys
import time

from matplotlib import pyplot as plt

try:
    from userDFS import dfs
except Exception as e:
    print(sys.argv[1], 'ERROR IMPORT')
    sys.exit()


class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)


def dfs_origin(graph: Graph, start: int, visited=None) -> []:
    if visited is None:
        visited = []
    visited.append(start)

    for neighbor in graph.graph.get(start, []):
        if neighbor not in visited:
            dfs_origin(graph, neighbor, visited)

    return visited


def generate_border_graph(n):
    border_graph = Graph()

    for i in range(n):
        for j in range(n):
            if i == 0 or i == n - 1 or j == 0 or j == n - 1:
                border_graph.add_edge(i, j)

    return border_graph


if __name__ == '__main__':
    x = []
    t1 = []
    t2 = []
    #i = 0
    for testNumber in range(0, 16):
        #i += 1
        #print(i)
        graphLenNode = 2 ** testNumber
        #print(graphLenNode)
        x.append(graphLenNode)
        graph = generate_border_graph(graphLenNode)

        start = time.time()
        # #print(graph.graph)
        dfs_origin(graph, 0)
        #print('origin: ', float((time.time() - start)))
        t1.append(float(time.time() - start))

        start = time.time()
        dfs(graph, 0)
        #print('DFS: ', time.time() - start)
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
    plt.title('DFS Algorithm')
    #plt.show()
    plt.savefig('chart.png')
