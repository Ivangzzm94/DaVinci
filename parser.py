import sys
import ply.yacc as yacc
from scanner import tokens

#branch develop

def p_program(p):
	'''program : PROGRAM ID SEMICOLON program1 DAVINCI block'''

def p_program1(p):
	'''program1 : funcs
	| vars
	| funcs vars
	| vars funcs '''

def p_block(p):
	'''block : LBRACE b1 RBRACE'''

def p_b1(p):
	'''b1 : vars b2 
	| b2''' 

def p_b2(p):
	'''b2 : statute
	| statute b2
	| empty''' 

def p_vars(p):
	'''vars : VAR vars2 '''

def p_vars2(p):
	'''vars2 : type ID vars3 SEMICOLON vars2
	| type ID vars3 SEMICOLON'''

def p_vars3(p):
	'''vars3 : COMMA ID vars3 
	| list vars3
	| list COMMA ID vars3 
	| empty'''

def p_list(p):
	'''list : LBRACKET exp RBRACKET'''

def p_statute(p):
	'''statute : assignment
	 | call
	 | condition
	 | triangle
	 | rectangle
	 | square
	 | circle
	 | poligon
	 | color
	 | pensize
	 | penforward
	 | penback
	 | rotate
	 | WHILE
	 | return
	 | penon
	 | penoff'''

def p_assignment(p):
	'''assignment : ID EQUAL expression SEMICOLON
	 | ID LBRACKET exp RBRACKET EQUAL expression SEMICOLON'''

def p_color_cte(p):
	'''color_cte : RED
		| BLUE
		| YELLOW
		| GREEN
		| PINK
		| PURPLE'''

def p_st_cte(p):
	'''st_cte : STRING SEMICOLON
		| CTE_BOOL SEMICOLON'''

def p_funcs(p):
	'''funcs : type ID LPAREN type ID funcs1 RPAREN LBRACE funcs2 RBRACE funcs3
	| VOID ID LPAREN type ID funcs1 RPAREN LBRACE funcs2 RBRACE funcs3 '''

def p_funcs1(p):
	'''funcs1 : COMMA type ID funcs1
	| empty'''

def p_funcs2(p):
	'''funcs2 : vars
	| vars statute
	| statute vars
	| statute
	| empty '''	

def p_funcs3(p):
	'''funcs3 : funcs
	| empty'''	

def p_color(p):
	'''color : COLOR LPAREN color_cte RPAREN SEMICOLON'''

def p_circle(p):
	'''circle : CIRCLE LPAREN exp RPAREN SEMICOLON'''

def p_square(p):
	'''square : SQUARE LPAREN exp RPAREN SEMICOLON'''

def p_triangle(p):
	'''triangle : TRIANGLE LPAREN exp COMMA exp RPAREN SEMICOLON'''

def p_rectangle(p):
	'''rectangle : RECTANGLE LPAREN exp COMMA exp RPAREN SEMICOLON'''

def p_poligon(p):
	'''poligon : POLIGON LPAREN exp COMMA exp RPAREN SEMICOLON'''

def p_rotate(p):
	'''rotate : ROTATE LPAREN exp RPAREN SEMICOLON
	| ROTATE LPAREN CTE_STRING RPAREN SEMICOLON'''

def p_pensize(p):
	'''pensize : PENSIZE LPAREN exp RPAREN SEMICOLON'''

def p_penforward(p):
	'''penforward : PENFORWARD LPAREN exp RPAREN SEMICOLON'''

def p_penback(p):
	'''penback : PENBACK LPAREN exp RPAREN SEMICOLON'''

def p_penon(p):
	'''penon : PENON LPAREN RPAREN SEMICOLON'''

def p_penoff(p):
	'''penoff : PENOFF LPAREN RPAREN SEMICOLON'''

def p_type(p):
	'''type : INT
		| FLOAT
		| BOOL
		| STRING'''

def p_cte_bool(p):
	'''cte_bool : TRUE
				| FALSE'''

def p_var_cte(p):
	'''var_cte : ID var_cte1
				| CTE_INT
				| CTE_FLOAT
				| call'''

def p_var_cte1(p):
	'''var_cte1 : LBRACKET exp RBRACKET
				 | LPAREN exp RPAREN
				 | empty'''

def p_condition(p): 
	'''condition : IF LPAREN EXPRESSION RPAREN BLOCK condition1 SEMICOLON'''

def p_condition1(p):
	'''condition1 : ELSE BLOCK
	| empty'''

def p_expression(p): 
	'''expression : exp expression1 ID'''

def p_expression1(p): 
	'''expression1 : expression2 '''

def p_expression2(p): 
	'''expression2 : LESSER 
	| GREATER 
	| EQUAL 
	| NOTEQUAL'''

def p_exp(p): 
	'''exp : term exp1'''

def p_exp1(p): 
	'''exp1 : MINUS term exp1
	| PLUS term exp1
	| empty'''

def p_factor(p): 
	'''factor : LPAREN EXPRESSION RPAREN
	| var_cte
	| factor1 var_cte'''

def p_factor1(p): 
	'''factor1 : MINUS 
	| PLUS'''

def p_term(p):
	'''term : DIVIDE 
	| TIMES 
	| factor'''

def p_call(p):
	'''call : ID LPAREN call1 RPAREN SEMICOLON'''

def p_call1(p):		
	'''call1 : ID COMMA call1
	| exp
	| ST_CTE'''

def p_return(p):
	'''return : exp SEMICOLON'''

def p_empty(p):
	'''empty :'''

def p_error(p):
    print("Unexpected {} at line {}".format(p.value, p.lexer.lineno))

parser_DaVinci = yacc.yacc()

if __name__ == '__main__':

    if len(sys.argv) > 1:
        file = sys.argv[1]
        try:
            f = open('test1.txt')
            data = f.read()
            f.close()
            if parser_DaVinci.parse(data) == "COMPILED":
                print("Valid input")
        except EOFError:
            print(EOFError)
    else:
        print("No file to test found")
