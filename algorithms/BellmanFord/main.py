import random
import resource
import signal
import sys

try:
    from userBellmanFord import bellman_ford
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

    def add_edge(self, source, destination, weight):
        if source not in self.graph:
            self.graph[source] = []
        self.graph[source].append((destination, weight))


def bellman_ford_origin(graph: Graph, start_vertex: int) -> {}:
    # Step 1: Initialize distances
    distances = {vertex: float('infinity') for vertex in graph.graph}
    distances[start_vertex] = 0

    # Step 2: Relax edges repeatedly
    for _ in range(len(graph.graph) - 1):
        for current_vertex in graph.graph:
            if current_vertex in distances:
                for neighbor, weight in graph.graph[current_vertex]:
                    if distances[current_vertex] + weight < distances.get(neighbor, float('infinity')):
                        distances[neighbor] = distances[current_vertex] + weight

    # Step 3: Check for negative cycles
    for current_vertex in graph.graph:
        if current_vertex in distances:
            for neighbor, weight in graph.graph[current_vertex]:
                if distances[current_vertex] + weight < distances[neighbor]:
                    return {}

    return distances


def generate_random_graph(size, min_weight, max_weight):
    graph = Graph()
    vertices = list(range(1, size + 1))

    for u in vertices:
        for v in vertices:
            if u != v:
                weight = random.randint(min_weight, max_weight)
                graph.add_edge(u, v, weight)

    return graph


# Example usage:
if __name__ == '__main__':
    set_max_runtime(10)
    print(sys.argv[1], 'START MAIN TEST')
    print('BRUTE FORCE TEST UNIT')
    for testNumber in range(1, 21):
        print('CASE :', testNumber)
        graph = generate_random_graph(5 * testNumber, testNumber * 5, testNumber * 5)
        #print(graph.graph)
        originResult = bellman_ford_origin(graph, list(graph.graph.keys())[0])
        try:
            userResult = bellman_ford(graph, list(graph.graph.keys())[0])
            print(originResult)
            print(userResult)
            if originResult != userResult:
                print(sys.argv[1], 'ERROR ALGORITHM RESULT')
                sys.exit()
        except Exception as e:
            print(sys.argv[1], 'ERROR USER IMPLEMENTATION', e)
            sys.exit()
    print(sys.argv[1], 'FINISH MAIN TEST')
