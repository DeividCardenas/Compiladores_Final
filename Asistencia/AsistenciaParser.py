# Generated from Asistencia.g4 by ANTLR 4.13.2
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
        4,1,12,62,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,1,0,4,0,20,8,0,11,0,12,0,21,1,1,1,1,1,1,1,1,3,
        1,28,8,1,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,4,1,4,1,4,5,4,41,8,4,
        10,4,12,4,44,9,4,1,5,1,5,1,5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,1,7,
        1,7,1,7,1,8,1,8,1,8,0,0,9,0,2,4,6,8,10,12,14,16,0,1,1,0,7,8,57,0,
        19,1,0,0,0,2,27,1,0,0,0,4,29,1,0,0,0,6,33,1,0,0,0,8,37,1,0,0,0,10,
        45,1,0,0,0,12,50,1,0,0,0,14,56,1,0,0,0,16,59,1,0,0,0,18,20,3,2,1,
        0,19,18,1,0,0,0,20,21,1,0,0,0,21,19,1,0,0,0,21,22,1,0,0,0,22,1,1,
        0,0,0,23,28,3,4,2,0,24,28,3,6,3,0,25,28,3,12,6,0,26,28,3,14,7,0,
        27,23,1,0,0,0,27,24,1,0,0,0,27,25,1,0,0,0,27,26,1,0,0,0,28,3,1,0,
        0,0,29,30,5,1,0,0,30,31,5,7,0,0,31,32,5,2,0,0,32,5,1,0,0,0,33,34,
        5,3,0,0,34,35,3,8,4,0,35,36,5,2,0,0,36,7,1,0,0,0,37,42,3,10,5,0,
        38,39,5,10,0,0,39,41,3,10,5,0,40,38,1,0,0,0,41,44,1,0,0,0,42,40,
        1,0,0,0,42,43,1,0,0,0,43,9,1,0,0,0,44,42,1,0,0,0,45,46,5,4,0,0,46,
        47,5,7,0,0,47,48,5,9,0,0,48,49,3,16,8,0,49,11,1,0,0,0,50,51,5,5,
        0,0,51,52,5,11,0,0,52,53,5,4,0,0,53,54,5,7,0,0,54,55,5,2,0,0,55,
        13,1,0,0,0,56,57,5,6,0,0,57,58,5,2,0,0,58,15,1,0,0,0,59,60,7,0,0,
        0,60,17,1,0,0,0,3,21,27,42
    ]

