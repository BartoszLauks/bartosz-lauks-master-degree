import heapq
import random
import resource
import signal
import sys

try:
    from userDijkstra import dijkstra
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

    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []

    def add_edge(self, source, destination, weight):
        self.add_vertex(source)
        self.add_vertex(destination)
        self.graph[source].append((destination, weight))
        self.graph[destination].append((source, weight))


def dijkstra_origin(graph: Graph, start):
    min_heap = [(0, start)]
    visited = set()

    distances = {vertex: float('infinity') for vertex in graph.graph}
    distances[start] = 0

    while min_heap:
        current_distance, current_vertex = heapq.heappop(min_heap)

        if current_vertex in visited:
            continue

        visited.add(current_vertex)

        for neighbor, weight in graph.graph[current_vertex]:
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(min_heap, (distance, neighbor))

    return distances


def generate_random_graph(size: int, max_weight: int) -> Graph:
    graph = Graph()

    for i in range(size):
        graph.add_vertex(i)

    for i in range(size):
        for j in range(i + 1, size):
            weight = random.randint(1, max_weight)
            graph.add_edge(i, j, weight)

    return graph


if __name__ == '__main__':
    set_max_runtime(2)
    print(sys.argv[1], 'START MAIN TEST')
    print('BRUTE FORCE TEST UNIT')
    for testNumber in range(1, 31):
        print("CASE :", testNumber)
        graph = generate_random_graph(2 * testNumber, testNumber)

        start_vertex = random.randint(0, 100 * testNumber - 1)
        print(graph.graph)
        originResult = dijkstra_origin(graph, 0)
        try:
            userResult = dijkstra(graph, 0)
            print(originResult)
            print(userResult)
            if originResult != userResult:
                print(sys.argv[1], 'ERROR ALGORITHM RESULT')
                sys.exit()
        except Exception as e:
            print(sys.argv[1], 'ERROR USER IMPLEMENTATION', e)
            sys.exit()
    print(sys.argv[1], 'FINISH MAIN TEST')
