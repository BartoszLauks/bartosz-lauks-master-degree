import resource
import signal
import sys
import tracemalloc

from userTopologicalSorting import topological_sort

def time_exceeded(signo, frame):
    print(sys.argv[1], 'ERROR TIME OUT')
    sys.exit(1)


def set_max_runtime(seconds):
    soft, hard = resource.getrlimit(resource.RLIMIT_CPU)
    resource.setrlimit(resource.RLIMIT_CPU, (seconds, hard))
    signal.signal(signal.SIGXCPU, time_exceeded)


class Graph:
    def __init__(self):
        self.graph = {340: [155, 148], 155: [], 239: [156, 200], 156: [], 477: [95], 95: [342, 375], 407: [138],
                      138: [390, 331], 423: [97], 97: [], 207: [372, 184], 372: [], 201: [247], 247: [], 444: [185],
                      185: [], 396: [253, 139], 253: [369, 443], 220: [99, 474, 379], 99: [212], 76: [119, 337],
                      119: [404], 373: [313, 48, 447, 137], 313: [], 264: [427, 41], 427: [216, 280, 113],
                      181: [66, 97], 66: [], 262: [216], 216: [], 48: [], 26: [184], 184: [117, 157],
                      237: [459, 310, 296], 459: [], 330: [8, 489], 8: [], 438: [308, 40, 326], 308: [], 306: [427],
                      219: [367, 267], 367: [483, 400, 447], 452: [487, 375], 487: [378], 5: [45], 45: [],
                      21: [417, 220, 52, 114], 417: [401, 231], 447: [76], 356: [327, 284], 327: [],
                      353: [447, 143, 167], 196: [19, 298, 483], 19: [476], 284: [95], 281: [290, 113], 290: [295],
                      299: [61], 61: [], 74: [235, 187, 392], 235: [30, 184], 395: [107, 465, 96], 107: [50], 0: [486],
                      486: [], 12: [303], 303: [], 215: [268, 208], 268: [266, 240], 226: [175], 175: [], 191: [434],
                      434: [41], 200: [137], 32: [286, 184], 286: [], 1: [2], 2: [340], 52: [147, 159], 147: [268, 368],
                      117: [244, 89], 139: [37, 269, 404, 6], 37: [], 331: [211, 175], 211: [375], 289: [134, 270, 322],
                      134: [], 114: [353, 124, 76], 241: [96], 96: [392, 498, 86], 198: [219], 58: [215],
                      40: [498, 47, 46], 252: [206, 252], 206: [], 384: [415], 415: [], 182: [44], 44: [125, 191, 403],
                      455: [495, 229], 495: [], 267: [217], 217: [294], 180: [403, 315], 403: [125, 350],
                      71: [285, 373], 285: [206, 164, 7], 333: [64, 127], 64: [311], 271: [313, 434],
                      38: [172, 430, 225, 65], 172: [], 276: [293], 293: [114], 92: [42], 42: [192, 183, 126, 477],
                      125: [], 314: [311, 438, 135, 217], 311: [12, 472, 66], 104: [256, 368], 256: [],
                      67: [298, 45, 303], 298: [284], 169: [344, 287], 344: [95, 231, 199, 298], 33: [444, 500],
                      392: [385, 339], 385: [414, 463], 102: [252, 65], 440: [178], 178: [1], 362: [186], 186: [],
                      460: [231], 231: [148], 171: [222], 222: [495, 112, 51], 454: [1, 496, 194], 270: [], 498: [],
                      348: [280, 196], 280: [], 41: [174], 174: [384], 428: [7, 1, 41], 7: [195, 422], 291: [402],
                      402: [], 475: [437], 437: [271, 105, 288], 364: [427, 282, 37, 305], 414: [444], 418: [10],
                      10: [84], 282: [], 433: [421], 421: [], 347: [54, 74, 482], 54: [444, 462, 210], 398: [61],
                      187: [204], 204: [203], 380: [16, 78, 205], 16: [], 449: [156], 326: [400, 376], 497: [190, 190],
                      190: [267], 370: [485], 485: [], 422: [453, 14], 453: [328, 304], 245: [394], 394: [], 78: [414],
                      250: [441, 26], 441: [82, 82], 124: [], 404: [318, 353], 318: [], 397: [413, 383], 413: [],
                      47: [], 322: [], 195: [], 476: [470, 417], 470: [239], 212: [], 62: [118], 118: [210, 40, 419],
                      260: [448, 458, 275], 448: [310, 70], 193: [223], 223: [70], 6: [449, 44], 203: [], 4: [243],
                      243: [2], 375: [246, 184], 197: [168], 168: [426], 368: [490], 490: [85, 397], 93: [475, 166, 25],
                      323: [426], 426: [7], 157: [], 483: [], 381: [253, 292], 458: [69], 69: [], 192: [212],
                      269: [74, 333], 98: [156, 431, 369], 35: [68, 97], 68: [342], 310: [33], 439: [100, 286], 100: [],
                      390: [258, 272], 258: [], 22: [491], 491: [], 39: [88, 425], 88: [], 400: [], 472: [99], 496: [],
                      335: [175, 475], 297: [174], 70: [396, 236, 310], 13: [252, 430, 363], 401: [], 342: [131, 413],
                      131: [], 374: [492], 492: [13, 418], 128: [109, 492], 109: [469], 469: [254, 376, 323],
                      254: [220], 166: [184], 143: [87, 199], 493: [113], 113: [], 376: [197, 129], 377: [159, 490],
                      159: [422], 388: [489, 103], 489: [], 194: [454, 39, 453], 346: [284], 294: [], 14: [352, 133],
                      352: [], 420: [46, 13, 448], 46: [], 208: [215], 20: [198, 498], 430: [499], 499: [224], 295: [],
                      416: [414, 386], 127: [494], 494: [], 305: [103, 114], 103: [], 199: [314],
                      307: [94, 253, 237, 306], 94: [351], 108: [241, 161, 299, 6], 500: [], 56: [407], 315: [],
                      167: [], 210: [160], 287: [], 148: [], 75: [46], 338: [258], 360: [113], 230: [331], 288: [81],
                      81: [], 275: [82, 337], 82: [372, 190, 302], 425: [214], 214: [353], 431: [], 160: [], 379: [451],
                      451: [], 339: [236], 312: [85, 444, 162], 85: [65], 320: [69, 77], 399: [141], 141: [],
                      115: [272], 272: [], 137: [], 341: [335], 244: [], 343: [244], 161: [258, 348, 434], 15: [455],
                      351: [], 358: [81], 158: [379], 225: [133, 80, 62], 133: [], 144: [173], 173: [],
                      209: [105, 127, 282, 465], 105: [], 153: [361, 451], 361: [], 240: [76, 249], 473: [367],
                      129: [321], 321: [], 474: [119], 49: [469, 233, 279], 17: [183], 183: [311, 113, 337], 324: [322],
                      478: [26], 378: [354, 170, 262], 354: [], 80: [], 419: [133], 189: [182], 234: [392, 60], 236: [],
                      126: [302, 157], 302: [336, 308], 224: [], 386: [], 232: [218, 140], 218: [411], 382: [443],
                      443: [], 466: [224], 411: [], 383: [90], 90: [242], 345: [499, 13], 30: [], 317: [360], 28: [492],
                      164: [], 366: [342, 62], 316: [121], 121: [108], 246: [273, 454], 461: [268], 249: [41],
                      110: [452], 77: [457], 18: [54], 60: [], 65: [], 463: [], 336: [391, 429], 9: [136], 136: [172],
                      337: [], 50: [127, 153], 53: [265], 265: [], 334: [236, 274], 273: [116], 116: [291], 205: [496],
                      233: [], 369: [151], 151: [], 165: [96, 56], 27: [47, 348], 462: [], 170: [], 328: [], 89: [],
                      465: [], 140: [], 482: [], 112: [], 266: [], 135: [167], 304: [], 43: [431], 176: [350], 350: [],
                      162: [320], 363: [141], 31: [357], 357: [], 279: [], 163: [272], 34: [384], 391: [], 242: [],
                      154: [8], 86: [], 467: [417], 464: [133], 296: [], 87: [], 274: [], 292: [], 471: [242], 25: [],
                      450: [434], 101: [233], 51: [], 248: [253], 484: [275], 84: [], 11: [468], 468: [], 72: [424],
                      424: [], 57: [183, 250], 229: [], 429: [], 457: []}


if __name__ == '__main__':
    if len(sys.argv) < 4:
        print(sys.argv[1], 'ERROR NO PARAMETERS IN THE CALL')
        sys.exit()
    set_max_runtime(int(sys.argv[2]))
    print(sys.argv[1], 'START COMPUTATIONAL COMPLEXITY TEST')
    PEEK_MEMORY = int(sys.argv[3])
    graph = Graph()
    tracemalloc.start()
    topological_sort(graph)
    peekTracedMemory = int(tracemalloc.get_traced_memory()[1])
    tracemalloc.stop()

    print(sys.argv[1], 'PEEK MEMORY USAGE BY YOUR IMPLEMENTATION:', peekTracedMemory)
    if peekTracedMemory < (PEEK_MEMORY * 2):
        print(sys.argv[1], 'FINISH COMPUTATIONAL COMPLEXITY TEST')
    else:
        print(sys.argv[1], 'ERROR MEMORY LIMIT EXCEEDED')