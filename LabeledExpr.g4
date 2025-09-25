grammar LabeledExpr;

prog: expr+;

expr
    : addExpr       # toAdd
    ;

addExpr
    : mulExpr( (ADD | SUB) addExpr )?    # addRight
    ;

mulExpr
    : unaryExpr ( (MUL | DIV | MOD) mulExpr)?  # mulRight
    ;

unaryExpr
    : SUB unaryExpr     # unaryMinus
    | ADD unaryExpr     # unaryPlus
    | postfixExpr       # toPostfix
    ;

postfixExpr
    : primaryExpr (FACT)*  # factf
    ;

primaryExpr
    : INT                 # int
    | DOUBLE              # double
    | ID                  # id
    | '(' expr ')'        # parens
    | RAD ID '(' expr ')' # funcRad
    | ID '(' expr ')'     # funcCall
    | SQRT '(' expr ')'   # sqrtf
    | LN '(' expr ')'     # lnf
    | LOG '(' expr ')'    # logf
    ;

MUL : '*' ;
DIV : '/' ;
MOD : '%' ;
POW : '^' ;
ADD : '+' ;
SUB : '-' ;
DOUBLE : [0-9]+ '.' [0-9]+ ;
INT : [0-9]+ ;
RAD : 'rad' ;
SQRT : 'sqrt' ;
LN : 'ln' ;
LOG : 'log' ;
FACT : '!' ;
ID  : [a-zA-Z]+ ;
NEWLINE:'\r'? '\n' ;
WS  : [ \t]+ -> skip ;
