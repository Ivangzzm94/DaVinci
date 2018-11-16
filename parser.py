import sys
import ply.yacc as yacc
from scanner import tokens
from variablesTable import VariablesTable
from functions import Function
from variables import *
from builder import Builder
from semanticCube import SemanticCube
from errors import ErrorHandler
from quads import *
from stack import *

varTable = VariablesTable()

funcParam = []  # Array to save function parameters
varList = []  # Array to save the ID of variables in the same line

quadList = Quads()
pilaOperandos = Stack()
pilaOperadores = Stack()
pTypes = Stack()
pJumps = Stack()

memory = Memory()
vartype = None
context_cont = 0
listsize = 1
cube = SemanticCube()

def p_program(p):
    '''program : PROGRAM ID SEMICOLON gotomain program1 DAVINCI fillmain block'''
    quadList.print_Quads()
    varTable.printVars()
    #memory.printVars()

def p_fillmain(p):
    '''fillmain : '''
    quadList.fill(0, quadList.index)

def p_gotomain(p):
    '''gotomain : '''
    q = Quad(Operations.GOTO.value, None, None, None)
    quadList.add_quad(q)

    f = open('quads.txt','w') #archivo de texto en donde se guardan los cuádruplos
    f.write(str(quadList.array[0])) #escribir en el archivo el cuádruplo
    f.close() # Cerrar el archivo de texto


def p_program1(p):
    '''program1 : program1 funcs save_funcs
	| program1 vars global_vars
	| empty'''

def p_save_funcs(p):
    '''save_funcs : '''

def p_global_vars(p):
    '''global_vars : '''
    try:
        global memory
        for var in varList:
            var.dir_virt = memory.putVarInMemory(context_cont, var.var_type, var.size, var.value)
            varTable.add_global(var)
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
            var.dir_virt = memory.putVarInMemory(context_cont, var.size, var.var_type, var.value)
            varTable.add_local(var)
        varList.clear()
    except ErrorHandler as e:
        e.print(p.lineno(1))

def p_b2(p):
    '''b2 : b2 statute
	| empty'''


def p_vars(p):
    '''vars : VAR vars2'''

def p_vars2(p):
    '''vars2 : type save_type vars3 SEMICOLON vars2
	| empty'''

def p_vars3(p):
    '''vars3 : ID ASSIGN expression saveassign vars4
	| ID list savelist vars4
	| ID saveid vars4'''

def p_savelist(p):
    '''savelist : '''
    v = Variable(p[-2], vartype, p[-1], None)
    varList.append(v)

def p_saveassign(p):
    '''saveassign : '''
    v = Variable(p[-3], vartype, 1, p[-1])
    varList.append(v)

def p_saveid(p):
    '''saveid : '''
    v = Variable(p[-1], vartype, 1, None)
    varList.append(v)

def p_vars4(p):
    '''vars4 : COMMA vars3
	| empty'''

def p_save_type(p):
    '''save_type : '''
    global vartype
    vartype = p[-1]

def p_list(p):
    '''list : LBRACKET CTE_INT RBRACKET'''
    p[0] = p[2]

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
    pJumps.push(quadList.index)

def p_end_while(p):
    '''end_while :'''
    end = pJumps.pop()
    ret = pJumps.pop()
    Quad(Operations.GOTO, None, None, ret)
    quadList.fill(quadList.index, end)

def p_assignment(p):
    '''assignment : ID ASSIGN expression SEMICOLON
	 | ID cte_id LBRACKET exp RBRACKET ASSIGN expression SEMICOLON'''

def p_cte_id(p):
    '''cte_id : '''

def p_color_cte(p):
    '''color_cte : RED
		| BLUE
		| YELLOW
		| GREEN
		| PINK
		| PURPLE'''
    if p[1] == 'red':
        p[0] = Color.RED.value
    if p[1] == 'blue':
        p[0] = Color.BLUE.value
    if p[1] == 'yellow':
        p[0] = Color.YELLOW.value
    if p[1] == 'pink':
        p[0] = Color.PINK.value
    if p[1] == 'purple':
        p[0] = Color.PURPLE.value

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
    quadList.add_quad(Functions.COLOR, p[3], None, None)

def p_circle(p):
    '''circle : CIRCLE LPAREN exp RPAREN SEMICOLON'''
    quadList.add_quad(Functions.CIRCLE, p[3], None, None)

def p_square(p):
    '''square : SQUARE LPAREN exp RPAREN SEMICOLON'''
    quadList.add_quad(Functions.SQUARE, p[3], None, None)

def p_triangle(p):
    '''triangle : TRIANGLE LPAREN exp COMMA exp RPAREN SEMICOLON'''
    quadList.add_quad(Functions.TRIANGLE, p[3], p[5], '')

def p_rectangle(p):
    '''rectangle : RECTANGLE LPAREN exp COMMA exp RPAREN SEMICOLON'''
    quadList.add_quad(Functions.RECTANGLE, p[3], p[5], None)