class AsistenciaParser ( Parser ):

    grammarFileName = "Asistencia.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'load'", "';'", "'filter'", "'column'", 
                     "'aggregate'", "'print'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "STRING", "NUMBER", 
                      "OPERATOR", "LOGICAL_OP", "AGG_OP", "WS" ]

    RULE_program = 0
    RULE_instruction = 1
    RULE_loadStmt = 2
    RULE_filterStmt = 3
    RULE_filterExpr = 4
    RULE_condition = 5
    RULE_aggregateStmt = 6
    RULE_printStmt = 7
    RULE_value = 8

    ruleNames =  [ "program", "instruction", "loadStmt", "filterStmt", "filterExpr", 
                   "condition", "aggregateStmt", "printStmt", "value" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    STRING=7
    NUMBER=8
    OPERATOR=9
    LOGICAL_OP=10
    AGG_OP=11
    WS=12

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def instruction(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AsistenciaParser.InstructionContext)
            else:
                return self.getTypedRuleContext(AsistenciaParser.InstructionContext,i)


        def getRuleIndex(self):
            return AsistenciaParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = AsistenciaParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 19 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 18
                self.instruction()
                self.state = 21 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 106) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InstructionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def loadStmt(self):
            return self.getTypedRuleContext(AsistenciaParser.LoadStmtContext,0)


        def filterStmt(self):
            return self.getTypedRuleContext(AsistenciaParser.FilterStmtContext,0)


        def aggregateStmt(self):
            return self.getTypedRuleContext(AsistenciaParser.AggregateStmtContext,0)


        def printStmt(self):
            return self.getTypedRuleContext(AsistenciaParser.PrintStmtContext,0)


        def getRuleIndex(self):
            return AsistenciaParser.RULE_instruction

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInstruction" ):
                listener.enterInstruction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInstruction" ):
                listener.exitInstruction(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstruction" ):
                return visitor.visitInstruction(self)
            else:
                return visitor.visitChildren(self)




    def instruction(self):

        localctx = AsistenciaParser.InstructionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_instruction)
        try:
            self.state = 27
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 23
                self.loadStmt()
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 2)
                self.state = 24
                self.filterStmt()
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 3)
                self.state = 25
                self.aggregateStmt()
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 4)
                self.state = 26
                self.printStmt()
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


    class LoadStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(AsistenciaParser.STRING, 0)

        def getRuleIndex(self):
            return AsistenciaParser.RULE_loadStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLoadStmt" ):
                listener.enterLoadStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLoadStmt" ):
                listener.exitLoadStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLoadStmt" ):
                return visitor.visitLoadStmt(self)
            else:
                return visitor.visitChildren(self)




    def loadStmt(self):

        localctx = AsistenciaParser.LoadStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_loadStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 29
            self.match(AsistenciaParser.T__0)
            self.state = 30
            self.match(AsistenciaParser.STRING)
            self.state = 31
            self.match(AsistenciaParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FilterStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def filterExpr(self):
            return self.getTypedRuleContext(AsistenciaParser.FilterExprContext,0)


        def getRuleIndex(self):
            return AsistenciaParser.RULE_filterStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFilterStmt" ):
                listener.enterFilterStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFilterStmt" ):
                listener.exitFilterStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFilterStmt" ):
                return visitor.visitFilterStmt(self)
            else:
                return visitor.visitChildren(self)




    def filterStmt(self):

        localctx = AsistenciaParser.FilterStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_filterStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 33
            self.match(AsistenciaParser.T__2)
            self.state = 34
            self.filterExpr()
            self.state = 35
            self.match(AsistenciaParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FilterExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def condition(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AsistenciaParser.ConditionContext)
            else:
                return self.getTypedRuleContext(AsistenciaParser.ConditionContext,i)


        def LOGICAL_OP(self, i:int=None):
            if i is None:
                return self.getTokens(AsistenciaParser.LOGICAL_OP)
            else:
                return self.getToken(AsistenciaParser.LOGICAL_OP, i)

        def getRuleIndex(self):
            return AsistenciaParser.RULE_filterExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFilterExpr" ):
                listener.enterFilterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFilterExpr" ):
                listener.exitFilterExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFilterExpr" ):
                return visitor.visitFilterExpr(self)
            else:
                return visitor.visitChildren(self)




    def filterExpr(self):

        localctx = AsistenciaParser.FilterExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_filterExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 37
            self.condition()
            self.state = 42
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==10:
                self.state = 38
                self.match(AsistenciaParser.LOGICAL_OP)
                self.state = 39
                self.condition()
                self.state = 44
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(AsistenciaParser.STRING, 0)

        def OPERATOR(self):
            return self.getToken(AsistenciaParser.OPERATOR, 0)

        def value(self):
            return self.getTypedRuleContext(AsistenciaParser.ValueContext,0)


        def getRuleIndex(self):
            return AsistenciaParser.RULE_condition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondition" ):
                listener.enterCondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondition" ):
                listener.exitCondition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondition" ):
                return visitor.visitCondition(self)
            else:
                return visitor.visitChildren(self)




    def condition(self):

        localctx = AsistenciaParser.ConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_condition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 45
            self.match(AsistenciaParser.T__3)
            self.state = 46
            self.match(AsistenciaParser.STRING)
            self.state = 47
            self.match(AsistenciaParser.OPERATOR)
            self.state = 48
            self.value()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AggregateStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AGG_OP(self):
            return self.getToken(AsistenciaParser.AGG_OP, 0)

        def STRING(self):
            return self.getToken(AsistenciaParser.STRING, 0)

        def getRuleIndex(self):
            return AsistenciaParser.RULE_aggregateStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAggregateStmt" ):
                listener.enterAggregateStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAggregateStmt" ):
                listener.exitAggregateStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAggregateStmt" ):
                return visitor.visitAggregateStmt(self)
            else:
                return visitor.visitChildren(self)




    def aggregateStmt(self):

        localctx = AsistenciaParser.AggregateStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_aggregateStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 50
            self.match(AsistenciaParser.T__4)
            self.state = 51
            self.match(AsistenciaParser.AGG_OP)
            self.state = 52
            self.match(AsistenciaParser.T__3)
            self.state = 53
            self.match(AsistenciaParser.STRING)
            self.state = 54
            self.match(AsistenciaParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrintStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return AsistenciaParser.RULE_printStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrintStmt" ):
                listener.enterPrintStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrintStmt" ):
                listener.exitPrintStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrintStmt" ):
                return visitor.visitPrintStmt(self)
            else:
                return visitor.visitChildren(self)




    def printStmt(self):

        localctx = AsistenciaParser.PrintStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_printStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 56
            self.match(AsistenciaParser.T__5)
            self.state = 57
            self.match(AsistenciaParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(AsistenciaParser.STRING, 0)

        def NUMBER(self):
            return self.getToken(AsistenciaParser.NUMBER, 0)

        def getRuleIndex(self):
            return AsistenciaParser.RULE_value

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValue" ):
                listener.enterValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValue" ):
                listener.exitValue(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitValue" ):
                return visitor.visitValue(self)
            else:
                return visitor.visitChildren(self)




    def value(self):

        localctx = AsistenciaParser.ValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_value)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 59
            _la = self._input.LA(1)
            if not(_la==7 or _la==8):
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





