import copy
import random
import resource
import signal
import sys

try:
    from userFleury import fleury
except Exception as e:
    print(sys.argv[1], 'ERROR IMPORT')
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

    def add_edge(self, u, v):
        self.graph.setdefault(u, []).append(v)
        self.graph.setdefault(v, []).append(u)


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


def generate_random_graph(num_vertices: int, num_edges: int):
    graph = Graph()

    for _ in range(num_edges):
        u = random.randint(0, num_vertices - 1)
        v = random.randint(0, num_vertices - 1)
        graph.add_edge(u, v)

    return graph


if __name__ == '__main__':
    set_max_runtime(10)
    print(sys.argv[1], 'START MAIN TEST')
    print('BRUTE FORCE TEST UNIT')
    for testNumber in range(1, 21):
        print('CASE :', testNumber)
        graph = generate_random_graph(testNumber, testNumber)
        graph2 = copy.deepcopy(graph)
        print(graph.graph)
        try:
            originResult = fleury_origin(graph)
        except Exception as e:
            continue
        try:
            userResult = fleury(graph2)
            print(originResult)
            print(userResult)
            if originResult != userResult:
                print(sys.argv[1], 'ERROR ALGORITHM RESULT')
                sys.exit()
        except Exception as e:
            print(sys.argv[1], 'ERROR USER IMPLEMENTATION', e)
            sys.exit()
    print(sys.argv[1], 'FINISH MAIN TEST')