def p_poligon(p):
    '''poligon : POLIGON LPAREN exp COMMA exp RPAREN SEMICOLON'''
    quadList.add_quad(Functions.POLIGON, p[3], p[5], None)

def p_rotate(p):
    '''rotate : ROTATE LPAREN exp RPAREN SEMICOLON
	| ROTATE LPAREN CTE_STRING RPAREN SEMICOLON'''
    quadList.add_quad(Functions.ROTATE, p[3], None, None)

def p_pensize(p):
    '''pensize : PENSIZE LPAREN exp RPAREN SEMICOLON'''
    quadList.add_quad(Functions.PENSIZE, p[3], None, None)

def p_penforward(p):
    '''penforward : PENFORWARD LPAREN exp RPAREN SEMICOLON'''
    quadList.add_quad(Functions.PENFORWARD, p[3], None, None)

def p_penback(p):
    '''penback : PENBACK LPAREN exp RPAREN SEMICOLON'''
    quadList.add_quad(Functions.PENBACK, p[3], None, None)

def p_penon(p):
    '''penon : PENON LPAREN RPAREN SEMICOLON'''
    quadList.add_quad(Functions.PENON, None, None, None)

def p_penoff(p):
    '''penoff : PENOFF LPAREN RPAREN SEMICOLON'''
    quadList.add_quad(Functions.PENOFF, None, None, None)

def p_type(p):
    '''type : INT
			| FLOAT
			| STRING
			| BOOL'''
    if p[1] == 'Int':
        p[0] = Type.INT.value
    elif p[1] == 'Float':
        p[0] = Type.FLOAT.value
    elif p[1] == 'String':
        p[0] = Type.STRING.value
    elif p[1] == 'Bool':
        p[0] = Type.BOOL.value

def p_var_cte(p):
    '''var_cte : ID getidvalue
				| CTE_INT getvalue_i
				| CTE_FLOAT getvalue_f
				| cte_bool getvalue_b
				| ID list getarrayvalue
				| call getcallvalue'''
    print("var_cte")
    if len(p) > 3:
        p[0] = p[3]
    else:
        p[0] = p[2]

def p_getidvalue(p):
    '''getidvalue : '''
    id = p[-1]
    var = varTable.find_variable(id)
    p[0] = var.value

def p_getvalue_i(p):
    '''getvalue_i : '''
    p[0] = memory.putConsInMemory(Type.INT.value, p[-1])
    pTypes.push(Type.INT.value)

def p_getvalue_f(p):
    '''getvalue_f : '''
    p[0] = memory.putConsInMemory(Type.FLOAT.value, p[-1])
    pTypes.push(Type.FLOAT.value)

def p_getvalue_b(p):
    '''getvalue_b : '''
    p[0] = memory.putConsInMemory(Type.BOOL.value, p[-1])
    pTypes.push(Type.BOOL.value)

def p_getarrayvalue(p):
    '''getarrayvalue : '''
    #TODO:
    #get value of an array

def p_getcallvalue(p):
    '''getcallvalue : '''
    #TODO:
    #obtener el valor desde una llamada

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
    exp_type = pTypes.pop()
    if exp_type != bool:
        ErrorHandler.type_error()
    else:
        result = pilaOperandos.pop()
        q = Quad(Operations.GOTOF, None, None, result)
        quadList.add_quad(q)
        pJumps.push(quadList.index)

def p_gotoElse(p):
    '''gotoElse :'''
    q = Quad(Operations.GOTO, None, None, None)
    quadList.add_quad(q)
    false = pJumps.pop()
    pJumps.push(quadList.index)
    quadList.fill(quadList.index, false)

def p_end_if(p):
    '''end_if :'''
    end = pJumps.pop()
    quadList.fill(quadList.index, end)

def p_expression(p):
    '''expression : exp expression1'''
    p[0] = p[1]
    print("expression")

def p_expression1(p):
    '''expression1 : LESSER relop exp top_relop
	| GREATER relop exp top_relop
	| EQUAL relop exp top_relop
	| NOTEQUAL relop exp top_relop
	| GREATEROREQUAL relop exp top_relop
    | LESSEROREQUAL relop exp top_relop
    | empty'''
    print("expression1")

def p_relop(p):
    '''relop :'''
    op = p[-1]
    if op == '<':
        pilaOperadores.push(Operations.LESSER)
    if op == '>':
        pilaOperadores.push(Operations.GREATER)
    if op == '<=':
        pilaOperadores.push(Operations.LESSEROREQUAL)
    if op == '==':
        pilaOperadores.push(Operations.EQUAL)
    if op == '>=':
        pilaOperadores.push(Operations.GREATEROREQUAL)
    if op == '!=':
        pilaOperadores.push(Operations.NOTEQUAL)
    print("relop")

