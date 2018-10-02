import sys
import ply.yacc as yacc
from scanner.py import tokens

#For adding me to github

def p_davinci(p):
	'''davinci : DAVINCI BLOCK'''
	p[0] = "DaVinci Compilado"

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
	'''vars : var vars2 '''

def p_vars2(p):
	'''vars2 : type ID vars3 SEMICOLON vars2
	| type ID vars3 SEMICOLON'''

def p_vars3(p):
	'''vars3 : COMMA ID vars3 
	| empty'''

def p_statute(p):
	'''statute: assignment
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
	 | rotate'''

def p_assignment(p):
	'''assignment : ID EQUAL expression SEMICOLON'''

def p_color_cte(p):
	'''color_cte: RED
		| BLUE
		| YELLOW
		| GREEN
		| PINK
		| PURPLE'''

def p_color(p):
	'''color: COLOR LPAREN color_cte RPAREN SEMICOLON'''

def p_circle(p):
	'''circle: CIRCLE LPAREN exp RPAREN SEMICOLON'''

def p_square(p):
	'''square: SQUARE LPAREN exp RPAREN SEMICOLON'''

def p_triangle(p):
	'''triangle: TRIANGLE LPAREN exp COMMA exp RPAREN SEMICOLON'''

def p_rectangle(p):
	'''rectangle: RECTANGLE LPAREN exp COMMA exp RPAREN SEMICOLON'''

def p_poligon(p):
	'''poligon: POLIGON LPAREN exp COMMA exp RPAREN SEMICOLON'''

def p_rotate(p):
	'''rotate : ROTATE LPAREN exp RPAREN SEMICOLON
	| ROTATE LPAREN cte_string RPAREN SEMICOLON'''

def p_pensize(p):
	'''pensize: PENSIZE LPAREN exp RPAREN SEMICOLON'''

def p_penforward(p):
	'''penforwars: PENFORWARD LPAREN exp RPAREN SEMICOLON'''

def p_penback(p):
	'''penback: PENBACK LPAREN exp RPAREN SEMICOLON'''

def p_type(p):
	'''type: INT
		| FLOAT
		| BOOL
		| STRING'''

def p_cte_bool(p):
	'''cte_bool : TRUE
				| FALSE'''

def p_var_cte(p):
	'''var_cte : ID
				| cte_int
				| cte_float
				| call'''

def p_condition(p): 
	'''condition : IF LPAREN EXPRESSION RPAREN BLOCK condition1 SEMICOLON'''

def p_condition1(p):
	'''condition1 : ELSE BLOCK
	| empty'''

def p_expression(p): 
	'''expression : EXP expression1 ID'''

def p_expression1(p): 
	'''expression1 : expression2 EXP'''

def p_expression2(p): 
	'''expression2 : LESSER | GREATER | EQUAL | NOTEQUAL'''

def p_exp(p): 
	'''exp : PLUS | MINOR | factor'''

def p_factor(p): 
	'''factor : LPAREN EXPRESSION RPAREN
	| var_cte
	| factor1 var_cte'''

def p_factor1(p): 
	'''factor1 : MINUS | PLUS'''

def p_term(p):
	'''term : DIVIDE | TIMES | factor'''

def p_call(p):
	'''call : ID LPAREN call1 RPAREN SEMICOLON'''

def p_call1(p):		
	'''call : ID COMMA call1
	| exp
	| st_cte'''



def p_empty(p):
	'''empty :'''