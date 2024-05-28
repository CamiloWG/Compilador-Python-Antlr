# Generated from Compiler/Grammar/gramatica.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,93,517,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,1,0,4,0,70,8,0,11,0,12,0,71,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,92,8,1,1,2,1,2,1,2,3,
        2,97,8,2,1,2,3,2,100,8,2,1,2,1,2,1,2,1,2,3,2,106,8,2,1,2,3,2,109,
        8,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,120,8,2,1,2,1,2,1,2,
        1,2,1,2,1,2,1,2,3,2,129,8,2,1,3,3,3,132,8,3,1,3,3,3,135,8,3,1,3,
        1,3,1,3,3,3,140,8,3,1,3,1,3,3,3,144,8,3,1,4,1,4,1,5,1,5,1,5,1,5,
        1,5,3,5,153,8,5,1,5,1,5,1,5,1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,8,1,8,
        1,9,1,9,1,9,1,9,3,9,171,8,9,1,9,1,9,1,9,1,9,1,9,1,10,5,10,179,8,
        10,10,10,12,10,182,9,10,1,10,3,10,185,8,10,1,11,1,11,1,11,1,11,1,
        12,1,12,1,12,3,12,194,8,12,1,12,1,12,1,13,1,13,1,13,3,13,201,8,13,
        1,13,1,13,1,13,1,13,3,13,207,8,13,5,13,209,8,13,10,13,12,13,212,
        9,13,1,14,1,14,1,14,1,14,3,14,218,8,14,1,14,1,14,1,14,5,14,223,8,
        14,10,14,12,14,226,9,14,1,14,1,14,3,14,230,8,14,1,14,3,14,233,8,
        14,1,15,4,15,236,8,15,11,15,12,15,237,1,16,1,16,1,16,1,16,3,16,244,
        8,16,1,16,1,16,1,16,5,16,249,8,16,10,16,12,16,252,9,16,1,16,1,16,
        1,17,1,17,1,17,5,17,259,8,17,10,17,12,17,262,9,17,1,17,1,17,1,18,
        1,18,1,18,1,18,1,18,1,18,1,18,3,18,273,8,18,1,18,3,18,276,8,18,1,
        18,3,18,279,8,18,1,18,3,18,282,8,18,1,18,1,18,1,18,4,18,287,8,18,
        11,18,12,18,288,1,18,3,18,292,8,18,1,18,1,18,1,18,1,18,1,18,1,18,
        1,18,1,18,4,18,302,8,18,11,18,12,18,303,1,18,3,18,307,8,18,1,18,
        1,18,1,18,1,18,1,18,1,18,1,18,1,18,4,18,317,8,18,11,18,12,18,318,
        1,18,3,18,322,8,18,1,18,1,18,3,18,326,8,18,1,19,1,19,3,19,330,8,
        19,1,19,1,19,3,19,334,8,19,1,19,1,19,4,19,338,8,19,11,19,12,19,339,
        1,19,1,19,1,20,1,20,1,20,5,20,347,8,20,10,20,12,20,350,9,20,1,21,
        1,21,1,21,1,21,1,21,1,21,1,21,1,22,1,22,1,22,1,22,3,22,363,8,22,
        1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,5,22,374,8,22,10,22,
        12,22,377,9,22,1,23,1,23,3,23,381,8,23,1,23,3,23,384,8,23,1,23,1,
        23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,
        23,1,23,1,23,1,23,3,23,404,8,23,1,24,1,24,1,24,1,24,5,24,410,8,24,
        10,24,12,24,413,9,24,1,24,1,24,1,25,1,25,1,25,1,25,5,25,421,8,25,
        10,25,12,25,424,9,25,1,25,1,25,1,26,1,26,1,26,1,27,1,27,1,27,1,27,
        1,27,1,27,3,27,437,8,27,1,28,1,28,1,28,1,28,1,28,1,28,4,28,445,8,
        28,11,28,12,28,446,1,28,1,28,1,29,1,29,1,29,1,29,1,29,1,29,4,29,
        457,8,29,11,29,12,29,458,1,29,1,29,1,30,1,30,1,30,1,30,1,30,1,30,
        1,30,1,30,1,30,1,30,1,30,1,30,1,30,1,30,1,30,1,30,1,30,1,30,3,30,
        481,8,30,1,30,1,30,1,30,1,30,1,30,3,30,488,8,30,1,31,1,31,1,31,1,
        31,1,31,1,31,1,31,1,31,1,31,1,31,1,31,1,31,1,31,1,32,1,32,1,32,1,
        32,1,32,1,32,1,33,1,33,1,33,1,33,1,33,1,33,1,33,1,33,1,33,0,1,44,
        34,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,
        44,46,48,50,52,54,56,58,60,62,64,66,0,10,1,0,53,56,1,0,1,2,1,0,3,
        10,3,0,63,63,65,67,88,89,2,0,64,64,68,73,1,0,59,60,2,0,1,1,13,14,
        1,0,15,20,1,0,21,22,1,0,23,25,582,0,69,1,0,0,0,2,91,1,0,0,0,4,128,
        1,0,0,0,6,131,1,0,0,0,8,145,1,0,0,0,10,147,1,0,0,0,12,157,1,0,0,
        0,14,159,1,0,0,0,16,164,1,0,0,0,18,166,1,0,0,0,20,180,1,0,0,0,22,
        186,1,0,0,0,24,190,1,0,0,0,26,200,1,0,0,0,28,213,1,0,0,0,30,235,
        1,0,0,0,32,239,1,0,0,0,34,255,1,0,0,0,36,325,1,0,0,0,38,327,1,0,
        0,0,40,343,1,0,0,0,42,351,1,0,0,0,44,362,1,0,0,0,46,403,1,0,0,0,
        48,405,1,0,0,0,50,416,1,0,0,0,52,427,1,0,0,0,54,436,1,0,0,0,56,438,
        1,0,0,0,58,450,1,0,0,0,60,487,1,0,0,0,62,489,1,0,0,0,64,502,1,0,
        0,0,66,508,1,0,0,0,68,70,3,2,1,0,69,68,1,0,0,0,70,71,1,0,0,0,71,
        69,1,0,0,0,71,72,1,0,0,0,72,1,1,0,0,0,73,92,3,10,5,0,74,92,3,4,2,
        0,75,92,3,24,12,0,76,92,3,28,14,0,77,92,3,38,19,0,78,92,3,44,22,
        0,79,92,3,18,9,0,80,92,3,36,18,0,81,92,3,6,3,0,82,92,3,14,7,0,83,
        92,3,60,30,0,84,92,3,52,26,0,85,92,3,42,21,0,86,92,3,46,23,0,87,
        92,5,31,0,0,88,92,3,64,32,0,89,92,3,66,33,0,90,92,3,8,4,0,91,73,
        1,0,0,0,91,74,1,0,0,0,91,75,1,0,0,0,91,76,1,0,0,0,91,77,1,0,0,0,
        91,78,1,0,0,0,91,79,1,0,0,0,91,80,1,0,0,0,91,81,1,0,0,0,91,82,1,
        0,0,0,91,83,1,0,0,0,91,84,1,0,0,0,91,85,1,0,0,0,91,86,1,0,0,0,91,
        87,1,0,0,0,91,88,1,0,0,0,91,89,1,0,0,0,91,90,1,0,0,0,92,3,1,0,0,
        0,93,94,5,92,0,0,94,96,5,64,0,0,95,97,3,12,6,0,96,95,1,0,0,0,96,
        97,1,0,0,0,97,99,1,0,0,0,98,100,5,80,0,0,99,98,1,0,0,0,99,100,1,
        0,0,0,100,105,1,0,0,0,101,106,3,44,22,0,102,106,3,6,3,0,103,106,
        3,46,23,0,104,106,3,62,31,0,105,101,1,0,0,0,105,102,1,0,0,0,105,
        103,1,0,0,0,105,104,1,0,0,0,106,108,1,0,0,0,107,109,5,81,0,0,108,
        107,1,0,0,0,108,109,1,0,0,0,109,110,1,0,0,0,110,111,5,77,0,0,111,
        129,1,0,0,0,112,113,5,92,0,0,113,114,5,64,0,0,114,115,5,92,0,0,115,
        119,5,80,0,0,116,120,3,40,20,0,117,120,3,44,22,0,118,120,3,46,23,
        0,119,116,1,0,0,0,119,117,1,0,0,0,119,118,1,0,0,0,119,120,1,0,0,
        0,120,121,1,0,0,0,121,122,5,81,0,0,122,129,5,77,0,0,123,124,5,92,
        0,0,124,125,5,64,0,0,125,126,3,16,8,0,126,127,5,77,0,0,127,129,1,
        0,0,0,128,93,1,0,0,0,128,112,1,0,0,0,128,123,1,0,0,0,129,5,1,0,0,
        0,130,132,3,12,6,0,131,130,1,0,0,0,131,132,1,0,0,0,132,134,1,0,0,
        0,133,135,5,80,0,0,134,133,1,0,0,0,134,135,1,0,0,0,135,136,1,0,0,
        0,136,137,5,51,0,0,137,139,5,80,0,0,138,140,3,44,22,0,139,138,1,
        0,0,0,139,140,1,0,0,0,140,141,1,0,0,0,141,143,5,81,0,0,142,144,5,
        81,0,0,143,142,1,0,0,0,143,144,1,0,0,0,144,7,1,0,0,0,145,146,5,30,
        0,0,146,9,1,0,0,0,147,148,5,52,0,0,148,152,5,80,0,0,149,153,3,44,
        22,0,150,153,5,75,0,0,151,153,3,46,23,0,152,149,1,0,0,0,152,150,
        1,0,0,0,152,151,1,0,0,0,152,153,1,0,0,0,153,154,1,0,0,0,154,155,
        5,81,0,0,155,156,5,77,0,0,156,11,1,0,0,0,157,158,7,0,0,0,158,13,
        1,0,0,0,159,160,3,12,6,0,160,161,5,80,0,0,161,162,3,44,22,0,162,
        163,5,81,0,0,163,15,1,0,0,0,164,165,5,93,0,0,165,17,1,0,0,0,166,
        167,5,36,0,0,167,168,5,92,0,0,168,170,5,80,0,0,169,171,3,40,20,0,
        170,169,1,0,0,0,170,171,1,0,0,0,171,172,1,0,0,0,172,173,5,81,0,0,
        173,174,5,83,0,0,174,175,3,20,10,0,175,176,5,82,0,0,176,19,1,0,0,
        0,177,179,3,2,1,0,178,177,1,0,0,0,179,182,1,0,0,0,180,178,1,0,0,
        0,180,181,1,0,0,0,181,184,1,0,0,0,182,180,1,0,0,0,183,185,3,22,11,
        0,184,183,1,0,0,0,184,185,1,0,0,0,185,21,1,0,0,0,186,187,5,48,0,
        0,187,188,3,44,22,0,188,189,5,77,0,0,189,23,1,0,0,0,190,191,5,92,
        0,0,191,193,5,80,0,0,192,194,3,26,13,0,193,192,1,0,0,0,193,194,1,
        0,0,0,194,195,1,0,0,0,195,196,5,81,0,0,196,25,1,0,0,0,197,201,3,
        54,27,0,198,201,5,92,0,0,199,201,3,24,12,0,200,197,1,0,0,0,200,198,
        1,0,0,0,200,199,1,0,0,0,201,210,1,0,0,0,202,206,5,75,0,0,203,207,
        3,54,27,0,204,207,5,92,0,0,205,207,3,24,12,0,206,203,1,0,0,0,206,
        204,1,0,0,0,206,205,1,0,0,0,207,209,1,0,0,0,208,202,1,0,0,0,209,
        212,1,0,0,0,210,208,1,0,0,0,210,211,1,0,0,0,211,27,1,0,0,0,212,210,
        1,0,0,0,213,214,5,38,0,0,214,217,5,80,0,0,215,218,3,40,20,0,216,
        218,3,44,22,0,217,215,1,0,0,0,217,216,1,0,0,0,218,219,1,0,0,0,219,
        220,5,81,0,0,220,224,5,83,0,0,221,223,3,2,1,0,222,221,1,0,0,0,223,
        226,1,0,0,0,224,222,1,0,0,0,224,225,1,0,0,0,225,227,1,0,0,0,226,
        224,1,0,0,0,227,229,5,82,0,0,228,230,3,30,15,0,229,228,1,0,0,0,229,
        230,1,0,0,0,230,232,1,0,0,0,231,233,3,34,17,0,232,231,1,0,0,0,232,
        233,1,0,0,0,233,29,1,0,0,0,234,236,3,32,16,0,235,234,1,0,0,0,236,
        237,1,0,0,0,237,235,1,0,0,0,237,238,1,0,0,0,238,31,1,0,0,0,239,240,
        5,62,0,0,240,243,5,80,0,0,241,244,3,40,20,0,242,244,3,44,22,0,243,
        241,1,0,0,0,243,242,1,0,0,0,244,245,1,0,0,0,245,246,5,81,0,0,246,
        250,5,83,0,0,247,249,3,2,1,0,248,247,1,0,0,0,249,252,1,0,0,0,250,
        248,1,0,0,0,250,251,1,0,0,0,251,253,1,0,0,0,252,250,1,0,0,0,253,
        254,5,82,0,0,254,33,1,0,0,0,255,256,5,39,0,0,256,260,5,83,0,0,257,
        259,3,2,1,0,258,257,1,0,0,0,259,262,1,0,0,0,260,258,1,0,0,0,260,
        261,1,0,0,0,261,263,1,0,0,0,262,260,1,0,0,0,263,264,5,82,0,0,264,
        35,1,0,0,0,265,266,5,40,0,0,266,267,5,92,0,0,267,268,5,41,0,0,268,
        269,5,42,0,0,269,270,5,80,0,0,270,272,3,44,22,0,271,273,5,75,0,0,
        272,271,1,0,0,0,272,273,1,0,0,0,273,275,1,0,0,0,274,276,3,44,22,
        0,275,274,1,0,0,0,275,276,1,0,0,0,276,278,1,0,0,0,277,279,5,75,0,
        0,278,277,1,0,0,0,278,279,1,0,0,0,279,281,1,0,0,0,280,282,3,44,22,
        0,281,280,1,0,0,0,281,282,1,0,0,0,282,283,1,0,0,0,283,284,5,81,0,
        0,284,286,5,83,0,0,285,287,3,2,1,0,286,285,1,0,0,0,287,288,1,0,0,
        0,288,286,1,0,0,0,288,289,1,0,0,0,289,291,1,0,0,0,290,292,3,22,11,
        0,291,290,1,0,0,0,291,292,1,0,0,0,292,293,1,0,0,0,293,294,5,82,0,
        0,294,326,1,0,0,0,295,296,5,40,0,0,296,297,5,92,0,0,297,298,5,41,
        0,0,298,299,3,44,22,0,299,301,5,83,0,0,300,302,3,2,1,0,301,300,1,
        0,0,0,302,303,1,0,0,0,303,301,1,0,0,0,303,304,1,0,0,0,304,306,1,
        0,0,0,305,307,3,22,11,0,306,305,1,0,0,0,306,307,1,0,0,0,307,308,
        1,0,0,0,308,309,5,82,0,0,309,326,1,0,0,0,310,311,5,40,0,0,311,312,
        5,92,0,0,312,313,5,41,0,0,313,314,3,16,8,0,314,316,5,83,0,0,315,
        317,3,2,1,0,316,315,1,0,0,0,317,318,1,0,0,0,318,316,1,0,0,0,318,
        319,1,0,0,0,319,321,1,0,0,0,320,322,3,22,11,0,321,320,1,0,0,0,321,
        322,1,0,0,0,322,323,1,0,0,0,323,324,5,82,0,0,324,326,1,0,0,0,325,
        265,1,0,0,0,325,295,1,0,0,0,325,310,1,0,0,0,326,37,1,0,0,0,327,329,
        5,44,0,0,328,330,5,80,0,0,329,328,1,0,0,0,329,330,1,0,0,0,330,331,
        1,0,0,0,331,333,3,44,22,0,332,334,5,81,0,0,333,332,1,0,0,0,333,334,
        1,0,0,0,334,335,1,0,0,0,335,337,5,83,0,0,336,338,3,2,1,0,337,336,
        1,0,0,0,338,339,1,0,0,0,339,337,1,0,0,0,339,340,1,0,0,0,340,341,
        1,0,0,0,341,342,5,82,0,0,342,39,1,0,0,0,343,348,5,92,0,0,344,345,
        5,75,0,0,345,347,5,92,0,0,346,344,1,0,0,0,347,350,1,0,0,0,348,346,
        1,0,0,0,348,349,1,0,0,0,349,41,1,0,0,0,350,348,1,0,0,0,351,352,7,
        1,0,0,352,353,5,74,0,0,353,354,7,2,0,0,354,355,5,80,0,0,355,356,
        3,44,22,0,356,357,5,81,0,0,357,43,1,0,0,0,358,359,6,22,-1,0,359,
        363,3,54,27,0,360,363,3,24,12,0,361,363,3,42,21,0,362,358,1,0,0,
        0,362,360,1,0,0,0,362,361,1,0,0,0,363,375,1,0,0,0,364,365,10,6,0,
        0,365,366,7,3,0,0,366,374,3,54,27,0,367,368,10,5,0,0,368,369,7,4,
        0,0,369,374,3,54,27,0,370,371,10,4,0,0,371,372,7,5,0,0,372,374,3,
        54,27,0,373,364,1,0,0,0,373,367,1,0,0,0,373,370,1,0,0,0,374,377,
        1,0,0,0,375,373,1,0,0,0,375,376,1,0,0,0,376,45,1,0,0,0,377,375,1,
        0,0,0,378,380,3,48,24,0,379,381,5,63,0,0,380,379,1,0,0,0,380,381,
        1,0,0,0,381,383,1,0,0,0,382,384,3,48,24,0,383,382,1,0,0,0,383,384,
        1,0,0,0,384,404,1,0,0,0,385,386,3,48,24,0,386,387,5,65,0,0,387,388,
        3,48,24,0,388,404,1,0,0,0,389,390,3,48,24,0,390,391,5,67,0,0,391,
        392,3,48,24,0,392,404,1,0,0,0,393,394,5,11,0,0,394,395,5,80,0,0,
        395,396,3,48,24,0,396,397,5,81,0,0,397,404,1,0,0,0,398,399,5,12,
        0,0,399,400,5,80,0,0,400,401,3,48,24,0,401,402,5,81,0,0,402,404,
        1,0,0,0,403,378,1,0,0,0,403,385,1,0,0,0,403,389,1,0,0,0,403,393,
        1,0,0,0,403,398,1,0,0,0,404,47,1,0,0,0,405,406,5,84,0,0,406,411,
        3,50,25,0,407,408,5,75,0,0,408,410,3,50,25,0,409,407,1,0,0,0,410,
        413,1,0,0,0,411,409,1,0,0,0,411,412,1,0,0,0,412,414,1,0,0,0,413,
        411,1,0,0,0,414,415,5,85,0,0,415,49,1,0,0,0,416,417,5,84,0,0,417,
        422,3,44,22,0,418,419,5,75,0,0,419,421,3,44,22,0,420,418,1,0,0,0,
        421,424,1,0,0,0,422,420,1,0,0,0,422,423,1,0,0,0,423,425,1,0,0,0,
        424,422,1,0,0,0,425,426,5,85,0,0,426,51,1,0,0,0,427,428,5,35,0,0,
        428,429,7,6,0,0,429,53,1,0,0,0,430,437,5,33,0,0,431,437,5,92,0,0,
        432,437,5,55,0,0,433,437,3,16,8,0,434,437,3,56,28,0,435,437,3,58,
        29,0,436,430,1,0,0,0,436,431,1,0,0,0,436,432,1,0,0,0,436,433,1,0,
        0,0,436,434,1,0,0,0,436,435,1,0,0,0,437,55,1,0,0,0,438,444,5,80,
        0,0,439,445,5,33,0,0,440,445,5,92,0,0,441,445,5,55,0,0,442,445,3,
        16,8,0,443,445,5,75,0,0,444,439,1,0,0,0,444,440,1,0,0,0,444,441,
        1,0,0,0,444,442,1,0,0,0,444,443,1,0,0,0,445,446,1,0,0,0,446,444,
        1,0,0,0,446,447,1,0,0,0,447,448,1,0,0,0,448,449,5,81,0,0,449,57,
        1,0,0,0,450,456,5,84,0,0,451,457,5,33,0,0,452,457,5,92,0,0,453,457,
        5,55,0,0,454,457,3,16,8,0,455,457,5,75,0,0,456,451,1,0,0,0,456,452,
        1,0,0,0,456,453,1,0,0,0,456,454,1,0,0,0,456,455,1,0,0,0,457,458,
        1,0,0,0,458,456,1,0,0,0,458,459,1,0,0,0,459,460,1,0,0,0,460,461,
        5,85,0,0,461,59,1,0,0,0,462,463,7,7,0,0,463,464,5,80,0,0,464,465,
        3,44,22,0,465,466,5,75,0,0,466,467,3,44,22,0,467,468,5,81,0,0,468,
        469,5,77,0,0,469,488,1,0,0,0,470,471,7,8,0,0,471,472,5,80,0,0,472,
        473,3,44,22,0,473,474,5,81,0,0,474,475,5,77,0,0,475,488,1,0,0,0,
        476,477,7,9,0,0,477,480,5,80,0,0,478,481,3,62,31,0,479,481,5,92,
        0,0,480,478,1,0,0,0,480,479,1,0,0,0,481,482,1,0,0,0,482,483,5,75,
        0,0,483,484,3,42,21,0,484,485,5,81,0,0,485,486,5,77,0,0,486,488,
        1,0,0,0,487,462,1,0,0,0,487,470,1,0,0,0,487,476,1,0,0,0,488,61,1,
        0,0,0,489,490,5,26,0,0,490,491,5,80,0,0,491,492,3,44,22,0,492,493,
        5,75,0,0,493,494,3,44,22,0,494,495,5,67,0,0,495,496,5,2,0,0,496,
        497,5,74,0,0,497,498,5,27,0,0,498,499,5,75,0,0,499,500,3,44,22,0,
        500,501,5,81,0,0,501,63,1,0,0,0,502,503,5,91,0,0,503,504,5,80,0,
        0,504,505,3,44,22,0,505,506,5,81,0,0,506,507,5,77,0,0,507,65,1,0,
        0,0,508,509,5,90,0,0,509,510,5,80,0,0,510,511,3,44,22,0,511,512,
        5,75,0,0,512,513,3,44,22,0,513,514,5,81,0,0,514,515,5,77,0,0,515,
        67,1,0,0,0,58,71,91,96,99,105,108,119,128,131,134,139,143,152,170,
        180,184,193,200,206,210,217,224,229,232,237,243,250,260,272,275,
        278,281,288,291,303,306,318,321,325,329,333,339,348,362,373,375,
        380,383,403,411,422,436,444,446,456,458,480,487
    ]

