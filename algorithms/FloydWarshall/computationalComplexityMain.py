import resource
import signal
import sys
import tracemalloc

from userFloydWarshall import floyd_warshall


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
            0: {1: -11, 2: -26, 3: -39, 4: -26, 5: 21, 6: -38, 7: 22, 8: -16, 9: 42, 10: -12, 11: -17, 12: 1, 13: 29,
                14: 4, 15: -33, 16: 18, 17: -7, 18: -8, 19: -9, 20: -27, 21: 44, 22: 24, 23: 4, 24: -7, 25: 28, 26: -8,
                27: 37, 28: 6, 29: 46, 30: -44, 31: 33, 32: -37, 33: 44, 34: 48, 35: 29, 36: 1, 37: 47, 38: 10, 39: -43,
                40: 41, 41: -31, 42: -45, 43: 40, 44: 47, 45: 48, 46: -15, 47: -19, 48: 18, 49: -18},
            1: {2: 41, 3: 32, 4: -14, 5: 36, 6: 7, 7: 26, 8: -10, 9: -33, 10: 33, 11: -10, 12: 12, 13: -43, 14: -39,
                15: -28, 16: 20, 17: -31, 18: -14, 19: -42, 20: 31, 21: -10, 22: -45, 23: -23, 24: 48, 25: 10, 26: 48,
                27: 6, 28: 24, 29: 18, 30: -41, 31: -11, 32: -19, 33: 46, 34: -7, 35: 46, 36: -30, 37: 26, 38: -16,
                39: -30, 40: -46, 41: 3, 42: -42, 43: 34, 44: 11, 45: -50, 46: 22, 47: 46, 48: 22, 49: 50},
            2: {3: -35, 4: 40, 5: 28, 6: -13, 7: -18, 8: -49, 9: 9, 10: 18, 11: -26, 12: -27, 13: 26, 14: 50, 15: -22,
                16: 0, 17: -2, 18: 13, 19: -5, 20: -41, 21: 50, 22: -11, 23: -12, 24: -45, 25: 24, 26: -25, 27: 48,
                28: 38, 29: -7, 30: 8, 31: -50, 32: -13, 33: -19, 34: 34, 35: -6, 36: 25, 37: -1, 38: -10, 39: -40,
                40: 24, 41: 25, 42: 39, 43: -30, 44: 5, 45: 28, 46: -34, 47: 21, 48: -40, 49: 22},
            3: {4: 39, 5: 43, 6: -11, 7: -31, 8: -37, 9: 38, 10: -37, 11: 34, 12: -48, 13: 18, 14: 10, 15: -29, 16: 32,
                17: -11, 18: 5, 19: -6, 20: -13, 21: 9, 22: -46, 23: -30, 24: 24, 25: -36, 26: -47, 27: -32, 28: 7,
                29: -15, 30: -15, 31: -34, 32: -49, 33: 37, 34: -47, 35: -12, 36: -14, 37: -7, 38: -32, 39: 19, 40: 5,
                41: 19, 42: -44, 43: -13, 44: 25, 45: 7, 46: 13, 47: 22, 48: -8, 49: 25},
            4: {5: 38, 6: -50, 7: -21, 8: -25, 9: -19, 10: -40, 11: 15, 12: -32, 13: -26, 14: -21, 15: -23, 16: 20,
                17: -12, 18: -1, 19: -15, 20: 45, 21: 27, 22: 8, 23: 19, 24: 38, 25: -27, 26: -11, 27: -4, 28: -49,
                29: 31, 30: 46, 31: -36, 32: 18, 33: -44, 34: -13, 35: -44, 36: 49, 37: -49, 38: 36, 39: 7, 40: -39,
                41: -6, 42: 28, 43: 23, 44: 37, 45: -25, 46: -20, 47: -7, 48: -1, 49: -41},
            5: {6: 17, 7: 32, 8: -23, 9: 35, 10: 17, 11: 27, 12: 20, 13: 28, 14: 10, 15: 22, 16: -46, 17: 27, 18: -19,
                19: -13, 20: -48, 21: -41, 22: 1, 23: -36, 24: 40, 25: 37, 26: -45, 27: -24, 28: 19, 29: 22, 30: 19,
                31: 37, 32: -35, 33: -10, 34: 12, 35: -30, 36: 20, 37: 4, 38: -33, 39: 33, 40: -36, 41: -5, 42: -2,
                43: 50, 44: 15, 45: 44, 46: 10, 47: 10, 48: -44, 49: -27},
            6: {7: 26, 8: -35, 9: 13, 10: 28, 11: 35, 12: 14, 13: -8, 14: 9, 15: 0, 16: 10, 17: 29, 18: -34, 19: 46,
                20: 28, 21: -31, 22: 19, 23: 28, 24: 12, 25: -20, 26: -31, 27: -2, 28: 49, 29: 22, 30: -35, 31: 23,
                32: 39, 33: 33, 34: 4, 35: -8, 36: 27, 37: 50, 38: -44, 39: -28, 40: -28, 41: -36, 42: -31, 43: 37,
                44: -32, 45: 35, 46: -13, 47: -48, 48: 44, 49: 44},
            7: {8: 3, 9: 40, 10: -4, 11: -40, 12: -41, 13: -24, 14: 14, 15: 17, 16: 47, 17: 14, 18: 50, 19: 23, 20: 17,
                21: 2, 22: -34, 23: -2, 24: -11, 25: -39, 26: -25, 27: 8, 28: -24, 29: 7, 30: -48, 31: 24, 32: 5,
                33: 33, 34: -45, 35: -34, 36: 6, 37: 13, 38: 37, 39: -14, 40: -11, 41: -15, 42: 46, 43: 10, 44: 44,
                45: 34, 46: 45, 47: -12, 48: -33, 49: 11},
            8: {9: -47, 10: -2, 11: 15, 12: -15, 13: 33, 14: 31, 15: 30, 16: -45, 17: -29, 18: -8, 19: 44, 20: -27,
                21: -23, 22: -50, 23: 38, 24: 44, 25: 5, 26: -49, 27: 32, 28: 29, 29: -7, 30: -38, 31: 23, 32: 30,
                33: -10, 34: -33, 35: 49, 36: -38, 37: 3, 38: -10, 39: 38, 40: 40, 41: 4, 42: 28, 43: 43, 44: 48,
                45: -30, 46: -8, 47: -47, 48: 2, 49: -16},
            9: {10: 6, 11: 41, 12: 1, 13: 17, 14: -20, 15: -35, 16: 2, 17: 49, 18: -48, 19: -3, 20: -15, 21: 34,
                22: -49, 23: 16, 24: -33, 25: 25, 26: 32, 27: 16, 28: -28, 29: 31, 30: -31, 31: -5, 32: 5, 33: 12,
                34: -24, 35: 35, 36: -38, 37: 34, 38: 4, 39: 28, 40: 35, 41: 47, 42: 16, 43: 12, 44: -17, 45: 34,
                46: 24, 47: 35, 48: -25, 49: 34},
            10: {11: 27, 12: 31, 13: 46, 14: -31, 15: 10, 16: 46, 17: -13, 18: 45, 19: 0, 20: -4, 21: 33, 22: 11,
                 23: -4, 24: 30, 25: -50, 26: 19, 27: -9, 28: 6, 29: -15, 30: -14, 31: -33, 32: -2, 33: -38, 34: -25,
                 35: 32, 36: 40, 37: -21, 38: -2, 39: -11, 40: 50, 41: 22, 42: -46, 43: -25, 44: -26, 45: -17, 46: 36,
                 47: 4, 48: -34, 49: -27},
            11: {12: 40, 13: 24, 14: 3, 15: 35, 16: -23, 17: -35, 18: 33, 19: -3, 20: -18, 21: 45, 22: 0, 23: 19,
                 24: 19, 25: -24, 26: 24, 27: 14, 28: -3, 29: 43, 30: 16, 31: 16, 32: 27, 33: 46, 34: 2, 35: -49,
                 36: -17, 37: -32, 38: -9, 39: -46, 40: 21, 41: -29, 42: 7, 43: -34, 44: 14, 45: -34, 46: 48, 47: 39,
                 48: 50, 49: 6},
            12: {13: 49, 14: 50, 15: 0, 16: 18, 17: 19, 18: -19, 19: 5, 20: 7, 21: -39, 22: -5, 23: -31, 24: -21,
                 25: -45, 26: 38, 27: 18, 28: -34, 29: 33, 30: 6, 31: -11, 32: -48, 33: 10, 34: 4, 35: -36, 36: -31,
                 37: -4, 38: -40, 39: 17, 40: 1, 41: -42, 42: 42, 43: 34, 44: 38, 45: 2, 46: 34, 47: -39, 48: -48,
                 49: 7},
            13: {14: -28, 15: 0, 16: -6, 17: -50, 18: 26, 19: 4, 20: 24, 21: 25, 22: -14, 23: -15, 24: 20, 25: 18,
                 26: 23, 27: 31, 28: 0, 29: 45, 30: 38, 31: -20, 32: 36, 33: 39, 34: 47, 35: -17, 36: -34, 37: 35,
                 38: 44, 39: -7, 40: -40, 41: -19, 42: -35, 43: 25, 44: -50, 45: -40, 46: -40, 47: -42, 48: -50, 49: 3},
            14: {15: 27, 16: -36, 17: 11, 18: -49, 19: -30, 20: -32, 21: 32, 22: -12, 23: 46, 24: 27, 25: 21, 26: -44,
                 27: 46, 28: 46, 29: -2, 30: -34, 31: 13, 32: 10, 33: -15, 34: -34, 35: 50, 36: -29, 37: 18, 38: 24,
                 39: -44, 40: -19, 41: -18, 42: 22, 43: 21, 44: 41, 45: 14, 46: -38, 47: -47, 48: -18, 49: 21},
            15: {16: 50, 17: 47, 18: -28, 19: 48, 20: 37, 21: -40, 22: 1, 23: 37, 24: 9, 25: -3, 26: 28, 27: -45,
                 28: 50, 29: -40, 30: 20, 31: -19, 32: -30, 33: -28, 34: 22, 35: -18, 36: 2, 37: 6, 38: 26, 39: -18,
                 40: -4, 41: 8, 42: 26, 43: -6, 44: -27, 45: 34, 46: -29, 47: 46, 48: -10, 49: -40},
            16: {17: -38, 18: -46, 19: -37, 20: 9, 21: -31, 22: 36, 23: -38, 24: 26, 25: -22, 26: 46, 27: 29, 28: 37,
                 29: 14, 30: 28, 31: 5, 32: 2, 33: -17, 34: 49, 35: 37, 36: -46, 37: -4, 38: 31, 39: -17, 40: 14,
                 41: 46, 42: -9, 43: -5, 44: -48, 45: -27, 46: 10, 47: -38, 48: -49, 49: 27},
            17: {18: -44, 19: -50, 20: -3, 21: -32, 22: 30, 23: 41, 24: 1, 25: -2, 26: 0, 27: -17, 28: 6, 29: -20,
                 30: -45, 31: 0, 32: 12, 33: -37, 34: 34, 35: -24, 36: -32, 37: 19, 38: 22, 39: -46, 40: 24, 41: 25,
                 42: 14, 43: 13, 44: 12, 45: -24, 46: -27, 47: 24, 48: 44, 49: 41},
            18: {19: 43, 20: -8, 21: 29, 22: -14, 23: 41, 24: -32, 25: 46, 26: 34, 27: -36, 28: 23, 29: -29, 30: -27,
                 31: -50, 32: -30, 33: -37, 34: -39, 35: -36, 36: 3, 37: -44, 38: 6, 39: -25, 40: -13, 41: -8, 42: 32,
                 43: 36, 44: -47, 45: 31, 46: 43, 47: -40, 48: 4, 49: 23},
            19: {20: 30, 21: 2, 22: -22, 23: 39, 24: -42, 25: 43, 26: 35, 27: 33, 28: 0, 29: 24, 30: 18, 31: -28,
                 32: -42, 33: 35, 34: 12, 35: 42, 36: 22, 37: 50, 38: -8, 39: -23, 40: -21, 41: 5, 42: 3, 43: -23,
                 44: 2, 45: -18, 46: 17, 47: 16, 48: -6, 49: 38},
            20: {21: 47, 22: 23, 23: 33, 24: 28, 25: 38, 26: 17, 27: -16, 28: 11, 29: -22, 30: 3, 31: -49, 32: 12,
                 33: 3, 34: 10, 35: -42, 36: 3, 37: 10, 38: -4, 39: 41, 40: 40, 41: 50, 42: -20, 43: -49, 44: 31,
                 45: -16, 46: 42, 47: 14, 48: -38, 49: 20},
            21: {22: -39, 23: 26, 24: -5, 25: 1, 26: 45, 27: -12, 28: 25, 29: 12, 30: 11, 31: -6, 32: -32, 33: 20,
                 34: -2, 35: 6, 36: -4, 37: -12, 38: 36, 39: -12, 40: 4, 41: 10, 42: -41, 43: -27, 44: -36, 45: -17,
                 46: 48, 47: 49, 48: -24, 49: -8},
            22: {23: 3, 24: 2, 25: 27, 26: 46, 27: 11, 28: 31, 29: 32, 30: 37, 31: -5, 32: -15, 33: -28, 34: 27, 35: 43,
                 36: 27, 37: -40, 38: 44, 39: 18, 40: 33, 41: 40, 42: 42, 43: -40, 44: -22, 45: 4, 46: -15, 47: -38,
                 48: 11, 49: -49},
            23: {24: 17, 25: -32, 26: -43, 27: -48, 28: 20, 29: -42, 30: 41, 31: -24, 32: -17, 33: 32, 34: 32, 35: 4,
                 36: -16, 37: -10, 38: 44, 39: 14, 40: -24, 41: -29, 42: -18, 43: 8, 44: 25, 45: 35, 46: -4, 47: -13,
                 48: -30, 49: -37},
            24: {25: 9, 26: -24, 27: 40, 28: 49, 29: -44, 30: -12, 31: -29, 32: -48, 33: -43, 34: -14, 35: 23, 36: -39,
                 37: 18, 38: 46, 39: 31, 40: 33, 41: 0, 42: -30, 43: 26, 44: 23, 45: 12, 46: -25, 47: 25, 48: -30,
                 49: 18},
            25: {26: -8, 27: 48, 28: -29, 29: -1, 30: 50, 31: 47, 32: -35, 33: -21, 34: -49, 35: -27, 36: 37, 37: -48,
                 38: 9, 39: 39, 40: 38, 41: -18, 42: -24, 43: 6, 44: -39, 45: 11, 46: -15, 47: 22, 48: -23, 49: -14},
            26: {27: -48, 28: -26, 29: 32, 30: 3, 31: 33, 32: -42, 33: -7, 34: 30, 35: -26, 36: 17, 37: -34, 38: -23,
                 39: -1, 40: -4, 41: 1, 42: -14, 43: 17, 44: 20, 45: 10, 46: 17, 47: 28, 48: -16, 49: -26},
            27: {28: -47, 29: -11, 30: 7, 31: 29, 32: -13, 33: -48, 34: -24, 35: 46, 36: -23, 37: -37, 38: -41, 39: -21,
                 40: -19, 41: -40, 42: -7, 43: -5, 44: -5, 45: -12, 46: -15, 47: 42, 48: 30, 49: -19},
            28: {29: -42, 30: 37, 31: -47, 32: -30, 33: 31, 34: -18, 35: 43, 36: 40, 37: 16, 38: 39, 39: 16, 40: -33,
                 41: 36, 42: -37, 43: -15, 44: -17, 45: -28, 46: 47, 47: -43, 48: -49, 49: 49},
            29: {30: -49, 31: -37, 32: 33, 33: -35, 34: -28, 35: -35, 36: 42, 37: -2, 38: 20, 39: -22, 40: 21, 41: -40,
                 42: -37, 43: -23, 44: -15, 45: 32, 46: -29, 47: -48, 48: 15, 49: 13},
            30: {31: -41, 32: -38, 33: -34, 34: -22, 35: -37, 36: -3, 37: 13, 38: -35, 39: 14, 40: 6, 41: 39, 42: 45,
                 43: -28, 44: -28, 45: 22, 46: -18, 47: -23, 48: -47, 49: 25},
            31: {32: -44, 33: 40, 34: 35, 35: -12, 36: 39, 37: 37, 38: -32, 39: -41, 40: -3, 41: 25, 42: 13, 43: 50,
                 44: 30, 45: 14, 46: 2, 47: -30, 48: -37, 49: -15},
            32: {33: -32, 34: -24, 35: 22, 36: -50, 37: -7, 38: -1, 39: 21, 40: -32, 41: 18, 42: 2, 43: 2, 44: 38,
                 45: 6, 46: 26, 47: -42, 48: -26, 49: 48},
            33: {34: 36, 35: 40, 36: -40, 37: -3, 38: 20, 39: 9, 40: -16, 41: 14, 42: -36, 43: -50, 44: 24, 45: 38,
                 46: 26, 47: 27, 48: 30, 49: 10},
            34: {35: -26, 36: 50, 37: -6, 38: 17, 39: -27, 40: -45, 41: 31, 42: -12, 43: -20, 44: 43, 45: 34, 46: -44,
                 47: -22, 48: 9, 49: -25},
            35: {36: -44, 37: 37, 38: -16, 39: -7, 40: 16, 41: 8, 42: -25, 43: -50, 44: 11, 45: -37, 46: 9, 47: -2,
                 48: -31, 49: -22},
            36: {37: 47, 38: -41, 39: -10, 40: 5, 41: 39, 42: -3, 43: 8, 44: 23, 45: 30, 46: -30, 47: 34, 48: -23,
                 49: 8},
            37: {38: -9, 39: -36, 40: 34, 41: -42, 42: -31, 43: -44, 44: -30, 45: -40, 46: 14, 47: -36, 48: -1, 49: 36},
            38: {39: -44, 40: 0, 41: -24, 42: 6, 43: 28, 44: 34, 45: 12, 46: 20, 47: 35, 48: 19, 49: -49},
            39: {40: 37, 41: 38, 42: 27, 43: 11, 44: 16, 45: -39, 46: -49, 47: -21, 48: 3, 49: -17},
            40: {41: 35, 42: -23, 43: -21, 44: -6, 45: -34, 46: -13, 47: -26, 48: -35, 49: -10},
            41: {42: 18, 43: 24, 44: 39, 45: -26, 46: 36, 47: -34, 48: 19, 49: 20},
            42: {43: 48, 44: -12, 45: 26, 46: -1, 47: -28, 48: -43, 49: 47},
            43: {44: -31, 45: -23, 46: 28, 47: 32, 48: -47, 49: 20}, 44: {45: -22, 46: -43, 47: 29, 48: 50, 49: -40},
            45: {46: 34, 47: -38, 48: 32, 49: -32}, 46: {47: 21, 48: 4, 49: -31}, 47: {48: -12, 49: 5}, 48: {49: -4}}


if __name__ == '__main__':
    set_max_runtime(3)
    print(sys.argv[1], 'START COMPUTATIONAL COMPLEXITY TEST')
    PEEK_MEMORY = 4488
    graph = Graph()
    tracemalloc.start()
    floyd_warshall(graph, list(graph.graph.keys())[0])
    peekTracedMemory = int(tracemalloc.get_traced_memory()[1])
    tracemalloc.stop()

    print(sys.argv[1], 'PEEK MEMORY USAGE BY YOUR IMPLEMENTATION:', peekTracedMemory)
    if peekTracedMemory < (PEEK_MEMORY * 2):
        print(sys.argv[1], 'FINISH COMPUTATIONAL COMPLEXITY TEST')
    else:
        print(sys.argv[1], 'ERROR MEMORY LIMIT EXCEEDED')
