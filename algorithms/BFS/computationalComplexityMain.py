import resource
import signal
import sys
import tracemalloc

from userBFS import bfs


def time_exceeded(signo, frame):
    print(sys.argv[1], 'ERROR TIME OUT')
    sys.exit(1)


def set_max_runtime(seconds):
    soft, hard = resource.getrlimit(resource.RLIMIT_CPU)
    resource.setrlimit(resource.RLIMIT_CPU, (seconds, hard))
    signal.signal(signal.SIGXCPU, time_exceeded)


class Graph:
    def __init__(self):
        self.graph = {314: [799, 483, 362, 523], 9: [748], 347: [55, 302], 843: [745, 869], 322: [412, 398], 342: [467],
                      225: [762, 481, 5], 749: [64, 12, 281], 15: [137], 602: [342], 299: [870], 484: [783, 224],
                      415: [649], 756: [766, 580], 576: [27, 247], 556: [157, 548], 332: [667], 502: [329, 222],
                      839: [247], 238: [448, 617], 494: [371], 777: [693, 698, 219, 571], 719: [456, 16, 173],
                      100: [551, 403, 390, 144], 171: [258, 634], 58: [834, 745], 298: [316, 13, 308, 632, 867],
                      399: [168, 368], 253: [367, 851], 301: [603, 629], 315: [634, 146], 715: [378, 492],
                      176: [332, 301, 860], 653: [586, 316, 791, 204], 106: [41, 879, 246, 150], 169: [599, 444],
                      588: [92], 116: [531, 824], 90: [191], 178: [594, 625], 786: [875, 455, 839], 93: [372, 97, 763],
                      218: [209], 463: [617, 442], 650: [447, 505], 83: [286, 717], 241: [574, 744], 12: [569, 139],
                      382: [861, 161], 596: [494], 308: [109], 674: [750], 545: [657, 726, 670, 631], 326: [256],
                      452: [34, 500, 602], 607: [728, 480], 251: [187], 371: [842, 456, 824], 117: [424, 447, 387],
                      407: [570], 667: [376, 645, 683], 126: [865], 529: [85], 549: [563, 450], 323: [795], 663: [518],
                      51: [22, 245], 188: [595], 426: [236], 244: [93, 150], 710: [417], 189: [9, 711, 436, 148],
                      840: [462, 854], 804: [145, 78], 6: [429, 608, 653], 449: [690], 543: [759], 810: [521], 99: [40],
                      609: [482, 404], 547: [557, 107], 459: [573], 510: [773, 594], 16: [564, 0], 593: [102],
                      456: [420], 198: [723, 804], 499: [537], 277: [701], 551: [340, 566], 559: [421, 669, 34],
                      845: [229], 613: [117, 788], 563: [377], 554: [355], 850: [290], 65: [303], 131: [544], 826: [45],
                      47: [38, 755], 263: [269, 612, 333], 43: [266, 594], 688: [763], 876: [604, 180],
                      566: [841, 279, 560], 349: [142, 767], 820: [211, 581, 566], 784: [817, 198], 249: [350],
                      367: [361, 460, 790], 425: [360], 335: [173, 321, 0, 652], 644: [39], 400: [782, 772], 491: [162],
                      391: [621, 494], 363: [425, 302], 712: [340], 405: [859], 216: [17, 231], 517: [674, 147],
                      817: [178], 0: [199, 379], 72: [548, 186], 361: [65], 185: [539, 696, 733], 632: [472, 266, 770],
                      520: [709, 105], 76: [740], 859: [332, 8], 575: [401], 14: [707], 722: [539], 539: [836],
                      758: [339, 169], 785: [187, 540, 315, 421], 832: [175], 461: [531], 861: [512, 32, 633, 386, 499],
                      279: [267, 382, 139], 487: [26, 741], 124: [447, 591], 794: [413, 606], 62: [93], 294: [844, 692],
                      557: [287], 229: [819], 60: [584], 103: [433, 360], 779: [685, 763], 85: [602, 192, 866],
                      492: [68, 115], 278: [456, 660], 498: [565, 293, 498], 413: [647, 156], 526: [727, 673],
                      546: [441, 809], 665: [271, 582, 387, 703, 334], 148: [295, 271, 285], 92: [150], 855: [764],
                      143: [432], 424: [778, 40], 408: [253], 202: [572], 505: [487], 474: [745, 203, 235],
                      33: [196, 34, 421, 207], 444: [38], 359: [81], 773: [283], 705: [304], 303: [160, 426],
                      360: [372], 692: [91, 483, 222], 295: [686], 778: [8], 699: [856, 671, 802], 389: [444, 816],
                      410: [104, 82], 851: [506], 48: [534, 673], 623: [66, 444, 202], 137: [252], 628: [297],
                      266: [561], 362: [90], 52: [591, 309], 414: [0, 789], 312: [609], 377: [240], 657: [153],
                      210: [423], 542: [751, 530], 848: [42, 290, 179], 8: [276], 871: [849, 627, 568],
                      82: [780, 565, 75], 406: [870, 781], 495: [37, 437], 488: [378, 491], 532: [606], 13: [727],
                      519: [296, 10], 522: [806], 664: [219, 241], 329: [508, 480], 533: [870], 724: [523], 446: [811],
                      740: [707, 275, 445], 775: [349], 66: [865], 738: [593, 843, 171, 867], 183: [274, 356],
                      230: [584, 24, 581, 369, 350], 658: [626, 815], 662: [501], 760: [620, 457, 754], 472: [802, 697],
                      483: [470], 140: [571, 717, 708], 130: [626], 139: [432], 423: [735, 213], 681: [780, 604],
                      450: [298, 549, 330], 224: [333, 58, 764], 671: [738, 785], 421: [739], 854: [403, 538],
                      111: [366, 582], 309: [737], 673: [449, 17], 728: [701, 66], 57: [75, 392, 859, 792, 40],
                      394: [674], 2: [844], 866: [662], 255: [556, 517], 291: [101], 125: [705, 572],
                      22: [418, 67, 856, 283], 482: [369, 46], 164: [232, 240], 119: [288, 570], 375: [528, 7],
                      396: [416, 141], 145: [797, 68], 395: [695, 820], 713: [156], 757: [317], 465: [800, 49],
                      571: [128, 707], 769: [451, 77], 237: [240], 422: [195, 485], 354: [451], 591: [367],
                      439: [773, 770], 528: [853], 163: [117], 771: [334, 218], 466: [811, 230, 339], 824: [469, 341],
                      194: [481], 190: [401, 485], 788: [880, 636], 454: [189, 574], 682: [228, 690], 544: [304],
                      203: [132], 518: [292], 429: [693, 1], 280: [523], 572: [697], 448: [42], 20: [826, 728],
                      569: [396], 770: [820, 11], 120: [303, 750], 304: [137], 256: [7], 865: [298], 753: [141, 45],
                      346: [637], 751: [246], 159: [272], 479: [68], 1: [293], 37: [180], 443: [435], 435: [626],
                      541: [485, 216], 221: [643], 600: [18], 404: [246, 719], 698: [524], 562: [181], 727: [450],
                      331: [556, 239], 46: [811, 635, 677], 515: [320], 626: [182, 811, 287], 161: [172],
                      89: [320, 135], 204: [12], 45: [140], 582: [688, 21, 786, 369], 783: [547, 782, 110],
                      828: [281, 392], 873: [524, 777], 369: [189, 379], 686: [392], 852: [813], 109: [183],
                      173: [85, 46], 656: [306], 684: [235], 880: [345, 687], 205: [148], 420: [598], 289: [58],
                      118: [858, 739, 671, 476], 427: [99], 604: [107, 224], 138: [774], 257: [656, 588], 645: [384],
                      478: [328, 786], 872: [9, 135], 152: [569, 75], 639: [381], 264: [143, 672], 311: [728],
                      174: [465], 226: [422], 745: [566], 95: [742, 651], 234: [584], 86: [548], 129: [568, 487],
                      270: [725], 285: [440, 178], 338: [36, 839, 639], 288: [812], 734: [39], 3: [329],
                      640: [880, 288], 36: [294], 42: [436], 146: [393], 874: [647], 55: [737], 108: [329, 268],
                      27: [834], 155: [377], 561: [371], 553: [272], 831: [566, 321, 724], 196: [443], 838: [205],
                      236: [531, 34], 248: [657], 806: [528, 542], 603: [847], 265: [329, 704], 867: [729], 352: [56],
                      693: [233], 320: [285], 428: [204], 113: [565], 275: [786, 720], 21: [839], 879: [719],
                      493: [445, 567], 500: [28], 862: [229], 283: [783], 513: [212, 352], 457: [167, 517, 670],
                      151: [682], 638: [116], 17: [608], 70: [652, 772], 344: [448, 462], 711: [2, 283], 30: [651, 704],
                      538: [500], 193: [237, 319], 211: [425], 34: [155], 648: [511], 877: [352], 521: [610],
                      470: [518], 78: [45, 787], 25: [99], 401: [56], 29: [291, 392], 317: [8, 804], 135: [363],
                      630: [5], 560: [243], 431: [880], 821: [734], 669: [428], 799: [599, 112, 880, 192],
                      243: [117, 792], 73: [817], 797: [818], 696: [656], 655: [707], 473: [341], 835: [436],
                      574: [443, 500], 383: [80, 335], 857: [597], 858: [40], 530: [192], 796: [196], 564: [533],
                      397: [121], 670: [491], 365: [93], 605: [810], 337: [197, 318], 272: [861, 736, 120],
                      7: [177, 204], 537: [629, 519], 403: [106], 733: [625], 453: [68], 755: [248], 827: [599],
                      675: [773, 710], 242: [528], 180: [534], 503: [136], 374: [511], 793: [593], 507: [310],
                      573: [173], 98: [136], 485: [346], 849: [61], 433: [766], 384: [624, 351], 69: [682], 330: [708],
                      697: [169], 44: [357], 652: [815], 107: [310], 869: [16], 651: [55, 270], 112: [493, 73],
                      187: [654], 105: [576], 11: [314], 741: [607], 418: [275], 310: [578, 669], 19: [830], 411: [177],
                      612: [333, 293], 489: [538], 250: [66], 192: [46], 166: [57], 647: [5], 622: [86],
                      813: [496, 825], 548: [541], 847: [668], 127: [597], 624: [175], 829: [839], 731: [681],
                      736: [732], 177: [170], 199: [76], 61: [110, 68], 464: [720], 534: [180], 358: [389], 267: [563],
                      368: [513], 460: [559], 136: [371], 870: [356], 863: [601, 681], 26: [549], 617: [264],
                      364: [651], 35: [246], 184: [82], 476: [560], 64: [422], 841: [473], 316: [797], 91: [662],
                      694: [365], 334: [767, 538], 28: [624, 731], 635: [239], 583: [729, 31], 720: [482], 441: [393],
                      385: [856], 281: [354], 191: [234], 586: [171], 860: [205], 393: [484], 39: [797, 398],
                      814: [117], 524: [610, 49], 239: [810], 672: [69], 455: [576, 323], 327: [557], 570: [683],
                      306: [344], 296: [739], 110: [841, 599], 774: [645], 523: [144], 514: [536], 636: [398],
                      313: [876], 447: [216], 606: [687], 67: [800], 328: [716], 259: [265, 428], 748: [786],
                      227: [491], 815: [654], 508: [803], 825: [693], 836: [702], 74: [362], 805: [47], 172: [294],
                      716: [587], 625: [782], 96: [760], 618: [429], 206: [555], 223: [818], 764: [473], 200: [701],
                      351: [732], 708: [750], 201: [16], 293: [371], 509: [832], 409: [805]}


if __name__ == '__main__':
    if len(sys.argv) < 4:
        print(sys.argv[1], 'ERROR NO PARAMETERS IN THE CALL')
    set_max_runtime(int(sys.argv[2]))
    print(sys.argv[1], 'START COMPUTATIONAL COMPLEXITY TEST')
    PEEK_MEMORY = int(sys.argv[3])
    graph = Graph()
    tracemalloc.start()
    bfs(graph, 0)
    peekTracedMemory = int(tracemalloc.get_traced_memory()[1])
    tracemalloc.stop()

    print(sys.argv[1], 'PEEK MEMORY USAGE BY YOUR IMPLEMENTATION:', peekTracedMemory)
    if peekTracedMemory < (PEEK_MEMORY * 2):
        print(sys.argv[1], 'FINISH COMPUTATIONAL COMPLEXITY TEST')
    else:
        print(sys.argv[1], 'ERROR MEMORY LIMIT EXCEEDED')
