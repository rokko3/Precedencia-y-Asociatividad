import math
from LabeledExprParser import LabeledExprParser
from LabeledExprVisitor import LabeledExprVisitor

class EvalVisitor(LabeledExprVisitor):
    def __init__(self):
        self.memory = {}

    # --- prog ---
    def visitProg(self, ctx:LabeledExprParser.ProgContext):
        result = None
        exprs = ctx.expr()
        if not isinstance(exprs, list):
            return self.visit(exprs)
        for e in exprs:
            result = self.visit(e)
        return result

    # --- addExpr derecha ---
    def visitAddRight(self, ctx:LabeledExprParser.AddRightContext):
        left = self.visit(ctx.mulExpr())
        right_ctx = None
        for child in ctx.children:
            if isinstance(child, LabeledExprParser.AddRightContext):
                right_ctx = child
                break
        if right_ctx:
            right = self.visit(right_ctx)
            op = ctx.getChild(1).getText()
            return left + right if op == '+' else left - right
        return left

    # --- mulExpr derecha ---
    def visitMulRight(self, ctx:LabeledExprParser.MulRightContext):
        left = self.visit(ctx.unaryExpr())
        right_ctx = None
        for child in ctx.children:
            if isinstance(child, LabeledExprParser.MulRightContext):
                right_ctx = child
                break
        if right_ctx:
            right = self.visit(right_ctx)
            op = ctx.getChild(1).getText()
            if op == '*':
                return left * right
            elif op == '/':
                return left / right
            elif op == '%':
                return left % right
        return left

    # --- unarios ---
    def visitUnaryMinus(self, ctx:LabeledExprParser.UnaryMinusContext):
        return -self.visit(ctx.unaryExpr())

    def visitUnaryPlus(self, ctx:LabeledExprParser.UnaryPlusContext):
        return +self.visit(ctx.unaryExpr())

    def visitToPostfix(self, ctx:LabeledExprParser.ToPostfixContext):
        return self.visit(ctx.postfixExpr())

    # --- factorial ---
    def visitFactf(self, ctx:LabeledExprParser.FactfContext):
        result = self.visit(ctx.primaryExpr())
        for _ in ctx.FACT():
            result = math.factorial(int(result))
        return result

    # --- funciones ---
    def visitFuncCall(self, ctx:LabeledExprParser.FuncCallContext):
        func_name = ctx.ID().getText()
        arg = self.visit(ctx.expr())
        if func_name == "sin": return math.sin(arg)
        if func_name == "cos": return math.cos(arg)
        if func_name == "tan": return math.tan(arg)
        if func_name == "exp": return math.exp(arg)
        raise Exception(f"Función desconocida: {func_name}")

    def visitSqrtf(self, ctx:LabeledExprParser.SqrtfContext):
        return math.sqrt(self.visit(ctx.expr()))

    def visitLnf(self, ctx:LabeledExprParser.LnfContext):
        return math.log(self.visit(ctx.expr()))

    def visitLogf(self, ctx:LabeledExprParser.LogfContext):
        return math.log10(self.visit(ctx.expr()))

    def visitFuncRad(self, ctx:LabeledExprParser.FuncRadContext):
        func_name = ctx.ID().getText()
        arg = self.visit(ctx.expr())
        if func_name == "sin": return math.sin(math.radians(arg))
        if func_name == "cos": return math.cos(math.radians(arg))
        if func_name == "tan": return math.tan(math.radians(arg))
        raise Exception(f"Función trigonométrica desconocida (rad): {func_name}")

    # --- literales ---
    def visitInt(self, ctx:LabeledExprParser.IntContext):
        return int(ctx.INT().getText())

    def visitDouble(self, ctx:LabeledExprParser.DoubleContext):
        return float(ctx.DOUBLE().getText())

    def visitId(self, ctx:LabeledExprParser.IdContext):
        name = ctx.ID().getText()
        if name in self.memory:
            return self.memory[name]
        raise Exception(f"Variable no definida: {name}")

    def visitParens(self, ctx:LabeledExprParser.ParensContext):
        return self.visit(ctx.expr())
