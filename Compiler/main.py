import sys
from antlr4 import *
from Grammar.gramaticaLexer import gramaticaLexer
from Grammar.gramaticaParser import gramaticaParser
from visitorImplemented import VisitorCompiler


def readFile(filename):
    with open(filename, "r") as f:
        return f.read()


def main():
    if(len(sys.argv) <= 1):
        print("ERROR: Indique por favor el archivo a compilar")
        return

    file = readFile(sys.argv[1])
    input = InputStream(file)
    lexer = gramaticaLexer(input)
    stream = CommonTokenStream(lexer)
    parser = gramaticaParser(stream)
    tree = parser.start()

    visitor = VisitorCompiler()
    visitor.visit(tree)


if __name__ == "__main__":
    main()