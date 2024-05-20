grammar gramatica;

options {
  language = Python3;
}
SEP:'¬';
ESP:'~';
EX : '!';
NEWLINE: '\r'? '\n' ; 
NUMERO: '-'?[0-9]+'.'?[0-9]?;
ID: [a-zA-Z0-9];           
WS: [ \t\r\n]+ -> skip;
IMPORT: 'import';
DEF: 'def';
CLASS: 'class';
IF: 'if';
ELSE: 'else';
FOR: 'for';
IN: 'in';
RANGE: 'range';
SELF: 'self';
WHILE: 'while';
TRY: 'try';
END: 'end';
EXCEPT: 'except';
RETURN: 'return';
BREAK: 'break';
NEXT: 'next';
INPUT: 'input';
PRINT: 'print';
INT: 'int';
FLOAT: 'float';
BOOLEAN: 'true' | 'false';
STR: 'str';
POW: 'pow';
MATHSQRT: 'mathsqrt';
AND: 'and';
OR: 'or';
NOT: 'not';
ELIF: 'elif';
SUMA: '+';
ASIGNACION: '=';
RESTA: '-';
DIVISION: '/';
MULTIPLICACION: '*';
IGUAL: '==';
DIFERENTE: '!=';
MAYORQUE: '>';
MENORQUE: '<';
MENORIGUAL: '>=';
MAYORIGUAL: '<=';
PUNTO: '.';
COMA: ',';
DOSPUNTOS: ':';
PUNTOCOMA: ';';
COMILLASIMPLE: '\'';
COMILLADOBLE: '"';
PARENTESIS_A: '(';
PARENTESIS_C: ')';
LLAVE_C: '}';
LLAVE_A: '{';
CORCHETE_A: '[';
CORCHETE_C: ']';
MASMAS: '++';
MENOSMENOS: '--';
POTENCIA:'^';
MODULO:'%';
WRITE: 'write';
OPEN: 'open';


start: sentencias+ ;

sentencias      : printf
                | asignacion
                | condicional
                | ciclo_while
                | expresion
                | funcion
                | llamafuncion 
                | ciclo_for
                | v_input 
                | casteo 
                | graficas 
                | importss 
                | func
                | matriz_operaciones
                | NEWLINE
                | lectura_archivo
                | escritura_archivo
                ;

asignacion: ID ASIGNACION var_casteo? PARENTESIS_A? (expresion | v_input | matriz_operaciones | arange) PARENTESIS_C? PUNTOCOMA
          | ID ASIGNACION ID PARENTESIS_A (parametro | expresion | matriz_operaciones )? PARENTESIS_C PUNTOCOMA
          | ID ASIGNACION cadena PUNTOCOMA
          ;

v_input: var_casteo? PARENTESIS_A? INPUT PARENTESIS_A expresion? PARENTESIS_C PARENTESIS_C?;

printf: PRINT PARENTESIS_A (expresion| COMA |matriz_operaciones)? PARENTESIS_C PUNTOCOMA
	;

var_casteo: STR
          | INT
          | FLOAT
          | BOOLEAN
          ;

casteo: var_casteo PARENTESIS_A expresion PARENTESIS_C;

cadena  : COMILLASIMPLE .+? COMILLASIMPLE
        | COMILLADOBLE .+? COMILLADOBLE 
        | COMILLADOBLE (.+? | EX)* COMILLADOBLE
        | COMILLASIMPLE (.+? | EX)* COMILLASIMPLE
        ;

funcion: DEF ID PARENTESIS_A parametro? PARENTESIS_C LLAVE_A stmt_func LLAVE_C;

stmt_func: sentencias* v_return?;


v_return: RETURN expresion PUNTOCOMA
        | RETURN PUNTOCOMA
        ;

llamafuncion: ID PARENTESIS_A parametro? PARENTESIS_C;

condicional: IF PARENTESIS_A? (parametro|expresion) PARENTESIS_C? LLAVE_A sentencias+ LLAVE_C elifBlock? condicional_else? ;

elifBlock: condicional_elif+;

condicional_elif: ELIF PARENTESIS_A? (parametro|expresion) PARENTESIS_C? LLAVE_A sentencias+ LLAVE_C;

condicional_else: ELSE LLAVE_A sentencias+ LLAVE_C;

ciclo_for: FOR ID IN RANGE PARENTESIS_A expresion COMA? expresion? COMA? expresion? PARENTESIS_C LLAVE_A sentencias+ v_return? LLAVE_C
          | FOR ID IN expresion LLAVE_A sentencias+ v_return? LLAVE_C
          | FOR ID IN cadena LLAVE_A sentencias+ v_return? LLAVE_C
          ;

ciclo_while: WHILE PARENTESIS_A? expresion PARENTESIS_C? LLAVE_A sentencias+ LLAVE_C;

parametro: ID (COMA ID)*;

func : ('math'|'np') PUNTO ('sin' | 'cos' | 'tan' | 'arcsin' | 'arccos' | 'arctan' |'factorial'|'sqrt' ) PARENTESIS_A expresion PARENTESIS_C;

expresion: expresion (SUMA | RESTA | MULTIPLICACION | DIVISION | POTENCIA | MODULO) termino
         | expresion ( MAYORQUE | MENORQUE | MENORIGUAL | MAYORIGUAL | DIFERENTE | IGUAL | ASIGNACION ) termino
         | expresion (OR | AND )termino
         | termino
         | func
         ;

matriz_operaciones: matriz SUMA? matriz?
                  | matriz RESTA matriz
                  | matriz MULTIPLICACION matriz
                  | 'inv' PARENTESIS_A matriz PARENTESIS_C
                  | 'trans' PARENTESIS_A matriz PARENTESIS_C
                  ;

matriz: CORCHETE_A fila_matriz (COMA fila_matriz)* CORCHETE_C;

fila_matriz: CORCHETE_A expresion (COMA expresion)* CORCHETE_C;

importss: IMPORT ('math' | 'matplotlib.pyplot' | 'numpy as np');

termino: NUMERO
       | ID+
       | BOOLEAN
       | cadena
       | lista
       | arreglo
       ;

lista: PARENTESIS_A (NUMERO | ID+ | BOOLEAN | cadena | COMA)+ PARENTESIS_C;

arreglo: CORCHETE_A (NUMERO | ID+ | BOOLEAN | cadena | COMA)+ CORCHETE_C;

graficas: ('plot'|'scatter'|'fill_between'|'bar'|'barh'|'hist') PARENTESIS_A x=expresion ',' y=expresion PARENTESIS_C
        | ('pie'|'boxplot') PARENTESIS_A x=expresion  PARENTESIS_C
        | ('grafsen'|'grafcos'|'graftan') PARENTESIS_A (arange|ID+) COMA func PARENTESIS_C
        ;

arange  : 'linspace' PARENTESIS_A expresion COMA expresion '*' 'np' PUNTO 'pi' COMA expresion PARENTESIS_C
        ;
lectura_archivo: OPEN PARENTESIS_A expresion PARENTESIS_C;

escritura_archivo: WRITE PARENTESIS_A expresion PARENTESIS_C DOSPUNTOS expresion END;
