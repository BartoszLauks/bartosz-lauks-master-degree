import resource
import signal
import sys
import tracemalloc

from userPrim import prim


def time_exceeded(signo, frame):
    print(sys.argv[1], 'ERROR TIME OUT')
    sys.exit(1)


def set_max_runtime(seconds):
    soft, hard = resource.getrlimit(resource.RLIMIT_CPU)
    resource.setrlimit(resource.RLIMIT_CPU, (seconds, hard))
    signal.signal(signal.SIGXCPU, time_exceeded)


class Graph:
    def __init__(self):
        self.graph = {42: [(110, 958), (166, 610)], 110: [(42, 958), (7, 823)], 7: [(110, 823), (192, 901)],
                      192: [(7, 901), (134, 431)], 134: [(192, 431), (115, 857)], 115: [(134, 857), (162, 893)],
                      162: [(115, 893), (88, 760)], 88: [(162, 760), (15, 319)], 15: [(88, 319), (82, 51)],
                      82: [(15, 51), (18, 931)], 18: [(82, 931), (93, 932)], 93: [(18, 932), (28, 710)],
                      28: [(93, 710), (151, 301)], 151: [(28, 301), (189, 981)], 189: [(151, 981), (36, 609)],
                      36: [(189, 609), (103, 783)], 103: [(36, 783), (179, 44)], 179: [(103, 44), (146, 893)],
                      146: [(179, 893), (11, 923)], 11: [(146, 923), (136, 36)], 136: [(11, 36), (190, 585)],
                      190: [(136, 585), (177, 46)], 177: [(190, 46), (24, 771)], 24: [(177, 771), (2, 901)],
                      2: [(24, 901), (138, 787)], 138: [(2, 787), (58, 431)], 58: [(138, 431), (193, 410)],
                      193: [(58, 410), (181, 338)], 181: [(193, 338), (9, 537)], 9: [(181, 537), (117, 194)],
                      117: [(9, 194), (124, 51)], 124: [(117, 51), (50, 916)], 50: [(124, 916), (120, 764)],
                      120: [(50, 764), (70, 452)], 70: [(120, 452), (59, 592)], 59: [(70, 592), (98, 503)],
                      98: [(59, 503), (97, 98)], 97: [(98, 98), (14, 379)], 14: [(97, 379), (126, 689)],
                      126: [(14, 689), (131, 521)], 131: [(126, 521), (26, 652)], 26: [(131, 652), (90, 474)],
                      90: [(26, 474), (74, 275)], 74: [(90, 275), (172, 995)], 172: [(74, 995), (99, 351)],
                      99: [(172, 351), (71, 208)], 71: [(99, 208), (22, 181)], 22: [(71, 181), (114, 641)],
                      114: [(22, 641), (168, 614)], 168: [(114, 614), (17, 546)], 17: [(168, 546), (159, 98)],
                      159: [(17, 98), (144, 910)], 144: [(159, 910), (13, 44)], 13: [(144, 44), (41, 403)],
                      41: [(13, 403), (153, 276)], 153: [(41, 276), (75, 443)], 75: [(153, 443), (183, 654)],
                      183: [(75, 654), (109, 839)], 109: [(183, 839), (12, 914)], 12: [(109, 914), (169, 279)],
                      169: [(12, 279), (182, 893)], 182: [(169, 893), (83, 382)], 83: [(182, 382), (137, 28)],
                      137: [(83, 28), (73, 816)], 73: [(137, 816), (128, 948)], 128: [(73, 948), (196, 815)],
                      196: [(128, 815), (91, 455)], 91: [(196, 455), (154, 648)], 154: [(91, 648), (142, 770)],
                      142: [(154, 770), (76, 219)], 76: [(142, 219), (135, 288)], 135: [(76, 288), (4, 696)],
                      4: [(135, 696), (194, 309)], 194: [(4, 309), (171, 867)], 171: [(194, 867), (65, 350)],
                      65: [(171, 350), (1, 496)], 1: [(65, 496), (108, 12)], 108: [(1, 12), (185, 202)],
                      185: [(108, 202), (186, 288)], 186: [(185, 288), (188, 300)], 188: [(186, 300), (86, 767)],
                      86: [(188, 767), (5, 11)], 5: [(86, 11), (89, 131)], 89: [(5, 131), (122, 768)],
                      122: [(89, 768), (175, 325)], 175: [(122, 325), (40, 808)], 40: [(175, 808), (132, 714)],
                      132: [(40, 714), (49, 579)], 49: [(132, 579), (35, 534)], 35: [(49, 534), (45, 790)],
                      45: [(35, 790), (87, 731)], 87: [(45, 731), (164, 364)], 164: [(87, 364), (150, 926)],
                      150: [(164, 926), (165, 627)], 165: [(150, 627), (30, 85)], 30: [(165, 85), (147, 521)],
                      147: [(30, 521), (57, 927)], 57: [(147, 927), (119, 588)], 119: [(57, 588), (116, 282)],
                      116: [(119, 282), (39, 791)], 39: [(116, 791), (68, 955)], 68: [(39, 955), (77, 806)],
                      77: [(68, 806), (56, 755)], 56: [(77, 755), (80, 417)], 80: [(56, 417), (173, 40)],
                      173: [(80, 40), (79, 889)], 79: [(173, 889), (180, 576)], 180: [(79, 576), (66, 483)],
                      66: [(180, 483), (104, 295)], 104: [(66, 295), (46, 750)], 46: [(104, 750), (148, 418)],
                      148: [(46, 418), (55, 368)], 55: [(148, 368), (6, 329)], 6: [(55, 329), (31, 854)],
                      31: [(6, 854), (21, 783)], 21: [(31, 783), (184, 938)], 184: [(21, 938), (10, 950)],
                      10: [(184, 950), (63, 396)], 63: [(10, 396), (101, 657)], 101: [(63, 657), (187, 149)],
                      187: [(101, 149), (60, 747)], 60: [(187, 747), (43, 8)], 43: [(60, 8), (32, 56)],
                      32: [(43, 56), (105, 103)], 105: [(32, 103), (100, 400)], 100: [(105, 400), (174, 41)],
                      174: [(100, 41), (106, 963)], 106: [(174, 963), (156, 813)], 156: [(106, 813), (8, 868)],
                      8: [(156, 868), (19, 500)], 19: [(8, 500), (23, 128)], 23: [(19, 128), (92, 965)],
                      92: [(23, 965), (191, 643)], 191: [(92, 643), (81, 37)], 81: [(191, 37), (170, 340)],
                      170: [(81, 340), (78, 908)], 78: [(170, 908), (111, 548)], 111: [(78, 548), (96, 132)],
                      96: [(111, 132), (44, 189)], 44: [(96, 189), (161, 308)], 161: [(44, 308), (37, 298)],
                      37: [(161, 298), (199, 928)], 199: [(37, 928), (125, 460)], 125: [(199, 460), (160, 904)],
                      160: [(125, 904), (29, 813)], 29: [(160, 813), (118, 752)], 118: [(29, 752), (112, 964)],
                      112: [(118, 964), (53, 112)], 53: [(112, 112), (195, 282)], 195: [(53, 282), (107, 368)],
                      107: [(195, 368), (143, 310)], 143: [(107, 310), (94, 885)], 94: [(143, 885), (198, 844)],
                      198: [(94, 844), (67, 169)], 67: [(198, 169), (47, 556)], 47: [(67, 556), (38, 160)],
                      38: [(47, 160), (20, 76)], 20: [(38, 76), (33, 526)], 33: [(20, 526), (141, 195)],
                      141: [(33, 195), (25, 113)], 25: [(141, 113), (84, 732)], 84: [(25, 732), (130, 829)],
                      130: [(84, 829), (163, 661)], 163: [(130, 661), (157, 909)], 157: [(163, 909), (123, 133)],
                      123: [(157, 133), (178, 440)], 178: [(123, 440), (48, 548)], 48: [(178, 548), (129, 764)],
                      129: [(48, 764), (102, 470)], 102: [(129, 470), (176, 858)], 176: [(102, 858), (167, 663)],
                      167: [(176, 663), (155, 725)], 155: [(167, 725), (61, 624)], 61: [(155, 624), (16, 860)],
                      16: [(61, 860), (95, 525)], 95: [(16, 525), (85, 232)], 85: [(95, 232), (69, 73)],
                      69: [(85, 73), (3, 931)], 3: [(69, 931), (158, 818)], 158: [(3, 818), (121, 485)],
                      121: [(158, 485), (27, 994)], 27: [(121, 994), (54, 961)], 54: [(27, 961), (62, 525)],
                      62: [(54, 525), (51, 539)], 51: [(62, 539), (34, 879)], 34: [(51, 879), (149, 881)],
                      149: [(34, 881), (145, 518)], 145: [(149, 518), (139, 579)], 139: [(145, 579), (72, 317)],
                      72: [(139, 317), (200, 747)], 200: [(72, 747), (152, 229)], 152: [(200, 229), (52, 452)],
                      52: [(152, 452), (140, 633)], 140: [(52, 633), (127, 224)], 127: [(140, 224), (64, 22)],
                      64: [(127, 22), (113, 53)], 113: [(64, 53), (133, 756)], 133: [(113, 756), (197, 579)],
                      197: [(133, 579), (166, 210)], 166: [(197, 210), (42, 610)]}


if __name__ == '__main__':
    if len(sys.argv) < 4:
        print(sys.argv[1], 'ERROR NO PARAMETERS IN THE CALL')
        sys.exit()
    set_max_runtime(int(sys.argv[2]))
    print(sys.argv[1], 'START COMPUTATIONAL COMPLEXITY TEST')
    PEEK_MEMORY = int(sys.argv[3])
    graph = Graph()
    tracemalloc.start()
    prim(graph, list(graph.graph.keys())[0])
    peekTracedMemory = int(tracemalloc.get_traced_memory()[1])
    tracemalloc.stop()

    print(sys.argv[1], 'PEEK MEMORY USAGE BY YOUR IMPLEMENTATION:', peekTracedMemory)
    if peekTracedMemory < (PEEK_MEMORY * 2):
        print(sys.argv[1], 'FINISH COMPUTATIONAL COMPLEXITY TEST')
    else:
        print(sys.argv[1], 'ERROR MEMORY LIMIT EXCEEDED')
