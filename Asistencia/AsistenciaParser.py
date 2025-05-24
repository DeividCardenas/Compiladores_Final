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
        4,1,13,70,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,1,0,1,0,5,0,23,8,0,10,0,12,0,26,9,0,1,
        0,1,0,1,1,1,1,1,2,1,2,1,2,1,2,3,2,36,8,2,1,3,1,3,1,3,1,3,1,4,1,4,
        1,4,1,4,1,5,1,5,1,5,5,5,49,8,5,10,5,12,5,52,9,5,1,6,1,6,1,6,1,6,
        1,6,1,7,1,7,1,7,1,7,1,7,1,7,1,8,1,8,1,8,1,9,1,9,1,9,0,0,10,0,2,4,
        6,8,10,12,14,16,18,0,1,1,0,8,9,65,0,24,1,0,0,0,2,29,1,0,0,0,4,35,
        1,0,0,0,6,37,1,0,0,0,8,41,1,0,0,0,10,45,1,0,0,0,12,53,1,0,0,0,14,
        58,1,0,0,0,16,64,1,0,0,0,18,67,1,0,0,0,20,23,3,2,1,0,21,23,3,4,2,
        0,22,20,1,0,0,0,22,21,1,0,0,0,23,26,1,0,0,0,24,22,1,0,0,0,24,25,
        1,0,0,0,25,27,1,0,0,0,26,24,1,0,0,0,27,28,5,0,0,1,28,1,1,0,0,0,29,
        30,5,7,0,0,30,3,1,0,0,0,31,36,3,6,3,0,32,36,3,8,4,0,33,36,3,14,7,
        0,34,36,3,16,8,0,35,31,1,0,0,0,35,32,1,0,0,0,35,33,1,0,0,0,35,34,
        1,0,0,0,36,5,1,0,0,0,37,38,5,1,0,0,38,39,5,8,0,0,39,40,5,2,0,0,40,
        7,1,0,0,0,41,42,5,3,0,0,42,43,3,10,5,0,43,44,5,2,0,0,44,9,1,0,0,
        0,45,50,3,12,6,0,46,47,5,11,0,0,47,49,3,12,6,0,48,46,1,0,0,0,49,
        52,1,0,0,0,50,48,1,0,0,0,50,51,1,0,0,0,51,11,1,0,0,0,52,50,1,0,0,
        0,53,54,5,4,0,0,54,55,5,8,0,0,55,56,5,10,0,0,56,57,3,18,9,0,57,13,
        1,0,0,0,58,59,5,5,0,0,59,60,5,12,0,0,60,61,5,4,0,0,61,62,5,8,0,0,
        62,63,5,2,0,0,63,15,1,0,0,0,64,65,5,6,0,0,65,66,5,2,0,0,66,17,1,
        0,0,0,67,68,7,0,0,0,68,19,1,0,0,0,4,22,24,35,50
    ]

class AsistenciaParser ( Parser ):

    grammarFileName = "Asistencia.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'load'", "';'", "'filter'", "'column'", 
                     "'aggregate'", "'print'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "SCRIPT_COMMENT", 
                      "STRING", "NUMBER", "OPERATOR", "LOGICAL_OP", "AGG_OP", 
                      "WS" ]

    RULE_program = 0
    RULE_scriptComment = 1
    RULE_instruction = 2
    RULE_loadStmt = 3
    RULE_filterStmt = 4
    RULE_filterExpr = 5
    RULE_condition = 6
    RULE_aggregateStmt = 7
    RULE_printStmt = 8
    RULE_value = 9

    ruleNames =  [ "program", "scriptComment", "instruction", "loadStmt", 
                   "filterStmt", "filterExpr", "condition", "aggregateStmt", 
                   "printStmt", "value" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    SCRIPT_COMMENT=7
    STRING=8
    NUMBER=9
    OPERATOR=10
    LOGICAL_OP=11
    AGG_OP=12
    WS=13

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

        def EOF(self):
            return self.getToken(AsistenciaParser.EOF, 0)

        def scriptComment(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AsistenciaParser.ScriptCommentContext)
            else:
                return self.getTypedRuleContext(AsistenciaParser.ScriptCommentContext,i)


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




    def program(self):

        localctx = AsistenciaParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 24
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 234) != 0):
                self.state = 22
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [7]:
                    self.state = 20
                    self.scriptComment()
                    pass
                elif token in [1, 3, 5, 6]:
                    self.state = 21
                    self.instruction()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 26
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 27
            self.match(AsistenciaParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ScriptCommentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SCRIPT_COMMENT(self):
            return self.getToken(AsistenciaParser.SCRIPT_COMMENT, 0)

        def getRuleIndex(self):
            return AsistenciaParser.RULE_scriptComment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterScriptComment" ):
                listener.enterScriptComment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitScriptComment" ):
                listener.exitScriptComment(self)




    def scriptComment(self):

        localctx = AsistenciaParser.ScriptCommentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_scriptComment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 29
            self.match(AsistenciaParser.SCRIPT_COMMENT)
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




    def instruction(self):

        localctx = AsistenciaParser.InstructionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_instruction)
        try:
            self.state = 35
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 31
                self.loadStmt()
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 2)
                self.state = 32
                self.filterStmt()
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 3)
                self.state = 33
                self.aggregateStmt()
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 4)
                self.state = 34
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




    def loadStmt(self):

        localctx = AsistenciaParser.LoadStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_loadStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 37
            self.match(AsistenciaParser.T__0)
            self.state = 38
            self.match(AsistenciaParser.STRING)
            self.state = 39
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




    def filterStmt(self):

        localctx = AsistenciaParser.FilterStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_filterStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 41
            self.match(AsistenciaParser.T__2)
            self.state = 42
            self.filterExpr()
            self.state = 43
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




    def filterExpr(self):

        localctx = AsistenciaParser.FilterExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_filterExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 45
            self.condition()
            self.state = 50
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==11:
                self.state = 46
                self.match(AsistenciaParser.LOGICAL_OP)
                self.state = 47
                self.condition()
                self.state = 52
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




    def condition(self):

        localctx = AsistenciaParser.ConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_condition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 53
            self.match(AsistenciaParser.T__3)
            self.state = 54
            self.match(AsistenciaParser.STRING)
            self.state = 55
            self.match(AsistenciaParser.OPERATOR)
            self.state = 56
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




    def aggregateStmt(self):

        localctx = AsistenciaParser.AggregateStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_aggregateStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 58
            self.match(AsistenciaParser.T__4)
            self.state = 59
            self.match(AsistenciaParser.AGG_OP)
            self.state = 60
            self.match(AsistenciaParser.T__3)
            self.state = 61
            self.match(AsistenciaParser.STRING)
            self.state = 62
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




    def printStmt(self):

        localctx = AsistenciaParser.PrintStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_printStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 64
            self.match(AsistenciaParser.T__5)
            self.state = 65
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




    def value(self):

        localctx = AsistenciaParser.ValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_value)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 67
            _la = self._input.LA(1)
            if not(_la==8 or _la==9):
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





