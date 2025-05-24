grammar Asistencia;

program: (scriptComment | instruction)* EOF;

scriptComment: SCRIPT_COMMENT;
instruction: loadStmt | filterStmt | aggregateStmt | printStmt;

loadStmt: 'load' STRING ';';
filterStmt: 'filter' filterExpr ';';
filterExpr: condition (LOGICAL_OP condition)*;
condition: 'column' STRING OPERATOR value;
aggregateStmt: 'aggregate' AGG_OP 'column' STRING ';';
printStmt: 'print' ';';

value: STRING | NUMBER;

SCRIPT_COMMENT: '# Script' [0-9]+ ':' ~[\r\n]* -> skip;
STRING: '"' (~["\r\n])* '"';
NUMBER: [0-9]+ ('.' [0-9]+)?;
OPERATOR: '>=' | '<=' | '>' | '<' | '==' | '!=';
LOGICAL_OP: 'AND' | 'OR';
AGG_OP: 'count' | 'sum' | 'average';

WS: [ \t\r\n]+ -> skip;