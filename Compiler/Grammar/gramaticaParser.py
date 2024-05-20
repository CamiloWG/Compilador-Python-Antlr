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
        4,1,91,556,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
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
        1,4,1,4,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,7,1,7,4,7,162,8,7,11,7,12,
        7,163,1,7,1,7,1,7,4,7,169,8,7,11,7,12,7,170,1,7,1,7,1,7,4,7,176,
        8,7,11,7,12,7,177,1,7,5,7,181,8,7,10,7,12,7,184,9,7,1,7,1,7,1,7,
        4,7,189,8,7,11,7,12,7,190,1,7,5,7,194,8,7,10,7,12,7,197,9,7,1,7,
        3,7,200,8,7,1,8,1,8,1,8,1,8,3,8,206,8,8,1,8,1,8,1,8,1,8,1,8,1,9,
        5,9,214,8,9,10,9,12,9,217,9,9,1,9,3,9,220,8,9,1,10,1,10,1,10,1,10,
        1,10,1,10,3,10,228,8,10,1,11,1,11,1,11,3,11,233,8,11,1,11,1,11,1,
        12,1,12,1,12,3,12,240,8,12,1,12,1,12,1,12,1,12,3,12,246,8,12,5,12,
        248,8,12,10,12,12,12,251,9,12,1,13,1,13,3,13,255,8,13,1,13,1,13,
        3,13,259,8,13,1,13,3,13,262,8,13,1,13,1,13,4,13,266,8,13,11,13,12,
        13,267,1,13,1,13,3,13,272,8,13,1,13,3,13,275,8,13,1,14,4,14,278,
        8,14,11,14,12,14,279,1,15,1,15,3,15,284,8,15,1,15,1,15,3,15,288,
        8,15,1,15,3,15,291,8,15,1,15,1,15,4,15,295,8,15,11,15,12,15,296,
        1,15,1,15,1,16,1,16,1,16,4,16,304,8,16,11,16,12,16,305,1,16,1,16,
        1,17,1,17,1,17,1,17,1,17,1,17,1,17,3,17,317,8,17,1,17,3,17,320,8,
        17,1,17,3,17,323,8,17,1,17,3,17,326,8,17,1,17,1,17,1,17,4,17,331,
        8,17,11,17,12,17,332,1,17,3,17,336,8,17,1,17,1,17,1,17,1,17,1,17,
        1,17,1,17,1,17,4,17,346,8,17,11,17,12,17,347,1,17,3,17,351,8,17,
        1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,4,17,361,8,17,11,17,12,17,
        362,1,17,3,17,366,8,17,1,17,1,17,3,17,370,8,17,1,18,1,18,3,18,374,
        8,18,1,18,1,18,3,18,378,8,18,1,18,1,18,4,18,382,8,18,11,18,12,18,
        383,1,18,1,18,1,19,1,19,1,19,5,19,391,8,19,10,19,12,19,394,9,19,
        1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,21,1,21,1,21,3,21,406,8,21,
        1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,5,21,417,8,21,10,21,
        12,21,420,9,21,1,22,1,22,3,22,424,8,22,1,22,3,22,427,8,22,1,22,1,
        22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,
        22,1,22,1,22,1,22,3,22,447,8,22,1,23,1,23,1,23,1,23,5,23,453,8,23,
        10,23,12,23,456,9,23,1,23,1,23,1,24,1,24,1,24,1,24,5,24,464,8,24,
        10,24,12,24,467,9,24,1,24,1,24,1,25,1,25,1,25,1,26,1,26,1,26,1,26,
        1,26,1,26,3,26,480,8,26,1,27,1,27,1,27,1,27,1,27,1,27,4,27,488,8,
        27,11,27,12,27,489,1,27,1,27,1,28,1,28,1,28,1,28,1,28,1,28,4,28,
        500,8,28,11,28,12,28,501,1,28,1,28,1,29,1,29,1,29,1,29,1,29,1,29,
        1,29,1,29,1,29,1,29,1,29,1,29,1,29,1,29,1,29,1,29,3,29,522,8,29,
        1,29,1,29,1,29,1,29,3,29,528,8,29,1,30,1,30,1,30,1,30,1,30,1,30,
        1,30,1,30,1,30,1,30,1,30,1,30,1,30,1,31,1,31,1,31,1,31,1,31,1,32,
        1,32,1,32,1,32,1,32,1,32,1,32,1,32,1,32,4,163,170,177,190,1,42,33,
        0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,
        46,48,50,52,54,56,58,60,62,64,0,10,1,0,52,55,1,0,1,2,1,0,3,10,3,
        0,62,62,64,66,87,88,2,0,63,63,67,72,1,0,58,59,2,0,1,1,13,14,1,0,
        15,20,1,0,21,22,1,0,23,25,636,0,67,1,0,0,0,2,88,1,0,0,0,4,125,1,
        0,0,0,6,128,1,0,0,0,8,142,1,0,0,0,10,152,1,0,0,0,12,154,1,0,0,0,
        14,199,1,0,0,0,16,201,1,0,0,0,18,215,1,0,0,0,20,227,1,0,0,0,22,229,
        1,0,0,0,24,239,1,0,0,0,26,252,1,0,0,0,28,277,1,0,0,0,30,281,1,0,
        0,0,32,300,1,0,0,0,34,369,1,0,0,0,36,371,1,0,0,0,38,387,1,0,0,0,
        40,395,1,0,0,0,42,405,1,0,0,0,44,446,1,0,0,0,46,448,1,0,0,0,48,459,
        1,0,0,0,50,470,1,0,0,0,52,479,1,0,0,0,54,481,1,0,0,0,56,493,1,0,
        0,0,58,527,1,0,0,0,60,529,1,0,0,0,62,542,1,0,0,0,64,547,1,0,0,0,
        66,68,3,2,1,0,67,66,1,0,0,0,68,69,1,0,0,0,69,67,1,0,0,0,69,70,1,
        0,0,0,70,1,1,0,0,0,71,89,3,8,4,0,72,89,3,4,2,0,73,89,3,22,11,0,74,
        89,3,26,13,0,75,89,3,36,18,0,76,89,3,42,21,0,77,89,3,16,8,0,78,89,
        3,34,17,0,79,89,3,6,3,0,80,89,3,12,6,0,81,89,3,58,29,0,82,89,3,50,
        25,0,83,89,3,40,20,0,84,89,3,44,22,0,85,89,5,31,0,0,86,89,3,62,31,
        0,87,89,3,64,32,0,88,71,1,0,0,0,88,72,1,0,0,0,88,73,1,0,0,0,88,74,
        1,0,0,0,88,75,1,0,0,0,88,76,1,0,0,0,88,77,1,0,0,0,88,78,1,0,0,0,
        88,79,1,0,0,0,88,80,1,0,0,0,88,81,1,0,0,0,88,82,1,0,0,0,88,83,1,
        0,0,0,88,84,1,0,0,0,88,85,1,0,0,0,88,86,1,0,0,0,88,87,1,0,0,0,89,
        3,1,0,0,0,90,91,5,91,0,0,91,93,5,63,0,0,92,94,3,10,5,0,93,92,1,0,
        0,0,93,94,1,0,0,0,94,96,1,0,0,0,95,97,5,79,0,0,96,95,1,0,0,0,96,
        97,1,0,0,0,97,102,1,0,0,0,98,103,3,42,21,0,99,103,3,6,3,0,100,103,
        3,44,22,0,101,103,3,60,30,0,102,98,1,0,0,0,102,99,1,0,0,0,102,100,
        1,0,0,0,102,101,1,0,0,0,103,105,1,0,0,0,104,106,5,80,0,0,105,104,
        1,0,0,0,105,106,1,0,0,0,106,107,1,0,0,0,107,108,5,76,0,0,108,126,
        1,0,0,0,109,110,5,91,0,0,110,111,5,63,0,0,111,112,5,91,0,0,112,116,
        5,79,0,0,113,117,3,38,19,0,114,117,3,42,21,0,115,117,3,44,22,0,116,
        113,1,0,0,0,116,114,1,0,0,0,116,115,1,0,0,0,116,117,1,0,0,0,117,
        118,1,0,0,0,118,119,5,80,0,0,119,126,5,76,0,0,120,121,5,91,0,0,121,
        122,5,63,0,0,122,123,3,14,7,0,123,124,5,76,0,0,124,126,1,0,0,0,125,
        90,1,0,0,0,125,109,1,0,0,0,125,120,1,0,0,0,126,5,1,0,0,0,127,129,
        3,10,5,0,128,127,1,0,0,0,128,129,1,0,0,0,129,131,1,0,0,0,130,132,
        5,79,0,0,131,130,1,0,0,0,131,132,1,0,0,0,132,133,1,0,0,0,133,134,
        5,50,0,0,134,136,5,79,0,0,135,137,3,42,21,0,136,135,1,0,0,0,136,
        137,1,0,0,0,137,138,1,0,0,0,138,140,5,80,0,0,139,141,5,80,0,0,140,
        139,1,0,0,0,140,141,1,0,0,0,141,7,1,0,0,0,142,143,5,51,0,0,143,147,
        5,79,0,0,144,148,3,42,21,0,145,148,5,74,0,0,146,148,3,44,22,0,147,
        144,1,0,0,0,147,145,1,0,0,0,147,146,1,0,0,0,147,148,1,0,0,0,148,
        149,1,0,0,0,149,150,5,80,0,0,150,151,5,76,0,0,151,9,1,0,0,0,152,
        153,7,0,0,0,153,11,1,0,0,0,154,155,3,10,5,0,155,156,5,79,0,0,156,
        157,3,42,21,0,157,158,5,80,0,0,158,13,1,0,0,0,159,161,5,77,0,0,160,
        162,9,0,0,0,161,160,1,0,0,0,162,163,1,0,0,0,163,164,1,0,0,0,163,
        161,1,0,0,0,164,165,1,0,0,0,165,200,5,77,0,0,166,168,5,78,0,0,167,
        169,9,0,0,0,168,167,1,0,0,0,169,170,1,0,0,0,170,171,1,0,0,0,170,
        168,1,0,0,0,171,172,1,0,0,0,172,200,5,78,0,0,173,182,5,78,0,0,174,
        176,9,0,0,0,175,174,1,0,0,0,176,177,1,0,0,0,177,178,1,0,0,0,177,
        175,1,0,0,0,178,181,1,0,0,0,179,181,5,30,0,0,180,175,1,0,0,0,180,
        179,1,0,0,0,181,184,1,0,0,0,182,180,1,0,0,0,182,183,1,0,0,0,183,
        185,1,0,0,0,184,182,1,0,0,0,185,200,5,78,0,0,186,195,5,77,0,0,187,
        189,9,0,0,0,188,187,1,0,0,0,189,190,1,0,0,0,190,191,1,0,0,0,190,
        188,1,0,0,0,191,194,1,0,0,0,192,194,5,30,0,0,193,188,1,0,0,0,193,
        192,1,0,0,0,194,197,1,0,0,0,195,193,1,0,0,0,195,196,1,0,0,0,196,
        198,1,0,0,0,197,195,1,0,0,0,198,200,5,77,0,0,199,159,1,0,0,0,199,
        166,1,0,0,0,199,173,1,0,0,0,199,186,1,0,0,0,200,15,1,0,0,0,201,202,
        5,35,0,0,202,203,5,91,0,0,203,205,5,79,0,0,204,206,3,38,19,0,205,
        204,1,0,0,0,205,206,1,0,0,0,206,207,1,0,0,0,207,208,5,80,0,0,208,
        209,5,82,0,0,209,210,3,18,9,0,210,211,5,81,0,0,211,17,1,0,0,0,212,
        214,3,2,1,0,213,212,1,0,0,0,214,217,1,0,0,0,215,213,1,0,0,0,215,
        216,1,0,0,0,216,219,1,0,0,0,217,215,1,0,0,0,218,220,3,20,10,0,219,
        218,1,0,0,0,219,220,1,0,0,0,220,19,1,0,0,0,221,222,5,47,0,0,222,
        223,3,42,21,0,223,224,5,76,0,0,224,228,1,0,0,0,225,226,5,47,0,0,
        226,228,5,76,0,0,227,221,1,0,0,0,227,225,1,0,0,0,228,21,1,0,0,0,
        229,230,5,91,0,0,230,232,5,79,0,0,231,233,3,24,12,0,232,231,1,0,
        0,0,232,233,1,0,0,0,233,234,1,0,0,0,234,235,5,80,0,0,235,23,1,0,
        0,0,236,240,3,52,26,0,237,240,5,91,0,0,238,240,3,22,11,0,239,236,
        1,0,0,0,239,237,1,0,0,0,239,238,1,0,0,0,240,249,1,0,0,0,241,245,
        5,74,0,0,242,246,3,52,26,0,243,246,5,91,0,0,244,246,3,22,11,0,245,
        242,1,0,0,0,245,243,1,0,0,0,245,244,1,0,0,0,246,248,1,0,0,0,247,
        241,1,0,0,0,248,251,1,0,0,0,249,247,1,0,0,0,249,250,1,0,0,0,250,
        25,1,0,0,0,251,249,1,0,0,0,252,254,5,37,0,0,253,255,5,79,0,0,254,
        253,1,0,0,0,254,255,1,0,0,0,255,258,1,0,0,0,256,259,3,38,19,0,257,
        259,3,42,21,0,258,256,1,0,0,0,258,257,1,0,0,0,259,261,1,0,0,0,260,
        262,5,80,0,0,261,260,1,0,0,0,261,262,1,0,0,0,262,263,1,0,0,0,263,
        265,5,82,0,0,264,266,3,2,1,0,265,264,1,0,0,0,266,267,1,0,0,0,267,
        265,1,0,0,0,267,268,1,0,0,0,268,269,1,0,0,0,269,271,5,81,0,0,270,
        272,3,28,14,0,271,270,1,0,0,0,271,272,1,0,0,0,272,274,1,0,0,0,273,
        275,3,32,16,0,274,273,1,0,0,0,274,275,1,0,0,0,275,27,1,0,0,0,276,
        278,3,30,15,0,277,276,1,0,0,0,278,279,1,0,0,0,279,277,1,0,0,0,279,
        280,1,0,0,0,280,29,1,0,0,0,281,283,5,61,0,0,282,284,5,79,0,0,283,
        282,1,0,0,0,283,284,1,0,0,0,284,287,1,0,0,0,285,288,3,38,19,0,286,
        288,3,42,21,0,287,285,1,0,0,0,287,286,1,0,0,0,288,290,1,0,0,0,289,
        291,5,80,0,0,290,289,1,0,0,0,290,291,1,0,0,0,291,292,1,0,0,0,292,
        294,5,82,0,0,293,295,3,2,1,0,294,293,1,0,0,0,295,296,1,0,0,0,296,
        294,1,0,0,0,296,297,1,0,0,0,297,298,1,0,0,0,298,299,5,81,0,0,299,
        31,1,0,0,0,300,301,5,38,0,0,301,303,5,82,0,0,302,304,3,2,1,0,303,
        302,1,0,0,0,304,305,1,0,0,0,305,303,1,0,0,0,305,306,1,0,0,0,306,
        307,1,0,0,0,307,308,5,81,0,0,308,33,1,0,0,0,309,310,5,39,0,0,310,
        311,5,91,0,0,311,312,5,40,0,0,312,313,5,41,0,0,313,314,5,79,0,0,
        314,316,3,42,21,0,315,317,5,74,0,0,316,315,1,0,0,0,316,317,1,0,0,
        0,317,319,1,0,0,0,318,320,3,42,21,0,319,318,1,0,0,0,319,320,1,0,
        0,0,320,322,1,0,0,0,321,323,5,74,0,0,322,321,1,0,0,0,322,323,1,0,
        0,0,323,325,1,0,0,0,324,326,3,42,21,0,325,324,1,0,0,0,325,326,1,
        0,0,0,326,327,1,0,0,0,327,328,5,80,0,0,328,330,5,82,0,0,329,331,
        3,2,1,0,330,329,1,0,0,0,331,332,1,0,0,0,332,330,1,0,0,0,332,333,
        1,0,0,0,333,335,1,0,0,0,334,336,3,20,10,0,335,334,1,0,0,0,335,336,
        1,0,0,0,336,337,1,0,0,0,337,338,5,81,0,0,338,370,1,0,0,0,339,340,
        5,39,0,0,340,341,5,91,0,0,341,342,5,40,0,0,342,343,3,42,21,0,343,
        345,5,82,0,0,344,346,3,2,1,0,345,344,1,0,0,0,346,347,1,0,0,0,347,
        345,1,0,0,0,347,348,1,0,0,0,348,350,1,0,0,0,349,351,3,20,10,0,350,
        349,1,0,0,0,350,351,1,0,0,0,351,352,1,0,0,0,352,353,5,81,0,0,353,
        370,1,0,0,0,354,355,5,39,0,0,355,356,5,91,0,0,356,357,5,40,0,0,357,
        358,3,14,7,0,358,360,5,82,0,0,359,361,3,2,1,0,360,359,1,0,0,0,361,
        362,1,0,0,0,362,360,1,0,0,0,362,363,1,0,0,0,363,365,1,0,0,0,364,
        366,3,20,10,0,365,364,1,0,0,0,365,366,1,0,0,0,366,367,1,0,0,0,367,
        368,5,81,0,0,368,370,1,0,0,0,369,309,1,0,0,0,369,339,1,0,0,0,369,
        354,1,0,0,0,370,35,1,0,0,0,371,373,5,43,0,0,372,374,5,79,0,0,373,
        372,1,0,0,0,373,374,1,0,0,0,374,375,1,0,0,0,375,377,3,42,21,0,376,
        378,5,80,0,0,377,376,1,0,0,0,377,378,1,0,0,0,378,379,1,0,0,0,379,
        381,5,82,0,0,380,382,3,2,1,0,381,380,1,0,0,0,382,383,1,0,0,0,383,
        381,1,0,0,0,383,384,1,0,0,0,384,385,1,0,0,0,385,386,5,81,0,0,386,
        37,1,0,0,0,387,392,5,91,0,0,388,389,5,74,0,0,389,391,5,91,0,0,390,
        388,1,0,0,0,391,394,1,0,0,0,392,390,1,0,0,0,392,393,1,0,0,0,393,
        39,1,0,0,0,394,392,1,0,0,0,395,396,7,1,0,0,396,397,5,73,0,0,397,
        398,7,2,0,0,398,399,5,79,0,0,399,400,3,42,21,0,400,401,5,80,0,0,
        401,41,1,0,0,0,402,403,6,21,-1,0,403,406,3,52,26,0,404,406,3,40,
        20,0,405,402,1,0,0,0,405,404,1,0,0,0,406,418,1,0,0,0,407,408,10,
        5,0,0,408,409,7,3,0,0,409,417,3,52,26,0,410,411,10,4,0,0,411,412,
        7,4,0,0,412,417,3,52,26,0,413,414,10,3,0,0,414,415,7,5,0,0,415,417,
        3,52,26,0,416,407,1,0,0,0,416,410,1,0,0,0,416,413,1,0,0,0,417,420,
        1,0,0,0,418,416,1,0,0,0,418,419,1,0,0,0,419,43,1,0,0,0,420,418,1,
        0,0,0,421,423,3,46,23,0,422,424,5,62,0,0,423,422,1,0,0,0,423,424,
        1,0,0,0,424,426,1,0,0,0,425,427,3,46,23,0,426,425,1,0,0,0,426,427,
        1,0,0,0,427,447,1,0,0,0,428,429,3,46,23,0,429,430,5,64,0,0,430,431,
        3,46,23,0,431,447,1,0,0,0,432,433,3,46,23,0,433,434,5,66,0,0,434,
        435,3,46,23,0,435,447,1,0,0,0,436,437,5,11,0,0,437,438,5,79,0,0,
        438,439,3,46,23,0,439,440,5,80,0,0,440,447,1,0,0,0,441,442,5,12,
        0,0,442,443,5,79,0,0,443,444,3,46,23,0,444,445,5,80,0,0,445,447,
        1,0,0,0,446,421,1,0,0,0,446,428,1,0,0,0,446,432,1,0,0,0,446,436,
        1,0,0,0,446,441,1,0,0,0,447,45,1,0,0,0,448,449,5,83,0,0,449,454,
        3,48,24,0,450,451,5,74,0,0,451,453,3,48,24,0,452,450,1,0,0,0,453,
        456,1,0,0,0,454,452,1,0,0,0,454,455,1,0,0,0,455,457,1,0,0,0,456,
        454,1,0,0,0,457,458,5,84,0,0,458,47,1,0,0,0,459,460,5,83,0,0,460,
        465,3,42,21,0,461,462,5,74,0,0,462,464,3,42,21,0,463,461,1,0,0,0,
        464,467,1,0,0,0,465,463,1,0,0,0,465,466,1,0,0,0,466,468,1,0,0,0,
        467,465,1,0,0,0,468,469,5,84,0,0,469,49,1,0,0,0,470,471,5,34,0,0,
        471,472,7,6,0,0,472,51,1,0,0,0,473,480,5,32,0,0,474,480,5,91,0,0,
        475,480,5,54,0,0,476,480,3,14,7,0,477,480,3,54,27,0,478,480,3,56,
        28,0,479,473,1,0,0,0,479,474,1,0,0,0,479,475,1,0,0,0,479,476,1,0,
        0,0,479,477,1,0,0,0,479,478,1,0,0,0,480,53,1,0,0,0,481,487,5,79,
        0,0,482,488,5,32,0,0,483,488,5,91,0,0,484,488,5,54,0,0,485,488,3,
        14,7,0,486,488,5,74,0,0,487,482,1,0,0,0,487,483,1,0,0,0,487,484,
        1,0,0,0,487,485,1,0,0,0,487,486,1,0,0,0,488,489,1,0,0,0,489,487,
        1,0,0,0,489,490,1,0,0,0,490,491,1,0,0,0,491,492,5,80,0,0,492,55,
        1,0,0,0,493,499,5,83,0,0,494,500,5,32,0,0,495,500,5,91,0,0,496,500,
        5,54,0,0,497,500,3,14,7,0,498,500,5,74,0,0,499,494,1,0,0,0,499,495,
        1,0,0,0,499,496,1,0,0,0,499,497,1,0,0,0,499,498,1,0,0,0,500,501,
        1,0,0,0,501,499,1,0,0,0,501,502,1,0,0,0,502,503,1,0,0,0,503,504,
        5,84,0,0,504,57,1,0,0,0,505,506,7,7,0,0,506,507,5,79,0,0,507,508,
        3,42,21,0,508,509,5,74,0,0,509,510,3,42,21,0,510,511,5,80,0,0,511,
        528,1,0,0,0,512,513,7,8,0,0,513,514,5,79,0,0,514,515,3,42,21,0,515,
        516,5,80,0,0,516,528,1,0,0,0,517,518,7,9,0,0,518,521,5,79,0,0,519,
        522,3,60,30,0,520,522,5,91,0,0,521,519,1,0,0,0,521,520,1,0,0,0,522,
        523,1,0,0,0,523,524,5,74,0,0,524,525,3,40,20,0,525,526,5,80,0,0,
        526,528,1,0,0,0,527,505,1,0,0,0,527,512,1,0,0,0,527,517,1,0,0,0,
        528,59,1,0,0,0,529,530,5,26,0,0,530,531,5,79,0,0,531,532,3,42,21,
        0,532,533,5,74,0,0,533,534,3,42,21,0,534,535,5,66,0,0,535,536,5,
        2,0,0,536,537,5,73,0,0,537,538,5,27,0,0,538,539,5,74,0,0,539,540,
        3,42,21,0,540,541,5,80,0,0,541,61,1,0,0,0,542,543,5,90,0,0,543,544,
        5,79,0,0,544,545,3,42,21,0,545,546,5,80,0,0,546,63,1,0,0,0,547,548,
        5,89,0,0,548,549,5,79,0,0,549,550,3,42,21,0,550,551,5,80,0,0,551,
        552,5,75,0,0,552,553,3,42,21,0,553,554,5,45,0,0,554,65,1,0,0,0,72,
        69,88,93,96,102,105,116,125,128,131,136,140,147,163,170,177,180,
        182,190,193,195,199,205,215,219,227,232,239,245,249,254,258,261,
        267,271,274,279,283,287,290,296,305,316,319,322,325,332,335,347,
        350,362,365,369,373,377,383,392,405,416,418,423,426,446,454,465,
        479,487,489,499,501,521,527
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
                     "'pi'", "'\\u00AC'", "'~'", "'!'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'import'", "'def'", "'class'", "'if'", 
                     "'else'", "'for'", "'in'", "'range'", "'self'", "'while'", 
                     "'try'", "'end'", "'except'", "'return'", "'break'", 
                     "'next'", "'input'", "'print'", "'int'", "'float'", 
                     "<INVALID>", "'str'", "'pow'", "'mathsqrt'", "'and'", 
                     "'or'", "'not'", "'elif'", "'+'", "'='", "'-'", "'/'", 
                     "'*'", "'=='", "'!='", "'>'", "'<'", "'>='", "'<='", 
                     "'.'", "','", "':'", "';'", "'''", "'\"'", "'('", "')'", 
                     "'}'", "'{'", "'['", "']'", "'++'", "'--'", "'^'", 
                     "'%'", "'write'", "'open'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "SEP", "ESP", "EX", "NEWLINE", "NUMERO", "WS", "IMPORT", 
                      "DEF", "CLASS", "IF", "ELSE", "FOR", "IN", "RANGE", 
                      "SELF", "WHILE", "TRY", "END", "EXCEPT", "RETURN", 
                      "BREAK", "NEXT", "INPUT", "PRINT", "INT", "FLOAT", 
                      "BOOLEAN", "STR", "POW", "MATHSQRT", "AND", "OR", 
                      "NOT", "ELIF", "SUMA", "ASIGNACION", "RESTA", "DIVISION", 
                      "MULTIPLICACION", "IGUAL", "DIFERENTE", "MAYORQUE", 
                      "MENORQUE", "MENORIGUAL", "MAYORIGUAL", "PUNTO", "COMA", 
                      "DOSPUNTOS", "PUNTOCOMA", "COMILLASIMPLE", "COMILLADOBLE", 
                      "PARENTESIS_A", "PARENTESIS_C", "LLAVE_C", "LLAVE_A", 
                      "CORCHETE_A", "CORCHETE_C", "MASMAS", "MENOSMENOS", 
                      "POTENCIA", "MODULO", "WRITE", "OPEN", "ID" ]

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
    NUMERO=32
    WS=33
    IMPORT=34
    DEF=35
    CLASS=36
    IF=37
    ELSE=38
    FOR=39
    IN=40
    RANGE=41
    SELF=42
    WHILE=43
    TRY=44
    END=45
    EXCEPT=46
    RETURN=47
    BREAK=48
    NEXT=49
    INPUT=50
    PRINT=51
    INT=52
    FLOAT=53
    BOOLEAN=54
    STR=55
    POW=56
    MATHSQRT=57
    AND=58
    OR=59
    NOT=60
    ELIF=61
    SUMA=62
    ASIGNACION=63
    RESTA=64
    DIVISION=65
    MULTIPLICACION=66
    IGUAL=67
    DIFERENTE=68
    MAYORQUE=69
    MENORQUE=70
    MENORIGUAL=71
    MAYORIGUAL=72
    PUNTO=73
    COMA=74
    DOSPUNTOS=75
    PUNTOCOMA=76
    COMILLASIMPLE=77
    COMILLADOBLE=78
    PARENTESIS_A=79
    PARENTESIS_C=80
    LLAVE_C=81
    LLAVE_A=82
    CORCHETE_A=83
    CORCHETE_C=84
    MASMAS=85
    MENOSMENOS=86
    POTENCIA=87
    MODULO=88
    WRITE=89
    OPEN=90
    ID=91

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
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 70941235468015622) != 0) or ((((_la - 77)) & ~0x3f) == 0 and ((1 << (_la - 77)) & 28743) != 0)):
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
                if _la==80:
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
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 67553994410557440) != 0):
                self.state = 127
                self.var_casteo()


            self.state = 131
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==79:
                self.state = 130
                self.match(gramaticaParser.PARENTESIS_A)


            self.state = 133
            self.match(gramaticaParser.INPUT)
            self.state = 134
            self.match(gramaticaParser.PARENTESIS_A)
            self.state = 136
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 18014402804449286) != 0) or ((((_la - 77)) & ~0x3f) == 0 and ((1 << (_la - 77)) & 16455) != 0):
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
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 67553994410557440) != 0)):
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

        def COMILLASIMPLE(self, i:int=None):
            if i is None:
                return self.getTokens(gramaticaParser.COMILLASIMPLE)
            else:
                return self.getToken(gramaticaParser.COMILLASIMPLE, i)

        def COMILLADOBLE(self, i:int=None):
            if i is None:
                return self.getTokens(gramaticaParser.COMILLADOBLE)
            else:
                return self.getToken(gramaticaParser.COMILLADOBLE, i)

        def EX(self, i:int=None):
            if i is None:
                return self.getTokens(gramaticaParser.EX)
            else:
                return self.getToken(gramaticaParser.EX, i)

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
            self.state = 199
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 159
                self.match(gramaticaParser.COMILLASIMPLE)
                self.state = 161 
                self._errHandler.sync(self)
                _alt = 1+1
                while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1+1:
                        self.state = 160
                        self.matchWildcard()

                    else:
                        raise NoViableAltException(self)
                    self.state = 163 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,13,self._ctx)

                self.state = 165
                self.match(gramaticaParser.COMILLASIMPLE)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 166
                self.match(gramaticaParser.COMILLADOBLE)
                self.state = 168 
                self._errHandler.sync(self)
                _alt = 1+1
                while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1+1:
                        self.state = 167
                        self.matchWildcard()

                    else:
                        raise NoViableAltException(self)
                    self.state = 170 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,14,self._ctx)

                self.state = 172
                self.match(gramaticaParser.COMILLADOBLE)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 173
                self.match(gramaticaParser.COMILLADOBLE)
                self.state = 182
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,17,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 180
                        self._errHandler.sync(self)
                        la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
                        if la_ == 1:
                            self.state = 175 
                            self._errHandler.sync(self)
                            _alt = 1+1
                            while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                                if _alt == 1+1:
                                    self.state = 174
                                    self.matchWildcard()

                                else:
                                    raise NoViableAltException(self)
                                self.state = 177 
                                self._errHandler.sync(self)
                                _alt = self._interp.adaptivePredict(self._input,15,self._ctx)

                            pass

                        elif la_ == 2:
                            self.state = 179
                            self.match(gramaticaParser.EX)
                            pass

                 
                    self.state = 184
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,17,self._ctx)

                self.state = 185
                self.match(gramaticaParser.COMILLADOBLE)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 186
                self.match(gramaticaParser.COMILLASIMPLE)
                self.state = 195
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,20,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 193
                        self._errHandler.sync(self)
                        la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
                        if la_ == 1:
                            self.state = 188 
                            self._errHandler.sync(self)
                            _alt = 1+1
                            while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                                if _alt == 1+1:
                                    self.state = 187
                                    self.matchWildcard()

                                else:
                                    raise NoViableAltException(self)
                                self.state = 190 
                                self._errHandler.sync(self)
                                _alt = self._interp.adaptivePredict(self._input,18,self._ctx)

                            pass

                        elif la_ == 2:
                            self.state = 192
                            self.match(gramaticaParser.EX)
                            pass

                 
                    self.state = 197
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,20,self._ctx)

                self.state = 198
                self.match(gramaticaParser.COMILLASIMPLE)
                pass


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
            self.state = 201
            self.match(gramaticaParser.DEF)
            self.state = 202
            self.match(gramaticaParser.ID)
            self.state = 203
            self.match(gramaticaParser.PARENTESIS_A)
            self.state = 205
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==91:
                self.state = 204
                self.parametro()


            self.state = 207
            self.match(gramaticaParser.PARENTESIS_C)
            self.state = 208
            self.match(gramaticaParser.LLAVE_A)
            self.state = 209
            self.stmt_func()
            self.state = 210
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
        self.enterRule(localctx, 18, self.RULE_stmt_func)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 215
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 70941235468015622) != 0) or ((((_la - 77)) & ~0x3f) == 0 and ((1 << (_la - 77)) & 28743) != 0):
                self.state = 212
                self.sentencias()
                self.state = 217
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 219
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==47:
                self.state = 218
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
            self.state = 227
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 221
                self.match(gramaticaParser.RETURN)
                self.state = 222
                self.expresion(0)
                self.state = 223
                self.match(gramaticaParser.PUNTOCOMA)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 225
                self.match(gramaticaParser.RETURN)
                self.state = 226
                self.match(gramaticaParser.PUNTOCOMA)
                pass


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
            self.state = 229
            self.match(gramaticaParser.ID)
            self.state = 230
            self.match(gramaticaParser.PARENTESIS_A)
            self.state = 232
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 32)) & ~0x3f) == 0 and ((1 << (_la - 32)) & 578958842725924865) != 0):
                self.state = 231
                self.args()


            self.state = 234
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
            self.state = 239
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.state = 236
                self.termino()
                pass

            elif la_ == 2:
                self.state = 237
                self.match(gramaticaParser.ID)
                pass

            elif la_ == 3:
                self.state = 238
                self.llamafuncion()
                pass


            self.state = 249
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==74:
                self.state = 241
                self.match(gramaticaParser.COMA)
                self.state = 245
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
                if la_ == 1:
                    self.state = 242
                    self.termino()
                    pass

                elif la_ == 2:
                    self.state = 243
                    self.match(gramaticaParser.ID)
                    pass

                elif la_ == 3:
                    self.state = 244
                    self.llamafuncion()
                    pass


                self.state = 251
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

        def LLAVE_A(self):
            return self.getToken(gramaticaParser.LLAVE_A, 0)

        def LLAVE_C(self):
            return self.getToken(gramaticaParser.LLAVE_C, 0)

        def parametro(self):
            return self.getTypedRuleContext(gramaticaParser.ParametroContext,0)


        def expresion(self):
            return self.getTypedRuleContext(gramaticaParser.ExpresionContext,0)


        def PARENTESIS_A(self):
            return self.getToken(gramaticaParser.PARENTESIS_A, 0)

        def PARENTESIS_C(self):
            return self.getToken(gramaticaParser.PARENTESIS_C, 0)

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
            self.state = 252
            self.match(gramaticaParser.IF)
            self.state = 254
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.state = 253
                self.match(gramaticaParser.PARENTESIS_A)


            self.state = 258
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.state = 256
                self.parametro()
                pass

            elif la_ == 2:
                self.state = 257
                self.expresion(0)
                pass


            self.state = 261
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==80:
                self.state = 260
                self.match(gramaticaParser.PARENTESIS_C)


            self.state = 263
            self.match(gramaticaParser.LLAVE_A)
            self.state = 265 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 264
                self.sentencias()
                self.state = 267 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 70941235468015622) != 0) or ((((_la - 77)) & ~0x3f) == 0 and ((1 << (_la - 77)) & 28743) != 0)):
                    break

            self.state = 269
            self.match(gramaticaParser.LLAVE_C)
            self.state = 271
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==61:
                self.state = 270
                self.elifBlock()


            self.state = 274
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==38:
                self.state = 273
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
            self.state = 277 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 276
                self.condicional_elif()
                self.state = 279 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==61):
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

        def LLAVE_A(self):
            return self.getToken(gramaticaParser.LLAVE_A, 0)

        def LLAVE_C(self):
            return self.getToken(gramaticaParser.LLAVE_C, 0)

        def parametro(self):
            return self.getTypedRuleContext(gramaticaParser.ParametroContext,0)


        def expresion(self):
            return self.getTypedRuleContext(gramaticaParser.ExpresionContext,0)


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
            self.state = 281
            self.match(gramaticaParser.ELIF)
            self.state = 283
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
            if la_ == 1:
                self.state = 282
                self.match(gramaticaParser.PARENTESIS_A)


            self.state = 287
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
            if la_ == 1:
                self.state = 285
                self.parametro()
                pass

            elif la_ == 2:
                self.state = 286
                self.expresion(0)
                pass


            self.state = 290
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==80:
                self.state = 289
                self.match(gramaticaParser.PARENTESIS_C)


            self.state = 292
            self.match(gramaticaParser.LLAVE_A)
            self.state = 294 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 293
                self.sentencias()
                self.state = 296 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 70941235468015622) != 0) or ((((_la - 77)) & ~0x3f) == 0 and ((1 << (_la - 77)) & 28743) != 0)):
                    break

            self.state = 298
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
            self.state = 300
            self.match(gramaticaParser.ELSE)
            self.state = 301
            self.match(gramaticaParser.LLAVE_A)
            self.state = 303 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 302
                self.sentencias()
                self.state = 305 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 70941235468015622) != 0) or ((((_la - 77)) & ~0x3f) == 0 and ((1 << (_la - 77)) & 28743) != 0)):
                    break

            self.state = 307
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
            self.state = 369
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,52,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 309
                self.match(gramaticaParser.FOR)
                self.state = 310
                self.match(gramaticaParser.ID)
                self.state = 311
                self.match(gramaticaParser.IN)
                self.state = 312
                self.match(gramaticaParser.RANGE)
                self.state = 313
                self.match(gramaticaParser.PARENTESIS_A)
                self.state = 314
                self.expresion(0)
                self.state = 316
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,42,self._ctx)
                if la_ == 1:
                    self.state = 315
                    self.match(gramaticaParser.COMA)


                self.state = 319
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,43,self._ctx)
                if la_ == 1:
                    self.state = 318
                    self.expresion(0)


                self.state = 322
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==74:
                    self.state = 321
                    self.match(gramaticaParser.COMA)


                self.state = 325
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 18014402804449286) != 0) or ((((_la - 77)) & ~0x3f) == 0 and ((1 << (_la - 77)) & 16455) != 0):
                    self.state = 324
                    self.expresion(0)


                self.state = 327
                self.match(gramaticaParser.PARENTESIS_C)
                self.state = 328
                self.match(gramaticaParser.LLAVE_A)
                self.state = 330 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 329
                    self.sentencias()
                    self.state = 332 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 70941235468015622) != 0) or ((((_la - 77)) & ~0x3f) == 0 and ((1 << (_la - 77)) & 28743) != 0)):
                        break

                self.state = 335
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==47:
                    self.state = 334
                    self.v_return()


                self.state = 337
                self.match(gramaticaParser.LLAVE_C)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 339
                self.match(gramaticaParser.FOR)
                self.state = 340
                self.match(gramaticaParser.ID)
                self.state = 341
                self.match(gramaticaParser.IN)
                self.state = 342
                self.expresion(0)
                self.state = 343
                self.match(gramaticaParser.LLAVE_A)
                self.state = 345 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 344
                    self.sentencias()
                    self.state = 347 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 70941235468015622) != 0) or ((((_la - 77)) & ~0x3f) == 0 and ((1 << (_la - 77)) & 28743) != 0)):
                        break

                self.state = 350
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==47:
                    self.state = 349
                    self.v_return()


                self.state = 352
                self.match(gramaticaParser.LLAVE_C)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 354
                self.match(gramaticaParser.FOR)
                self.state = 355
                self.match(gramaticaParser.ID)
                self.state = 356
                self.match(gramaticaParser.IN)
                self.state = 357
                self.cadena()
                self.state = 358
                self.match(gramaticaParser.LLAVE_A)
                self.state = 360 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 359
                    self.sentencias()
                    self.state = 362 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 70941235468015622) != 0) or ((((_la - 77)) & ~0x3f) == 0 and ((1 << (_la - 77)) & 28743) != 0)):
                        break

                self.state = 365
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==47:
                    self.state = 364
                    self.v_return()


                self.state = 367
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
            self.state = 371
            self.match(gramaticaParser.WHILE)
            self.state = 373
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,53,self._ctx)
            if la_ == 1:
                self.state = 372
                self.match(gramaticaParser.PARENTESIS_A)


            self.state = 375
            self.expresion(0)
            self.state = 377
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==80:
                self.state = 376
                self.match(gramaticaParser.PARENTESIS_C)


            self.state = 379
            self.match(gramaticaParser.LLAVE_A)
            self.state = 381 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 380
                self.sentencias()
                self.state = 383 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 70941235468015622) != 0) or ((((_la - 77)) & ~0x3f) == 0 and ((1 << (_la - 77)) & 28743) != 0)):
                    break

            self.state = 385
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
            self.state = 387
            self.match(gramaticaParser.ID)
            self.state = 392
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==74:
                self.state = 388
                self.match(gramaticaParser.COMA)
                self.state = 389
                self.match(gramaticaParser.ID)
                self.state = 394
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
            self.state = 395
            _la = self._input.LA(1)
            if not(_la==1 or _la==2):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 396
            self.match(gramaticaParser.PUNTO)
            self.state = 397
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 2040) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 398
            self.match(gramaticaParser.PARENTESIS_A)
            self.state = 399
            self.expresion(0)
            self.state = 400
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
            self.state = 405
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [32, 54, 77, 78, 79, 83, 91]:
                self.state = 403
                self.termino()
                pass
            elif token in [1, 2]:
                self.state = 404
                self.func()
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 418
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,59,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 416
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,58,self._ctx)
                    if la_ == 1:
                        localctx = gramaticaParser.ExpresionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expresion)
                        self.state = 407
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 408
                        _la = self._input.LA(1)
                        if not(((((_la - 62)) & ~0x3f) == 0 and ((1 << (_la - 62)) & 100663325) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 409
                        self.termino()
                        pass

                    elif la_ == 2:
                        localctx = gramaticaParser.ExpresionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expresion)
                        self.state = 410
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 411
                        _la = self._input.LA(1)
                        if not(((((_la - 63)) & ~0x3f) == 0 and ((1 << (_la - 63)) & 1009) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 412
                        self.termino()
                        pass

                    elif la_ == 3:
                        localctx = gramaticaParser.ExpresionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expresion)
                        self.state = 413
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 414
                        _la = self._input.LA(1)
                        if not(_la==58 or _la==59):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 415
                        self.termino()
                        pass

             
                self.state = 420
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,59,self._ctx)

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
            self.state = 446
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,62,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 421
                self.matriz()
                self.state = 423
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==62:
                    self.state = 422
                    self.match(gramaticaParser.SUMA)


                self.state = 426
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,61,self._ctx)
                if la_ == 1:
                    self.state = 425
                    self.matriz()


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 428
                self.matriz()
                self.state = 429
                self.match(gramaticaParser.RESTA)
                self.state = 430
                self.matriz()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 432
                self.matriz()
                self.state = 433
                self.match(gramaticaParser.MULTIPLICACION)
                self.state = 434
                self.matriz()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 436
                self.match(gramaticaParser.T__10)
                self.state = 437
                self.match(gramaticaParser.PARENTESIS_A)
                self.state = 438
                self.matriz()
                self.state = 439
                self.match(gramaticaParser.PARENTESIS_C)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 441
                self.match(gramaticaParser.T__11)
                self.state = 442
                self.match(gramaticaParser.PARENTESIS_A)
                self.state = 443
                self.matriz()
                self.state = 444
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
            self.state = 448
            self.match(gramaticaParser.CORCHETE_A)
            self.state = 449
            self.fila_matriz()
            self.state = 454
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==74:
                self.state = 450
                self.match(gramaticaParser.COMA)
                self.state = 451
                self.fila_matriz()
                self.state = 456
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 457
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
            self.state = 459
            self.match(gramaticaParser.CORCHETE_A)
            self.state = 460
            self.expresion(0)
            self.state = 465
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==74:
                self.state = 461
                self.match(gramaticaParser.COMA)
                self.state = 462
                self.expresion(0)
                self.state = 467
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 468
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
            self.state = 470
            self.match(gramaticaParser.IMPORT)
            self.state = 471
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
            self.state = 479
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [32]:
                self.enterOuterAlt(localctx, 1)
                self.state = 473
                self.match(gramaticaParser.NUMERO)
                pass
            elif token in [91]:
                self.enterOuterAlt(localctx, 2)
                self.state = 474
                self.match(gramaticaParser.ID)
                pass
            elif token in [54]:
                self.enterOuterAlt(localctx, 3)
                self.state = 475
                self.match(gramaticaParser.BOOLEAN)
                pass
            elif token in [77, 78]:
                self.enterOuterAlt(localctx, 4)
                self.state = 476
                self.cadena()
                pass
            elif token in [79]:
                self.enterOuterAlt(localctx, 5)
                self.state = 477
                self.lista()
                pass
            elif token in [83]:
                self.enterOuterAlt(localctx, 6)
                self.state = 478
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
            self.state = 481
            self.match(gramaticaParser.PARENTESIS_A)
            self.state = 487 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 487
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [32]:
                    self.state = 482
                    self.match(gramaticaParser.NUMERO)
                    pass
                elif token in [91]:
                    self.state = 483
                    self.match(gramaticaParser.ID)
                    pass
                elif token in [54]:
                    self.state = 484
                    self.match(gramaticaParser.BOOLEAN)
                    pass
                elif token in [77, 78]:
                    self.state = 485
                    self.cadena()
                    pass
                elif token in [74]:
                    self.state = 486
                    self.match(gramaticaParser.COMA)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 489 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (((((_la - 32)) & ~0x3f) == 0 and ((1 << (_la - 32)) & 576570703470395393) != 0)):
                    break

            self.state = 491
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
            self.state = 493
            self.match(gramaticaParser.CORCHETE_A)
            self.state = 499 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 499
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [32]:
                    self.state = 494
                    self.match(gramaticaParser.NUMERO)
                    pass
                elif token in [91]:
                    self.state = 495
                    self.match(gramaticaParser.ID)
                    pass
                elif token in [54]:
                    self.state = 496
                    self.match(gramaticaParser.BOOLEAN)
                    pass
                elif token in [77, 78]:
                    self.state = 497
                    self.cadena()
                    pass
                elif token in [74]:
                    self.state = 498
                    self.match(gramaticaParser.COMA)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 501 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (((((_la - 32)) & ~0x3f) == 0 and ((1 << (_la - 32)) & 576570703470395393) != 0)):
                    break

            self.state = 503
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
            self.state = 527
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [15, 16, 17, 18, 19, 20]:
                self.enterOuterAlt(localctx, 1)
                self.state = 505
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 2064384) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 506
                self.match(gramaticaParser.PARENTESIS_A)
                self.state = 507
                localctx.x = self.expresion(0)
                self.state = 508
                self.match(gramaticaParser.COMA)
                self.state = 509
                localctx.y = self.expresion(0)
                self.state = 510
                self.match(gramaticaParser.PARENTESIS_C)
                pass
            elif token in [21, 22]:
                self.enterOuterAlt(localctx, 2)
                self.state = 512
                _la = self._input.LA(1)
                if not(_la==21 or _la==22):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 513
                self.match(gramaticaParser.PARENTESIS_A)
                self.state = 514
                localctx.x = self.expresion(0)
                self.state = 515
                self.match(gramaticaParser.PARENTESIS_C)
                pass
            elif token in [23, 24, 25]:
                self.enterOuterAlt(localctx, 3)
                self.state = 517
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 58720256) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 518
                self.match(gramaticaParser.PARENTESIS_A)
                self.state = 521
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [26]:
                    self.state = 519
                    self.arange()
                    pass
                elif token in [91]:
                    self.state = 520
                    self.match(gramaticaParser.ID)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 523
                self.match(gramaticaParser.COMA)
                self.state = 524
                self.func()
                self.state = 525
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
            self.state = 529
            self.match(gramaticaParser.T__25)
            self.state = 530
            self.match(gramaticaParser.PARENTESIS_A)
            self.state = 531
            self.expresion(0)
            self.state = 532
            self.match(gramaticaParser.COMA)
            self.state = 533
            self.expresion(0)
            self.state = 534
            self.match(gramaticaParser.MULTIPLICACION)
            self.state = 535
            self.match(gramaticaParser.T__1)
            self.state = 536
            self.match(gramaticaParser.PUNTO)
            self.state = 537
            self.match(gramaticaParser.T__26)
            self.state = 538
            self.match(gramaticaParser.COMA)
            self.state = 539
            self.expresion(0)
            self.state = 540
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
            self.state = 542
            self.match(gramaticaParser.OPEN)
            self.state = 543
            self.match(gramaticaParser.PARENTESIS_A)
            self.state = 544
            self.expresion(0)
            self.state = 545
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
            self.state = 547
            self.match(gramaticaParser.WRITE)
            self.state = 548
            self.match(gramaticaParser.PARENTESIS_A)
            self.state = 549
            self.expresion(0)
            self.state = 550
            self.match(gramaticaParser.PARENTESIS_C)
            self.state = 551
            self.match(gramaticaParser.DOSPUNTOS)
            self.state = 552
            self.expresion(0)
            self.state = 553
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
                return self.precpred(self._ctx, 5)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 3)
         




