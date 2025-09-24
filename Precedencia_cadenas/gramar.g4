grammar gramar;
prog: expr+ ;



expr: '-' expr                      # unaryMinus
    | '+' expr                      # unaryPlus
    | expr op=('*'|'/'|'%'|'^') expr # MulDiv
    | expr op=('+'|'-') expr        # AddSub
    | INT                           # int 
    | ID                            # id 
    | DOUBLE                        # double
    | '(' expr ')'                  # parens 
    | RAD func=ID '(' expr ')'       # funcRad
    | func=ID '(' expr ')'          # funcCall
    | SQRT '(' expr ')'             # sqrtf   
    | LN '(' expr ')'               # lnf
    | LOG '(' expr ')'              # logf  
    | expr FACT                     # factf
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
