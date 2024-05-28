#!/bin/bash

antlr4 -Dlanguage=Python3 -visitor Compiler/Grammar/gramatica.g4 

python3 Compiler/main.py prueba.txt
