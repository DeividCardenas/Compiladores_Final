# Generated from Asistencia.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .AsistenciaParser import AsistenciaParser
else:
    from AsistenciaParser import AsistenciaParser

# This class defines a complete listener for a parse tree produced by AsistenciaParser.
class AsistenciaListener(ParseTreeListener):

    # Enter a parse tree produced by AsistenciaParser#program.
    def enterProgram(self, ctx:AsistenciaParser.ProgramContext):
        pass

    # Exit a parse tree produced by AsistenciaParser#program.
    def exitProgram(self, ctx:AsistenciaParser.ProgramContext):
        pass

    # Enter a parse tree produced by AsistenciaParser#scriptComment.
    def enterScriptComment(self, ctx:AsistenciaParser.ScriptCommentContext):
        pass

    # Exit a parse tree produced by AsistenciaParser#scriptComment.
    def exitScriptComment(self, ctx:AsistenciaParser.ScriptCommentContext):
        pass

    # Enter a parse tree produced by AsistenciaParser#instruction.
    def enterInstruction(self, ctx:AsistenciaParser.InstructionContext):
        pass

    # Exit a parse tree produced by AsistenciaParser#instruction.
    def exitInstruction(self, ctx:AsistenciaParser.InstructionContext):
        pass

    # Enter a parse tree produced by AsistenciaParser#loadStmt.
    def enterLoadStmt(self, ctx:AsistenciaParser.LoadStmtContext):
        pass

    # Exit a parse tree produced by AsistenciaParser#loadStmt.
    def exitLoadStmt(self, ctx:AsistenciaParser.LoadStmtContext):
        pass

    # Enter a parse tree produced by AsistenciaParser#filterStmt.
    def enterFilterStmt(self, ctx:AsistenciaParser.FilterStmtContext):
        pass

    # Exit a parse tree produced by AsistenciaParser#filterStmt.
    def exitFilterStmt(self, ctx:AsistenciaParser.FilterStmtContext):
        pass

    # Enter a parse tree produced by AsistenciaParser#filterExpr.
    def enterFilterExpr(self, ctx:AsistenciaParser.FilterExprContext):
        pass

    # Exit a parse tree produced by AsistenciaParser#filterExpr.
    def exitFilterExpr(self, ctx:AsistenciaParser.FilterExprContext):
        pass

    # Enter a parse tree produced by AsistenciaParser#condition.
    def enterCondition(self, ctx:AsistenciaParser.ConditionContext):
        pass

    # Exit a parse tree produced by AsistenciaParser#condition.
    def exitCondition(self, ctx:AsistenciaParser.ConditionContext):
        pass

    # Enter a parse tree produced by AsistenciaParser#aggregateStmt.
    def enterAggregateStmt(self, ctx:AsistenciaParser.AggregateStmtContext):
        pass

    # Exit a parse tree produced by AsistenciaParser#aggregateStmt.
    def exitAggregateStmt(self, ctx:AsistenciaParser.AggregateStmtContext):
        pass

    # Enter a parse tree produced by AsistenciaParser#printStmt.
    def enterPrintStmt(self, ctx:AsistenciaParser.PrintStmtContext):
        pass

    # Exit a parse tree produced by AsistenciaParser#printStmt.
    def exitPrintStmt(self, ctx:AsistenciaParser.PrintStmtContext):
        pass

    # Enter a parse tree produced by AsistenciaParser#value.
    def enterValue(self, ctx:AsistenciaParser.ValueContext):
        pass

    # Exit a parse tree produced by AsistenciaParser#value.
    def exitValue(self, ctx:AsistenciaParser.ValueContext):
        pass

del AsistenciaParser