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
        4,1,93,507,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,1,0,
        4,0,68,8,0,11,0,12,0,69,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,89,8,1,1,2,1,2,1,2,3,2,94,8,2,1,
        2,3,2,97,8,2,1,2,1,2,1,2,1,2,3,2,103,8,2,1,2,3,2,106,8,2,1,2,1,2,
        1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,117,8,2,1,2,1,2,1,2,1,2,1,2,1,2,
        1,2,3,2,126,8,2,1,3,3,3,129,8,3,1,3,3,3,132,8,3,1,3,1,3,1,3,3,3,
        137,8,3,1,3,1,3,3,3,141,8,3,1,4,1,4,1,4,1,4,1,4,3,4,148,8,4,1,4,
        1,4,1,4,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,7,1,7,1,8,1,8,1,8,1,8,3,8,
        166,8,8,1,8,1,8,1,8,1,8,1,8,1,9,5,9,174,8,9,10,9,12,9,177,9,9,1,
        9,1,9,1,10,1,10,1,10,1,10,1,11,1,11,1,11,3,11,188,8,11,1,11,1,11,
        1,12,1,12,1,12,3,12,195,8,12,1,12,1,12,1,12,1,12,3,12,201,8,12,5,
        12,203,8,12,10,12,12,12,206,9,12,1,13,1,13,1,13,1,13,3,13,212,8,
        13,1,13,1,13,1,13,5,13,217,8,13,10,13,12,13,220,9,13,1,13,1,13,3,
        13,224,8,13,1,13,3,13,227,8,13,1,14,4,14,230,8,14,11,14,12,14,231,
        1,15,1,15,1,15,1,15,3,15,238,8,15,1,15,1,15,1,15,5,15,243,8,15,10,
        15,12,15,246,9,15,1,15,1,15,1,16,1,16,1,16,5,16,253,8,16,10,16,12,
        16,256,9,16,1,16,1,16,1,17,1,17,1,17,1,17,1,17,1,17,1,17,3,17,267,
        8,17,1,17,3,17,270,8,17,1,17,3,17,273,8,17,1,17,3,17,276,8,17,1,
        17,1,17,1,17,4,17,281,8,17,11,17,12,17,282,1,17,3,17,286,8,17,1,
        17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,4,17,296,8,17,11,17,12,17,
        297,1,17,3,17,301,8,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,4,
        17,311,8,17,11,17,12,17,312,1,17,3,17,316,8,17,1,17,1,17,3,17,320,
        8,17,1,18,1,18,3,18,324,8,18,1,18,1,18,3,18,328,8,18,1,18,1,18,4,
        18,332,8,18,11,18,12,18,333,1,18,1,18,1,19,1,19,1,19,5,19,341,8,
        19,10,19,12,19,344,9,19,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,21,
        1,21,1,21,1,21,3,21,357,8,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,
        1,21,1,21,5,21,368,8,21,10,21,12,21,371,9,21,1,22,1,22,3,22,375,
        8,22,1,22,3,22,378,8,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,
        1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,3,22,398,8,22,
        1,23,1,23,1,23,1,23,5,23,404,8,23,10,23,12,23,407,9,23,1,23,1,23,
        1,24,1,24,1,24,1,24,5,24,415,8,24,10,24,12,24,418,9,24,1,24,1,24,
        1,25,1,25,1,25,1,26,1,26,1,26,1,26,1,26,1,26,3,26,431,8,26,1,27,
        1,27,1,27,1,27,1,27,1,27,4,27,439,8,27,11,27,12,27,440,1,27,1,27,
        1,28,1,28,1,28,1,28,1,28,1,28,4,28,451,8,28,11,28,12,28,452,1,28,
        1,28,1,29,1,29,1,29,1,29,1,29,1,29,1,29,1,29,1,29,1,29,1,29,1,29,
        1,29,1,29,1,29,1,29,3,29,473,8,29,1,29,1,29,1,29,1,29,3,29,479,8,
        29,1,30,1,30,1,30,1,30,1,30,1,30,1,30,1,30,1,30,1,30,1,30,1,30,1,
        30,1,31,1,31,1,31,1,31,1,31,1,32,1,32,1,32,1,32,1,32,1,32,1,32,1,
        32,1,32,0,1,42,33,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,
        34,36,38,40,42,44,46,48,50,52,54,56,58,60,62,64,0,10,1,0,53,56,1,
        0,1,2,1,0,3,10,3,0,63,63,65,67,88,89,2,0,64,64,68,73,1,0,59,60,2,
        0,1,1,13,14,1,0,15,20,1,0,21,22,1,0,23,25,571,0,67,1,0,0,0,2,88,
        1,0,0,0,4,125,1,0,0,0,6,128,1,0,0,0,8,142,1,0,0,0,10,152,1,0,0,0,
        12,154,1,0,0,0,14,159,1,0,0,0,16,161,1,0,0,0,18,175,1,0,0,0,20,180,
        1,0,0,0,22,184,1,0,0,0,24,194,1,0,0,0,26,207,1,0,0,0,28,229,1,0,
        0,0,30,233,1,0,0,0,32,249,1,0,0,0,34,319,1,0,0,0,36,321,1,0,0,0,
        38,337,1,0,0,0,40,345,1,0,0,0,42,356,1,0,0,0,44,397,1,0,0,0,46,399,
        1,0,0,0,48,410,1,0,0,0,50,421,1,0,0,0,52,430,1,0,0,0,54,432,1,0,
        0,0,56,444,1,0,0,0,58,478,1,0,0,0,60,480,1,0,0,0,62,493,1,0,0,0,
        64,498,1,0,0,0,66,68,3,2,1,0,67,66,1,0,0,0,68,69,1,0,0,0,69,67,1,
        0,0,0,69,70,1,0,0,0,70,1,1,0,0,0,71,89,3,8,4,0,72,89,3,4,2,0,73,
        89,3,22,11,0,74,89,3,26,13,0,75,89,3,36,18,0,76,89,3,42,21,0,77,
        89,3,16,8,0,78,89,3,34,17,0,79,89,3,6,3,0,80,89,3,12,6,0,81,89,3,
        58,29,0,82,89,3,50,25,0,83,89,3,40,20,0,84,89,3,44,22,0,85,89,5,
        31,0,0,86,89,3,62,31,0,87,89,3,64,32,0,88,71,1,0,0,0,88,72,1,0,0,
        0,88,73,1,0,0,0,88,74,1,0,0,0,88,75,1,0,0,0,88,76,1,0,0,0,88,77,
        1,0,0,0,88,78,1,0,0,0,88,79,1,0,0,0,88,80,1,0,0,0,88,81,1,0,0,0,
        88,82,1,0,0,0,88,83,1,0,0,0,88,84,1,0,0,0,88,85,1,0,0,0,88,86,1,
        0,0,0,88,87,1,0,0,0,89,3,1,0,0,0,90,91,5,92,0,0,91,93,5,64,0,0,92,
        94,3,10,5,0,93,92,1,0,0,0,93,94,1,0,0,0,94,96,1,0,0,0,95,97,5,80,
        0,0,96,95,1,0,0,0,96,97,1,0,0,0,97,102,1,0,0,0,98,103,3,42,21,0,
        99,103,3,6,3,0,100,103,3,44,22,0,101,103,3,60,30,0,102,98,1,0,0,
        0,102,99,1,0,0,0,102,100,1,0,0,0,102,101,1,0,0,0,103,105,1,0,0,0,
        104,106,5,81,0,0,105,104,1,0,0,0,105,106,1,0,0,0,106,107,1,0,0,0,
        107,108,5,77,0,0,108,126,1,0,0,0,109,110,5,92,0,0,110,111,5,64,0,
        0,111,112,5,92,0,0,112,116,5,80,0,0,113,117,3,38,19,0,114,117,3,
        42,21,0,115,117,3,44,22,0,116,113,1,0,0,0,116,114,1,0,0,0,116,115,
        1,0,0,0,116,117,1,0,0,0,117,118,1,0,0,0,118,119,5,81,0,0,119,126,
        5,77,0,0,120,121,5,92,0,0,121,122,5,64,0,0,122,123,3,14,7,0,123,
        124,5,77,0,0,124,126,1,0,0,0,125,90,1,0,0,0,125,109,1,0,0,0,125,
        120,1,0,0,0,126,5,1,0,0,0,127,129,3,10,5,0,128,127,1,0,0,0,128,129,
        1,0,0,0,129,131,1,0,0,0,130,132,5,80,0,0,131,130,1,0,0,0,131,132,
        1,0,0,0,132,133,1,0,0,0,133,134,5,51,0,0,134,136,5,80,0,0,135,137,
        3,42,21,0,136,135,1,0,0,0,136,137,1,0,0,0,137,138,1,0,0,0,138,140,
        5,81,0,0,139,141,5,81,0,0,140,139,1,0,0,0,140,141,1,0,0,0,141,7,
        1,0,0,0,142,143,5,52,0,0,143,147,5,80,0,0,144,148,3,42,21,0,145,
        148,5,75,0,0,146,148,3,44,22,0,147,144,1,0,0,0,147,145,1,0,0,0,147,
        146,1,0,0,0,147,148,1,0,0,0,148,149,1,0,0,0,149,150,5,81,0,0,150,
        151,5,77,0,0,151,9,1,0,0,0,152,153,7,0,0,0,153,11,1,0,0,0,154,155,
        3,10,5,0,155,156,5,80,0,0,156,157,3,42,21,0,157,158,5,81,0,0,158,
        13,1,0,0,0,159,160,5,93,0,0,160,15,1,0,0,0,161,162,5,36,0,0,162,
        163,5,92,0,0,163,165,5,80,0,0,164,166,3,38,19,0,165,164,1,0,0,0,
        165,166,1,0,0,0,166,167,1,0,0,0,167,168,5,81,0,0,168,169,5,83,0,
        0,169,170,3,18,9,0,170,171,5,82,0,0,171,17,1,0,0,0,172,174,3,2,1,
        0,173,172,1,0,0,0,174,177,1,0,0,0,175,173,1,0,0,0,175,176,1,0,0,
        0,176,178,1,0,0,0,177,175,1,0,0,0,178,179,3,20,10,0,179,19,1,0,0,
        0,180,181,5,48,0,0,181,182,3,42,21,0,182,183,5,77,0,0,183,21,1,0,
        0,0,184,185,5,92,0,0,185,187,5,80,0,0,186,188,3,24,12,0,187,186,
        1,0,0,0,187,188,1,0,0,0,188,189,1,0,0,0,189,190,5,81,0,0,190,23,
        1,0,0,0,191,195,3,52,26,0,192,195,5,92,0,0,193,195,3,22,11,0,194,
        191,1,0,0,0,194,192,1,0,0,0,194,193,1,0,0,0,195,204,1,0,0,0,196,
        200,5,75,0,0,197,201,3,52,26,0,198,201,5,92,0,0,199,201,3,22,11,
        0,200,197,1,0,0,0,200,198,1,0,0,0,200,199,1,0,0,0,201,203,1,0,0,
        0,202,196,1,0,0,0,203,206,1,0,0,0,204,202,1,0,0,0,204,205,1,0,0,
        0,205,25,1,0,0,0,206,204,1,0,0,0,207,208,5,38,0,0,208,211,5,80,0,
        0,209,212,3,38,19,0,210,212,3,42,21,0,211,209,1,0,0,0,211,210,1,
        0,0,0,212,213,1,0,0,0,213,214,5,81,0,0,214,218,5,83,0,0,215,217,
        3,2,1,0,216,215,1,0,0,0,217,220,1,0,0,0,218,216,1,0,0,0,218,219,
        1,0,0,0,219,221,1,0,0,0,220,218,1,0,0,0,221,223,5,82,0,0,222,224,
        3,28,14,0,223,222,1,0,0,0,223,224,1,0,0,0,224,226,1,0,0,0,225,227,
        3,32,16,0,226,225,1,0,0,0,226,227,1,0,0,0,227,27,1,0,0,0,228,230,
        3,30,15,0,229,228,1,0,0,0,230,231,1,0,0,0,231,229,1,0,0,0,231,232,
        1,0,0,0,232,29,1,0,0,0,233,234,5,62,0,0,234,237,5,80,0,0,235,238,
        3,38,19,0,236,238,3,42,21,0,237,235,1,0,0,0,237,236,1,0,0,0,238,
        239,1,0,0,0,239,240,5,81,0,0,240,244,5,83,0,0,241,243,3,2,1,0,242,
        241,1,0,0,0,243,246,1,0,0,0,244,242,1,0,0,0,244,245,1,0,0,0,245,
        247,1,0,0,0,246,244,1,0,0,0,247,248,5,82,0,0,248,31,1,0,0,0,249,
        250,5,39,0,0,250,254,5,83,0,0,251,253,3,2,1,0,252,251,1,0,0,0,253,
        256,1,0,0,0,254,252,1,0,0,0,254,255,1,0,0,0,255,257,1,0,0,0,256,
        254,1,0,0,0,257,258,5,82,0,0,258,33,1,0,0,0,259,260,5,40,0,0,260,
        261,5,92,0,0,261,262,5,41,0,0,262,263,5,42,0,0,263,264,5,80,0,0,
        264,266,3,42,21,0,265,267,5,75,0,0,266,265,1,0,0,0,266,267,1,0,0,
        0,267,269,1,0,0,0,268,270,3,42,21,0,269,268,1,0,0,0,269,270,1,0,
        0,0,270,272,1,0,0,0,271,273,5,75,0,0,272,271,1,0,0,0,272,273,1,0,
        0,0,273,275,1,0,0,0,274,276,3,42,21,0,275,274,1,0,0,0,275,276,1,
        0,0,0,276,277,1,0,0,0,277,278,5,81,0,0,278,280,5,83,0,0,279,281,
        3,2,1,0,280,279,1,0,0,0,281,282,1,0,0,0,282,280,1,0,0,0,282,283,
        1,0,0,0,283,285,1,0,0,0,284,286,3,20,10,0,285,284,1,0,0,0,285,286,
        1,0,0,0,286,287,1,0,0,0,287,288,5,82,0,0,288,320,1,0,0,0,289,290,
        5,40,0,0,290,291,5,92,0,0,291,292,5,41,0,0,292,293,3,42,21,0,293,
        295,5,83,0,0,294,296,3,2,1,0,295,294,1,0,0,0,296,297,1,0,0,0,297,
        295,1,0,0,0,297,298,1,0,0,0,298,300,1,0,0,0,299,301,3,20,10,0,300,
        299,1,0,0,0,300,301,1,0,0,0,301,302,1,0,0,0,302,303,5,82,0,0,303,
        320,1,0,0,0,304,305,5,40,0,0,305,306,5,92,0,0,306,307,5,41,0,0,307,
        308,3,14,7,0,308,310,5,83,0,0,309,311,3,2,1,0,310,309,1,0,0,0,311,
        312,1,0,0,0,312,310,1,0,0,0,312,313,1,0,0,0,313,315,1,0,0,0,314,
        316,3,20,10,0,315,314,1,0,0,0,315,316,1,0,0,0,316,317,1,0,0,0,317,
        318,5,82,0,0,318,320,1,0,0,0,319,259,1,0,0,0,319,289,1,0,0,0,319,
        304,1,0,0,0,320,35,1,0,0,0,321,323,5,44,0,0,322,324,5,80,0,0,323,
        322,1,0,0,0,323,324,1,0,0,0,324,325,1,0,0,0,325,327,3,42,21,0,326,
        328,5,81,0,0,327,326,1,0,0,0,327,328,1,0,0,0,328,329,1,0,0,0,329,
        331,5,83,0,0,330,332,3,2,1,0,331,330,1,0,0,0,332,333,1,0,0,0,333,
        331,1,0,0,0,333,334,1,0,0,0,334,335,1,0,0,0,335,336,5,82,0,0,336,
        37,1,0,0,0,337,342,5,92,0,0,338,339,5,75,0,0,339,341,5,92,0,0,340,
        338,1,0,0,0,341,344,1,0,0,0,342,340,1,0,0,0,342,343,1,0,0,0,343,
        39,1,0,0,0,344,342,1,0,0,0,345,346,7,1,0,0,346,347,5,74,0,0,347,
        348,7,2,0,0,348,349,5,80,0,0,349,350,3,42,21,0,350,351,5,81,0,0,
        351,41,1,0,0,0,352,353,6,21,-1,0,353,357,3,52,26,0,354,357,3,22,
        11,0,355,357,3,40,20,0,356,352,1,0,0,0,356,354,1,0,0,0,356,355,1,
        0,0,0,357,369,1,0,0,0,358,359,10,6,0,0,359,360,7,3,0,0,360,368,3,
        52,26,0,361,362,10,5,0,0,362,363,7,4,0,0,363,368,3,52,26,0,364,365,
        10,4,0,0,365,366,7,5,0,0,366,368,3,52,26,0,367,358,1,0,0,0,367,361,
        1,0,0,0,367,364,1,0,0,0,368,371,1,0,0,0,369,367,1,0,0,0,369,370,
        1,0,0,0,370,43,1,0,0,0,371,369,1,0,0,0,372,374,3,46,23,0,373,375,
        5,63,0,0,374,373,1,0,0,0,374,375,1,0,0,0,375,377,1,0,0,0,376,378,
        3,46,23,0,377,376,1,0,0,0,377,378,1,0,0,0,378,398,1,0,0,0,379,380,
        3,46,23,0,380,381,5,65,0,0,381,382,3,46,23,0,382,398,1,0,0,0,383,
        384,3,46,23,0,384,385,5,67,0,0,385,386,3,46,23,0,386,398,1,0,0,0,
        387,388,5,11,0,0,388,389,5,80,0,0,389,390,3,46,23,0,390,391,5,81,
        0,0,391,398,1,0,0,0,392,393,5,12,0,0,393,394,5,80,0,0,394,395,3,
        46,23,0,395,396,5,81,0,0,396,398,1,0,0,0,397,372,1,0,0,0,397,379,
        1,0,0,0,397,383,1,0,0,0,397,387,1,0,0,0,397,392,1,0,0,0,398,45,1,
        0,0,0,399,400,5,84,0,0,400,405,3,48,24,0,401,402,5,75,0,0,402,404,
        3,48,24,0,403,401,1,0,0,0,404,407,1,0,0,0,405,403,1,0,0,0,405,406,
        1,0,0,0,406,408,1,0,0,0,407,405,1,0,0,0,408,409,5,85,0,0,409,47,
        1,0,0,0,410,411,5,84,0,0,411,416,3,42,21,0,412,413,5,75,0,0,413,
        415,3,42,21,0,414,412,1,0,0,0,415,418,1,0,0,0,416,414,1,0,0,0,416,
        417,1,0,0,0,417,419,1,0,0,0,418,416,1,0,0,0,419,420,5,85,0,0,420,
        49,1,0,0,0,421,422,5,35,0,0,422,423,7,6,0,0,423,51,1,0,0,0,424,431,
        5,33,0,0,425,431,5,92,0,0,426,431,5,55,0,0,427,431,3,14,7,0,428,
        431,3,54,27,0,429,431,3,56,28,0,430,424,1,0,0,0,430,425,1,0,0,0,
        430,426,1,0,0,0,430,427,1,0,0,0,430,428,1,0,0,0,430,429,1,0,0,0,
        431,53,1,0,0,0,432,438,5,80,0,0,433,439,5,33,0,0,434,439,5,92,0,
        0,435,439,5,55,0,0,436,439,3,14,7,0,437,439,5,75,0,0,438,433,1,0,
        0,0,438,434,1,0,0,0,438,435,1,0,0,0,438,436,1,0,0,0,438,437,1,0,
        0,0,439,440,1,0,0,0,440,438,1,0,0,0,440,441,1,0,0,0,441,442,1,0,
        0,0,442,443,5,81,0,0,443,55,1,0,0,0,444,450,5,84,0,0,445,451,5,33,
        0,0,446,451,5,92,0,0,447,451,5,55,0,0,448,451,3,14,7,0,449,451,5,
        75,0,0,450,445,1,0,0,0,450,446,1,0,0,0,450,447,1,0,0,0,450,448,1,
        0,0,0,450,449,1,0,0,0,451,452,1,0,0,0,452,450,1,0,0,0,452,453,1,
        0,0,0,453,454,1,0,0,0,454,455,5,85,0,0,455,57,1,0,0,0,456,457,7,
        7,0,0,457,458,5,80,0,0,458,459,3,42,21,0,459,460,5,75,0,0,460,461,
        3,42,21,0,461,462,5,81,0,0,462,479,1,0,0,0,463,464,7,8,0,0,464,465,
        5,80,0,0,465,466,3,42,21,0,466,467,5,81,0,0,467,479,1,0,0,0,468,
        469,7,9,0,0,469,472,5,80,0,0,470,473,3,60,30,0,471,473,5,92,0,0,
        472,470,1,0,0,0,472,471,1,0,0,0,473,474,1,0,0,0,474,475,5,75,0,0,
        475,476,3,40,20,0,476,477,5,81,0,0,477,479,1,0,0,0,478,456,1,0,0,
        0,478,463,1,0,0,0,478,468,1,0,0,0,479,59,1,0,0,0,480,481,5,26,0,
        0,481,482,5,80,0,0,482,483,3,42,21,0,483,484,5,75,0,0,484,485,3,
        42,21,0,485,486,5,67,0,0,486,487,5,2,0,0,487,488,5,74,0,0,488,489,
        5,27,0,0,489,490,5,75,0,0,490,491,3,42,21,0,491,492,5,81,0,0,492,
        61,1,0,0,0,493,494,5,91,0,0,494,495,5,80,0,0,495,496,3,42,21,0,496,
        497,5,81,0,0,497,63,1,0,0,0,498,499,5,90,0,0,499,500,5,80,0,0,500,
        501,3,42,21,0,501,502,5,81,0,0,502,503,5,76,0,0,503,504,3,42,21,
        0,504,505,5,46,0,0,505,65,1,0,0,0,57,69,88,93,96,102,105,116,125,
        128,131,136,140,147,165,175,187,194,200,204,211,218,223,226,231,
        237,244,254,266,269,272,275,282,285,297,300,312,315,319,323,327,
        333,342,356,367,369,374,377,397,405,416,430,438,440,450,452,472,
        478
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
                      "SEP", "ESP", "EX", "NEWLINE", "TAB", "NUMERO", "WS", 
                      "IMPORT", "DEF", "CLASS", "IF", "ELSE", "FOR", "IN", 
                      "RANGE", "SELF", "WHILE", "TRY", "END", "EXCEPT", 
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
    RULE_printf = 4
    RULE_var_casteo = 5
    RULE_casteo = 6
    RULE_cadena = 7
    RULE_funcion = 8
    RULE_stmt_func = 9
    RULE_v_return = 10
    RULE_llamafuncion = 11
    RULE_args = 12
    RULE_condicional = 13
    RULE_elifBlock = 14
    RULE_condicional_elif = 15
    RULE_condicional_else = 16
    RULE_ciclo_for = 17
    RULE_ciclo_while = 18
    RULE_parametro = 19
    RULE_func = 20
    RULE_expresion = 21
    RULE_matriz_operaciones = 22
    RULE_matriz = 23
    RULE_fila_matriz = 24
    RULE_importss = 25
    RULE_termino = 26
    RULE_lista = 27
    RULE_arreglo = 28
    RULE_graficas = 29
    RULE_arange = 30
    RULE_lectura_archivo = 31
    RULE_escritura_archivo = 32

    ruleNames =  [ "start", "sentencias", "asignacion", "v_input", "printf", 
                   "var_casteo", "casteo", "cadena", "funcion", "stmt_func", 
                   "v_return", "llamafuncion", "args", "condicional", "elifBlock", 
                   "condicional_elif", "condicional_else", "ciclo_for", 
                   "ciclo_while", "parametro", "func", "expresion", "matriz_operaciones", 
                   "matriz", "fila_matriz", "importss", "termino", "lista", 
                   "arreglo", "graficas", "arange", "lectura_archivo", "escritura_archivo" ]

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
    EX=30
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
            self.state = 67 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 66
                self.sentencias()
                self.state = 69 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 141882468721465350) != 0) or ((((_la - 80)) & ~0x3f) == 0 and ((1 << (_la - 80)) & 15377) != 0)):
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
            self.state = 88
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 71
                self.printf()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 72
                self.asignacion()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 73
                self.llamafuncion()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 74
                self.condicional()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 75
                self.ciclo_while()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 76
                self.expresion(0)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 77
                self.funcion()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 78
                self.ciclo_for()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 79
                self.v_input()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 80
                self.casteo()
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 81
                self.graficas()
                pass

            elif la_ == 12:
                self.enterOuterAlt(localctx, 12)
                self.state = 82
                self.importss()
                pass

            elif la_ == 13:
                self.enterOuterAlt(localctx, 13)
                self.state = 83
                self.func()
                pass

            elif la_ == 14:
                self.enterOuterAlt(localctx, 14)
                self.state = 84
                self.matriz_operaciones()
                pass

            elif la_ == 15:
                self.enterOuterAlt(localctx, 15)
                self.state = 85
                self.match(gramaticaParser.NEWLINE)
                pass

            elif la_ == 16:
                self.enterOuterAlt(localctx, 16)
                self.state = 86
                self.lectura_archivo()
                pass

            elif la_ == 17:
                self.enterOuterAlt(localctx, 17)
                self.state = 87
                self.escritura_archivo()
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
            self.state = 125
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 90
                self.match(gramaticaParser.ID)
                self.state = 91
                self.match(gramaticaParser.ASIGNACION)
                self.state = 93
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
                if la_ == 1:
                    self.state = 92
                    self.var_casteo()


                self.state = 96
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
                if la_ == 1:
                    self.state = 95
                    self.match(gramaticaParser.PARENTESIS_A)


                self.state = 102
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
                if la_ == 1:
                    self.state = 98
                    self.expresion(0)
                    pass

                elif la_ == 2:
                    self.state = 99
                    self.v_input()
                    pass

                elif la_ == 3:
                    self.state = 100
                    self.matriz_operaciones()
                    pass

                elif la_ == 4:
                    self.state = 101
                    self.arange()
                    pass


                self.state = 105
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==81:
                    self.state = 104
                    self.match(gramaticaParser.PARENTESIS_C)


                self.state = 107
                self.match(gramaticaParser.PUNTOCOMA)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 109
                self.match(gramaticaParser.ID)
                self.state = 110
                self.match(gramaticaParser.ASIGNACION)
                self.state = 111
                self.match(gramaticaParser.ID)
                self.state = 112
                self.match(gramaticaParser.PARENTESIS_A)
                self.state = 116
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
                if la_ == 1:
                    self.state = 113
                    self.parametro()

                elif la_ == 2:
                    self.state = 114
                    self.expresion(0)

                elif la_ == 3:
                    self.state = 115
                    self.matriz_operaciones()


                self.state = 118
                self.match(gramaticaParser.PARENTESIS_C)
                self.state = 119
                self.match(gramaticaParser.PUNTOCOMA)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 120
                self.match(gramaticaParser.ID)
                self.state = 121
                self.match(gramaticaParser.ASIGNACION)
                self.state = 122
                self.cadena()
                self.state = 123
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
            self.state = 128
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 135107988821114880) != 0):
                self.state = 127
                self.var_casteo()


            self.state = 131
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==80:
                self.state = 130
                self.match(gramaticaParser.PARENTESIS_A)


            self.state = 133
            self.match(gramaticaParser.INPUT)
            self.state = 134
            self.match(gramaticaParser.PARENTESIS_A)
            self.state = 136
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 36028805608898566) != 0) or ((((_la - 80)) & ~0x3f) == 0 and ((1 << (_la - 80)) & 12305) != 0):
                self.state = 135
                self.expresion(0)


            self.state = 138
            self.match(gramaticaParser.PARENTESIS_C)
            self.state = 140
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.state = 139
                self.match(gramaticaParser.PARENTESIS_C)


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
        self.enterRule(localctx, 8, self.RULE_printf)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 142
            self.match(gramaticaParser.PRINT)
            self.state = 143
            self.match(gramaticaParser.PARENTESIS_A)
            self.state = 147
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.state = 144
                self.expresion(0)

            elif la_ == 2:
                self.state = 145
                self.match(gramaticaParser.COMA)

            elif la_ == 3:
                self.state = 146
                self.matriz_operaciones()


            self.state = 149
            self.match(gramaticaParser.PARENTESIS_C)
            self.state = 150
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
        self.enterRule(localctx, 10, self.RULE_var_casteo)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 152
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
        self.enterRule(localctx, 12, self.RULE_casteo)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 154
            self.var_casteo()
            self.state = 155
            self.match(gramaticaParser.PARENTESIS_A)
            self.state = 156
            self.expresion(0)
            self.state = 157
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
        self.enterRule(localctx, 14, self.RULE_cadena)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 159
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
        self.enterRule(localctx, 16, self.RULE_funcion)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 161
            self.match(gramaticaParser.DEF)
            self.state = 162
            self.match(gramaticaParser.ID)
            self.state = 163
            self.match(gramaticaParser.PARENTESIS_A)
            self.state = 165
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==92:
                self.state = 164
                self.parametro()


            self.state = 167
            self.match(gramaticaParser.PARENTESIS_C)
            self.state = 168
            self.match(gramaticaParser.LLAVE_A)
            self.state = 169
            self.stmt_func()
            self.state = 170
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

        def v_return(self):
            return self.getTypedRuleContext(gramaticaParser.V_returnContext,0)


        def sentencias(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramaticaParser.SentenciasContext)
            else:
                return self.getTypedRuleContext(gramaticaParser.SentenciasContext,i)


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
        self.enterRule(localctx, 18, self.RULE_stmt_func)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 175
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 141882468721465350) != 0) or ((((_la - 80)) & ~0x3f) == 0 and ((1 << (_la - 80)) & 15377) != 0):
                self.state = 172
                self.sentencias()
                self.state = 177
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 178
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
        self.enterRule(localctx, 20, self.RULE_v_return)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 180
            self.match(gramaticaParser.RETURN)
            self.state = 181
            self.expresion(0)
            self.state = 182
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
        self.enterRule(localctx, 22, self.RULE_llamafuncion)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 184
            self.match(gramaticaParser.ID)
            self.state = 185
            self.match(gramaticaParser.PARENTESIS_A)
            self.state = 187
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 33)) & ~0x3f) == 0 and ((1 << (_la - 33)) & 1731774794216505345) != 0):
                self.state = 186
                self.args()


            self.state = 189
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
        self.enterRule(localctx, 24, self.RULE_args)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 194
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.state = 191
                self.termino()
                pass

            elif la_ == 2:
                self.state = 192
                self.match(gramaticaParser.ID)
                pass

            elif la_ == 3:
                self.state = 193
                self.llamafuncion()
                pass


            self.state = 204
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==75:
                self.state = 196
                self.match(gramaticaParser.COMA)
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


                self.state = 206
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
        self.enterRule(localctx, 26, self.RULE_condicional)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 207
            self.match(gramaticaParser.IF)
            self.state = 208
            self.match(gramaticaParser.PARENTESIS_A)
            self.state = 211
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.state = 209
                self.parametro()
                pass

            elif la_ == 2:
                self.state = 210
                self.expresion(0)
                pass


            self.state = 213
            self.match(gramaticaParser.PARENTESIS_C)
            self.state = 214
            self.match(gramaticaParser.LLAVE_A)
            self.state = 218
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 141882468721465350) != 0) or ((((_la - 80)) & ~0x3f) == 0 and ((1 << (_la - 80)) & 15377) != 0):
                self.state = 215
                self.sentencias()
                self.state = 220
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 221
            self.match(gramaticaParser.LLAVE_C)
            self.state = 223
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==62:
                self.state = 222
                self.elifBlock()


            self.state = 226
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==39:
                self.state = 225
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
        self.enterRule(localctx, 28, self.RULE_elifBlock)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 229 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 228
                self.condicional_elif()
                self.state = 231 
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
        self.enterRule(localctx, 30, self.RULE_condicional_elif)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 233
            self.match(gramaticaParser.ELIF)
            self.state = 234
            self.match(gramaticaParser.PARENTESIS_A)
            self.state = 237
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.state = 235
                self.parametro()
                pass

            elif la_ == 2:
                self.state = 236
                self.expresion(0)
                pass


            self.state = 239
            self.match(gramaticaParser.PARENTESIS_C)
            self.state = 240
            self.match(gramaticaParser.LLAVE_A)
            self.state = 244
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 141882468721465350) != 0) or ((((_la - 80)) & ~0x3f) == 0 and ((1 << (_la - 80)) & 15377) != 0):
                self.state = 241
                self.sentencias()
                self.state = 246
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 247
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
        self.enterRule(localctx, 32, self.RULE_condicional_else)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 249
            self.match(gramaticaParser.ELSE)
            self.state = 250
            self.match(gramaticaParser.LLAVE_A)
            self.state = 254
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 141882468721465350) != 0) or ((((_la - 80)) & ~0x3f) == 0 and ((1 << (_la - 80)) & 15377) != 0):
                self.state = 251
                self.sentencias()
                self.state = 256
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 257
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
        self.enterRule(localctx, 34, self.RULE_ciclo_for)
        self._la = 0 # Token type
        try:
            self.state = 319
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 259
                self.match(gramaticaParser.FOR)
                self.state = 260
                self.match(gramaticaParser.ID)
                self.state = 261
                self.match(gramaticaParser.IN)
                self.state = 262
                self.match(gramaticaParser.RANGE)
                self.state = 263
                self.match(gramaticaParser.PARENTESIS_A)
                self.state = 264
                self.expresion(0)
                self.state = 266
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
                if la_ == 1:
                    self.state = 265
                    self.match(gramaticaParser.COMA)


                self.state = 269
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
                if la_ == 1:
                    self.state = 268
                    self.expresion(0)


                self.state = 272
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==75:
                    self.state = 271
                    self.match(gramaticaParser.COMA)


                self.state = 275
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 36028805608898566) != 0) or ((((_la - 80)) & ~0x3f) == 0 and ((1 << (_la - 80)) & 12305) != 0):
                    self.state = 274
                    self.expresion(0)


                self.state = 277
                self.match(gramaticaParser.PARENTESIS_C)
                self.state = 278
                self.match(gramaticaParser.LLAVE_A)
                self.state = 280 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 279
                    self.sentencias()
                    self.state = 282 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 141882468721465350) != 0) or ((((_la - 80)) & ~0x3f) == 0 and ((1 << (_la - 80)) & 15377) != 0)):
                        break

                self.state = 285
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==48:
                    self.state = 284
                    self.v_return()


                self.state = 287
                self.match(gramaticaParser.LLAVE_C)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 289
                self.match(gramaticaParser.FOR)
                self.state = 290
                self.match(gramaticaParser.ID)
                self.state = 291
                self.match(gramaticaParser.IN)
                self.state = 292
                self.expresion(0)
                self.state = 293
                self.match(gramaticaParser.LLAVE_A)
                self.state = 295 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 294
                    self.sentencias()
                    self.state = 297 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 141882468721465350) != 0) or ((((_la - 80)) & ~0x3f) == 0 and ((1 << (_la - 80)) & 15377) != 0)):
                        break

                self.state = 300
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==48:
                    self.state = 299
                    self.v_return()


                self.state = 302
                self.match(gramaticaParser.LLAVE_C)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 304
                self.match(gramaticaParser.FOR)
                self.state = 305
                self.match(gramaticaParser.ID)
                self.state = 306
                self.match(gramaticaParser.IN)
                self.state = 307
                self.cadena()
                self.state = 308
                self.match(gramaticaParser.LLAVE_A)
                self.state = 310 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 309
                    self.sentencias()
                    self.state = 312 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 141882468721465350) != 0) or ((((_la - 80)) & ~0x3f) == 0 and ((1 << (_la - 80)) & 15377) != 0)):
                        break

                self.state = 315
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==48:
                    self.state = 314
                    self.v_return()


                self.state = 317
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
        self.enterRule(localctx, 36, self.RULE_ciclo_while)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 321
            self.match(gramaticaParser.WHILE)
            self.state = 323
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
            if la_ == 1:
                self.state = 322
                self.match(gramaticaParser.PARENTESIS_A)


            self.state = 325
            self.expresion(0)
            self.state = 327
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==81:
                self.state = 326
                self.match(gramaticaParser.PARENTESIS_C)


            self.state = 329
            self.match(gramaticaParser.LLAVE_A)
            self.state = 331 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 330
                self.sentencias()
                self.state = 333 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 141882468721465350) != 0) or ((((_la - 80)) & ~0x3f) == 0 and ((1 << (_la - 80)) & 15377) != 0)):
                    break

            self.state = 335
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
        self.enterRule(localctx, 38, self.RULE_parametro)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 337
            self.match(gramaticaParser.ID)
            self.state = 342
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==75:
                self.state = 338
                self.match(gramaticaParser.COMA)
                self.state = 339
                self.match(gramaticaParser.ID)
                self.state = 344
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
        self.enterRule(localctx, 40, self.RULE_func)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 345
            _la = self._input.LA(1)
            if not(_la==1 or _la==2):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 346
            self.match(gramaticaParser.PUNTO)
            self.state = 347
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 2040) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 348
            self.match(gramaticaParser.PARENTESIS_A)
            self.state = 349
            self.expresion(0)
            self.state = 350
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
        _startState = 42
        self.enterRecursionRule(localctx, 42, self.RULE_expresion, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 356
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,42,self._ctx)
            if la_ == 1:
                self.state = 353
                self.termino()
                pass

            elif la_ == 2:
                self.state = 354
                self.llamafuncion()
                pass

            elif la_ == 3:
                self.state = 355
                self.func()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 369
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,44,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 367
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,43,self._ctx)
                    if la_ == 1:
                        localctx = gramaticaParser.ExpresionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expresion)
                        self.state = 358
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 359
                        _la = self._input.LA(1)
                        if not(((((_la - 63)) & ~0x3f) == 0 and ((1 << (_la - 63)) & 100663325) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 360
                        self.termino()
                        pass

                    elif la_ == 2:
                        localctx = gramaticaParser.ExpresionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expresion)
                        self.state = 361
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 362
                        _la = self._input.LA(1)
                        if not(((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & 1009) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 363
                        self.termino()
                        pass

                    elif la_ == 3:
                        localctx = gramaticaParser.ExpresionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expresion)
                        self.state = 364
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 365
                        _la = self._input.LA(1)
                        if not(_la==59 or _la==60):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 366
                        self.termino()
                        pass

             
                self.state = 371
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,44,self._ctx)

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
        self.enterRule(localctx, 44, self.RULE_matriz_operaciones)
        self._la = 0 # Token type
        try:
            self.state = 397
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,47,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 372
                self.matriz()
                self.state = 374
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==63:
                    self.state = 373
                    self.match(gramaticaParser.SUMA)


                self.state = 377
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,46,self._ctx)
                if la_ == 1:
                    self.state = 376
                    self.matriz()


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 379
                self.matriz()
                self.state = 380
                self.match(gramaticaParser.RESTA)
                self.state = 381
                self.matriz()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 383
                self.matriz()
                self.state = 384
                self.match(gramaticaParser.MULTIPLICACION)
                self.state = 385
                self.matriz()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 387
                self.match(gramaticaParser.T__10)
                self.state = 388
                self.match(gramaticaParser.PARENTESIS_A)
                self.state = 389
                self.matriz()
                self.state = 390
                self.match(gramaticaParser.PARENTESIS_C)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 392
                self.match(gramaticaParser.T__11)
                self.state = 393
                self.match(gramaticaParser.PARENTESIS_A)
                self.state = 394
                self.matriz()
                self.state = 395
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
        self.enterRule(localctx, 46, self.RULE_matriz)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 399
            self.match(gramaticaParser.CORCHETE_A)
            self.state = 400
            self.fila_matriz()
            self.state = 405
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==75:
                self.state = 401
                self.match(gramaticaParser.COMA)
                self.state = 402
                self.fila_matriz()
                self.state = 407
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 408
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
        self.enterRule(localctx, 48, self.RULE_fila_matriz)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 410
            self.match(gramaticaParser.CORCHETE_A)
            self.state = 411
            self.expresion(0)
            self.state = 416
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==75:
                self.state = 412
                self.match(gramaticaParser.COMA)
                self.state = 413
                self.expresion(0)
                self.state = 418
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 419
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
        self.enterRule(localctx, 50, self.RULE_importss)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 421
            self.match(gramaticaParser.IMPORT)
            self.state = 422
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
        self.enterRule(localctx, 52, self.RULE_termino)
        try:
            self.state = 430
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [33]:
                self.enterOuterAlt(localctx, 1)
                self.state = 424
                self.match(gramaticaParser.NUMERO)
                pass
            elif token in [92]:
                self.enterOuterAlt(localctx, 2)
                self.state = 425
                self.match(gramaticaParser.ID)
                pass
            elif token in [55]:
                self.enterOuterAlt(localctx, 3)
                self.state = 426
                self.match(gramaticaParser.BOOLEAN)
                pass
            elif token in [93]:
                self.enterOuterAlt(localctx, 4)
                self.state = 427
                self.cadena()
                pass
            elif token in [80]:
                self.enterOuterAlt(localctx, 5)
                self.state = 428
                self.lista()
                pass
            elif token in [84]:
                self.enterOuterAlt(localctx, 6)
                self.state = 429
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
        self.enterRule(localctx, 54, self.RULE_lista)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 432
            self.match(gramaticaParser.PARENTESIS_A)
            self.state = 438 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 438
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [33]:
                    self.state = 433
                    self.match(gramaticaParser.NUMERO)
                    pass
                elif token in [92]:
                    self.state = 434
                    self.match(gramaticaParser.ID)
                    pass
                elif token in [55]:
                    self.state = 435
                    self.match(gramaticaParser.BOOLEAN)
                    pass
                elif token in [93]:
                    self.state = 436
                    self.cadena()
                    pass
                elif token in [75]:
                    self.state = 437
                    self.match(gramaticaParser.COMA)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 440 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (((((_la - 33)) & ~0x3f) == 0 and ((1 << (_la - 33)) & 1729386654960975873) != 0)):
                    break

            self.state = 442
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
        self.enterRule(localctx, 56, self.RULE_arreglo)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 444
            self.match(gramaticaParser.CORCHETE_A)
            self.state = 450 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 450
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [33]:
                    self.state = 445
                    self.match(gramaticaParser.NUMERO)
                    pass
                elif token in [92]:
                    self.state = 446
                    self.match(gramaticaParser.ID)
                    pass
                elif token in [55]:
                    self.state = 447
                    self.match(gramaticaParser.BOOLEAN)
                    pass
                elif token in [93]:
                    self.state = 448
                    self.cadena()
                    pass
                elif token in [75]:
                    self.state = 449
                    self.match(gramaticaParser.COMA)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 452 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (((((_la - 33)) & ~0x3f) == 0 and ((1 << (_la - 33)) & 1729386654960975873) != 0)):
                    break

            self.state = 454
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
        self.enterRule(localctx, 58, self.RULE_graficas)
        self._la = 0 # Token type
        try:
            self.state = 478
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [15, 16, 17, 18, 19, 20]:
                self.enterOuterAlt(localctx, 1)
                self.state = 456
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 2064384) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 457
                self.match(gramaticaParser.PARENTESIS_A)
                self.state = 458
                localctx.x = self.expresion(0)
                self.state = 459
                self.match(gramaticaParser.COMA)
                self.state = 460
                localctx.y = self.expresion(0)
                self.state = 461
                self.match(gramaticaParser.PARENTESIS_C)
                pass
            elif token in [21, 22]:
                self.enterOuterAlt(localctx, 2)
                self.state = 463
                _la = self._input.LA(1)
                if not(_la==21 or _la==22):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 464
                self.match(gramaticaParser.PARENTESIS_A)
                self.state = 465
                localctx.x = self.expresion(0)
                self.state = 466
                self.match(gramaticaParser.PARENTESIS_C)
                pass
            elif token in [23, 24, 25]:
                self.enterOuterAlt(localctx, 3)
                self.state = 468
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 58720256) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 469
                self.match(gramaticaParser.PARENTESIS_A)
                self.state = 472
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [26]:
                    self.state = 470
                    self.arange()
                    pass
                elif token in [92]:
                    self.state = 471
                    self.match(gramaticaParser.ID)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 474
                self.match(gramaticaParser.COMA)
                self.state = 475
                self.func()
                self.state = 476
                self.match(gramaticaParser.PARENTESIS_C)
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
        self.enterRule(localctx, 60, self.RULE_arange)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 480
            self.match(gramaticaParser.T__25)
            self.state = 481
            self.match(gramaticaParser.PARENTESIS_A)
            self.state = 482
            self.expresion(0)
            self.state = 483
            self.match(gramaticaParser.COMA)
            self.state = 484
            self.expresion(0)
            self.state = 485
            self.match(gramaticaParser.MULTIPLICACION)
            self.state = 486
            self.match(gramaticaParser.T__1)
            self.state = 487
            self.match(gramaticaParser.PUNTO)
            self.state = 488
            self.match(gramaticaParser.T__26)
            self.state = 489
            self.match(gramaticaParser.COMA)
            self.state = 490
            self.expresion(0)
            self.state = 491
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
        self.enterRule(localctx, 62, self.RULE_lectura_archivo)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 493
            self.match(gramaticaParser.OPEN)
            self.state = 494
            self.match(gramaticaParser.PARENTESIS_A)
            self.state = 495
            self.expresion(0)
            self.state = 496
            self.match(gramaticaParser.PARENTESIS_C)
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


        def PARENTESIS_C(self):
            return self.getToken(gramaticaParser.PARENTESIS_C, 0)

        def DOSPUNTOS(self):
            return self.getToken(gramaticaParser.DOSPUNTOS, 0)

        def END(self):
            return self.getToken(gramaticaParser.END, 0)

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
        self.enterRule(localctx, 64, self.RULE_escritura_archivo)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 498
            self.match(gramaticaParser.WRITE)
            self.state = 499
            self.match(gramaticaParser.PARENTESIS_A)
            self.state = 500
            self.expresion(0)
            self.state = 501
            self.match(gramaticaParser.PARENTESIS_C)
            self.state = 502
            self.match(gramaticaParser.DOSPUNTOS)
            self.state = 503
            self.expresion(0)
            self.state = 504
            self.match(gramaticaParser.END)
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
        self._predicates[21] = self.expresion_sempred
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
         




