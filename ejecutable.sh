#!/bin/bash

antlr4  -Dlanguage=Python3 -visitor gramatica.g4 

python3 logica.py < prueba.txt
