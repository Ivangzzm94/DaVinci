import sys
import ply.yacc as yacc
from scanner import tokens
from variablesTable import VariablesTable
from functions import Function
from variables import Variable
from builder import Builder
from semanticCube import SemanticCube
from errors import ErrorHandler
from quads import Quad, Quads
import turtle

#Inicializacion de variables para manejar el pincel
window = turtle.Screen()
tur = turtle.Turtle()
tur.shape("turtle")

#we are on develop branch

varTable = VariablesTable()

funcParam = []  # Array to save function parameters
varList = []  # Array to save the ID of variables in the same line
functionBuilder = Builder(Function)
varBuilder = Builder(Variable)

pilaO = []
POper = []
PTypes = []
PJumps = []

# Declaracion de direcciones para globales y temporales

nextAvailable = {'globalInt':1000,'globalFloat':5000,'globalBool':10000,
		   		'tempInt':15000,'tempFloat':20000,'tempBool':25000 }

def p_program(p):
	'''program : PROGRAM ID SEMICOLON program1 DAVINCI block'''
	print('COMPILED!\n')

def p_program1(p):
	'''program1 : program1 funcs
	| program1 vars global_vars
	| empty'''

def p_global_vars(p):
	'''global_vars : '''
	try:
		global varList
		for var in varList:
			varTable.add_global(var)
			print("global var")
		varList.clear()
	except ErrorHandler as e:
		e.print(p.lineno(1))

def p_block(p):
	'''block : LBRACE b1 RBRACE'''

def p_b1(p):
	'''b1 : vars local_vars b2 
	| b2''' 

def p_local_vars(p):
	'''local_vars : '''
	try:
		global varList
		for var in varList:
			varTable.add_local(var)
			print("local var")
		varList.clear()
	except ErrorHandler as e:
		e.print(p.lineno(1))

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
	varBuilder.put('var_id', p[1])
	varList.append(varBuilder.build())
	varBuilder.clear()

def p_vars4(p):
	'''vars4 : vars4 COMMA ID
	| empty'''
	if len(p) > 2:
		varBuilder.put('var_id', p[3])
		varList.append(varBuilder.build())

def p_save_type(p):
	'''save_type : '''
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
	'''while : WHILE while_return LPAREN type_check expression RPAREN LBRACE b2 RBRACE end_while'''

def p_while_return(p):
	'''while_return :'''
	PJumps.push(Quads.index)

def p_end_while(p):
	'''end_while :'''
	end = PJumps.pop()
	ret = Pjumps.pop()
	Quad.init(Goto, None, None, ret)
	#FILL(end, Quads.index) #***********************FALTA DECLARAR **************************

def p_assignment(p):
	'''assignment : ID cte_id ASSIGN expression SEMICOLON
	 | ID cte_id LBRACKET exp RBRACKET ASSIGN expression SEMICOLON'''

def p_cte_id(p):
	'''cte_id : '''
# try:
# 	var = VariablesTable.find_variable(p[-1])
# 	quads.add_operand(var)
# except ErrorHandler as e:
#     e.print(p.lineno(-1))
#     raise e

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
	'''condition : IF LPAREN expression RPAREN type_check LBRACE b2 RBRACE condition1 end_if'''

def p_condition1(p):
	'''condition1 : gotoElse ELSE LBRACE b2 RBRACE
	| empty'''

def p_type_check(p):
	'''type_check :'''
	exp_type = PTypes.pop()
	if exp_type != bool:
		ErrorHandler.type_error()
	else:
		result = pilaO.pop()
		Quad.init(GoToF, None, None , result)
		PJumps.push(Quads.index - 1)

def p_gotoElse(p):
	'''gotoElse :'''
	Quad.init(GoTo, None, None, None)
	false = PJumps.pop()
	PJumps.push(Quads.index - 1)
	#FILL(false, Quads.index) #***********************FALTA DECLARAR **************************

def p_end_if(p):
	'''end_if :'''
	end = PJumps.pop()
	#FILL(end, Quads.index) #***********************FALTA DECLARAR **************************

def p_expression(p): 
	'''expression : exp expression1'''

def p_expression1(p): 
	'''expression1 : LESSER relop exp top_relop
	| GREATER relop exp top_relop
	| EQUAL relop exp top_relop
	| NOTEQUAL relop exp top_relop
	| GREATEROREQUAL relop exp top_relop
    | LESSEROREQUAL relop exp top_relop
    | empty'''

