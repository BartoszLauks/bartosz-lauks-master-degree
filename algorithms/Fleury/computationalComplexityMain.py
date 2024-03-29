import resource
import signal
import sys
import tracemalloc

from userFleury import fleury


def time_exceeded(signo, frame):
    print(sys.argv[1], 'ERROR TIME OUT')
    sys.exit(1)


def set_max_runtime(seconds):
    soft, hard = resource.getrlimit(resource.RLIMIT_CPU)
    resource.setrlimit(resource.RLIMIT_CPU, (seconds, hard))
    signal.signal(signal.SIGXCPU, time_exceeded)


class Graph:
    def __init__(self):
        self.graph = {6: [3, 7, 5, 4], 3: [6, 7, 9, 0], 7: [3, 6, 1, 5], 2: [0, 9], 0: [2, 3], 9: [2, 3], 5: [6, 7],
                      4: [6], 1: [7]}


if __name__ == '__main__':
    if len(sys.argv) < 4:
        print(sys.argv[1], 'ERROR NO PARAMETERS IN THE CALL')
        sys.exit()
    set_max_runtime(int(sys.argv[2]))
    print(sys.argv[1], 'START COMPUTATIONAL COMPLEXITY TEST')
    PEEK_MEMORY = int(sys.argv[3])
    graph = Graph()
    tracemalloc.start()
    fleury(graph)
    peekTracedMemory = int(tracemalloc.get_traced_memory()[1])
    tracemalloc.stop()

    print(sys.argv[1], 'PEEK MEMORY USAGE BY YOUR IMPLEMENTATION:', peekTracedMemory)
    if peekTracedMemory < (PEEK_MEMORY * 2):
        print(sys.argv[1], 'FINISH COMPUTATIONAL COMPLEXITY TEST')
    else:
        pprint(sys.argv[1], 'ERROR MEMORY LIMIT EXCEEDED')