class gramaticaParser ( Parser ):

    grammarFileName = "gramatica.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'math'", "'np'", "'sin'", "'cos'", "'tan'", 
                     "'arcsin'", "'arccos'", "'arctan'", "'factorial'", 
                     "'sqrt'", "'inv'", "'trans'", "'matplotlib.pyplot'", 
                     "'numpy as np'", "'plot'", "'scatter'", "'fill_between'", 
                     "'bar'", "'barh'", "'hist'", "'pie'", "'boxplot'", 
                     "'grafsen'", "'grafcos'", "'graftan'", "'linspace'", 
                     "'pi'", "'\\u00AC'", "'~'", "'#'", "<INVALID>", "'\\t'", 
                     "<INVALID>", "<INVALID>", "'import'", "'def'", "'class'", 
                     "'if'", "'else'", "'for'", "'in'", "'range'", "'self'", 
                     "'while'", "'try'", "'end'", "'except'", "'return'", 
                     "'break'", "'next'", "'input'", "'print'", "'int'", 
                     "'float'", "<INVALID>", "'str'", "'pow'", "'mathsqrt'", 
                     "'and'", "'or'", "'not'", "'elif'", "'+'", "'='", "'-'", 
                     "'/'", "'*'", "'=='", "'!='", "'>'", "'<'", "'>='", 
                     "'<='", "'.'", "','", "':'", "';'", "'''", "'\"'", 
                     "'('", "')'", "'}'", "'{'", "'['", "']'", "'++'", "'--'", 
                     "'^'", "'%'", "'write'", "'open'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "SEP", "ESP", "COMMENT", "NEWLINE", "TAB", "NUMERO", 
                      "WS", "IMPORT", "DEF", "CLASS", "IF", "ELSE", "FOR", 
                      "IN", "RANGE", "SELF", "WHILE", "TRY", "END", "EXCEPT", 
                      "RETURN", "BREAK", "NEXT", "INPUT", "PRINT", "INT", 
                      "FLOAT", "BOOLEAN", "STR", "POW", "MATHSQRT", "AND", 
                      "OR", "NOT", "ELIF", "SUMA", "ASIGNACION", "RESTA", 
                      "DIVISION", "MULTIPLICACION", "IGUAL", "DIFERENTE", 
                      "MAYORQUE", "MENORQUE", "MENORIGUAL", "MAYORIGUAL", 
                      "PUNTO", "COMA", "DOSPUNTOS", "PUNTOCOMA", "COMILLASIMPLE", 
                      "COMILLADOBLE", "PARENTESIS_A", "PARENTESIS_C", "LLAVE_C", 
                      "LLAVE_A", "CORCHETE_A", "CORCHETE_C", "MASMAS", "MENOSMENOS", 
                      "POTENCIA", "MODULO", "WRITE", "OPEN", "ID", "STRING" ]

    RULE_start = 0
    RULE_sentencias = 1
    RULE_asignacion = 2
    RULE_v_input = 3
    RULE_comment = 4
    RULE_printf = 5
    RULE_var_casteo = 6
    RULE_casteo = 7
    RULE_cadena = 8
    RULE_funcion = 9
    RULE_stmt_func = 10
    RULE_v_return = 11
    RULE_llamafuncion = 12
    RULE_args = 13
    RULE_condicional = 14
    RULE_elifBlock = 15
    RULE_condicional_elif = 16
    RULE_condicional_else = 17
    RULE_ciclo_for = 18
    RULE_ciclo_while = 19
    RULE_parametro = 20
    RULE_func = 21
    RULE_expresion = 22
    RULE_matriz_operaciones = 23
    RULE_matriz = 24
    RULE_fila_matriz = 25
    RULE_importss = 26
    RULE_termino = 27
    RULE_lista = 28
    RULE_arreglo = 29
    RULE_graficas = 30
    RULE_arange = 31
    RULE_lectura_archivo = 32
    RULE_escritura_archivo = 33

    ruleNames =  [ "start", "sentencias", "asignacion", "v_input", "comment", 
                   "printf", "var_casteo", "casteo", "cadena", "funcion", 
                   "stmt_func", "v_return", "llamafuncion", "args", "condicional", 
                   "elifBlock", "condicional_elif", "condicional_else", 
                   "ciclo_for", "ciclo_while", "parametro", "func", "expresion", 
                   "matriz_operaciones", "matriz", "fila_matriz", "importss", 
                   "termino", "lista", "arreglo", "graficas", "arange", 
                   "lectura_archivo", "escritura_archivo" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    T__23=24
    T__24=25
    T__25=26
    T__26=27
    SEP=28
    ESP=29
    COMMENT=30
    NEWLINE=31
    TAB=32
    NUMERO=33
    WS=34
    IMPORT=35
    DEF=36
    CLASS=37
    IF=38
    ELSE=39
    FOR=40
    IN=41
    RANGE=42
    SELF=43
    WHILE=44
    TRY=45
    END=46
    EXCEPT=47
    RETURN=48
    BREAK=49
    NEXT=50
    INPUT=51
    PRINT=52
    INT=53
    FLOAT=54
    BOOLEAN=55
    STR=56
    POW=57
    MATHSQRT=58
    AND=59
    OR=60
    NOT=61
    ELIF=62
    SUMA=63
    ASIGNACION=64
    RESTA=65
    DIVISION=66
    MULTIPLICACION=67
    IGUAL=68
    DIFERENTE=69
    MAYORQUE=70
    MENORQUE=71
    MENORIGUAL=72
    MAYORIGUAL=73
    PUNTO=74
    COMA=75
    DOSPUNTOS=76
    PUNTOCOMA=77
    COMILLASIMPLE=78
    COMILLADOBLE=79
    PARENTESIS_A=80
    PARENTESIS_C=81
    LLAVE_C=82
    LLAVE_A=83
    CORCHETE_A=84
    CORCHETE_C=85
    MASMAS=86
    MENOSMENOS=87
    POTENCIA=88
    MODULO=89
    WRITE=90
    OPEN=91
    ID=92
    STRING=93

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class StartContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def sentencias(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramaticaParser.SentenciasContext)
            else:
                return self.getTypedRuleContext(gramaticaParser.SentenciasContext,i)


        def getRuleIndex(self):
            return gramaticaParser.RULE_start

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStart" ):
                listener.enterStart(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStart" ):
                listener.exitStart(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStart" ):
                return visitor.visitStart(self)
            else:
                return visitor.visitChildren(self)




    def start(self):

        localctx = gramaticaParser.StartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_start)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 69 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 68
                self.sentencias()
                self.state = 71 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 141882469795207174) != 0) or ((((_la - 80)) & ~0x3f) == 0 and ((1 << (_la - 80)) & 15377) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SentenciasContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def printf(self):
            return self.getTypedRuleContext(gramaticaParser.PrintfContext,0)


        def asignacion(self):
            return self.getTypedRuleContext(gramaticaParser.AsignacionContext,0)


        def llamafuncion(self):
            return self.getTypedRuleContext(gramaticaParser.LlamafuncionContext,0)


        def condicional(self):
            return self.getTypedRuleContext(gramaticaParser.CondicionalContext,0)


        def ciclo_while(self):
            return self.getTypedRuleContext(gramaticaParser.Ciclo_whileContext,0)


        def expresion(self):
            return self.getTypedRuleContext(gramaticaParser.ExpresionContext,0)


        def funcion(self):
            return self.getTypedRuleContext(gramaticaParser.FuncionContext,0)


        def ciclo_for(self):
            return self.getTypedRuleContext(gramaticaParser.Ciclo_forContext,0)


        def v_input(self):
            return self.getTypedRuleContext(gramaticaParser.V_inputContext,0)


        def casteo(self):
            return self.getTypedRuleContext(gramaticaParser.CasteoContext,0)


        def graficas(self):
            return self.getTypedRuleContext(gramaticaParser.GraficasContext,0)


        def importss(self):
            return self.getTypedRuleContext(gramaticaParser.ImportssContext,0)


        def func(self):
            return self.getTypedRuleContext(gramaticaParser.FuncContext,0)


        def matriz_operaciones(self):
            return self.getTypedRuleContext(gramaticaParser.Matriz_operacionesContext,0)


        def NEWLINE(self):
            return self.getToken(gramaticaParser.NEWLINE, 0)

        def lectura_archivo(self):
            return self.getTypedRuleContext(gramaticaParser.Lectura_archivoContext,0)


        def escritura_archivo(self):
            return self.getTypedRuleContext(gramaticaParser.Escritura_archivoContext,0)


        def comment(self):
            return self.getTypedRuleContext(gramaticaParser.CommentContext,0)


        def getRuleIndex(self):
            return gramaticaParser.RULE_sentencias

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSentencias" ):
                listener.enterSentencias(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSentencias" ):
                listener.exitSentencias(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSentencias" ):
                return visitor.visitSentencias(self)
            else:
                return visitor.visitChildren(self)




    def sentencias(self):

        localctx = gramaticaParser.SentenciasContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_sentencias)
        try:
            self.state = 91
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 73
                self.printf()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 74
                self.asignacion()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 75
                self.llamafuncion()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 76
                self.condicional()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 77
                self.ciclo_while()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 78
                self.expresion(0)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 79
                self.funcion()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 80
                self.ciclo_for()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 81
                self.v_input()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 82
                self.casteo()
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 83
                self.graficas()
                pass

            elif la_ == 12:
                self.enterOuterAlt(localctx, 12)
                self.state = 84
                self.importss()
                pass

            elif la_ == 13:
                self.enterOuterAlt(localctx, 13)
                self.state = 85
                self.func()
                pass

            elif la_ == 14:
                self.enterOuterAlt(localctx, 14)
                self.state = 86
                self.matriz_operaciones()
                pass

            elif la_ == 15:
                self.enterOuterAlt(localctx, 15)
                self.state = 87
                self.match(gramaticaParser.NEWLINE)
                pass

            elif la_ == 16:
                self.enterOuterAlt(localctx, 16)
                self.state = 88
                self.lectura_archivo()
                pass

            elif la_ == 17:
                self.enterOuterAlt(localctx, 17)
                self.state = 89
                self.escritura_archivo()
                pass

            elif la_ == 18:
                self.enterOuterAlt(localctx, 18)
                self.state = 90
                self.comment()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AsignacionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(gramaticaParser.ID)
            else:
                return self.getToken(gramaticaParser.ID, i)

        def ASIGNACION(self):
            return self.getToken(gramaticaParser.ASIGNACION, 0)

        def PUNTOCOMA(self):
            return self.getToken(gramaticaParser.PUNTOCOMA, 0)

        def expresion(self):
            return self.getTypedRuleContext(gramaticaParser.ExpresionContext,0)


        def v_input(self):
            return self.getTypedRuleContext(gramaticaParser.V_inputContext,0)


        def matriz_operaciones(self):
            return self.getTypedRuleContext(gramaticaParser.Matriz_operacionesContext,0)


        def arange(self):
            return self.getTypedRuleContext(gramaticaParser.ArangeContext,0)


        def var_casteo(self):
            return self.getTypedRuleContext(gramaticaParser.Var_casteoContext,0)


        def PARENTESIS_A(self):
            return self.getToken(gramaticaParser.PARENTESIS_A, 0)

        def PARENTESIS_C(self):
            return self.getToken(gramaticaParser.PARENTESIS_C, 0)

        def parametro(self):
            return self.getTypedRuleContext(gramaticaParser.ParametroContext,0)


        def cadena(self):
            return self.getTypedRuleContext(gramaticaParser.CadenaContext,0)


        def getRuleIndex(self):
            return gramaticaParser.RULE_asignacion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAsignacion" ):
                listener.enterAsignacion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAsignacion" ):
                listener.exitAsignacion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAsignacion" ):
                return visitor.visitAsignacion(self)
            else:
                return visitor.visitChildren(self)




    def asignacion(self):

        localctx = gramaticaParser.AsignacionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_asignacion)
        self._la = 0 # Token type
        try:
            self.state = 128
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 93
                self.match(gramaticaParser.ID)
                self.state = 94
                self.match(gramaticaParser.ASIGNACION)
                self.state = 96
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
                if la_ == 1:
                    self.state = 95
                    self.var_casteo()


                self.state = 99
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
                if la_ == 1:
                    self.state = 98
                    self.match(gramaticaParser.PARENTESIS_A)


                self.state = 105
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
                if la_ == 1:
                    self.state = 101
                    self.expresion(0)
                    pass

                elif la_ == 2:
                    self.state = 102
                    self.v_input()
                    pass

                elif la_ == 3:
                    self.state = 103
                    self.matriz_operaciones()
                    pass

                elif la_ == 4:
                    self.state = 104
                    self.arange()
                    pass


                self.state = 108
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==81:
                    self.state = 107
                    self.match(gramaticaParser.PARENTESIS_C)


                self.state = 110
                self.match(gramaticaParser.PUNTOCOMA)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 112
                self.match(gramaticaParser.ID)
                self.state = 113
                self.match(gramaticaParser.ASIGNACION)
                self.state = 114
                self.match(gramaticaParser.ID)
                self.state = 115
                self.match(gramaticaParser.PARENTESIS_A)
                self.state = 119
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
                if la_ == 1:
                    self.state = 116
                    self.parametro()

                elif la_ == 2:
                    self.state = 117
                    self.expresion(0)

                elif la_ == 3:
                    self.state = 118
                    self.matriz_operaciones()


                self.state = 121
                self.match(gramaticaParser.PARENTESIS_C)
                self.state = 122
                self.match(gramaticaParser.PUNTOCOMA)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 123
                self.match(gramaticaParser.ID)
                self.state = 124
                self.match(gramaticaParser.ASIGNACION)
                self.state = 125
                self.cadena()
                self.state = 126
                self.match(gramaticaParser.PUNTOCOMA)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class V_inputContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INPUT(self):
            return self.getToken(gramaticaParser.INPUT, 0)

        def PARENTESIS_A(self, i:int=None):
            if i is None:
                return self.getTokens(gramaticaParser.PARENTESIS_A)
            else:
                return self.getToken(gramaticaParser.PARENTESIS_A, i)

        def PARENTESIS_C(self, i:int=None):
            if i is None:
                return self.getTokens(gramaticaParser.PARENTESIS_C)
            else:
                return self.getToken(gramaticaParser.PARENTESIS_C, i)

        def var_casteo(self):
            return self.getTypedRuleContext(gramaticaParser.Var_casteoContext,0)


        def expresion(self):
            return self.getTypedRuleContext(gramaticaParser.ExpresionContext,0)


        def getRuleIndex(self):
            return gramaticaParser.RULE_v_input

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterV_input" ):
                listener.enterV_input(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitV_input" ):
                listener.exitV_input(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitV_input" ):
                return visitor.visitV_input(self)
            else:
                return visitor.visitChildren(self)




    def v_input(self):

        localctx = gramaticaParser.V_inputContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_v_input)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 131
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 135107988821114880) != 0):
                self.state = 130
                self.var_casteo()


            self.state = 134
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==80:
                self.state = 133
                self.match(gramaticaParser.PARENTESIS_A)


            self.state = 136
            self.match(gramaticaParser.INPUT)
            self.state = 137
            self.match(gramaticaParser.PARENTESIS_A)
            self.state = 139
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 36028805608898566) != 0) or ((((_la - 80)) & ~0x3f) == 0 and ((1 << (_la - 80)) & 12305) != 0):
                self.state = 138
                self.expresion(0)


            self.state = 141
            self.match(gramaticaParser.PARENTESIS_C)
            self.state = 143
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.state = 142
                self.match(gramaticaParser.PARENTESIS_C)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CommentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMENT(self):
            return self.getToken(gramaticaParser.COMMENT, 0)

        def getRuleIndex(self):
            return gramaticaParser.RULE_comment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComment" ):
                listener.enterComment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComment" ):
                listener.exitComment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComment" ):
                return visitor.visitComment(self)
            else:
                return visitor.visitChildren(self)




    def comment(self):

        localctx = gramaticaParser.CommentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_comment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 145
            self.match(gramaticaParser.COMMENT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrintfContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PRINT(self):
            return self.getToken(gramaticaParser.PRINT, 0)

        def PARENTESIS_A(self):
            return self.getToken(gramaticaParser.PARENTESIS_A, 0)

        def PARENTESIS_C(self):
            return self.getToken(gramaticaParser.PARENTESIS_C, 0)

        def PUNTOCOMA(self):
            return self.getToken(gramaticaParser.PUNTOCOMA, 0)

        def expresion(self):
            return self.getTypedRuleContext(gramaticaParser.ExpresionContext,0)


        def COMA(self):
            return self.getToken(gramaticaParser.COMA, 0)

        def matriz_operaciones(self):
            return self.getTypedRuleContext(gramaticaParser.Matriz_operacionesContext,0)


        def getRuleIndex(self):
            return gramaticaParser.RULE_printf

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrintf" ):
                listener.enterPrintf(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrintf" ):
                listener.exitPrintf(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrintf" ):
                return visitor.visitPrintf(self)
            else:
                return visitor.visitChildren(self)




    def printf(self):

        localctx = gramaticaParser.PrintfContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_printf)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 147
            self.match(gramaticaParser.PRINT)
            self.state = 148
            self.match(gramaticaParser.PARENTESIS_A)
            self.state = 152
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.state = 149
                self.expresion(0)

            elif la_ == 2:
                self.state = 150
                self.match(gramaticaParser.COMA)

            elif la_ == 3:
                self.state = 151
                self.matriz_operaciones()


            self.state = 154
            self.match(gramaticaParser.PARENTESIS_C)
            self.state = 155
            self.match(gramaticaParser.PUNTOCOMA)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_casteoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STR(self):
            return self.getToken(gramaticaParser.STR, 0)

        def INT(self):
            return self.getToken(gramaticaParser.INT, 0)

        def FLOAT(self):
            return self.getToken(gramaticaParser.FLOAT, 0)

        def BOOLEAN(self):
            return self.getToken(gramaticaParser.BOOLEAN, 0)

        def getRuleIndex(self):
            return gramaticaParser.RULE_var_casteo

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVar_casteo" ):
                listener.enterVar_casteo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVar_casteo" ):
                listener.exitVar_casteo(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_casteo" ):
                return visitor.visitVar_casteo(self)
            else:
                return visitor.visitChildren(self)




    def var_casteo(self):

        localctx = gramaticaParser.Var_casteoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_var_casteo)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 157
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 135107988821114880) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CasteoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_casteo(self):
            return self.getTypedRuleContext(gramaticaParser.Var_casteoContext,0)


        def PARENTESIS_A(self):
            return self.getToken(gramaticaParser.PARENTESIS_A, 0)

        def expresion(self):
            return self.getTypedRuleContext(gramaticaParser.ExpresionContext,0)


        def PARENTESIS_C(self):
            return self.getToken(gramaticaParser.PARENTESIS_C, 0)

        def getRuleIndex(self):
            return gramaticaParser.RULE_casteo

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCasteo" ):
                listener.enterCasteo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCasteo" ):
                listener.exitCasteo(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCasteo" ):
                return visitor.visitCasteo(self)
            else:
                return visitor.visitChildren(self)




    def casteo(self):

        localctx = gramaticaParser.CasteoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_casteo)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 159
            self.var_casteo()
            self.state = 160
            self.match(gramaticaParser.PARENTESIS_A)
            self.state = 161
            self.expresion(0)
            self.state = 162
            self.match(gramaticaParser.PARENTESIS_C)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CadenaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(gramaticaParser.STRING, 0)

        def getRuleIndex(self):
            return gramaticaParser.RULE_cadena

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCadena" ):
                listener.enterCadena(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCadena" ):
                listener.exitCadena(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCadena" ):
                return visitor.visitCadena(self)
            else:
                return visitor.visitChildren(self)




    def cadena(self):

        localctx = gramaticaParser.CadenaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_cadena)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 164
            self.match(gramaticaParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DEF(self):
            return self.getToken(gramaticaParser.DEF, 0)

        def ID(self):
            return self.getToken(gramaticaParser.ID, 0)

        def PARENTESIS_A(self):
            return self.getToken(gramaticaParser.PARENTESIS_A, 0)

        def PARENTESIS_C(self):
            return self.getToken(gramaticaParser.PARENTESIS_C, 0)

        def LLAVE_A(self):
            return self.getToken(gramaticaParser.LLAVE_A, 0)

        def stmt_func(self):
            return self.getTypedRuleContext(gramaticaParser.Stmt_funcContext,0)


        def LLAVE_C(self):
            return self.getToken(gramaticaParser.LLAVE_C, 0)

        def parametro(self):
            return self.getTypedRuleContext(gramaticaParser.ParametroContext,0)


        def getRuleIndex(self):
            return gramaticaParser.RULE_funcion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFuncion" ):
                listener.enterFuncion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFuncion" ):
                listener.exitFuncion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncion" ):
                return visitor.visitFuncion(self)
            else:
                return visitor.visitChildren(self)




    def funcion(self):

        localctx = gramaticaParser.FuncionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_funcion)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 166
            self.match(gramaticaParser.DEF)
            self.state = 167
            self.match(gramaticaParser.ID)
            self.state = 168
            self.match(gramaticaParser.PARENTESIS_A)
            self.state = 170
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==92:
                self.state = 169
                self.parametro()


            self.state = 172
            self.match(gramaticaParser.PARENTESIS_C)
            self.state = 173
            self.match(gramaticaParser.LLAVE_A)
            self.state = 174
            self.stmt_func()
            self.state = 175
            self.match(gramaticaParser.LLAVE_C)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Stmt_funcContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def sentencias(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramaticaParser.SentenciasContext)
            else:
                return self.getTypedRuleContext(gramaticaParser.SentenciasContext,i)


        def v_return(self):
            return self.getTypedRuleContext(gramaticaParser.V_returnContext,0)


        def getRuleIndex(self):
            return gramaticaParser.RULE_stmt_func

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStmt_func" ):
                listener.enterStmt_func(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStmt_func" ):
                listener.exitStmt_func(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt_func" ):
                return visitor.visitStmt_func(self)
            else:
                return visitor.visitChildren(self)




    def stmt_func(self):

        localctx = gramaticaParser.Stmt_funcContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_stmt_func)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 180
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 141882469795207174) != 0) or ((((_la - 80)) & ~0x3f) == 0 and ((1 << (_la - 80)) & 15377) != 0):
                self.state = 177
                self.sentencias()
                self.state = 182
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 184
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==48:
                self.state = 183
                self.v_return()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class V_returnContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(gramaticaParser.RETURN, 0)

        def expresion(self):
            return self.getTypedRuleContext(gramaticaParser.ExpresionContext,0)


        def PUNTOCOMA(self):
            return self.getToken(gramaticaParser.PUNTOCOMA, 0)

        def getRuleIndex(self):
            return gramaticaParser.RULE_v_return

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterV_return" ):
                listener.enterV_return(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitV_return" ):
                listener.exitV_return(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitV_return" ):
                return visitor.visitV_return(self)
            else:
                return visitor.visitChildren(self)




    def v_return(self):

        localctx = gramaticaParser.V_returnContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_v_return)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 186
            self.match(gramaticaParser.RETURN)
            self.state = 187
            self.expresion(0)
            self.state = 188
            self.match(gramaticaParser.PUNTOCOMA)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LlamafuncionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(gramaticaParser.ID, 0)

        def PARENTESIS_A(self):
            return self.getToken(gramaticaParser.PARENTESIS_A, 0)

        def PARENTESIS_C(self):
            return self.getToken(gramaticaParser.PARENTESIS_C, 0)

        def args(self):
            return self.getTypedRuleContext(gramaticaParser.ArgsContext,0)


        def getRuleIndex(self):
            return gramaticaParser.RULE_llamafuncion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLlamafuncion" ):
                listener.enterLlamafuncion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLlamafuncion" ):
                listener.exitLlamafuncion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLlamafuncion" ):
                return visitor.visitLlamafuncion(self)
            else:
                return visitor.visitChildren(self)




    def llamafuncion(self):

        localctx = gramaticaParser.LlamafuncionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_llamafuncion)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 190
            self.match(gramaticaParser.ID)
            self.state = 191
            self.match(gramaticaParser.PARENTESIS_A)
            self.state = 193
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 33)) & ~0x3f) == 0 and ((1 << (_la - 33)) & 1731774794216505345) != 0):
                self.state = 192
                self.args()


            self.state = 195
            self.match(gramaticaParser.PARENTESIS_C)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def termino(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramaticaParser.TerminoContext)
            else:
                return self.getTypedRuleContext(gramaticaParser.TerminoContext,i)


        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(gramaticaParser.ID)
            else:
                return self.getToken(gramaticaParser.ID, i)

        def llamafuncion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramaticaParser.LlamafuncionContext)
            else:
                return self.getTypedRuleContext(gramaticaParser.LlamafuncionContext,i)


        def COMA(self, i:int=None):
            if i is None:
                return self.getTokens(gramaticaParser.COMA)
            else:
                return self.getToken(gramaticaParser.COMA, i)

        def getRuleIndex(self):
            return gramaticaParser.RULE_args

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArgs" ):
                listener.enterArgs(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArgs" ):
                listener.exitArgs(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgs" ):
                return visitor.visitArgs(self)
            else:
                return visitor.visitChildren(self)




    def args(self):

        localctx = gramaticaParser.ArgsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_args)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 200
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.state = 197
                self.termino()
                pass

            elif la_ == 2:
                self.state = 198
                self.match(gramaticaParser.ID)
                pass

            elif la_ == 3:
                self.state = 199
                self.llamafuncion()
                pass


            self.state = 210
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==75:
                self.state = 202
                self.match(gramaticaParser.COMA)
                self.state = 206
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
                if la_ == 1:
                    self.state = 203
                    self.termino()
                    pass

                elif la_ == 2:
                    self.state = 204
                    self.match(gramaticaParser.ID)
                    pass

                elif la_ == 3:
                    self.state = 205
                    self.llamafuncion()
                    pass


                self.state = 212
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CondicionalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(gramaticaParser.IF, 0)

        def PARENTESIS_A(self):
            return self.getToken(gramaticaParser.PARENTESIS_A, 0)

        def PARENTESIS_C(self):
            return self.getToken(gramaticaParser.PARENTESIS_C, 0)

        def LLAVE_A(self):
            return self.getToken(gramaticaParser.LLAVE_A, 0)

        def LLAVE_C(self):
            return self.getToken(gramaticaParser.LLAVE_C, 0)

        def parametro(self):
            return self.getTypedRuleContext(gramaticaParser.ParametroContext,0)


        def expresion(self):
            return self.getTypedRuleContext(gramaticaParser.ExpresionContext,0)


        def sentencias(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramaticaParser.SentenciasContext)
            else:
                return self.getTypedRuleContext(gramaticaParser.SentenciasContext,i)


        def elifBlock(self):
            return self.getTypedRuleContext(gramaticaParser.ElifBlockContext,0)


        def condicional_else(self):
            return self.getTypedRuleContext(gramaticaParser.Condicional_elseContext,0)


        def getRuleIndex(self):
            return gramaticaParser.RULE_condicional

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondicional" ):
                listener.enterCondicional(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondicional" ):
                listener.exitCondicional(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondicional" ):
                return visitor.visitCondicional(self)
            else:
                return visitor.visitChildren(self)




    def condicional(self):

        localctx = gramaticaParser.CondicionalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_condicional)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 213
            self.match(gramaticaParser.IF)
            self.state = 214
            self.match(gramaticaParser.PARENTESIS_A)
            self.state = 217
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.state = 215
                self.parametro()
                pass

            elif la_ == 2:
                self.state = 216
                self.expresion(0)
                pass


            self.state = 219
            self.match(gramaticaParser.PARENTESIS_C)
            self.state = 220
            self.match(gramaticaParser.LLAVE_A)
            self.state = 224
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 141882469795207174) != 0) or ((((_la - 80)) & ~0x3f) == 0 and ((1 << (_la - 80)) & 15377) != 0):
                self.state = 221
                self.sentencias()
                self.state = 226
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 227
            self.match(gramaticaParser.LLAVE_C)
            self.state = 229
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==62:
                self.state = 228
                self.elifBlock()


            self.state = 232
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==39:
                self.state = 231
                self.condicional_else()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElifBlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def condicional_elif(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramaticaParser.Condicional_elifContext)
            else:
                return self.getTypedRuleContext(gramaticaParser.Condicional_elifContext,i)


        def getRuleIndex(self):
            return gramaticaParser.RULE_elifBlock

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElifBlock" ):
                listener.enterElifBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElifBlock" ):
                listener.exitElifBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElifBlock" ):
                return visitor.visitElifBlock(self)
            else:
                return visitor.visitChildren(self)




    def elifBlock(self):

        localctx = gramaticaParser.ElifBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_elifBlock)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 235 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 234
                self.condicional_elif()
                self.state = 237 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==62):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Condicional_elifContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELIF(self):
            return self.getToken(gramaticaParser.ELIF, 0)

        def PARENTESIS_A(self):
            return self.getToken(gramaticaParser.PARENTESIS_A, 0)

        def PARENTESIS_C(self):
            return self.getToken(gramaticaParser.PARENTESIS_C, 0)

        def LLAVE_A(self):
            return self.getToken(gramaticaParser.LLAVE_A, 0)

        def LLAVE_C(self):
            return self.getToken(gramaticaParser.LLAVE_C, 0)

        def parametro(self):
            return self.getTypedRuleContext(gramaticaParser.ParametroContext,0)


        def expresion(self):
            return self.getTypedRuleContext(gramaticaParser.ExpresionContext,0)


        def sentencias(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramaticaParser.SentenciasContext)
            else:
                return self.getTypedRuleContext(gramaticaParser.SentenciasContext,i)


        def getRuleIndex(self):
            return gramaticaParser.RULE_condicional_elif

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondicional_elif" ):
                listener.enterCondicional_elif(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondicional_elif" ):
                listener.exitCondicional_elif(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondicional_elif" ):
                return visitor.visitCondicional_elif(self)
            else:
                return visitor.visitChildren(self)




    def condicional_elif(self):

        localctx = gramaticaParser.Condicional_elifContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_condicional_elif)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 239
            self.match(gramaticaParser.ELIF)
            self.state = 240
            self.match(gramaticaParser.PARENTESIS_A)
            self.state = 243
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.state = 241
                self.parametro()
                pass

            elif la_ == 2:
                self.state = 242
                self.expresion(0)
                pass


            self.state = 245
            self.match(gramaticaParser.PARENTESIS_C)
            self.state = 246
            self.match(gramaticaParser.LLAVE_A)
            self.state = 250
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 141882469795207174) != 0) or ((((_la - 80)) & ~0x3f) == 0 and ((1 << (_la - 80)) & 15377) != 0):
                self.state = 247
                self.sentencias()
                self.state = 252
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 253
            self.match(gramaticaParser.LLAVE_C)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Condicional_elseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(gramaticaParser.ELSE, 0)

        def LLAVE_A(self):
            return self.getToken(gramaticaParser.LLAVE_A, 0)

        def LLAVE_C(self):
            return self.getToken(gramaticaParser.LLAVE_C, 0)

        def sentencias(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramaticaParser.SentenciasContext)
            else:
                return self.getTypedRuleContext(gramaticaParser.SentenciasContext,i)


        def getRuleIndex(self):
            return gramaticaParser.RULE_condicional_else

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondicional_else" ):
                listener.enterCondicional_else(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondicional_else" ):
                listener.exitCondicional_else(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondicional_else" ):
                return visitor.visitCondicional_else(self)
            else:
                return visitor.visitChildren(self)




    def condicional_else(self):

        localctx = gramaticaParser.Condicional_elseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_condicional_else)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 255
            self.match(gramaticaParser.ELSE)
            self.state = 256
            self.match(gramaticaParser.LLAVE_A)
            self.state = 260
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 141882469795207174) != 0) or ((((_la - 80)) & ~0x3f) == 0 and ((1 << (_la - 80)) & 15377) != 0):
                self.state = 257
                self.sentencias()
                self.state = 262
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 263
            self.match(gramaticaParser.LLAVE_C)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Ciclo_forContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(gramaticaParser.FOR, 0)

        def ID(self):
            return self.getToken(gramaticaParser.ID, 0)

        def IN(self):
            return self.getToken(gramaticaParser.IN, 0)

        def RANGE(self):
            return self.getToken(gramaticaParser.RANGE, 0)

        def PARENTESIS_A(self):
            return self.getToken(gramaticaParser.PARENTESIS_A, 0)

        def expresion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramaticaParser.ExpresionContext)
            else:
                return self.getTypedRuleContext(gramaticaParser.ExpresionContext,i)


        def PARENTESIS_C(self):
            return self.getToken(gramaticaParser.PARENTESIS_C, 0)

        def LLAVE_A(self):
            return self.getToken(gramaticaParser.LLAVE_A, 0)

        def LLAVE_C(self):
            return self.getToken(gramaticaParser.LLAVE_C, 0)

        def COMA(self, i:int=None):
            if i is None:
                return self.getTokens(gramaticaParser.COMA)
            else:
                return self.getToken(gramaticaParser.COMA, i)

        def sentencias(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramaticaParser.SentenciasContext)
            else:
                return self.getTypedRuleContext(gramaticaParser.SentenciasContext,i)


        def v_return(self):
            return self.getTypedRuleContext(gramaticaParser.V_returnContext,0)


        def cadena(self):
            return self.getTypedRuleContext(gramaticaParser.CadenaContext,0)


        def getRuleIndex(self):
            return gramaticaParser.RULE_ciclo_for

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCiclo_for" ):
                listener.enterCiclo_for(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCiclo_for" ):
                listener.exitCiclo_for(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCiclo_for" ):
                return visitor.visitCiclo_for(self)
            else:
                return visitor.visitChildren(self)




    def ciclo_for(self):

        localctx = gramaticaParser.Ciclo_forContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_ciclo_for)
        self._la = 0 # Token type
        try:
            self.state = 325
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 265
                self.match(gramaticaParser.FOR)
                self.state = 266
                self.match(gramaticaParser.ID)
                self.state = 267
                self.match(gramaticaParser.IN)
                self.state = 268
                self.match(gramaticaParser.RANGE)
                self.state = 269
                self.match(gramaticaParser.PARENTESIS_A)
                self.state = 270
                self.expresion(0)
                self.state = 272
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
                if la_ == 1:
                    self.state = 271
                    self.match(gramaticaParser.COMA)


                self.state = 275
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
                if la_ == 1:
                    self.state = 274
                    self.expresion(0)


                self.state = 278
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==75:
                    self.state = 277
                    self.match(gramaticaParser.COMA)


                self.state = 281
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 36028805608898566) != 0) or ((((_la - 80)) & ~0x3f) == 0 and ((1 << (_la - 80)) & 12305) != 0):
                    self.state = 280
                    self.expresion(0)


                self.state = 283
                self.match(gramaticaParser.PARENTESIS_C)
                self.state = 284
                self.match(gramaticaParser.LLAVE_A)
                self.state = 286 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 285
                    self.sentencias()
                    self.state = 288 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 141882469795207174) != 0) or ((((_la - 80)) & ~0x3f) == 0 and ((1 << (_la - 80)) & 15377) != 0)):
                        break

                self.state = 291
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==48:
                    self.state = 290
                    self.v_return()


                self.state = 293
                self.match(gramaticaParser.LLAVE_C)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 295
                self.match(gramaticaParser.FOR)
                self.state = 296
                self.match(gramaticaParser.ID)
                self.state = 297
                self.match(gramaticaParser.IN)
                self.state = 298
                self.expresion(0)
                self.state = 299
                self.match(gramaticaParser.LLAVE_A)
                self.state = 301 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 300
                    self.sentencias()
                    self.state = 303 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 141882469795207174) != 0) or ((((_la - 80)) & ~0x3f) == 0 and ((1 << (_la - 80)) & 15377) != 0)):
                        break

                self.state = 306
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==48:
                    self.state = 305
                    self.v_return()


                self.state = 308
                self.match(gramaticaParser.LLAVE_C)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 310
                self.match(gramaticaParser.FOR)
                self.state = 311
                self.match(gramaticaParser.ID)
                self.state = 312
                self.match(gramaticaParser.IN)
                self.state = 313
                self.cadena()
                self.state = 314
                self.match(gramaticaParser.LLAVE_A)
                self.state = 316 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 315
                    self.sentencias()
                    self.state = 318 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 141882469795207174) != 0) or ((((_la - 80)) & ~0x3f) == 0 and ((1 << (_la - 80)) & 15377) != 0)):
                        break

                self.state = 321
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==48:
                    self.state = 320
                    self.v_return()


                self.state = 323
                self.match(gramaticaParser.LLAVE_C)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Ciclo_whileContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(gramaticaParser.WHILE, 0)

        def expresion(self):
            return self.getTypedRuleContext(gramaticaParser.ExpresionContext,0)


        def LLAVE_A(self):
            return self.getToken(gramaticaParser.LLAVE_A, 0)

        def LLAVE_C(self):
            return self.getToken(gramaticaParser.LLAVE_C, 0)

        def PARENTESIS_A(self):
            return self.getToken(gramaticaParser.PARENTESIS_A, 0)

        def PARENTESIS_C(self):
            return self.getToken(gramaticaParser.PARENTESIS_C, 0)

        def sentencias(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramaticaParser.SentenciasContext)
            else:
                return self.getTypedRuleContext(gramaticaParser.SentenciasContext,i)


        def getRuleIndex(self):
            return gramaticaParser.RULE_ciclo_while

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCiclo_while" ):
                listener.enterCiclo_while(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCiclo_while" ):
                listener.exitCiclo_while(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCiclo_while" ):
                return visitor.visitCiclo_while(self)
            else:
                return visitor.visitChildren(self)




    def ciclo_while(self):

        localctx = gramaticaParser.Ciclo_whileContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_ciclo_while)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 327
            self.match(gramaticaParser.WHILE)
            self.state = 329
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,39,self._ctx)
            if la_ == 1:
                self.state = 328
                self.match(gramaticaParser.PARENTESIS_A)


            self.state = 331
            self.expresion(0)
            self.state = 333
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==81:
                self.state = 332
                self.match(gramaticaParser.PARENTESIS_C)


            self.state = 335
            self.match(gramaticaParser.LLAVE_A)
            self.state = 337 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 336
                self.sentencias()
                self.state = 339 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 141882469795207174) != 0) or ((((_la - 80)) & ~0x3f) == 0 and ((1 << (_la - 80)) & 15377) != 0)):
                    break

            self.state = 341
            self.match(gramaticaParser.LLAVE_C)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParametroContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(gramaticaParser.ID)
            else:
                return self.getToken(gramaticaParser.ID, i)

        def COMA(self, i:int=None):
            if i is None:
                return self.getTokens(gramaticaParser.COMA)
            else:
                return self.getToken(gramaticaParser.COMA, i)

        def getRuleIndex(self):
            return gramaticaParser.RULE_parametro

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParametro" ):
                listener.enterParametro(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParametro" ):
                listener.exitParametro(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParametro" ):
                return visitor.visitParametro(self)
            else:
                return visitor.visitChildren(self)




    def parametro(self):

        localctx = gramaticaParser.ParametroContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_parametro)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 343
            self.match(gramaticaParser.ID)
            self.state = 348
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==75:
                self.state = 344
                self.match(gramaticaParser.COMA)
                self.state = 345
                self.match(gramaticaParser.ID)
                self.state = 350
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PUNTO(self):
            return self.getToken(gramaticaParser.PUNTO, 0)

        def PARENTESIS_A(self):
            return self.getToken(gramaticaParser.PARENTESIS_A, 0)

        def expresion(self):
            return self.getTypedRuleContext(gramaticaParser.ExpresionContext,0)


        def PARENTESIS_C(self):
            return self.getToken(gramaticaParser.PARENTESIS_C, 0)

        def getRuleIndex(self):
            return gramaticaParser.RULE_func

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunc" ):
                listener.enterFunc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunc" ):
                listener.exitFunc(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc" ):
                return visitor.visitFunc(self)
            else:
                return visitor.visitChildren(self)




    def func(self):

        localctx = gramaticaParser.FuncContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_func)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 351
            _la = self._input.LA(1)
            if not(_la==1 or _la==2):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 352
            self.match(gramaticaParser.PUNTO)
            self.state = 353
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 2040) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 354
            self.match(gramaticaParser.PARENTESIS_A)
            self.state = 355
            self.expresion(0)
            self.state = 356
            self.match(gramaticaParser.PARENTESIS_C)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpresionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def termino(self):
            return self.getTypedRuleContext(gramaticaParser.TerminoContext,0)


        def llamafuncion(self):
            return self.getTypedRuleContext(gramaticaParser.LlamafuncionContext,0)


        def func(self):
            return self.getTypedRuleContext(gramaticaParser.FuncContext,0)


        def expresion(self):
            return self.getTypedRuleContext(gramaticaParser.ExpresionContext,0)


        def SUMA(self):
            return self.getToken(gramaticaParser.SUMA, 0)

        def RESTA(self):
            return self.getToken(gramaticaParser.RESTA, 0)

        def MULTIPLICACION(self):
            return self.getToken(gramaticaParser.MULTIPLICACION, 0)

        def DIVISION(self):
            return self.getToken(gramaticaParser.DIVISION, 0)

        def POTENCIA(self):
            return self.getToken(gramaticaParser.POTENCIA, 0)

        def MODULO(self):
            return self.getToken(gramaticaParser.MODULO, 0)

        def MAYORQUE(self):
            return self.getToken(gramaticaParser.MAYORQUE, 0)

        def MENORQUE(self):
            return self.getToken(gramaticaParser.MENORQUE, 0)

        def MENORIGUAL(self):
            return self.getToken(gramaticaParser.MENORIGUAL, 0)

        def MAYORIGUAL(self):
            return self.getToken(gramaticaParser.MAYORIGUAL, 0)

        def DIFERENTE(self):
            return self.getToken(gramaticaParser.DIFERENTE, 0)

        def IGUAL(self):
            return self.getToken(gramaticaParser.IGUAL, 0)

        def ASIGNACION(self):
            return self.getToken(gramaticaParser.ASIGNACION, 0)

        def OR(self):
            return self.getToken(gramaticaParser.OR, 0)

        def AND(self):
            return self.getToken(gramaticaParser.AND, 0)

        def getRuleIndex(self):
            return gramaticaParser.RULE_expresion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpresion" ):
                listener.enterExpresion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpresion" ):
                listener.exitExpresion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpresion" ):
                return visitor.visitExpresion(self)
            else:
                return visitor.visitChildren(self)



    def expresion(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = gramaticaParser.ExpresionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 44
        self.enterRecursionRule(localctx, 44, self.RULE_expresion, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 362
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,43,self._ctx)
            if la_ == 1:
                self.state = 359
                self.termino()
                pass

            elif la_ == 2:
                self.state = 360
                self.llamafuncion()
                pass

            elif la_ == 3:
                self.state = 361
                self.func()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 375
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,45,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 373
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,44,self._ctx)
                    if la_ == 1:
                        localctx = gramaticaParser.ExpresionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expresion)
                        self.state = 364
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 365
                        _la = self._input.LA(1)
                        if not(((((_la - 63)) & ~0x3f) == 0 and ((1 << (_la - 63)) & 100663325) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 366
                        self.termino()
                        pass

                    elif la_ == 2:
                        localctx = gramaticaParser.ExpresionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expresion)
                        self.state = 367
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 368
                        _la = self._input.LA(1)
                        if not(((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & 1009) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 369
                        self.termino()
                        pass

                    elif la_ == 3:
                        localctx = gramaticaParser.ExpresionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expresion)
                        self.state = 370
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 371
                        _la = self._input.LA(1)
                        if not(_la==59 or _la==60):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 372
                        self.termino()
                        pass

             
                self.state = 377
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,45,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Matriz_operacionesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def matriz(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramaticaParser.MatrizContext)
            else:
                return self.getTypedRuleContext(gramaticaParser.MatrizContext,i)


        def SUMA(self):
            return self.getToken(gramaticaParser.SUMA, 0)

        def RESTA(self):
            return self.getToken(gramaticaParser.RESTA, 0)

        def MULTIPLICACION(self):
            return self.getToken(gramaticaParser.MULTIPLICACION, 0)

        def PARENTESIS_A(self):
            return self.getToken(gramaticaParser.PARENTESIS_A, 0)

        def PARENTESIS_C(self):
            return self.getToken(gramaticaParser.PARENTESIS_C, 0)

        def getRuleIndex(self):
            return gramaticaParser.RULE_matriz_operaciones

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMatriz_operaciones" ):
                listener.enterMatriz_operaciones(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMatriz_operaciones" ):
                listener.exitMatriz_operaciones(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMatriz_operaciones" ):
                return visitor.visitMatriz_operaciones(self)
            else:
                return visitor.visitChildren(self)




    def matriz_operaciones(self):

        localctx = gramaticaParser.Matriz_operacionesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_matriz_operaciones)
        self._la = 0 # Token type
        try:
            self.state = 403
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,48,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 378
                self.matriz()
                self.state = 380
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==63:
                    self.state = 379
                    self.match(gramaticaParser.SUMA)


                self.state = 383
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,47,self._ctx)
                if la_ == 1:
                    self.state = 382
                    self.matriz()


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 385
                self.matriz()
                self.state = 386
                self.match(gramaticaParser.RESTA)
                self.state = 387
                self.matriz()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 389
                self.matriz()
                self.state = 390
                self.match(gramaticaParser.MULTIPLICACION)
                self.state = 391
                self.matriz()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 393
                self.match(gramaticaParser.T__10)
                self.state = 394
                self.match(gramaticaParser.PARENTESIS_A)
                self.state = 395
                self.matriz()
                self.state = 396
                self.match(gramaticaParser.PARENTESIS_C)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 398
                self.match(gramaticaParser.T__11)
                self.state = 399
                self.match(gramaticaParser.PARENTESIS_A)
                self.state = 400
                self.matriz()
                self.state = 401
                self.match(gramaticaParser.PARENTESIS_C)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MatrizContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CORCHETE_A(self):
            return self.getToken(gramaticaParser.CORCHETE_A, 0)

        def fila_matriz(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramaticaParser.Fila_matrizContext)
            else:
                return self.getTypedRuleContext(gramaticaParser.Fila_matrizContext,i)


        def CORCHETE_C(self):
            return self.getToken(gramaticaParser.CORCHETE_C, 0)

        def COMA(self, i:int=None):
            if i is None:
                return self.getTokens(gramaticaParser.COMA)
            else:
                return self.getToken(gramaticaParser.COMA, i)

        def getRuleIndex(self):
            return gramaticaParser.RULE_matriz

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMatriz" ):
                listener.enterMatriz(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMatriz" ):
                listener.exitMatriz(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMatriz" ):
                return visitor.visitMatriz(self)
            else:
                return visitor.visitChildren(self)




    def matriz(self):

        localctx = gramaticaParser.MatrizContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_matriz)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 405
            self.match(gramaticaParser.CORCHETE_A)
            self.state = 406
            self.fila_matriz()
            self.state = 411
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==75:
                self.state = 407
                self.match(gramaticaParser.COMA)
                self.state = 408
                self.fila_matriz()
                self.state = 413
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 414
            self.match(gramaticaParser.CORCHETE_C)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Fila_matrizContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CORCHETE_A(self):
            return self.getToken(gramaticaParser.CORCHETE_A, 0)

        def expresion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramaticaParser.ExpresionContext)
            else:
                return self.getTypedRuleContext(gramaticaParser.ExpresionContext,i)


        def CORCHETE_C(self):
            return self.getToken(gramaticaParser.CORCHETE_C, 0)

        def COMA(self, i:int=None):
            if i is None:
                return self.getTokens(gramaticaParser.COMA)
            else:
                return self.getToken(gramaticaParser.COMA, i)

        def getRuleIndex(self):
            return gramaticaParser.RULE_fila_matriz

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFila_matriz" ):
                listener.enterFila_matriz(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFila_matriz" ):
                listener.exitFila_matriz(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFila_matriz" ):
                return visitor.visitFila_matriz(self)
            else:
                return visitor.visitChildren(self)




    def fila_matriz(self):

        localctx = gramaticaParser.Fila_matrizContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_fila_matriz)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 416
            self.match(gramaticaParser.CORCHETE_A)
            self.state = 417
            self.expresion(0)
            self.state = 422
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==75:
                self.state = 418
                self.match(gramaticaParser.COMA)
                self.state = 419
                self.expresion(0)
                self.state = 424
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 425
            self.match(gramaticaParser.CORCHETE_C)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ImportssContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IMPORT(self):
            return self.getToken(gramaticaParser.IMPORT, 0)

        def getRuleIndex(self):
            return gramaticaParser.RULE_importss

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterImportss" ):
                listener.enterImportss(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitImportss" ):
                listener.exitImportss(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitImportss" ):
                return visitor.visitImportss(self)
            else:
                return visitor.visitChildren(self)




    def importss(self):

        localctx = gramaticaParser.ImportssContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_importss)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 427
            self.match(gramaticaParser.IMPORT)
            self.state = 428
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 24578) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TerminoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMERO(self):
            return self.getToken(gramaticaParser.NUMERO, 0)

        def ID(self):
            return self.getToken(gramaticaParser.ID, 0)

        def BOOLEAN(self):
            return self.getToken(gramaticaParser.BOOLEAN, 0)

        def cadena(self):
            return self.getTypedRuleContext(gramaticaParser.CadenaContext,0)


        def lista(self):
            return self.getTypedRuleContext(gramaticaParser.ListaContext,0)


        def arreglo(self):
            return self.getTypedRuleContext(gramaticaParser.ArregloContext,0)


        def getRuleIndex(self):
            return gramaticaParser.RULE_termino

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTermino" ):
                listener.enterTermino(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTermino" ):
                listener.exitTermino(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTermino" ):
                return visitor.visitTermino(self)
            else:
                return visitor.visitChildren(self)




    def termino(self):

        localctx = gramaticaParser.TerminoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_termino)
        try:
            self.state = 436
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [33]:
                self.enterOuterAlt(localctx, 1)
                self.state = 430
                self.match(gramaticaParser.NUMERO)
                pass
            elif token in [92]:
                self.enterOuterAlt(localctx, 2)
                self.state = 431
                self.match(gramaticaParser.ID)
                pass
            elif token in [55]:
                self.enterOuterAlt(localctx, 3)
                self.state = 432
                self.match(gramaticaParser.BOOLEAN)
                pass
            elif token in [93]:
                self.enterOuterAlt(localctx, 4)
                self.state = 433
                self.cadena()
                pass
            elif token in [80]:
                self.enterOuterAlt(localctx, 5)
                self.state = 434
                self.lista()
                pass
            elif token in [84]:
                self.enterOuterAlt(localctx, 6)
                self.state = 435
                self.arreglo()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ListaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PARENTESIS_A(self):
            return self.getToken(gramaticaParser.PARENTESIS_A, 0)

        def PARENTESIS_C(self):
            return self.getToken(gramaticaParser.PARENTESIS_C, 0)

        def NUMERO(self, i:int=None):
            if i is None:
                return self.getTokens(gramaticaParser.NUMERO)
            else:
                return self.getToken(gramaticaParser.NUMERO, i)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(gramaticaParser.ID)
            else:
                return self.getToken(gramaticaParser.ID, i)

        def BOOLEAN(self, i:int=None):
            if i is None:
                return self.getTokens(gramaticaParser.BOOLEAN)
            else:
                return self.getToken(gramaticaParser.BOOLEAN, i)

        def cadena(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramaticaParser.CadenaContext)
            else:
                return self.getTypedRuleContext(gramaticaParser.CadenaContext,i)


        def COMA(self, i:int=None):
            if i is None:
                return self.getTokens(gramaticaParser.COMA)
            else:
                return self.getToken(gramaticaParser.COMA, i)

        def getRuleIndex(self):
            return gramaticaParser.RULE_lista

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLista" ):
                listener.enterLista(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLista" ):
                listener.exitLista(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLista" ):
                return visitor.visitLista(self)
            else:
                return visitor.visitChildren(self)




    def lista(self):

        localctx = gramaticaParser.ListaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_lista)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 438
            self.match(gramaticaParser.PARENTESIS_A)
            self.state = 444 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 444
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [33]:
                    self.state = 439
                    self.match(gramaticaParser.NUMERO)
                    pass
                elif token in [92]:
                    self.state = 440
                    self.match(gramaticaParser.ID)
                    pass
                elif token in [55]:
                    self.state = 441
                    self.match(gramaticaParser.BOOLEAN)
                    pass
                elif token in [93]:
                    self.state = 442
                    self.cadena()
                    pass
                elif token in [75]:
                    self.state = 443
                    self.match(gramaticaParser.COMA)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 446 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (((((_la - 33)) & ~0x3f) == 0 and ((1 << (_la - 33)) & 1729386654960975873) != 0)):
                    break

            self.state = 448
            self.match(gramaticaParser.PARENTESIS_C)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArregloContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CORCHETE_A(self):
            return self.getToken(gramaticaParser.CORCHETE_A, 0)

        def CORCHETE_C(self):
            return self.getToken(gramaticaParser.CORCHETE_C, 0)

        def NUMERO(self, i:int=None):
            if i is None:
                return self.getTokens(gramaticaParser.NUMERO)
            else:
                return self.getToken(gramaticaParser.NUMERO, i)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(gramaticaParser.ID)
            else:
                return self.getToken(gramaticaParser.ID, i)

        def BOOLEAN(self, i:int=None):
            if i is None:
                return self.getTokens(gramaticaParser.BOOLEAN)
            else:
                return self.getToken(gramaticaParser.BOOLEAN, i)

        def cadena(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramaticaParser.CadenaContext)
            else:
                return self.getTypedRuleContext(gramaticaParser.CadenaContext,i)


        def COMA(self, i:int=None):
            if i is None:
                return self.getTokens(gramaticaParser.COMA)
            else:
                return self.getToken(gramaticaParser.COMA, i)

        def getRuleIndex(self):
            return gramaticaParser.RULE_arreglo

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArreglo" ):
                listener.enterArreglo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArreglo" ):
                listener.exitArreglo(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArreglo" ):
                return visitor.visitArreglo(self)
            else:
                return visitor.visitChildren(self)




    def arreglo(self):

        localctx = gramaticaParser.ArregloContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_arreglo)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 450
            self.match(gramaticaParser.CORCHETE_A)
            self.state = 456 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 456
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [33]:
                    self.state = 451
                    self.match(gramaticaParser.NUMERO)
                    pass
                elif token in [92]:
                    self.state = 452
                    self.match(gramaticaParser.ID)
                    pass
                elif token in [55]:
                    self.state = 453
                    self.match(gramaticaParser.BOOLEAN)
                    pass
                elif token in [93]:
                    self.state = 454
                    self.cadena()
                    pass
                elif token in [75]:
                    self.state = 455
                    self.match(gramaticaParser.COMA)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 458 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (((((_la - 33)) & ~0x3f) == 0 and ((1 << (_la - 33)) & 1729386654960975873) != 0)):
                    break

            self.state = 460
            self.match(gramaticaParser.CORCHETE_C)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class GraficasContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.x = None # ExpresionContext
            self.y = None # ExpresionContext

        def PARENTESIS_A(self):
            return self.getToken(gramaticaParser.PARENTESIS_A, 0)

        def COMA(self):
            return self.getToken(gramaticaParser.COMA, 0)

        def PARENTESIS_C(self):
            return self.getToken(gramaticaParser.PARENTESIS_C, 0)

        def PUNTOCOMA(self):
            return self.getToken(gramaticaParser.PUNTOCOMA, 0)

        def expresion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramaticaParser.ExpresionContext)
            else:
                return self.getTypedRuleContext(gramaticaParser.ExpresionContext,i)


        def func(self):
            return self.getTypedRuleContext(gramaticaParser.FuncContext,0)


        def arange(self):
            return self.getTypedRuleContext(gramaticaParser.ArangeContext,0)


        def ID(self):
            return self.getToken(gramaticaParser.ID, 0)

        def getRuleIndex(self):
            return gramaticaParser.RULE_graficas

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGraficas" ):
                listener.enterGraficas(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGraficas" ):
                listener.exitGraficas(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGraficas" ):
                return visitor.visitGraficas(self)
            else:
                return visitor.visitChildren(self)




    def graficas(self):

        localctx = gramaticaParser.GraficasContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_graficas)
        self._la = 0 # Token type
        try:
            self.state = 487
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [15, 16, 17, 18, 19, 20]:
                self.enterOuterAlt(localctx, 1)
                self.state = 462
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 2064384) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 463
                self.match(gramaticaParser.PARENTESIS_A)
                self.state = 464
                localctx.x = self.expresion(0)
                self.state = 465
                self.match(gramaticaParser.COMA)
                self.state = 466
                localctx.y = self.expresion(0)
                self.state = 467
                self.match(gramaticaParser.PARENTESIS_C)
                self.state = 468
                self.match(gramaticaParser.PUNTOCOMA)
                pass
            elif token in [21, 22]:
                self.enterOuterAlt(localctx, 2)
                self.state = 470
                _la = self._input.LA(1)
                if not(_la==21 or _la==22):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 471
                self.match(gramaticaParser.PARENTESIS_A)
                self.state = 472
                localctx.x = self.expresion(0)
                self.state = 473
                self.match(gramaticaParser.PARENTESIS_C)
                self.state = 474
                self.match(gramaticaParser.PUNTOCOMA)
                pass
            elif token in [23, 24, 25]:
                self.enterOuterAlt(localctx, 3)
                self.state = 476
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 58720256) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 477
                self.match(gramaticaParser.PARENTESIS_A)
                self.state = 480
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [26]:
                    self.state = 478
                    self.arange()
                    pass
                elif token in [92]:
                    self.state = 479
                    self.match(gramaticaParser.ID)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 482
                self.match(gramaticaParser.COMA)
                self.state = 483
                self.func()
                self.state = 484
                self.match(gramaticaParser.PARENTESIS_C)
                self.state = 485
                self.match(gramaticaParser.PUNTOCOMA)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArangeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PARENTESIS_A(self):
            return self.getToken(gramaticaParser.PARENTESIS_A, 0)

        def expresion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramaticaParser.ExpresionContext)
            else:
                return self.getTypedRuleContext(gramaticaParser.ExpresionContext,i)


        def COMA(self, i:int=None):
            if i is None:
                return self.getTokens(gramaticaParser.COMA)
            else:
                return self.getToken(gramaticaParser.COMA, i)

        def MULTIPLICACION(self):
            return self.getToken(gramaticaParser.MULTIPLICACION, 0)

        def PUNTO(self):
            return self.getToken(gramaticaParser.PUNTO, 0)

        def PARENTESIS_C(self):
            return self.getToken(gramaticaParser.PARENTESIS_C, 0)

        def getRuleIndex(self):
            return gramaticaParser.RULE_arange

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArange" ):
                listener.enterArange(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArange" ):
                listener.exitArange(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArange" ):
                return visitor.visitArange(self)
            else:
                return visitor.visitChildren(self)




    def arange(self):

        localctx = gramaticaParser.ArangeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_arange)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 489
            self.match(gramaticaParser.T__25)
            self.state = 490
            self.match(gramaticaParser.PARENTESIS_A)
            self.state = 491
            self.expresion(0)
            self.state = 492
            self.match(gramaticaParser.COMA)
            self.state = 493
            self.expresion(0)
            self.state = 494
            self.match(gramaticaParser.MULTIPLICACION)
            self.state = 495
            self.match(gramaticaParser.T__1)
            self.state = 496
            self.match(gramaticaParser.PUNTO)
            self.state = 497
            self.match(gramaticaParser.T__26)
            self.state = 498
            self.match(gramaticaParser.COMA)
            self.state = 499
            self.expresion(0)
            self.state = 500
            self.match(gramaticaParser.PARENTESIS_C)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Lectura_archivoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPEN(self):
            return self.getToken(gramaticaParser.OPEN, 0)

        def PARENTESIS_A(self):
            return self.getToken(gramaticaParser.PARENTESIS_A, 0)

        def expresion(self):
            return self.getTypedRuleContext(gramaticaParser.ExpresionContext,0)


        def PARENTESIS_C(self):
            return self.getToken(gramaticaParser.PARENTESIS_C, 0)

        def PUNTOCOMA(self):
            return self.getToken(gramaticaParser.PUNTOCOMA, 0)

        def getRuleIndex(self):
            return gramaticaParser.RULE_lectura_archivo

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLectura_archivo" ):
                listener.enterLectura_archivo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLectura_archivo" ):
                listener.exitLectura_archivo(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLectura_archivo" ):
                return visitor.visitLectura_archivo(self)
            else:
                return visitor.visitChildren(self)




    def lectura_archivo(self):

        localctx = gramaticaParser.Lectura_archivoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_lectura_archivo)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 502
            self.match(gramaticaParser.OPEN)
            self.state = 503
            self.match(gramaticaParser.PARENTESIS_A)
            self.state = 504
            self.expresion(0)
            self.state = 505
            self.match(gramaticaParser.PARENTESIS_C)
            self.state = 506
            self.match(gramaticaParser.PUNTOCOMA)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Escritura_archivoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WRITE(self):
            return self.getToken(gramaticaParser.WRITE, 0)

        def PARENTESIS_A(self):
            return self.getToken(gramaticaParser.PARENTESIS_A, 0)

        def expresion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramaticaParser.ExpresionContext)
            else:
                return self.getTypedRuleContext(gramaticaParser.ExpresionContext,i)


        def COMA(self):
            return self.getToken(gramaticaParser.COMA, 0)

        def PARENTESIS_C(self):
            return self.getToken(gramaticaParser.PARENTESIS_C, 0)

        def PUNTOCOMA(self):
            return self.getToken(gramaticaParser.PUNTOCOMA, 0)

        def getRuleIndex(self):
            return gramaticaParser.RULE_escritura_archivo

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEscritura_archivo" ):
                listener.enterEscritura_archivo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEscritura_archivo" ):
                listener.exitEscritura_archivo(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEscritura_archivo" ):
                return visitor.visitEscritura_archivo(self)
            else:
                return visitor.visitChildren(self)




    def escritura_archivo(self):

        localctx = gramaticaParser.Escritura_archivoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_escritura_archivo)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 508
            self.match(gramaticaParser.WRITE)
            self.state = 509
            self.match(gramaticaParser.PARENTESIS_A)
            self.state = 510
            self.expresion(0)
            self.state = 511
            self.match(gramaticaParser.COMA)
            self.state = 512
            self.expresion(0)
            self.state = 513
            self.match(gramaticaParser.PARENTESIS_C)
            self.state = 514
            self.match(gramaticaParser.PUNTOCOMA)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[22] = self.expresion_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expresion_sempred(self, localctx:ExpresionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 4)
         