def p_relop(p): 
	'''relop :'''
	op = p[-1]
	if op == '<':
		POper.append('<')
	if op == '>':
		POper.append('>')
	if op == '<=':
		POper.append('<=')
	if op == '==':
		POper.append('==')
	if op == '>=':
		POper.append('>=')
	if op == '!=':
		POper.append('!=')

def p_top_relop(p):
	'''top_relop :'''
	operator = POper.pop()
	if operator == '<' or operator == '>' or operator == '>=' or operator == '<=' or operator == '==' or operator == '!=':
		r_operand = pilaO.pop()
		r_type = PTypes.pop()
		l_operand = pilaO.pop()
		l_type = PTypes.pop()
		result_type = SemanticCube.getType(l_type, r_type, operator)
		if result_type != "Error":
			#calcular resultado
			result = nextCasillaEnMemoria
			q = Quad.init(operator, l_operand, r_operand, result)
			Quads.add_Quad(q)
			pilaO.append(result)
			PTypes.append(result_type)
		else:
			ErrorHandler.print(p.lineno(-1))
        	#raise ErrorHandler CHECAR***********CHECAR***********CHECAR***********CHECAR***********
	else:
		POper.append(operator)

def p_exp(p): 
	'''exp : term top_exp exp1'''

def p_exp1(p): 
	'''exp1 : MINUS push_sign exp
	| PLUS push_sign exp
	| empty'''

def p_top_exp(p):
	'''top_exp :'''
	operator = POper.pop()
	if operator == '+' or operator == '-':
		r_operand = pilaO.pop()
		r_type = PTypes.pop()
		l_operand = pilaO.pop()
		l_type = PTypes.pop()
		result_type = SemanticCube.getType(l_type, r_type, operator)
		if result_type != "Error":
			#calcular resultado
			result = nextCasillaEnMemoria
			q = Quad.init(operator, l_operand, r_operand, result)
			Quads.add_Quad(q)
			pilaO.append(result)
			PTypes.append(result_type)
		else:
			ErrorHandler.print(p.lineno(-1))
        	#raise ErrorHandler CHECAR***********CHECAR***********CHECAR***********CHECAR***********
	else:
		POper.append(operator)
	

def p_push_sign(p):
	'''push_sign :'''
	if not p[1] is None:
		sign = p[1]
	if sign is "/":
    		POper.append(Operators.DIVIDE)
	if sign is "*":
        	POper.append(Operators.TIMES)
	if sign is "+":
            POper.append(Operators.PLUS)
	if sign is "-":
            POper.append(Operators.MINUS)

def p_top_factor(p):
	'''top_factor :'''
	operator = POper.pop()
	if operator == Operators.TIMES or operator == Operators.DIVIDE: 
		r_operand = pilaO.pop()
		r_type = PTypes.pop()
		l_operand = pilaO.pop()
		l_type = PTypes.pop()
		result_type = SemanticCube.getType(l_type, r_type, operator)
		if result_type != "Error":
			#calcular resultado
			result = nextCasillaEnMemoria
			q = Quad.init(operator, l_operand, r_operand, result)
			Quads.add_Quad(q)
			pilaO.append(result)
			PTypes.append(result_type)
		else:
			ErrorHandler.print(p.lineno(-1))
        	#raise ErrorHandler CHECAR***********CHECAR***********CHECAR***********CHECAR
	else: 
		POper.append(operator)

def p_factor(p): 
	'''factor : LPAREN false_bottom expression RPAREN end_par
	| var_cte
	| ID push_id'''

def p_false_bottom(p): 
	'''false_bottom :'''
	if p[-1] is "(":
		POper.append(Operators.LPAREN)

def p_end_par(p): 
	'''end_par :'''
	if p[-1] is ")":
		POper.pop()

def p_push_id(p):
	'''push_id : '''
	try:
		var = VariablesTable.find_variable(p[-1])
		pilaO.append(var.var_id)
		PTypes.append(var.var_type)
	except ErrorHandler as error:
		error.type_error()
		raise error


def p_term(p):
	'''term : factor top_factor term1'''

def p_term1(p):
	'''term1 : DIVIDE push_sign term
		| TIMES push_sign term
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
