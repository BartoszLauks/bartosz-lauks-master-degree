import random
import sys
import time

from matplotlib import pyplot as plt

try:
    from userJohnson import johnson
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


def remove_inf_origin(dict):
    for key, value in list(dict.items()):
        if isinstance(value, dict):
            remove_inf_origin(value)
        elif value == float('inf'):
            del dict[key]


def bellman_ford_origin(graph: Graph, source):
    distance = {node: float('inf') for node in graph.graph}
    distance[source] = 0

    for node in graph.graph:
        if node != source and node not in distance:
            distance[node] = float('inf')

    for _ in range(len(graph.graph) - 1):
        for node in graph.graph:
            if distance[node] == float('inf'):
                continue
            for neighbor, weight in graph.graph.get(node, []):
                if distance[node] + weight < distance.get(neighbor, float('inf')):
                    distance[neighbor] = distance[node] + weight

    return distance


def reweight_edges_origin(graph: Graph, distances):
    for u in graph.graph:
        for i, (v, weight) in enumerate(graph.graph[u]):
            graph.graph[u][i] = (v, weight + distances[u] - distances[v])


def dijkstra_origin(graph: Graph, source, distances):
    distance = {node: float('inf') for node in graph.graph}
    distance[source] = 0
    visited = set()

    while len(visited) < len(graph.graph):
        current_node = min((node for node in graph.graph if node not in visited), key=lambda x: distance[x])
        visited.add(current_node)

        for neighbor, weight in graph.graph.get(current_node, []):
            if distance[current_node] + weight < distance.get(neighbor, float('inf')):
                distance[neighbor] = distance[current_node] + weight
    distance = {node: dist - distances[source] + distances[node] for node, dist in distance.items()}

    return distance


def johnson_origin(graph: Graph):
    new_node = 'NEW_NODE'
    graph.graph[new_node] = [(node, 0) for node in graph.graph]

    distances = bellman_ford_origin(graph, new_node)

    if any(distances[node] == float('inf') for node in distances):
        return None

    reweight_edges_origin(graph, distances)

    del graph.graph[new_node]

    shortest_paths = {}
    for node in graph.graph:
        shortest_paths[node] = dijkstra_origin(graph, node, distances)

    # remove_inf_origin(shortest_paths)

    if shortest_paths is None:
        return {}

    return shortest_paths


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
    i = 0
    for testNumber in range(1, 20):
        i += 1
        #print(i)
        graphLenNode = testNumber ** 2 + 1
        #print(graphLenNode)
        x.append(graphLenNode)
        graph = generate_random_graph(graphLenNode, 0, graphLenNode)

        start = time.time()
        # #print(graph.graph)
        johnson_origin(graph)
        #print('origin: ', float((time.time() - start)))
        t1.append(float(time.time() - start))

        start = time.time()
        johnson(graph)
        #print('Johnson: ', time.time() - start)
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
    plt.title('Johnson Algorithm')
    #plt.show()
    plt.savefig('chart.png')