def p_top_relop(p):
    '''top_relop :'''
    operator = pilaOperadores.pop()
    if operator == Operations.LESSER or operator == Operations.GREATER or operator == Operations.LESSEROREQUAL or operator == Operations.EQUAL or operator == Operations.GREATEROREQUAL or operator == Operations.NOTEQUAL:
        r_operand = pilaOperandos.pop()
        r_type = pTypes.pop()
        l_operand = pilaOperandos.pop()
        l_type = pTypes.pop()
        result_type = cube.getType(l_type, r_type, operator)
        if result_type != Type.ERROR.value:
            result = memory.putVarInMemory(-1, Type.BOOL.value, 1, None)
            q = Quad(operator, l_operand, r_operand, result)
            quadList.add_quad(q)
            pilaOperandos.push(result)
            pTypes.push(result_type)
        else:
            ErrorHandler.print(p.lineno(-1))
    else:
        pilaOperadores.push(operator)
    print("top relop")


def p_exp(p):
    '''exp : term top_exp exp1'''
    p[0] = p[1]
    print("exp")

def p_exp1(p):
    '''exp1 : MINUS push_sign exp
	| PLUS push_sign exp
	| empty'''
    print("exp1")

def p_top_exp(p):
    '''top_exp : '''
    operator = pilaOperadores.top()
    if operator == Operations.PLUS.value or operator == Operations.MINUS.value:
        r_operand = pilaOperandos.pop()
        r_type = pTypes.pop()
        l_operand = pilaOperandos.pop()
        l_type = pTypes.pop()
        result_type = cube.getType(l_type, r_type, operator)
        if result_type != Type.ERROR.value:
            result = memory.putVarInMemory(-1, result_type, 1, None)
            q = Quad(operator, l_operand, r_operand, result)
            quadList.add_quad(q)
            pilaOperandos.push(result)
            pTypes.push(result_type)
        else:
            ErrorHandler.print(p.lineno(-1))
    else:
        pilaOperadores.push(operator)
    print("top exp")

def p_push_sign(p):
    '''push_sign :'''
    if not p[-1] is None:
        sign = p[-1]
    if sign is "/":
        pilaOperadores.push(Operations.DIVIDE.value)
    if sign is "*":
        pilaOperadores.push(Operations.TIMES.value)
    if sign is "+":
        pilaOperadores.push(Operations.PLUS.value)
    if sign is "-":
        pilaOperadores.push(Operations.MINUS.value)
    print("top exp")

def p_top_factor(p):
    '''top_factor :'''
    operator = pilaOperadores.top()
    if operator == Operations.TIMES.value or operator == Operations.DIVIDE.value:
        r_operand = pilaOperandos.pop()
        r_type = pTypes.pop()
        l_operand = pilaOperandos.pop()
        l_type = pTypes.pop()
        result_type = cube.getType(l_type, r_type, operator)
        if result_type != Type.ERROR.value:
            # calcular resultado
            result = memory.putVarInMemory(-1, result_type, 1, None)
            q = Quad(operator, l_operand, r_operand, result)
            quadList.add_quad(q)
            pilaOperandos.push(result)
            pTypes.push(result_type)
        else:
            ErrorHandler.print(p.lineno(-1))
    # raise ErrorHandler CHECAR***********CHECAR***********CHECAR***********CHECAR
    else:
        pilaOperadores.push(operator)
    print("top factor")

def p_factor(p):
    '''factor : LPAREN false_bottom expression RPAREN end_par
	| var_cte push_cte
	| ID push_id'''
    if len(p) > 3:
        p[0] = p[3]
    else:
        p[0] = p[1]

def p_false_bottom(p):
    '''false_bottom :'''
    if p[-1] is "(":
        pilaOperadores.push(Operations.LPAREN)
    print("false bottom")

def p_end_par(p):
    '''end_par :'''
    if p[-1] is ")":
        pilaOperadores.pop()
    print("end par")

def p_push_cte(p):
    '''push_cte : '''
    pilaOperandos.push(p[-1])

def p_push_id(p):
    '''push_id : '''
    try:
        var = VariablesTable.find_variable(p[-1])
        pilaOperandos.push(var.value)
        pTypes.push(var.var_type)
    except ErrorHandler as error:
        error.type_error()
        raise error
    print("push id")

def p_term(p):
    '''term : factor top_factor term1'''

def p_term1(p):
    '''term1 : DIVIDE push_sign term
		| TIMES push_sign term
		| empty'''
    if len(p) > 2:



def p_call(p):
    '''call : ID check_name LPAREN create_era call1 RPAREN SEMICOLON gosub'''

def p_check_name(p):
    '''check_name : '''
    try:
        f = VariablesTable.find_function(p[-1])
        quadList.add_quad(Operations.ERA, f, None, None)
    except ErrorHandler as error:
        error.print(p.lineno(0))

def p_create_era(p):
        '''create_era : '''

def p_gosub(p):
    '''gosub : '''

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
