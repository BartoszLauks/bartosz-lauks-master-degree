import resource
import signal
import sys
import tracemalloc

from userJohnson import johnson


def time_exceeded(signo, frame):
    print(sys.argv[1], 'ERROR TIME OUT')
    sys.exit(1)


def set_max_runtime(seconds):
    soft, hard = resource.getrlimit(resource.RLIMIT_CPU)
    resource.setrlimit(resource.RLIMIT_CPU, (seconds, hard))
    signal.signal(signal.SIGXCPU, time_exceeded)


class Graph:
    def __init__(self):
        self.graph = {
            1: [(2, 25), (3, 13), (4, 8), (5, 14), (6, 3), (7, 0), (8, 10), (9, 22), (10, 25), (11, 13), (12, 12),
                (13, 18), (14, 15), (15, 1), (16, 18), (17, 20), (18, 21), (19, 11), (20, 16), (21, 20), (22, 8),
                (23, 7), (24, 15), (25, 9)],
            2: [(1, 3), (3, 16), (4, 10), (5, 1), (6, 23), (7, 16), (8, 8), (9, 1), (10, 23), (11, 23), (12, 21),
                (13, 4), (14, 18), (15, 17), (16, 10), (17, 22), (18, 2), (19, 2), (20, 4), (21, 1), (22, 2), (23, 10),
                (24, 11), (25, 12)],
            3: [(1, 7), (2, 21), (4, 24), (5, 24), (6, 12), (7, 8), (8, 18), (9, 21), (10, 2), (11, 8), (12, 12),
                (13, 10), (14, 22), (15, 15), (16, 18), (17, 18), (18, 10), (19, 13), (20, 8), (21, 16), (22, 13),
                (23, 13), (24, 24), (25, 1)],
            4: [(1, 1), (2, 18), (3, 16), (5, 13), (6, 6), (7, 25), (8, 6), (9, 0), (10, 13), (11, 6), (12, 7),
                (13, 25), (14, 23), (15, 4), (16, 11), (17, 7), (18, 11), (19, 23), (20, 3), (21, 11), (22, 15),
                (23, 8), (24, 7), (25, 18)],
            5: [(1, 18), (2, 20), (3, 3), (4, 3), (6, 9), (7, 0), (8, 20), (9, 22), (10, 20), (11, 21), (12, 19),
                (13, 14), (14, 7), (15, 13), (16, 25), (17, 22), (18, 16), (19, 21), (20, 13), (21, 21), (22, 8),
                (23, 15), (24, 6), (25, 20)],
            6: [(1, 19), (2, 17), (3, 24), (4, 16), (5, 20), (7, 14), (8, 15), (9, 6), (10, 23), (11, 12), (12, 21),
                (13, 5), (14, 11), (15, 13), (16, 25), (17, 14), (18, 15), (19, 24), (20, 8), (21, 5), (22, 16),
                (23, 25), (24, 0), (25, 15)],
            7: [(1, 21), (2, 23), (3, 2), (4, 11), (5, 0), (6, 8), (8, 25), (9, 5), (10, 0), (11, 1), (12, 13),
                (13, 18), (14, 5), (15, 5), (16, 24), (17, 10), (18, 15), (19, 13), (20, 2), (21, 14), (22, 18),
                (23, 7), (24, 5), (25, 2)],
            8: [(1, 15), (2, 10), (3, 23), (4, 3), (5, 21), (6, 17), (7, 1), (9, 13), (10, 16), (11, 12), (12, 6),
                (13, 25), (14, 17), (15, 10), (16, 1), (17, 14), (18, 18), (19, 10), (20, 18), (21, 3), (22, 25),
                (23, 7), (24, 0), (25, 20)],
            9: [(1, 19), (2, 5), (3, 25), (4, 15), (5, 12), (6, 6), (7, 4), (8, 23), (10, 2), (11, 19), (12, 12),
                (13, 10), (14, 11), (15, 25), (16, 12), (17, 11), (18, 18), (19, 21), (20, 24), (21, 23), (22, 16),
                (23, 25), (24, 13), (25, 1)],
            10: [(1, 16), (2, 9), (3, 6), (4, 24), (5, 13), (6, 21), (7, 0), (8, 3), (9, 24), (11, 16), (12, 1),
                 (13, 6), (14, 19), (15, 2), (16, 22), (17, 3), (18, 18), (19, 23), (20, 8), (21, 11), (22, 17),
                 (23, 21), (24, 16), (25, 5)],
            11: [(1, 15), (2, 18), (3, 24), (4, 19), (5, 16), (6, 15), (7, 0), (8, 12), (9, 0), (10, 23), (12, 5),
                 (13, 22), (14, 0), (15, 4), (16, 15), (17, 21), (18, 14), (19, 16), (20, 22), (21, 3), (22, 23),
                 (23, 15), (24, 3), (25, 4)],
            12: [(1, 24), (2, 22), (3, 24), (4, 24), (5, 3), (6, 16), (7, 25), (8, 4), (9, 16), (10, 18), (11, 1),
                 (13, 6), (14, 13), (15, 7), (16, 20), (17, 4), (18, 10), (19, 23), (20, 19), (21, 2), (22, 6),
                 (23, 18), (24, 14), (25, 25)],
            13: [(1, 21), (2, 9), (3, 10), (4, 19), (5, 25), (6, 14), (7, 16), (8, 7), (9, 1), (10, 1), (11, 0),
                 (12, 20), (14, 18), (15, 20), (16, 20), (17, 2), (18, 18), (19, 17), (20, 19), (21, 4), (22, 22),
                 (23, 8), (24, 12), (25, 10)],
            14: [(1, 21), (2, 17), (3, 8), (4, 13), (5, 21), (6, 13), (7, 1), (8, 25), (9, 16), (10, 4), (11, 24),
                 (12, 8), (13, 19), (15, 14), (16, 20), (17, 17), (18, 2), (19, 20), (20, 8), (21, 15), (22, 8),
                 (23, 19), (24, 0), (25, 20)],
            15: [(1, 4), (2, 11), (3, 18), (4, 8), (5, 5), (6, 25), (7, 13), (8, 16), (9, 0), (10, 11), (11, 22),
                 (12, 9), (13, 3), (14, 2), (16, 15), (17, 5), (18, 8), (19, 2), (20, 21), (21, 18), (22, 20), (23, 24),
                 (24, 21), (25, 7)],
            16: [(1, 9), (2, 21), (3, 21), (4, 25), (5, 6), (6, 1), (7, 5), (8, 4), (9, 18), (10, 21), (11, 8),
                 (12, 17), (13, 24), (14, 2), (15, 21), (17, 5), (18, 3), (19, 14), (20, 10), (21, 1), (22, 8), (23, 2),
                 (24, 1), (25, 6)],
            17: [(1, 21), (2, 23), (3, 2), (4, 15), (5, 13), (6, 12), (7, 12), (8, 25), (9, 11), (10, 10), (11, 1),
                 (12, 21), (13, 9), (14, 17), (15, 16), (16, 9), (18, 14), (19, 16), (20, 16), (21, 3), (22, 3),
                 (23, 13), (24, 22), (25, 14)],
            18: [(1, 4), (2, 4), (3, 25), (4, 18), (5, 21), (6, 2), (7, 20), (8, 8), (9, 7), (10, 1), (11, 14),
                 (12, 18), (13, 1), (14, 22), (15, 1), (16, 14), (17, 24), (19, 11), (20, 18), (21, 7), (22, 5),
                 (23, 23), (24, 5), (25, 15)],
            19: [(1, 3), (2, 16), (3, 4), (4, 22), (5, 0), (6, 21), (7, 0), (8, 12), (9, 10), (10, 3), (11, 13),
                 (12, 10), (13, 19), (14, 3), (15, 12), (16, 17), (17, 8), (18, 20), (20, 14), (21, 13), (22, 16),
                 (23, 2), (24, 15), (25, 13)],
            20: [(1, 24), (2, 12), (3, 8), (4, 10), (5, 19), (6, 5), (7, 16), (8, 23), (9, 13), (10, 10), (11, 3),
                 (12, 2), (13, 17), (14, 19), (15, 22), (16, 17), (17, 4), (18, 19), (19, 15), (21, 9), (22, 1),
                 (23, 0), (24, 10), (25, 4)],
            21: [(1, 19), (2, 12), (3, 7), (4, 25), (5, 10), (6, 23), (7, 9), (8, 14), (9, 15), (10, 1), (11, 9),
                 (12, 11), (13, 4), (14, 20), (15, 5), (16, 9), (17, 13), (18, 8), (19, 23), (20, 16), (22, 12),
                 (23, 18), (24, 7), (25, 4)],
            22: [(1, 21), (2, 24), (3, 14), (4, 24), (5, 7), (6, 17), (7, 22), (8, 4), (9, 11), (10, 24), (11, 21),
                 (12, 12), (13, 0), (14, 22), (15, 20), (16, 9), (17, 19), (18, 1), (19, 0), (20, 18), (21, 0),
                 (23, 23), (24, 18), (25, 23)],
            23: [(1, 3), (2, 17), (3, 12), (4, 23), (5, 11), (6, 25), (7, 22), (8, 0), (9, 23), (10, 18), (11, 4),
                 (12, 3), (13, 16), (14, 16), (15, 16), (16, 24), (17, 23), (18, 7), (19, 11), (20, 9), (21, 19),
                 (22, 23), (24, 8), (25, 12)],
            24: [(1, 24), (2, 0), (3, 23), (4, 14), (5, 22), (6, 9), (7, 0), (8, 3), (9, 21), (10, 8), (11, 3),
                 (12, 11), (13, 25), (14, 20), (15, 23), (16, 11), (17, 9), (18, 9), (19, 3), (20, 19), (21, 20),
                 (22, 15), (23, 14), (25, 24)],
            25: [(1, 24), (2, 15), (3, 23), (4, 7), (5, 10), (6, 0), (7, 1), (8, 23), (9, 15), (10, 21), (11, 0),
                 (12, 15), (13, 22), (14, 2), (15, 19), (16, 18), (17, 14), (18, 17), (19, 3), (20, 13), (21, 12),
                 (22, 10), (23, 3), (24, 10)]}


if __name__ == '__main__':
    set_max_runtime(3)
    print(sys.argv[1], 'START COMPUTATIONAL COMPLEXITY TEST')
    PEEK_MEMORY = 42040
    graph = Graph()
    tracemalloc.start()
    johnson(graph)
    peekTracedMemory = int(tracemalloc.get_traced_memory()[1])
    tracemalloc.stop()

    print(sys.argv[1], 'PEEK MEMORY USAGE BY YOUR IMPLEMENTATION:', peekTracedMemory)
    if peekTracedMemory < (PEEK_MEMORY * 2):
        print(sys.argv[1], 'FINISH COMPUTATIONAL COMPLEXITY TEST')
    else:
        print(sys.argv[1], 'ERROR')
        print('MEMORY LIMIT EXCEEDED')
