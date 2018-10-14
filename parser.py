import sys
import ply.yacc as yacc
from scanner import tokens
from variablesTable import VariablesTable
from functions import Function
from variables import Variable

#we are on develop branch

varTable = VariablesTable()

funcParam = []  # Array to save function parameters
varList = []  # Array to save the ID of variables in the same line
functionBuilder = Builder(Function)
varBuilder = Builder(Variable)

def p_program(p):
	'''program : PROGRAM ID SEMICOLON program1 DAVINCI block'''
	print('COMPILED!\n')

def p_program1(p):
	'''program1 :program1 funcs
	| program1 vars global_vars
	| empty'''

def p_global_vars(p):
	'''global_vars : '''
	try:
		global varList
		for var in varList:
			varTable.add_global_variable(var)

		varList.clear()
	except ErrorHandler as e:
		e.print(p.lineno(1))

def p_block(p):
	'''block : LBRACE b1 RBRACE'''

def p_b1(p):
	'''b1 : vars b2 
	| b2''' 

def p_b2(p):
	'''b2 : b2 statute
	| empty''' 

def p_vars(p):
	'''vars : VAR vars2'''

def p_vars2(p):
	'''vars2 : vars2 type save_type vars3 SEMICOLON 
	| empty'''

def p_vars3(p):
	'''vars3 : ID ASSIGN expression vars4
	| ID list vars4
	| ID vars4'''
	varBuilder.put('id_var', p[1])
	varList.append(var_builder.build())
	varBuilder.clear()

def p_vars4(p):
	'''vars4 : vars4 COMMA ID
	| empty'''
	if len(p) > 2:
		varBuilder.put('id_var', p[3])
		varList.append(varBuilder.build())

def saveType(p):
	'''save_type: '''
	varBuilder.put('var_type', p[-1])

def p_list(p):
	'''list : LIST'''
	p[0] = p[1]

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
	 | while
	 | return
	 | penon
	 | penoff'''

def p_while(p):
	'''while : WHILE LPAREN expression RPAREN LBRACE b2 RBRACE'''

def p_assignment(p):
	'''assignment : ID ASSIGN expression SEMICOLON
	 | ID LBRACKET exp RBRACKET ASSIGN expression SEMICOLON'''

def p_color_cte(p):
	'''color_cte : RED
		| BLUE
		| YELLOW
		| GREEN
		| PINK
		| PURPLE'''

def p_st_cte(p):
	'''st_cte : STRING
		| cte_bool'''

def p_funcs(p):
	'''funcs : FUNC type ID LPAREN type ID funcs1 RPAREN LBRACE funcs2 RBRACE funcs3
	| FUNC VOID ID LPAREN type ID funcs1 RPAREN LBRACE funcs2 RBRACE funcs3 '''

def p_funcs1(p):
	'''funcs1 : funcs1 COMMA type ID 
	| empty'''

def p_funcs2(p):
	'''funcs2 : funcs2 vars
	| funcs2 statute
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
			| STRING
			| BOOL'''

def p_var_cte(p):
	'''var_cte : ID
				| CTE_INT
				| CTE_FLOAT
				| cte_bool
				| ID list
				| call'''

def p_cte_bool(p):
	'''cte_bool : TRUE
	| FALSE'''

def p_condition(p): 
	'''condition : IF LPAREN expression RPAREN LBRACE b2 RBRACE condition1'''

def p_condition1(p):
	'''condition1 : ELSE LBRACE b2 RBRACE
	| empty'''

def p_expression(p): 
	'''expression : exp expression1'''

def p_expression1(p): 
	'''expression1 : LESSER exp
	| GREATER exp
	| EQUAL exp
	| NOTEQUAL exp
	| GREATEROREQUAL exp
    | LESSEROREQUAL exp
    | empty'''

def p_exp(p): 
	'''exp : term exp1'''

def p_exp1(p): 
	'''exp1 : MINUS exp
	| PLUS exp
	| empty'''

def p_factor(p): 
	'''factor : LPAREN expression RPAREN
	| var_cte
	| factor1 var_cte'''

def p_factor1(p): 
	'''factor1 : MINUS 
	| PLUS
	| empty'''

def p_term(p):
	'''term : factor term1'''

def p_term1(p):
	'''term1 : DIVIDE term
		| TIMES term
		| empty'''

def p_call(p):
	'''call : ID LPAREN call1 RPAREN SEMICOLON'''

def p_call1(p):		
	'''call1 : ID COMMA call1
	| exp
	| st_cte'''

def p_return(p):
	'''return : RETURN var_cte SEMICOLON
			| RETURN st_cte SEMICOLON'''

def p_empty(p):
	'''empty :'''
	pass

def p_error(p):
    print("Unexpected {} at line {}".format(p.value, p.lexer.lineno))

parser_DaVinci = yacc.yacc()

if __name__ == '__main__':

    if len(sys.argv) > 1:
        file = sys.argv[1]
        try:
            f = open('test2.txt')
            data = f.read()
            f.close()
            if parser_DaVinci.parse(data) == "COMPILED":
                print("Valid input")
        except EOFError:
            print(EOFError)
    else:
        print("No file to test found")
