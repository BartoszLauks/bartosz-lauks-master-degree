import random
import resource
import signal
import sys

try:
    from userKruskal import kruskal
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
    set_max_runtime(3)
    print(sys.argv[1], 'START MAIN TEST')
    print('BRUTE FORCE TEST UNIT')
    for testNumber in range(1, 21):
        print('CASE :', testNumber)
        graph = generate_random_graph(testNumber * 2, testNumber * 10)
        print(graph.graph)
        originResult = kruskal_origin(graph)
        try:
            userResult = kruskal(graph)
            print(originResult)
            print(userResult)
            if originResult != userResult:
                print(sys.argv[1], 'ERROR ALGORITHM RESULT')
                sys.exit()
        except Exception as e:
            print(sys.argv[1], 'ERROR USER IMPLEMENTATION', e)
            sys.exit()
    print(sys.argv[1], 'FINISH MAIN TEST')
