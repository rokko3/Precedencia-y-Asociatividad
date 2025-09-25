import sys
from antlr4 import *
from antlr4.tree.Trees import Trees
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
    resultado=visitor.visit(tree)
    print(resultado)
    print(Trees.toStringTree(tree, None, parser))
if __name__ == '__main__':
    main(sys.argv)
