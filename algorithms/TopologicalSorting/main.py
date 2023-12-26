import random
import resource
import signal
import sys

try:
    from userTopologicalSorting import topological_sort
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


if __name__ == '__main__':
    set_max_runtime(2)
    print(sys.argv[1], 'START MAIN TEST')
    print('BRUTE FORCE TEST UNIT')
    for testNumber in range(1, 51):
        print('CASE :', testNumber)
        graphLenNode = testNumber * 10
        graph = Graph()

        for createGraph in range(1, graphLenNode):
            graph.add_edge(random.randint(0, 10 * testNumber), random.randint(0, 10 * testNumber))

        print(graph.graph)
        originResult = topological_sort_original(graph)
        try:
            userResult = topological_sort(graph)
            print(originResult)
            print(userResult)
            if originResult != userResult:
                print(sys.argv[1], 'ERROR ALGORITHM RESULT')
                sys.exit()
        except Exception as e:
            print(sys.argv[1], 'ERROR USER IMPLEMENTATION', e)
            sys.exit()
    print(sys.argv[1], 'FINISH MAIN TEST')
