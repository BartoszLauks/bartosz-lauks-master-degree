import random
import resource
import signal
import sys

try:
    from userDFS import dfs
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


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print(sys.argv[1], 'ERROR NO PARAMETERS IN THE CALL')
        sys.exit()
    set_max_runtime(int(sys.argv[2]) * 2)
    print(sys.argv[1], 'START MAIN TEST')
    print('BRUTE FORCE TEST UNIT')
    for testNumber in range(1, 501):
        print('CASE :', testNumber)
        graphLenNode = testNumber * 10
        graph = Graph()

        for createGraph in range(1, graphLenNode):
            graph.add_edge(random.randint(0, 100), random.randint(0, 100))

        originResult = dfs_origin(graph, 0)

        try:
            userResult = dfs(graph, 0)
            print(originResult)
            print(userResult)
            if originResult != userResult:
                print(sys.argv[1], 'ERROR ALGORITHM RESULT')
                sys.exit()
        except Exception as e:
            print(sys.argv[1], 'ERROR USER IMPLEMENTATION', e)
            sys.exit()
    print(sys.argv[1], 'FINISH MAIN TEST')
