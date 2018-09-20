import sys
import ply.yacc as yacc
from scanner.py import tokens

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
	'''circle: CIRCLE LPAREN cte_int RPAREN SEMICOLON'''

def p_square(p):
	'''square: SQUARE LPAREN cte_int RPAREN SEMICOLON'''

def p_triangle(p):
	'''triangle: TRIANGLE LPAREN cte_int COMMA cte_int RPAREN SEMICOLON'''

def p_rectangle(p):
	'''rectangle: RECTANGLE LPAREN cte_int COMMA cte_int RPAREN SEMICOLON'''

def p_poligon(p):
	'''poligon: POLIGON LPAREN cte_int COMMA cte_int RPAREN SEMICOLON'''

def p_rotate(p):
	'''rotate : ROTATE LPAREN cte_int RPAREN SEMICOLON
	| ROTATE LPAREN cte_string RPAREN SEMICOLON'''

def p_pensize(p):
	'''pensize: PENSIZE LPAREN cte_int RPAREN SEMICOLON'''

def p_penforward(p):
	'''penforwars: PENFORWARD LPAREN cte_int RPAREN SEMICOLON'''

def p_penback(p):
	'''penback: PENBACK LPAREN cte_int RPAREN SEMICOLON'''

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



def p_empty(p):
	'''empty :'''