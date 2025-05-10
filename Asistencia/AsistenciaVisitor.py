# Generated from Asistencia.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .AsistenciaParser import AsistenciaParser
else:
    from AsistenciaParser import AsistenciaParser

# This class defines a complete generic visitor for a parse tree produced by AsistenciaParser.

class AsistenciaVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by AsistenciaParser#program.
    def visitProgram(self, ctx:AsistenciaParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AsistenciaParser#instruction.
    def visitInstruction(self, ctx:AsistenciaParser.InstructionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AsistenciaParser#loadStmt.
    def visitLoadStmt(self, ctx:AsistenciaParser.LoadStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AsistenciaParser#filterStmt.
    def visitFilterStmt(self, ctx:AsistenciaParser.FilterStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AsistenciaParser#filterExpr.
    def visitFilterExpr(self, ctx:AsistenciaParser.FilterExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AsistenciaParser#condition.
    def visitCondition(self, ctx:AsistenciaParser.ConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AsistenciaParser#aggregateStmt.
    def visitAggregateStmt(self, ctx:AsistenciaParser.AggregateStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AsistenciaParser#printStmt.
    def visitPrintStmt(self, ctx:AsistenciaParser.PrintStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AsistenciaParser#value.
    def visitValue(self, ctx:AsistenciaParser.ValueContext):
        return self.visitChildren(ctx)



del AsistenciaParser