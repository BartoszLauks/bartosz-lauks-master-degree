import copy
import random
import resource
import signal
import sys

try:
    from userJohnson import johnson
except Exception as e:
    print(sys.argv[1], "ERROR IMPORT")
    sys.exit()


def time_exceeded(signo, frame):
    print(sys.argv[1], 'ERROR TIME OUT')
    sys.exit(1)


def set_max_runtime(seconds):
    soft, hard = resource.getrlimit(resource.RLIMIT_CPU)
    resource.setrlimit(resource.RLIMIT_CPU, (seconds, hard))
    signal.signal(signal.SIGXCPU, time_exceeded)


class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v, weight):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append((v, weight))


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
    set_max_runtime(10)
    print(sys.argv[1], 'START MAIN TEST')
    print('BRUTE FORCE TEST UNIT')
    for testNumber in range(1, 16):
        print("CASE :", testNumber)
        graph = generate_random_graph(5 * testNumber, 0, testNumber * 5)
        print(graph.graph)
        #graph2 = copy.deepcopy(graph)
        originResult = johnson_origin(graph)
        try:
            userResult = johnson(graph)
            print(originResult)
            print(userResult)
            if originResult != userResult:
                print(sys.argv[1], 'ERROR ALGORITHM RESULT')
                sys.exit()
        except Exception as e:
            print(sys.argv[1], 'ERROR USER IMPLEMENTATION', e)
            sys.exit()
    print(sys.argv[1], 'FINISH MAIN TEST')