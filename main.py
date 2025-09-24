import sys
from antlr4 import *
from LabeledExprLexer import LabeledExprLexer
from LabeledExprParser import LabeledExprParser
from EvalVisitor import EvalVisitor
def main(argv):
    input_stream = FileStream(argv[1])
    lexer = LabeledExprLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = LabeledExprParser(stream)
    tree = parser.prog()

    visitor = EvalVisitor()
    result = visitor.visit(tree)

if __name__ == '__main__':
    main(sys.argv)
