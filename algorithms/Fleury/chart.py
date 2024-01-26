import copy
import random
import sys
import time

from matplotlib import pyplot as plt

try:
    from userFleury import fleury
except Exception as e:
    print(sys.argv[1], "ERROR IMPORT")
    sys.exit()

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, source, destination):
        self.graph.setdefault(source, []).append(destination)
        self.graph.setdefault(destination, []).append(source)


def is_bridge_origin(graph, u, v):
    visited = set()
    dfs_stack = [u]
    visited.add(u)

    while dfs_stack:
        current = dfs_stack.pop()
        for neighbor in graph[current]:
            if neighbor == v:
                continue
            if neighbor not in visited:
                dfs_stack.append(neighbor)
                visited.add(neighbor)

    return v not in visited


def fleury_origin(graph):
    odd_degree_nodes = [node for node, neighbors in graph.graph.items() if len(neighbors) % 2 == 1]
    if len(odd_degree_nodes) not in [0, 2]:
        return {}

    current_node = list(graph.graph.keys())[0] if len(odd_degree_nodes) == 0 else odd_degree_nodes[0]
    circuit = []

    while graph.graph:
        neighbors = graph.graph[current_node]

        if not neighbors:
            break

        edge_to_remove = None

        for neighbor in list(neighbors):
            if is_bridge_origin(graph.graph, current_node, neighbor):
                continue

            edge_to_remove = (current_node, neighbor)
            break

        if edge_to_remove is None:
            edge_to_remove = (current_node, neighbors[0])

        graph.graph[edge_to_remove[0]].remove(edge_to_remove[1])
        graph.graph[edge_to_remove[1]].remove(edge_to_remove[0])

        if not graph.graph[current_node]:
            del graph.graph[current_node]

        circuit.append(edge_to_remove)
        current_node = edge_to_remove[1]

    return circuit


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
    i = 0
    for testNumber in range(2, 17):
        i += 1
        #print(i)
        graphLenNode = testNumber ** 2
        #print(graphLenNode)
        # #print(graphLenNode)
        x.append(graphLenNode)
        graph = generate_border_graph(graphLenNode)
        graph2 = copy.deepcopy(graph)

        start = time.time()
        # #print(graph.graph)
        fleury_origin(graph)
        #print('origin: ', float((time.time() - start)))
        t1.append(float(time.time() - start))

        start = time.time()
        fleury(graph2)
        #print('Fleury: ', time.time() - start)
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
    plt.title('Fleury Algorithm')
    #plt.show()
    plt.savefig('chart.png')