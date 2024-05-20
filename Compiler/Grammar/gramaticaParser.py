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
        4,1,91,554,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,1,0,4,0,66,8,0,
        11,0,12,0,67,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,3,1,87,8,1,1,2,1,2,1,2,3,2,92,8,2,1,2,3,2,95,8,2,
        1,2,1,2,1,2,1,2,3,2,101,8,2,1,2,3,2,104,8,2,1,2,1,2,1,2,1,2,1,2,
        1,2,1,2,1,2,1,2,3,2,115,8,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,124,
        8,2,1,3,3,3,127,8,3,1,3,3,3,130,8,3,1,3,1,3,1,3,3,3,135,8,3,1,3,
        1,3,3,3,139,8,3,1,4,1,4,1,4,1,4,1,4,3,4,146,8,4,1,4,1,4,1,4,1,5,
        1,5,1,6,1,6,1,6,1,6,1,6,1,7,1,7,4,7,160,8,7,11,7,12,7,161,1,7,1,
        7,1,7,4,7,167,8,7,11,7,12,7,168,1,7,1,7,1,7,4,7,174,8,7,11,7,12,
        7,175,1,7,5,7,179,8,7,10,7,12,7,182,9,7,1,7,1,7,1,7,4,7,187,8,7,
        11,7,12,7,188,1,7,5,7,192,8,7,10,7,12,7,195,9,7,1,7,3,7,198,8,7,
        1,8,1,8,1,8,1,8,3,8,204,8,8,1,8,1,8,1,8,1,8,1,8,1,9,5,9,212,8,9,
        10,9,12,9,215,9,9,1,9,3,9,218,8,9,1,10,1,10,1,10,1,10,1,10,1,10,
        3,10,226,8,10,1,11,1,11,1,11,3,11,231,8,11,1,11,1,11,1,12,1,12,3,
        12,237,8,12,1,12,1,12,3,12,241,8,12,1,12,3,12,244,8,12,1,12,1,12,
        4,12,248,8,12,11,12,12,12,249,1,12,1,12,3,12,254,8,12,1,12,3,12,
        257,8,12,1,13,4,13,260,8,13,11,13,12,13,261,1,14,1,14,3,14,266,8,
        14,1,14,1,14,3,14,270,8,14,1,14,3,14,273,8,14,1,14,1,14,4,14,277,
        8,14,11,14,12,14,278,1,14,1,14,1,15,1,15,1,15,4,15,286,8,15,11,15,
        12,15,287,1,15,1,15,1,16,1,16,1,16,1,16,1,16,1,16,1,16,3,16,299,
        8,16,1,16,3,16,302,8,16,1,16,3,16,305,8,16,1,16,3,16,308,8,16,1,
        16,1,16,1,16,4,16,313,8,16,11,16,12,16,314,1,16,3,16,318,8,16,1,
        16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,4,16,328,8,16,11,16,12,16,
        329,1,16,3,16,333,8,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,4,
        16,343,8,16,11,16,12,16,344,1,16,3,16,348,8,16,1,16,1,16,3,16,352,
        8,16,1,17,1,17,3,17,356,8,17,1,17,1,17,3,17,360,8,17,1,17,1,17,4,
        17,364,8,17,11,17,12,17,365,1,17,1,17,1,18,1,18,1,18,5,18,373,8,
        18,10,18,12,18,376,9,18,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,20,
        1,20,1,20,3,20,388,8,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,
        1,20,5,20,399,8,20,10,20,12,20,402,9,20,1,21,1,21,3,21,406,8,21,
        1,21,3,21,409,8,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,
        1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,3,21,429,8,21,1,22,
        1,22,1,22,1,22,5,22,435,8,22,10,22,12,22,438,9,22,1,22,1,22,1,23,
        1,23,1,23,1,23,5,23,446,8,23,10,23,12,23,449,9,23,1,23,1,23,1,24,
        1,24,1,24,1,25,1,25,4,25,458,8,25,11,25,12,25,459,1,25,1,25,1,25,
        1,25,3,25,466,8,25,1,26,1,26,1,26,4,26,471,8,26,11,26,12,26,472,
        1,26,1,26,1,26,4,26,478,8,26,11,26,12,26,479,1,26,1,26,1,27,1,27,
        1,27,4,27,487,8,27,11,27,12,27,488,1,27,1,27,1,27,4,27,494,8,27,
        11,27,12,27,495,1,27,1,27,1,28,1,28,1,28,1,28,1,28,1,28,1,28,1,28,
        1,28,1,28,1,28,1,28,1,28,1,28,1,28,1,28,4,28,516,8,28,11,28,12,28,
        517,3,28,520,8,28,1,28,1,28,1,28,1,28,3,28,526,8,28,1,29,1,29,1,
        29,1,29,1,29,1,29,1,29,1,29,1,29,1,29,1,29,1,29,1,29,1,30,1,30,1,
        30,1,30,1,30,1,31,1,31,1,31,1,31,1,31,1,31,1,31,1,31,1,31,4,161,
        168,175,188,1,40,32,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,
        34,36,38,40,42,44,46,48,50,52,54,56,58,60,62,0,10,1,0,53,56,1,0,
        1,2,1,0,3,10,3,0,63,63,65,67,88,89,2,0,64,64,68,73,1,0,59,60,2,0,
        1,1,13,14,1,0,15,20,1,0,21,22,1,0,23,25,634,0,65,1,0,0,0,2,86,1,
        0,0,0,4,123,1,0,0,0,6,126,1,0,0,0,8,140,1,0,0,0,10,150,1,0,0,0,12,
        152,1,0,0,0,14,197,1,0,0,0,16,199,1,0,0,0,18,213,1,0,0,0,20,225,
        1,0,0,0,22,227,1,0,0,0,24,234,1,0,0,0,26,259,1,0,0,0,28,263,1,0,
        0,0,30,282,1,0,0,0,32,351,1,0,0,0,34,353,1,0,0,0,36,369,1,0,0,0,
        38,377,1,0,0,0,40,387,1,0,0,0,42,428,1,0,0,0,44,430,1,0,0,0,46,441,
        1,0,0,0,48,452,1,0,0,0,50,465,1,0,0,0,52,467,1,0,0,0,54,483,1,0,
        0,0,56,525,1,0,0,0,58,527,1,0,0,0,60,540,1,0,0,0,62,545,1,0,0,0,
        64,66,3,2,1,0,65,64,1,0,0,0,66,67,1,0,0,0,67,65,1,0,0,0,67,68,1,
        0,0,0,68,1,1,0,0,0,69,87,3,8,4,0,70,87,3,4,2,0,71,87,3,24,12,0,72,
        87,3,34,17,0,73,87,3,40,20,0,74,87,3,16,8,0,75,87,3,22,11,0,76,87,
        3,32,16,0,77,87,3,6,3,0,78,87,3,12,6,0,79,87,3,56,28,0,80,87,3,48,
        24,0,81,87,3,38,19,0,82,87,3,42,21,0,83,87,5,31,0,0,84,87,3,60,30,
        0,85,87,3,62,31,0,86,69,1,0,0,0,86,70,1,0,0,0,86,71,1,0,0,0,86,72,
        1,0,0,0,86,73,1,0,0,0,86,74,1,0,0,0,86,75,1,0,0,0,86,76,1,0,0,0,
        86,77,1,0,0,0,86,78,1,0,0,0,86,79,1,0,0,0,86,80,1,0,0,0,86,81,1,
        0,0,0,86,82,1,0,0,0,86,83,1,0,0,0,86,84,1,0,0,0,86,85,1,0,0,0,87,
        3,1,0,0,0,88,89,5,33,0,0,89,91,5,64,0,0,90,92,3,10,5,0,91,90,1,0,
        0,0,91,92,1,0,0,0,92,94,1,0,0,0,93,95,5,80,0,0,94,93,1,0,0,0,94,
        95,1,0,0,0,95,100,1,0,0,0,96,101,3,40,20,0,97,101,3,6,3,0,98,101,
        3,42,21,0,99,101,3,58,29,0,100,96,1,0,0,0,100,97,1,0,0,0,100,98,
        1,0,0,0,100,99,1,0,0,0,101,103,1,0,0,0,102,104,5,81,0,0,103,102,
        1,0,0,0,103,104,1,0,0,0,104,105,1,0,0,0,105,106,5,77,0,0,106,124,
        1,0,0,0,107,108,5,33,0,0,108,109,5,64,0,0,109,110,5,33,0,0,110,114,
        5,80,0,0,111,115,3,36,18,0,112,115,3,40,20,0,113,115,3,42,21,0,114,
        111,1,0,0,0,114,112,1,0,0,0,114,113,1,0,0,0,114,115,1,0,0,0,115,
        116,1,0,0,0,116,117,5,81,0,0,117,124,5,77,0,0,118,119,5,33,0,0,119,
        120,5,64,0,0,120,121,3,14,7,0,121,122,5,77,0,0,122,124,1,0,0,0,123,
        88,1,0,0,0,123,107,1,0,0,0,123,118,1,0,0,0,124,5,1,0,0,0,125,127,
        3,10,5,0,126,125,1,0,0,0,126,127,1,0,0,0,127,129,1,0,0,0,128,130,
        5,80,0,0,129,128,1,0,0,0,129,130,1,0,0,0,130,131,1,0,0,0,131,132,
        5,51,0,0,132,134,5,80,0,0,133,135,3,40,20,0,134,133,1,0,0,0,134,
        135,1,0,0,0,135,136,1,0,0,0,136,138,5,81,0,0,137,139,5,81,0,0,138,
        137,1,0,0,0,138,139,1,0,0,0,139,7,1,0,0,0,140,141,5,52,0,0,141,145,
        5,80,0,0,142,146,3,40,20,0,143,146,5,75,0,0,144,146,3,42,21,0,145,
        142,1,0,0,0,145,143,1,0,0,0,145,144,1,0,0,0,145,146,1,0,0,0,146,
        147,1,0,0,0,147,148,5,81,0,0,148,149,5,77,0,0,149,9,1,0,0,0,150,
        151,7,0,0,0,151,11,1,0,0,0,152,153,3,10,5,0,153,154,5,80,0,0,154,
        155,3,40,20,0,155,156,5,81,0,0,156,13,1,0,0,0,157,159,5,78,0,0,158,
        160,9,0,0,0,159,158,1,0,0,0,160,161,1,0,0,0,161,162,1,0,0,0,161,
        159,1,0,0,0,162,163,1,0,0,0,163,198,5,78,0,0,164,166,5,79,0,0,165,
        167,9,0,0,0,166,165,1,0,0,0,167,168,1,0,0,0,168,169,1,0,0,0,168,
        166,1,0,0,0,169,170,1,0,0,0,170,198,5,79,0,0,171,180,5,79,0,0,172,
        174,9,0,0,0,173,172,1,0,0,0,174,175,1,0,0,0,175,176,1,0,0,0,175,
        173,1,0,0,0,176,179,1,0,0,0,177,179,5,30,0,0,178,173,1,0,0,0,178,
        177,1,0,0,0,179,182,1,0,0,0,180,178,1,0,0,0,180,181,1,0,0,0,181,
        183,1,0,0,0,182,180,1,0,0,0,183,198,5,79,0,0,184,193,5,78,0,0,185,
        187,9,0,0,0,186,185,1,0,0,0,187,188,1,0,0,0,188,189,1,0,0,0,188,
        186,1,0,0,0,189,192,1,0,0,0,190,192,5,30,0,0,191,186,1,0,0,0,191,
        190,1,0,0,0,192,195,1,0,0,0,193,191,1,0,0,0,193,194,1,0,0,0,194,
        196,1,0,0,0,195,193,1,0,0,0,196,198,5,78,0,0,197,157,1,0,0,0,197,
        164,1,0,0,0,197,171,1,0,0,0,197,184,1,0,0,0,198,15,1,0,0,0,199,200,
        5,36,0,0,200,201,5,33,0,0,201,203,5,80,0,0,202,204,3,36,18,0,203,
        202,1,0,0,0,203,204,1,0,0,0,204,205,1,0,0,0,205,206,5,81,0,0,206,
        207,5,83,0,0,207,208,3,18,9,0,208,209,5,82,0,0,209,17,1,0,0,0,210,
        212,3,2,1,0,211,210,1,0,0,0,212,215,1,0,0,0,213,211,1,0,0,0,213,
        214,1,0,0,0,214,217,1,0,0,0,215,213,1,0,0,0,216,218,3,20,10,0,217,
        216,1,0,0,0,217,218,1,0,0,0,218,19,1,0,0,0,219,220,5,48,0,0,220,
        221,3,40,20,0,221,222,5,77,0,0,222,226,1,0,0,0,223,224,5,48,0,0,
        224,226,5,77,0,0,225,219,1,0,0,0,225,223,1,0,0,0,226,21,1,0,0,0,
        227,228,5,33,0,0,228,230,5,80,0,0,229,231,3,36,18,0,230,229,1,0,
        0,0,230,231,1,0,0,0,231,232,1,0,0,0,232,233,5,81,0,0,233,23,1,0,
        0,0,234,236,5,38,0,0,235,237,5,80,0,0,236,235,1,0,0,0,236,237,1,
        0,0,0,237,240,1,0,0,0,238,241,3,36,18,0,239,241,3,40,20,0,240,238,
        1,0,0,0,240,239,1,0,0,0,241,243,1,0,0,0,242,244,5,81,0,0,243,242,
        1,0,0,0,243,244,1,0,0,0,244,245,1,0,0,0,245,247,5,83,0,0,246,248,
        3,2,1,0,247,246,1,0,0,0,248,249,1,0,0,0,249,247,1,0,0,0,249,250,
        1,0,0,0,250,251,1,0,0,0,251,253,5,82,0,0,252,254,3,26,13,0,253,252,
        1,0,0,0,253,254,1,0,0,0,254,256,1,0,0,0,255,257,3,30,15,0,256,255,
        1,0,0,0,256,257,1,0,0,0,257,25,1,0,0,0,258,260,3,28,14,0,259,258,
        1,0,0,0,260,261,1,0,0,0,261,259,1,0,0,0,261,262,1,0,0,0,262,27,1,
        0,0,0,263,265,5,62,0,0,264,266,5,80,0,0,265,264,1,0,0,0,265,266,
        1,0,0,0,266,269,1,0,0,0,267,270,3,36,18,0,268,270,3,40,20,0,269,
        267,1,0,0,0,269,268,1,0,0,0,270,272,1,0,0,0,271,273,5,81,0,0,272,
        271,1,0,0,0,272,273,1,0,0,0,273,274,1,0,0,0,274,276,5,83,0,0,275,
        277,3,2,1,0,276,275,1,0,0,0,277,278,1,0,0,0,278,276,1,0,0,0,278,
        279,1,0,0,0,279,280,1,0,0,0,280,281,5,82,0,0,281,29,1,0,0,0,282,
        283,5,39,0,0,283,285,5,83,0,0,284,286,3,2,1,0,285,284,1,0,0,0,286,
        287,1,0,0,0,287,285,1,0,0,0,287,288,1,0,0,0,288,289,1,0,0,0,289,
        290,5,82,0,0,290,31,1,0,0,0,291,292,5,40,0,0,292,293,5,33,0,0,293,
        294,5,41,0,0,294,295,5,42,0,0,295,296,5,80,0,0,296,298,3,40,20,0,
        297,299,5,75,0,0,298,297,1,0,0,0,298,299,1,0,0,0,299,301,1,0,0,0,
        300,302,3,40,20,0,301,300,1,0,0,0,301,302,1,0,0,0,302,304,1,0,0,
        0,303,305,5,75,0,0,304,303,1,0,0,0,304,305,1,0,0,0,305,307,1,0,0,
        0,306,308,3,40,20,0,307,306,1,0,0,0,307,308,1,0,0,0,308,309,1,0,
        0,0,309,310,5,81,0,0,310,312,5,83,0,0,311,313,3,2,1,0,312,311,1,
        0,0,0,313,314,1,0,0,0,314,312,1,0,0,0,314,315,1,0,0,0,315,317,1,
        0,0,0,316,318,3,20,10,0,317,316,1,0,0,0,317,318,1,0,0,0,318,319,
        1,0,0,0,319,320,5,82,0,0,320,352,1,0,0,0,321,322,5,40,0,0,322,323,
        5,33,0,0,323,324,5,41,0,0,324,325,3,40,20,0,325,327,5,83,0,0,326,
        328,3,2,1,0,327,326,1,0,0,0,328,329,1,0,0,0,329,327,1,0,0,0,329,
        330,1,0,0,0,330,332,1,0,0,0,331,333,3,20,10,0,332,331,1,0,0,0,332,
        333,1,0,0,0,333,334,1,0,0,0,334,335,5,82,0,0,335,352,1,0,0,0,336,
        337,5,40,0,0,337,338,5,33,0,0,338,339,5,41,0,0,339,340,3,14,7,0,
        340,342,5,83,0,0,341,343,3,2,1,0,342,341,1,0,0,0,343,344,1,0,0,0,
        344,342,1,0,0,0,344,345,1,0,0,0,345,347,1,0,0,0,346,348,3,20,10,
        0,347,346,1,0,0,0,347,348,1,0,0,0,348,349,1,0,0,0,349,350,5,82,0,
        0,350,352,1,0,0,0,351,291,1,0,0,0,351,321,1,0,0,0,351,336,1,0,0,
        0,352,33,1,0,0,0,353,355,5,44,0,0,354,356,5,80,0,0,355,354,1,0,0,
        0,355,356,1,0,0,0,356,357,1,0,0,0,357,359,3,40,20,0,358,360,5,81,
        0,0,359,358,1,0,0,0,359,360,1,0,0,0,360,361,1,0,0,0,361,363,5,83,
        0,0,362,364,3,2,1,0,363,362,1,0,0,0,364,365,1,0,0,0,365,363,1,0,
        0,0,365,366,1,0,0,0,366,367,1,0,0,0,367,368,5,82,0,0,368,35,1,0,
        0,0,369,374,5,33,0,0,370,371,5,75,0,0,371,373,5,33,0,0,372,370,1,
        0,0,0,373,376,1,0,0,0,374,372,1,0,0,0,374,375,1,0,0,0,375,37,1,0,
        0,0,376,374,1,0,0,0,377,378,7,1,0,0,378,379,5,74,0,0,379,380,7,2,
        0,0,380,381,5,80,0,0,381,382,3,40,20,0,382,383,5,81,0,0,383,39,1,
        0,0,0,384,385,6,20,-1,0,385,388,3,50,25,0,386,388,3,38,19,0,387,
        384,1,0,0,0,387,386,1,0,0,0,388,400,1,0,0,0,389,390,10,5,0,0,390,
        391,7,3,0,0,391,399,3,50,25,0,392,393,10,4,0,0,393,394,7,4,0,0,394,
        399,3,50,25,0,395,396,10,3,0,0,396,397,7,5,0,0,397,399,3,50,25,0,
        398,389,1,0,0,0,398,392,1,0,0,0,398,395,1,0,0,0,399,402,1,0,0,0,
        400,398,1,0,0,0,400,401,1,0,0,0,401,41,1,0,0,0,402,400,1,0,0,0,403,
        405,3,44,22,0,404,406,5,63,0,0,405,404,1,0,0,0,405,406,1,0,0,0,406,
        408,1,0,0,0,407,409,3,44,22,0,408,407,1,0,0,0,408,409,1,0,0,0,409,
        429,1,0,0,0,410,411,3,44,22,0,411,412,5,65,0,0,412,413,3,44,22,0,
        413,429,1,0,0,0,414,415,3,44,22,0,415,416,5,67,0,0,416,417,3,44,
        22,0,417,429,1,0,0,0,418,419,5,11,0,0,419,420,5,80,0,0,420,421,3,
        44,22,0,421,422,5,81,0,0,422,429,1,0,0,0,423,424,5,12,0,0,424,425,
        5,80,0,0,425,426,3,44,22,0,426,427,5,81,0,0,427,429,1,0,0,0,428,
        403,1,0,0,0,428,410,1,0,0,0,428,414,1,0,0,0,428,418,1,0,0,0,428,
        423,1,0,0,0,429,43,1,0,0,0,430,431,5,84,0,0,431,436,3,46,23,0,432,
        433,5,75,0,0,433,435,3,46,23,0,434,432,1,0,0,0,435,438,1,0,0,0,436,
        434,1,0,0,0,436,437,1,0,0,0,437,439,1,0,0,0,438,436,1,0,0,0,439,
        440,5,85,0,0,440,45,1,0,0,0,441,442,5,84,0,0,442,447,3,40,20,0,443,
        444,5,75,0,0,444,446,3,40,20,0,445,443,1,0,0,0,446,449,1,0,0,0,447,
        445,1,0,0,0,447,448,1,0,0,0,448,450,1,0,0,0,449,447,1,0,0,0,450,
        451,5,85,0,0,451,47,1,0,0,0,452,453,5,35,0,0,453,454,7,6,0,0,454,
        49,1,0,0,0,455,466,5,32,0,0,456,458,5,33,0,0,457,456,1,0,0,0,458,
        459,1,0,0,0,459,457,1,0,0,0,459,460,1,0,0,0,460,466,1,0,0,0,461,
        466,5,55,0,0,462,466,3,14,7,0,463,466,3,52,26,0,464,466,3,54,27,
        0,465,455,1,0,0,0,465,457,1,0,0,0,465,461,1,0,0,0,465,462,1,0,0,
        0,465,463,1,0,0,0,465,464,1,0,0,0,466,51,1,0,0,0,467,477,5,80,0,
        0,468,478,5,32,0,0,469,471,5,33,0,0,470,469,1,0,0,0,471,472,1,0,
        0,0,472,470,1,0,0,0,472,473,1,0,0,0,473,478,1,0,0,0,474,478,5,55,
        0,0,475,478,3,14,7,0,476,478,5,75,0,0,477,468,1,0,0,0,477,470,1,
        0,0,0,477,474,1,0,0,0,477,475,1,0,0,0,477,476,1,0,0,0,478,479,1,
        0,0,0,479,477,1,0,0,0,479,480,1,0,0,0,480,481,1,0,0,0,481,482,5,
        81,0,0,482,53,1,0,0,0,483,493,5,84,0,0,484,494,5,32,0,0,485,487,
        5,33,0,0,486,485,1,0,0,0,487,488,1,0,0,0,488,486,1,0,0,0,488,489,
        1,0,0,0,489,494,1,0,0,0,490,494,5,55,0,0,491,494,3,14,7,0,492,494,
        5,75,0,0,493,484,1,0,0,0,493,486,1,0,0,0,493,490,1,0,0,0,493,491,
        1,0,0,0,493,492,1,0,0,0,494,495,1,0,0,0,495,493,1,0,0,0,495,496,
        1,0,0,0,496,497,1,0,0,0,497,498,5,85,0,0,498,55,1,0,0,0,499,500,
        7,7,0,0,500,501,5,80,0,0,501,502,3,40,20,0,502,503,5,75,0,0,503,
        504,3,40,20,0,504,505,5,81,0,0,505,526,1,0,0,0,506,507,7,8,0,0,507,
        508,5,80,0,0,508,509,3,40,20,0,509,510,5,81,0,0,510,526,1,0,0,0,
        511,512,7,9,0,0,512,519,5,80,0,0,513,520,3,58,29,0,514,516,5,33,
        0,0,515,514,1,0,0,0,516,517,1,0,0,0,517,515,1,0,0,0,517,518,1,0,
        0,0,518,520,1,0,0,0,519,513,1,0,0,0,519,515,1,0,0,0,520,521,1,0,
        0,0,521,522,5,75,0,0,522,523,3,38,19,0,523,524,5,81,0,0,524,526,
        1,0,0,0,525,499,1,0,0,0,525,506,1,0,0,0,525,511,1,0,0,0,526,57,1,
        0,0,0,527,528,5,26,0,0,528,529,5,80,0,0,529,530,3,40,20,0,530,531,
        5,75,0,0,531,532,3,40,20,0,532,533,5,67,0,0,533,534,5,2,0,0,534,
        535,5,74,0,0,535,536,5,27,0,0,536,537,5,75,0,0,537,538,3,40,20,0,
        538,539,5,81,0,0,539,59,1,0,0,0,540,541,5,91,0,0,541,542,5,80,0,
        0,542,543,3,40,20,0,543,544,5,81,0,0,544,61,1,0,0,0,545,546,5,90,
        0,0,546,547,5,80,0,0,547,548,3,40,20,0,548,549,5,81,0,0,549,550,
        5,76,0,0,550,551,3,40,20,0,551,552,5,46,0,0,552,63,1,0,0,0,73,67,
        86,91,94,100,103,114,123,126,129,134,138,145,161,168,175,178,180,
        188,191,193,197,203,213,217,225,230,236,240,243,249,253,256,261,
        265,269,272,278,287,298,301,304,307,314,317,329,332,344,347,351,
        355,359,365,374,387,398,400,405,408,428,436,447,459,465,472,477,
        479,488,493,495,517,519,525
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
                      "SEP", "ESP", "EX", "NEWLINE", "NUMERO", "ID", "WS", 
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
                      "POTENCIA", "MODULO", "WRITE", "OPEN" ]

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
    RULE_condicional = 12
    RULE_elifBlock = 13
    RULE_condicional_elif = 14
    RULE_condicional_else = 15
    RULE_ciclo_for = 16
    RULE_ciclo_while = 17
    RULE_parametro = 18
    RULE_func = 19
    RULE_expresion = 20
    RULE_matriz_operaciones = 21
    RULE_matriz = 22
    RULE_fila_matriz = 23
    RULE_importss = 24
    RULE_termino = 25
    RULE_lista = 26
    RULE_arreglo = 27
    RULE_graficas = 28
    RULE_arange = 29
    RULE_lectura_archivo = 30
    RULE_escritura_archivo = 31

    ruleNames =  [ "start", "sentencias", "asignacion", "v_input", "printf", 
                   "var_casteo", "casteo", "cadena", "funcion", "stmt_func", 
                   "v_return", "llamafuncion", "condicional", "elifBlock", 
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
    ID=33
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
            self.state = 65 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 64
                self.sentencias()
                self.state = 67 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 141882473016432646) != 0) or ((((_la - 78)) & ~0x3f) == 0 and ((1 << (_la - 78)) & 12359) != 0)):
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


        def condicional(self):
            return self.getTypedRuleContext(gramaticaParser.CondicionalContext,0)


        def ciclo_while(self):
            return self.getTypedRuleContext(gramaticaParser.Ciclo_whileContext,0)


        def expresion(self):
            return self.getTypedRuleContext(gramaticaParser.ExpresionContext,0)


        def funcion(self):
            return self.getTypedRuleContext(gramaticaParser.FuncionContext,0)


        def llamafuncion(self):
            return self.getTypedRuleContext(gramaticaParser.LlamafuncionContext,0)


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
            self.state = 86
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 69
                self.printf()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 70
                self.asignacion()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 71
                self.condicional()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 72
                self.ciclo_while()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 73
                self.expresion(0)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 74
                self.funcion()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 75
                self.llamafuncion()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 76
                self.ciclo_for()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 77
                self.v_input()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 78
                self.casteo()
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 79
                self.graficas()
                pass

            elif la_ == 12:
                self.enterOuterAlt(localctx, 12)
                self.state = 80
                self.importss()
                pass

            elif la_ == 13:
                self.enterOuterAlt(localctx, 13)
                self.state = 81
                self.func()
                pass

            elif la_ == 14:
                self.enterOuterAlt(localctx, 14)
                self.state = 82
                self.matriz_operaciones()
                pass

            elif la_ == 15:
                self.enterOuterAlt(localctx, 15)
                self.state = 83
                self.match(gramaticaParser.NEWLINE)
                pass

            elif la_ == 16:
                self.enterOuterAlt(localctx, 16)
                self.state = 84
                self.lectura_archivo()
                pass

            elif la_ == 17:
                self.enterOuterAlt(localctx, 17)
                self.state = 85
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
            self.state = 123
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 88
                self.match(gramaticaParser.ID)
                self.state = 89
                self.match(gramaticaParser.ASIGNACION)
                self.state = 91
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
                if la_ == 1:
                    self.state = 90
                    self.var_casteo()


                self.state = 94
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
                if la_ == 1:
                    self.state = 93
                    self.match(gramaticaParser.PARENTESIS_A)


                self.state = 100
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
                if la_ == 1:
                    self.state = 96
                    self.expresion(0)
                    pass

                elif la_ == 2:
                    self.state = 97
                    self.v_input()
                    pass

                elif la_ == 3:
                    self.state = 98
                    self.matriz_operaciones()
                    pass

                elif la_ == 4:
                    self.state = 99
                    self.arange()
                    pass


                self.state = 103
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==81:
                    self.state = 102
                    self.match(gramaticaParser.PARENTESIS_C)


                self.state = 105
                self.match(gramaticaParser.PUNTOCOMA)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 107
                self.match(gramaticaParser.ID)
                self.state = 108
                self.match(gramaticaParser.ASIGNACION)
                self.state = 109
                self.match(gramaticaParser.ID)
                self.state = 110
                self.match(gramaticaParser.PARENTESIS_A)
                self.state = 114
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
                if la_ == 1:
                    self.state = 111
                    self.parametro()

                elif la_ == 2:
                    self.state = 112
                    self.expresion(0)

                elif la_ == 3:
                    self.state = 113
                    self.matriz_operaciones()


                self.state = 116
                self.match(gramaticaParser.PARENTESIS_C)
                self.state = 117
                self.match(gramaticaParser.PUNTOCOMA)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 118
                self.match(gramaticaParser.ID)
                self.state = 119
                self.match(gramaticaParser.ASIGNACION)
                self.state = 120
                self.cadena()
                self.state = 121
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
            self.state = 126
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 135107988821114880) != 0):
                self.state = 125
                self.var_casteo()


            self.state = 129
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==80:
                self.state = 128
                self.match(gramaticaParser.PARENTESIS_A)


            self.state = 131
            self.match(gramaticaParser.INPUT)
            self.state = 132
            self.match(gramaticaParser.PARENTESIS_A)
            self.state = 134
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 36028809903865862) != 0) or ((((_la - 78)) & ~0x3f) == 0 and ((1 << (_la - 78)) & 71) != 0):
                self.state = 133
                self.expresion(0)


            self.state = 136
            self.match(gramaticaParser.PARENTESIS_C)
            self.state = 138
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.state = 137
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
            self.state = 140
            self.match(gramaticaParser.PRINT)
            self.state = 141
            self.match(gramaticaParser.PARENTESIS_A)
            self.state = 145
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.state = 142
                self.expresion(0)

            elif la_ == 2:
                self.state = 143
                self.match(gramaticaParser.COMA)

            elif la_ == 3:
                self.state = 144
                self.matriz_operaciones()


            self.state = 147
            self.match(gramaticaParser.PARENTESIS_C)
            self.state = 148
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
            self.state = 150
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
            self.state = 152
            self.var_casteo()
            self.state = 153
            self.match(gramaticaParser.PARENTESIS_A)
            self.state = 154
            self.expresion(0)
            self.state = 155
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
            self.state = 197
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 157
                self.match(gramaticaParser.COMILLASIMPLE)
                self.state = 159 
                self._errHandler.sync(self)
                _alt = 1+1
                while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1+1:
                        self.state = 158
                        self.matchWildcard()

                    else:
                        raise NoViableAltException(self)
                    self.state = 161 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,13,self._ctx)

                self.state = 163
                self.match(gramaticaParser.COMILLASIMPLE)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 164
                self.match(gramaticaParser.COMILLADOBLE)
                self.state = 166 
                self._errHandler.sync(self)
                _alt = 1+1
                while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1+1:
                        self.state = 165
                        self.matchWildcard()

                    else:
                        raise NoViableAltException(self)
                    self.state = 168 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,14,self._ctx)

                self.state = 170
                self.match(gramaticaParser.COMILLADOBLE)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 171
                self.match(gramaticaParser.COMILLADOBLE)
                self.state = 180
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,17,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 178
                        self._errHandler.sync(self)
                        la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
                        if la_ == 1:
                            self.state = 173 
                            self._errHandler.sync(self)
                            _alt = 1+1
                            while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                                if _alt == 1+1:
                                    self.state = 172
                                    self.matchWildcard()

                                else:
                                    raise NoViableAltException(self)
                                self.state = 175 
                                self._errHandler.sync(self)
                                _alt = self._interp.adaptivePredict(self._input,15,self._ctx)

                            pass

                        elif la_ == 2:
                            self.state = 177
                            self.match(gramaticaParser.EX)
                            pass

                 
                    self.state = 182
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,17,self._ctx)

                self.state = 183
                self.match(gramaticaParser.COMILLADOBLE)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 184
                self.match(gramaticaParser.COMILLASIMPLE)
                self.state = 193
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,20,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 191
                        self._errHandler.sync(self)
                        la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
                        if la_ == 1:
                            self.state = 186 
                            self._errHandler.sync(self)
                            _alt = 1+1
                            while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                                if _alt == 1+1:
                                    self.state = 185
                                    self.matchWildcard()

                                else:
                                    raise NoViableAltException(self)
                                self.state = 188 
                                self._errHandler.sync(self)
                                _alt = self._interp.adaptivePredict(self._input,18,self._ctx)

                            pass

                        elif la_ == 2:
                            self.state = 190
                            self.match(gramaticaParser.EX)
                            pass

                 
                    self.state = 195
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,20,self._ctx)

                self.state = 196
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
            self.state = 199
            self.match(gramaticaParser.DEF)
            self.state = 200
            self.match(gramaticaParser.ID)
            self.state = 201
            self.match(gramaticaParser.PARENTESIS_A)
            self.state = 203
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==33:
                self.state = 202
                self.parametro()


            self.state = 205
            self.match(gramaticaParser.PARENTESIS_C)
            self.state = 206
            self.match(gramaticaParser.LLAVE_A)
            self.state = 207
            self.stmt_func()
            self.state = 208
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
            self.state = 213
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 141882473016432646) != 0) or ((((_la - 78)) & ~0x3f) == 0 and ((1 << (_la - 78)) & 12359) != 0):
                self.state = 210
                self.sentencias()
                self.state = 215
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 217
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==48:
                self.state = 216
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
            self.state = 225
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 219
                self.match(gramaticaParser.RETURN)
                self.state = 220
                self.expresion(0)
                self.state = 221
                self.match(gramaticaParser.PUNTOCOMA)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 223
                self.match(gramaticaParser.RETURN)
                self.state = 224
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

        def parametro(self):
            return self.getTypedRuleContext(gramaticaParser.ParametroContext,0)


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
            self.state = 227
            self.match(gramaticaParser.ID)
            self.state = 228
            self.match(gramaticaParser.PARENTESIS_A)
            self.state = 230
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==33:
                self.state = 229
                self.parametro()


            self.state = 232
            self.match(gramaticaParser.PARENTESIS_C)
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
        self.enterRule(localctx, 24, self.RULE_condicional)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 234
            self.match(gramaticaParser.IF)
            self.state = 236
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.state = 235
                self.match(gramaticaParser.PARENTESIS_A)


            self.state = 240
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.state = 238
                self.parametro()
                pass

            elif la_ == 2:
                self.state = 239
                self.expresion(0)
                pass


            self.state = 243
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==81:
                self.state = 242
                self.match(gramaticaParser.PARENTESIS_C)


            self.state = 245
            self.match(gramaticaParser.LLAVE_A)
            self.state = 247 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 246
                self.sentencias()
                self.state = 249 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 141882473016432646) != 0) or ((((_la - 78)) & ~0x3f) == 0 and ((1 << (_la - 78)) & 12359) != 0)):
                    break

            self.state = 251
            self.match(gramaticaParser.LLAVE_C)
            self.state = 253
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==62:
                self.state = 252
                self.elifBlock()


            self.state = 256
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==39:
                self.state = 255
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
        self.enterRule(localctx, 26, self.RULE_elifBlock)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 259 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 258
                self.condicional_elif()
                self.state = 261 
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
        self.enterRule(localctx, 28, self.RULE_condicional_elif)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 263
            self.match(gramaticaParser.ELIF)
            self.state = 265
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.state = 264
                self.match(gramaticaParser.PARENTESIS_A)


            self.state = 269
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
            if la_ == 1:
                self.state = 267
                self.parametro()
                pass

            elif la_ == 2:
                self.state = 268
                self.expresion(0)
                pass


            self.state = 272
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==81:
                self.state = 271
                self.match(gramaticaParser.PARENTESIS_C)


            self.state = 274
            self.match(gramaticaParser.LLAVE_A)
            self.state = 276 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 275
                self.sentencias()
                self.state = 278 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 141882473016432646) != 0) or ((((_la - 78)) & ~0x3f) == 0 and ((1 << (_la - 78)) & 12359) != 0)):
                    break

            self.state = 280
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
        self.enterRule(localctx, 30, self.RULE_condicional_else)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 282
            self.match(gramaticaParser.ELSE)
            self.state = 283
            self.match(gramaticaParser.LLAVE_A)
            self.state = 285 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 284
                self.sentencias()
                self.state = 287 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 141882473016432646) != 0) or ((((_la - 78)) & ~0x3f) == 0 and ((1 << (_la - 78)) & 12359) != 0)):
                    break

            self.state = 289
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
        self.enterRule(localctx, 32, self.RULE_ciclo_for)
        self._la = 0 # Token type
        try:
            self.state = 351
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,49,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 291
                self.match(gramaticaParser.FOR)
                self.state = 292
                self.match(gramaticaParser.ID)
                self.state = 293
                self.match(gramaticaParser.IN)
                self.state = 294
                self.match(gramaticaParser.RANGE)
                self.state = 295
                self.match(gramaticaParser.PARENTESIS_A)
                self.state = 296
                self.expresion(0)
                self.state = 298
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,39,self._ctx)
                if la_ == 1:
                    self.state = 297
                    self.match(gramaticaParser.COMA)


                self.state = 301
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,40,self._ctx)
                if la_ == 1:
                    self.state = 300
                    self.expresion(0)


                self.state = 304
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==75:
                    self.state = 303
                    self.match(gramaticaParser.COMA)


                self.state = 307
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 36028809903865862) != 0) or ((((_la - 78)) & ~0x3f) == 0 and ((1 << (_la - 78)) & 71) != 0):
                    self.state = 306
                    self.expresion(0)


                self.state = 309
                self.match(gramaticaParser.PARENTESIS_C)
                self.state = 310
                self.match(gramaticaParser.LLAVE_A)
                self.state = 312 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 311
                    self.sentencias()
                    self.state = 314 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 141882473016432646) != 0) or ((((_la - 78)) & ~0x3f) == 0 and ((1 << (_la - 78)) & 12359) != 0)):
                        break

                self.state = 317
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==48:
                    self.state = 316
                    self.v_return()


                self.state = 319
                self.match(gramaticaParser.LLAVE_C)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 321
                self.match(gramaticaParser.FOR)
                self.state = 322
                self.match(gramaticaParser.ID)
                self.state = 323
                self.match(gramaticaParser.IN)
                self.state = 324
                self.expresion(0)
                self.state = 325
                self.match(gramaticaParser.LLAVE_A)
                self.state = 327 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 326
                    self.sentencias()
                    self.state = 329 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 141882473016432646) != 0) or ((((_la - 78)) & ~0x3f) == 0 and ((1 << (_la - 78)) & 12359) != 0)):
                        break

                self.state = 332
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==48:
                    self.state = 331
                    self.v_return()


                self.state = 334
                self.match(gramaticaParser.LLAVE_C)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 336
                self.match(gramaticaParser.FOR)
                self.state = 337
                self.match(gramaticaParser.ID)
                self.state = 338
                self.match(gramaticaParser.IN)
                self.state = 339
                self.cadena()
                self.state = 340
                self.match(gramaticaParser.LLAVE_A)
                self.state = 342 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 341
                    self.sentencias()
                    self.state = 344 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 141882473016432646) != 0) or ((((_la - 78)) & ~0x3f) == 0 and ((1 << (_la - 78)) & 12359) != 0)):
                        break

                self.state = 347
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==48:
                    self.state = 346
                    self.v_return()


                self.state = 349
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
        self.enterRule(localctx, 34, self.RULE_ciclo_while)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 353
            self.match(gramaticaParser.WHILE)
            self.state = 355
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,50,self._ctx)
            if la_ == 1:
                self.state = 354
                self.match(gramaticaParser.PARENTESIS_A)


            self.state = 357
            self.expresion(0)
            self.state = 359
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==81:
                self.state = 358
                self.match(gramaticaParser.PARENTESIS_C)


            self.state = 361
            self.match(gramaticaParser.LLAVE_A)
            self.state = 363 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 362
                self.sentencias()
                self.state = 365 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 141882473016432646) != 0) or ((((_la - 78)) & ~0x3f) == 0 and ((1 << (_la - 78)) & 12359) != 0)):
                    break

            self.state = 367
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
        self.enterRule(localctx, 36, self.RULE_parametro)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 369
            self.match(gramaticaParser.ID)
            self.state = 374
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==75:
                self.state = 370
                self.match(gramaticaParser.COMA)
                self.state = 371
                self.match(gramaticaParser.ID)
                self.state = 376
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
        self.enterRule(localctx, 38, self.RULE_func)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 377
            _la = self._input.LA(1)
            if not(_la==1 or _la==2):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 378
            self.match(gramaticaParser.PUNTO)
            self.state = 379
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 2040) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 380
            self.match(gramaticaParser.PARENTESIS_A)
            self.state = 381
            self.expresion(0)
            self.state = 382
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
        _startState = 40
        self.enterRecursionRule(localctx, 40, self.RULE_expresion, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 387
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [32, 33, 55, 78, 79, 80, 84]:
                self.state = 385
                self.termino()
                pass
            elif token in [1, 2]:
                self.state = 386
                self.func()
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 400
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,56,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 398
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,55,self._ctx)
                    if la_ == 1:
                        localctx = gramaticaParser.ExpresionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expresion)
                        self.state = 389
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 390
                        _la = self._input.LA(1)
                        if not(((((_la - 63)) & ~0x3f) == 0 and ((1 << (_la - 63)) & 100663325) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 391
                        self.termino()
                        pass

                    elif la_ == 2:
                        localctx = gramaticaParser.ExpresionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expresion)
                        self.state = 392
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 393
                        _la = self._input.LA(1)
                        if not(((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & 1009) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 394
                        self.termino()
                        pass

                    elif la_ == 3:
                        localctx = gramaticaParser.ExpresionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expresion)
                        self.state = 395
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 396
                        _la = self._input.LA(1)
                        if not(_la==59 or _la==60):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 397
                        self.termino()
                        pass

             
                self.state = 402
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,56,self._ctx)

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
        self.enterRule(localctx, 42, self.RULE_matriz_operaciones)
        self._la = 0 # Token type
        try:
            self.state = 428
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,59,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 403
                self.matriz()
                self.state = 405
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==63:
                    self.state = 404
                    self.match(gramaticaParser.SUMA)


                self.state = 408
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,58,self._ctx)
                if la_ == 1:
                    self.state = 407
                    self.matriz()


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 410
                self.matriz()
                self.state = 411
                self.match(gramaticaParser.RESTA)
                self.state = 412
                self.matriz()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 414
                self.matriz()
                self.state = 415
                self.match(gramaticaParser.MULTIPLICACION)
                self.state = 416
                self.matriz()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 418
                self.match(gramaticaParser.T__10)
                self.state = 419
                self.match(gramaticaParser.PARENTESIS_A)
                self.state = 420
                self.matriz()
                self.state = 421
                self.match(gramaticaParser.PARENTESIS_C)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 423
                self.match(gramaticaParser.T__11)
                self.state = 424
                self.match(gramaticaParser.PARENTESIS_A)
                self.state = 425
                self.matriz()
                self.state = 426
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
        self.enterRule(localctx, 44, self.RULE_matriz)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 430
            self.match(gramaticaParser.CORCHETE_A)
            self.state = 431
            self.fila_matriz()
            self.state = 436
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==75:
                self.state = 432
                self.match(gramaticaParser.COMA)
                self.state = 433
                self.fila_matriz()
                self.state = 438
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 439
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
        self.enterRule(localctx, 46, self.RULE_fila_matriz)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 441
            self.match(gramaticaParser.CORCHETE_A)
            self.state = 442
            self.expresion(0)
            self.state = 447
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==75:
                self.state = 443
                self.match(gramaticaParser.COMA)
                self.state = 444
                self.expresion(0)
                self.state = 449
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 450
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
        self.enterRule(localctx, 48, self.RULE_importss)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 452
            self.match(gramaticaParser.IMPORT)
            self.state = 453
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

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(gramaticaParser.ID)
            else:
                return self.getToken(gramaticaParser.ID, i)

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
        self.enterRule(localctx, 50, self.RULE_termino)
        try:
            self.state = 465
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [32]:
                self.enterOuterAlt(localctx, 1)
                self.state = 455
                self.match(gramaticaParser.NUMERO)
                pass
            elif token in [33]:
                self.enterOuterAlt(localctx, 2)
                self.state = 457 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 456
                        self.match(gramaticaParser.ID)

                    else:
                        raise NoViableAltException(self)
                    self.state = 459 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,62,self._ctx)

                pass
            elif token in [55]:
                self.enterOuterAlt(localctx, 3)
                self.state = 461
                self.match(gramaticaParser.BOOLEAN)
                pass
            elif token in [78, 79]:
                self.enterOuterAlt(localctx, 4)
                self.state = 462
                self.cadena()
                pass
            elif token in [80]:
                self.enterOuterAlt(localctx, 5)
                self.state = 463
                self.lista()
                pass
            elif token in [84]:
                self.enterOuterAlt(localctx, 6)
                self.state = 464
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

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(gramaticaParser.ID)
            else:
                return self.getToken(gramaticaParser.ID, i)

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
        self.enterRule(localctx, 52, self.RULE_lista)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 467
            self.match(gramaticaParser.PARENTESIS_A)
            self.state = 477 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 477
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [32]:
                    self.state = 468
                    self.match(gramaticaParser.NUMERO)
                    pass
                elif token in [33]:
                    self.state = 470 
                    self._errHandler.sync(self)
                    _alt = 1
                    while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                        if _alt == 1:
                            self.state = 469
                            self.match(gramaticaParser.ID)

                        else:
                            raise NoViableAltException(self)
                        self.state = 472 
                        self._errHandler.sync(self)
                        _alt = self._interp.adaptivePredict(self._input,64,self._ctx)

                    pass
                elif token in [55]:
                    self.state = 474
                    self.match(gramaticaParser.BOOLEAN)
                    pass
                elif token in [78, 79]:
                    self.state = 475
                    self.cadena()
                    pass
                elif token in [75]:
                    self.state = 476
                    self.match(gramaticaParser.COMA)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 479 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (((((_la - 32)) & ~0x3f) == 0 and ((1 << (_la - 32)) & 219902333943811) != 0)):
                    break

            self.state = 481
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

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(gramaticaParser.ID)
            else:
                return self.getToken(gramaticaParser.ID, i)

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
        self.enterRule(localctx, 54, self.RULE_arreglo)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 483
            self.match(gramaticaParser.CORCHETE_A)
            self.state = 493 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 493
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [32]:
                    self.state = 484
                    self.match(gramaticaParser.NUMERO)
                    pass
                elif token in [33]:
                    self.state = 486 
                    self._errHandler.sync(self)
                    _alt = 1
                    while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                        if _alt == 1:
                            self.state = 485
                            self.match(gramaticaParser.ID)

                        else:
                            raise NoViableAltException(self)
                        self.state = 488 
                        self._errHandler.sync(self)
                        _alt = self._interp.adaptivePredict(self._input,67,self._ctx)

                    pass
                elif token in [55]:
                    self.state = 490
                    self.match(gramaticaParser.BOOLEAN)
                    pass
                elif token in [78, 79]:
                    self.state = 491
                    self.cadena()
                    pass
                elif token in [75]:
                    self.state = 492
                    self.match(gramaticaParser.COMA)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 495 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (((((_la - 32)) & ~0x3f) == 0 and ((1 << (_la - 32)) & 219902333943811) != 0)):
                    break

            self.state = 497
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


        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(gramaticaParser.ID)
            else:
                return self.getToken(gramaticaParser.ID, i)

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
        self.enterRule(localctx, 56, self.RULE_graficas)
        self._la = 0 # Token type
        try:
            self.state = 525
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [15, 16, 17, 18, 19, 20]:
                self.enterOuterAlt(localctx, 1)
                self.state = 499
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 2064384) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 500
                self.match(gramaticaParser.PARENTESIS_A)
                self.state = 501
                localctx.x = self.expresion(0)
                self.state = 502
                self.match(gramaticaParser.COMA)
                self.state = 503
                localctx.y = self.expresion(0)
                self.state = 504
                self.match(gramaticaParser.PARENTESIS_C)
                pass
            elif token in [21, 22]:
                self.enterOuterAlt(localctx, 2)
                self.state = 506
                _la = self._input.LA(1)
                if not(_la==21 or _la==22):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 507
                self.match(gramaticaParser.PARENTESIS_A)
                self.state = 508
                localctx.x = self.expresion(0)
                self.state = 509
                self.match(gramaticaParser.PARENTESIS_C)
                pass
            elif token in [23, 24, 25]:
                self.enterOuterAlt(localctx, 3)
                self.state = 511
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 58720256) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 512
                self.match(gramaticaParser.PARENTESIS_A)
                self.state = 519
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [26]:
                    self.state = 513
                    self.arange()
                    pass
                elif token in [33]:
                    self.state = 515 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while True:
                        self.state = 514
                        self.match(gramaticaParser.ID)
                        self.state = 517 
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if not (_la==33):
                            break

                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 521
                self.match(gramaticaParser.COMA)
                self.state = 522
                self.func()
                self.state = 523
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
        self.enterRule(localctx, 58, self.RULE_arange)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 527
            self.match(gramaticaParser.T__25)
            self.state = 528
            self.match(gramaticaParser.PARENTESIS_A)
            self.state = 529
            self.expresion(0)
            self.state = 530
            self.match(gramaticaParser.COMA)
            self.state = 531
            self.expresion(0)
            self.state = 532
            self.match(gramaticaParser.MULTIPLICACION)
            self.state = 533
            self.match(gramaticaParser.T__1)
            self.state = 534
            self.match(gramaticaParser.PUNTO)
            self.state = 535
            self.match(gramaticaParser.T__26)
            self.state = 536
            self.match(gramaticaParser.COMA)
            self.state = 537
            self.expresion(0)
            self.state = 538
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
        self.enterRule(localctx, 60, self.RULE_lectura_archivo)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 540
            self.match(gramaticaParser.OPEN)
            self.state = 541
            self.match(gramaticaParser.PARENTESIS_A)
            self.state = 542
            self.expresion(0)
            self.state = 543
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
        self.enterRule(localctx, 62, self.RULE_escritura_archivo)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 545
            self.match(gramaticaParser.WRITE)
            self.state = 546
            self.match(gramaticaParser.PARENTESIS_A)
            self.state = 547
            self.expresion(0)
            self.state = 548
            self.match(gramaticaParser.PARENTESIS_C)
            self.state = 549
            self.match(gramaticaParser.DOSPUNTOS)
            self.state = 550
            self.expresion(0)
            self.state = 551
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
        self._predicates[20] = self.expresion_sempred
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
         




