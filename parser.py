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
from virtualMachine import *

varTable = VariablesTable()

param_index = 0
varList = []  # Array to save the ID of variables in the same line
funcList = []

quadList = Quads()
pilaOperandos = Stack()
pilaOperadores = Stack()
pTypes = Stack()
pJumps = Stack()

funcTable = {}
variableTable = {}


vartype = None
functype = None
func_calling = None
listsize = 1
cube = SemanticCube()
DaVinci = Function('DaVinci', 'void', -1)
funcTable['DaVinci'] = DaVinci
currentFunc = funcTable['DaVinci']
memory = currentFunc.memory

def p_program(p):
    '''program : PROGRAM ID SEMICOLON gotomain program1 getglobalmemory DAVINCI fillmain block'''
    quadList.print_Quads()
    #varTable.printVars()
    #print(funcTable)
    vm = VirtualMachine()
    vm.funcTable = funcTable
    for func in funcTable:
        f = funcTable[func]
        vm.memory[f.function_id] = f.memory.memory

    f = open('quads.txt','w') #archivo de texto en donde se guardan los cuádruplos
    for i in range(len(quadList.array)):
        f.write(str(quadList.array[i])) #escribir en el archivo el cuádruplo
        if i < len(quadList.array)-1:
            f.write('\n')
    f.close() # Cerrar el archivo de texto

    vm.run()

def p_fillmain(p):
    '''fillmain : '''
    quadList.fill(0, quadList.index)

def p_gotomain(p):
    '''gotomain : '''
    q = Quad(Operations.GOTO.value, None, None, None)
    quadList.add_quad(q)

def p_program1(p):
    '''program1 : program1 funcs save_funcs
	| program1 vars global_vars
	| empty'''

def p_getglobalmemory(p):
    '''getglobalmemory : '''
    global currentFunc, memory
    currentFunc = funcTable['DaVinci']
    memory = currentFunc.memory

def p_save_funcs(p):
    '''save_funcs : '''

def p_global_vars(p):
    '''global_vars : '''
    try:
        for var in varList:
            if not var.var_id in currentFunc.varTable:
                dir = funcTable['DaVinci'].declareVariable(var.var_id,var.var_type)
        varList.clear()
    except ErrorHandler as e:
        e.redefined_variable('Variable duplicada')
        ErrorHandler.exitWhenError()

def p_block(p):
    '''block : LBRACE b1 RBRACE'''

def p_b1(p):
    '''b1 : vars local_vars b2
	| b2'''

def p_local_vars(p):
    '''local_vars : '''
    try:
        for var in varList:
            if not var.var_id in currentFunc.varTable or not var.var_id in funcTable['DaVinci'].varTable:
                currentFunc.declareVariable(var.var_id,var.var_type)
        varList.clear()
    except ErrorHandler as e:
        e.redefined_variable('Variable duplicada')
        ErrorHandler.exitWhenError()

def p_b2(p):
    '''b2 : b2 statute
	| empty'''

def p_vars(p):
    '''vars : VAR vars2'''

def p_vars2(p):
    '''vars2 : type save_type vars3 SEMICOLON vars2
	| empty'''

def p_vars3(p):
    '''vars3 : ID list savelist vars4
	| ID saveid vars4'''

def p_vars4(p):
    '''vars4 : COMMA vars3
	| empty'''

def p_savelist(p):
    '''savelist : '''
    v = Variable(p[-2], vartype, p[-1])
    varList.append(v)

def p_saveid(p):
    '''saveid : '''
    v = Variable(p[-1], vartype, 1)
    varList.append(v)

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
	 | penon
	 | penoff
	 | print'''

def p_while(p):
    '''while : WHILE while_return LPAREN expression RPAREN type_check block end_while'''

def p_while_return(p):
    '''while_return :'''
    pJumps.push(quadList.index)

def p_end_while(p):
    '''end_while :'''
    end = pJumps.pop()
    ret = pJumps.pop()
    quadList.add_quad(Quad(Operations.GOTO.value, None, None, ret))
    quadList.fill(end, quadList.index)

def p_assignment(p):
    '''assignment : ID verify_id ASSIGN push_sign expression set_value SEMICOLON
	 | ID cte_id LBRACKET exp RBRACKET ASSIGN expression SEMICOLON'''

def p_verify_id(p):
    '''verify_id : '''
    id = p[-1]
    try:
        var = currentFunc.varTable[id]
        pilaOperandos.push(var)
        pTypes.push(currentFunc.memory.getType(var))
    except ValueError:
        print ("Variable not found")
        ErrorHandler.exitWhenError()

def p_set_value(p):
    '''set_value : '''
    operator = pilaOperadores.top()
    if operator == Operations.ASSIGN.value:
        operator = pilaOperadores.pop()
        result_operand = pilaOperandos.pop()
        result_type = pTypes.pop()
        id_operand = pilaOperandos.pop()
        id_type = pTypes.pop()
        if result_type == id_type:
            q = Quad(operator, result_operand, None, id_operand)
            quadList.add_quad(q)
        else:
            print('Tipos no compatibles')
            ErrorHandler.exitWhenError()

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
        pilaOperandos.push(Color.RED.value)
    if p[1] == 'blue':
        pilaOperandos.push(Color.BLUE.value)
    if p[1] == 'yellow':
        pilaOperandos.push(Color.YELLOW.value)
    if p[1] == 'pink':
        pilaOperandos.push(Color.PINK.value)
    if p[1] == 'purple':
        pilaOperandos.push(Color.PURPLE.value)

def p_st_cte(p):
    '''st_cte : STRING
		| cte_bool'''

def p_funcs(p):
    '''funcs : FUNC type functype ID saveidfunc LPAREN params RPAREN funcvars LBRACE statements return RBRACE end_func funcs3
	        | FUNC VOID functype ID saveidfunc LPAREN params RPAREN funcvars LBRACE statements RBRACE end_func funcs3 '''

def p_functype(p):
    '''functype : '''
    global functype
    functype = p[-1]

def p_params(p):
    '''params : type ID save_par params1
                | empty'''
    currentFunc.starting_instruction = quadList.index

def p_params1(p):
    '''params1 : COMMA type ID save_par params1
                | empty'''

def p_funcs1(p):
    '''funcs1 : funcs1 COMMA type save_type ID save_par
	| empty'''

def p_statements(p):
    '''statements : statements statute
	| empty '''

def p_test(p):
    '''test : '''
    print(p[-1])

def p_funcs3(p):
    '''funcs3 : funcs
	| empty'''

def p_funcvars(p):
    '''funcvars : vars local_vars
    | empty'''

def p_saveidfunc(p):
    '''saveidfunc : '''
    global currentFunc, memory
    id = p[-1]
    f = Function(id, functype, -1)
    currentFunc = f
    funcTable[currentFunc.function_id] = currentFunc
    memory = currentFunc.memory

def p_end_func(p):
    '''end_func : '''
    #funcTable[currentFunc.function_id] = currentFunc
    q = Quad(Operations.ENDPROC.value,None, None, None)
    quadList.add_quad(q)

def p_save_par(p):
    '''save_par : '''
    global currentFunc
    v = Variable(p[-1], p[-2], 1)
    dir = currentFunc.declareVariable(v.var_id, v.var_type)
    currentFunc.memory.setValue(dir, 'TAKEN')
    currentFunc.parameters.append(dir)

def p_color(p):
    '''color : COLOR LPAREN color_cte RPAREN SEMICOLON'''
    quadList.add_quad(Quad(Functions.COLOR.value, pilaOperandos.pop(), None, None))

def p_circle(p):
    '''circle : CIRCLE LPAREN exp RPAREN SEMICOLON'''
    quadList.add_quad(Quad(Functions.CIRCLE.value, pilaOperandos.pop(), None, None))

def p_square(p):
    '''square : SQUARE LPAREN exp RPAREN SEMICOLON'''
    quadList.add_quad(Quad(Functions.SQUARE.value, pilaOperandos.pop(), None, None))

def p_triangle(p):
    '''triangle : TRIANGLE LPAREN exp COMMA exp RPAREN SEMICOLON'''
    quadList.add_quad(Quad(Functions.TRIANGLE.value, pilaOperandos.pop(), pilaOperandos.pop(), None))

def p_rectangle(p):
    '''rectangle : RECTANGLE LPAREN exp COMMA exp RPAREN SEMICOLON'''
    quadList.add_quad(Quad(Functions.RECTANGLE.value, pilaOperandos.pop(), pilaOperandos.pop(), None))

def p_poligon(p):
    '''poligon : POLIGON LPAREN exp COMMA exp RPAREN SEMICOLON'''
    quadList.add_quad(Quad(Functions.POLIGON.value, pilaOperandos.pop(), pilaOperandos.pop(), None))

def p_rotate(p):
    '''rotate : ROTATE LPAREN exp RPAREN SEMICOLON
	| ROTATE LPAREN CTE_STRING RPAREN SEMICOLON'''
    quadList.add_quad(Quad(Functions.ROTATE.value, pilaOperandos.pop(), None, None))

def p_pensize(p):
    '''pensize : PENSIZE LPAREN exp RPAREN SEMICOLON'''
    quadList.add_quad(Quad(Functions.PENSIZE.value, pilaOperandos.pop(), None, None))

def p_penforward(p):
    '''penforward : PENFORWARD LPAREN exp RPAREN SEMICOLON'''
    val = pilaOperandos.pop()
    q = Quad(Functions.PENFORWARD.value, val, None, None)
    quadList.add_quad(q)

def p_penback(p):
    '''penback : PENBACK LPAREN exp RPAREN SEMICOLON'''
    quadList.add_quad(Quad(Functions.PENBACK.value, pilaOperandos.pop(), None, None))

def p_penon(p):
    '''penon : PENON LPAREN RPAREN SEMICOLON'''
    quadList.add_quad(Quad(Functions.PENON.value, None, None, None))

def p_penoff(p):
    '''penoff : PENOFF LPAREN RPAREN SEMICOLON'''
    quadList.add_quad(Quad(Functions.PENOFF.value, None, None, None))

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

def p_getarrayvalue(p):
    '''getarrayvalue : '''
    #TODO:
    #get value of an array

def p_getcallvalue(p):
    '''getcallvalue : '''
    #TODO:
    #obtener el valor desde una llamada
    global func_calling
    dir = memory.pushVarInMemory(func_calling.function_type, 1)
    pTypes.push(func_calling.function_type)
    pilaOperandos.push(dir)
    memory.setValue(dir, 'TAKEN')
    q = Quad(Functions.SAVERETURN.value, None, None, dir)
    quadList.add_quad(q)

def p_cte_bool(p):
    '''cte_bool : TRUE
	| FALSE'''
    if p[1] == 'true':
        p[0] = Values.TRUE
        return p[0]
    elif p[1] == 'false':
        p[0] = Values.FALSE
        return p[0]

def p_condition(p):
    '''condition : IF LPAREN expression RPAREN type_check LBRACE b2 RBRACE condition1 end_if'''

def p_condition1(p):
    '''condition1 : gotoElse ELSE LBRACE b2 RBRACE
	| empty'''

def p_type_check(p):
    '''type_check :'''
    exp_type = pTypes.pop()
    if exp_type != Type.BOOL.value:
        print('Error: Variable no booleana')
        ErrorHandler.exitWhenError()
    else:
        result = pilaOperandos.pop()
        q = Quad(Operations.GOTOF.value, result, None, None)
        quadList.add_quad(q)
        pJumps.push(quadList.index-1)

def p_gotoElse(p):
    '''gotoElse :'''
    q = Quad(Operations.GOTO.value, None, None, None)
    quadList.add_quad(q)
    false = pJumps.pop()
    pJumps.push(quadList.index-1)
    quadList.fill(false, quadList.index)

def p_end_if(p):
    '''end_if :'''
    end = pJumps.pop()
    quadList.fill(end, quadList.index)

def p_expression(p):
    '''expression : exp expression1'''
    p[0] = p[1]
    return p[0]

def p_expression1(p):
    '''expression1 : LESSER relop exp top_relop
	| GREATER relop exp top_relop
	| EQUAL relop exp top_relop
	| NOTEQUAL relop exp top_relop
	| GREATEROREQUAL relop exp top_relop
    | LESSEROREQUAL relop exp top_relop
    | empty'''

def p_exp(p):
    '''exp : term top_exp exp1'''
    p[0] = p[1]

def p_exp1(p):
    '''exp1 : MINUS push_sign exp
	| PLUS push_sign exp
	| empty'''

def p_top_exp(p):
    '''top_exp : '''
    operator = pilaOperadores.top()
    if operator == Operations.PLUS.value or operator == Operations.MINUS.value:
        operator = pilaOperadores.pop()
        r_operand = pilaOperandos.pop()
        r_type = pTypes.pop()
        l_operand = pilaOperandos.pop()
        l_type = pTypes.pop()
        result_type = cube.getType(l_type, r_type, operator)
        if result_type != Type.ERROR.value:
            result = memory.pushVarInMemory(result_type, 1)
            q = Quad(operator, l_operand, r_operand, result)
            quadList.add_quad(q)
            pilaOperandos.push(result)
            pTypes.push(result_type)
        else:
            ErrorHandler.print(p.lineno(-1))

def p_term(p):
    '''term : factor top_factor term1'''
    return p[1]

def p_term1(p):
    '''term1 : DIVIDE push_sign term
		| TIMES push_sign term
		| empty'''

def p_factor(p):
    '''factor : LPAREN false_bottom expression RPAREN end_par
	| var_cte
	| ID push_id'''
    if len(p) > 3:
        p[0] = p[3]
    else:
        p[0] = p[1]
    return p[0]

def p_top_factor(p):
    '''top_factor :'''
    operator = pilaOperadores.top()
    if operator == Operations.TIMES.value or operator == Operations.DIVIDE.value:
        operator = pilaOperadores.pop()
        r_operand = pilaOperandos.pop()
        r_type = pTypes.pop()
        l_operand = pilaOperandos.pop()
        l_type = pTypes.pop()
        result_type = cube.getType(l_type, r_type, operator)
        if result_type != Type.ERROR.value:
            # calcular resultado
            result = memory.pushVarInMemory(result_type, 1)
            q = Quad(operator, l_operand, r_operand, result)
            quadList.add_quad(q)
            pilaOperandos.push(result)
            pTypes.push(result_type)
        else:
            ErrorHandler.print(p.lineno(-1))

def p_var_cte(p):
    '''var_cte : ID getidvalue
				| CTE_INT getvalue_i
				| CTE_FLOAT getvalue_f
				| cte_bool getvalue_b
				| ID list getarrayvalue
				| call getcallvalue'''
    if len(p) > 3:
        p[0] = p[3]
    else:
        p[0] = p[2]
    return p[0]

def p_getidvalue(p):
    '''getidvalue : '''
    id = p[-1]
    global currentFunc
    try:
        print(currentFunc.varTable)
        var = currentFunc.varTable[id]
        pTypes.push(memory.getType(var))
        pilaOperandos.push(var)
    except:
        print('Variable no definida', id)
        ErrorHandler.exitWhenError()
    return p[0]

def p_getvalue_i(p):
    '''getvalue_i : '''
    dir = memory.pushVarInMemory(Type.INT.value, 1)
    pTypes.push(Type.INT.value)
    pilaOperandos.push(dir)
    memory.setValue(dir, p[-1])

def p_getvalue_f(p):
    '''getvalue_f : '''
    dir = memory.pushVarInMemory(Type.FLOAT.value, 1)
    pTypes.push(Type.FLOAT.value)
    pilaOperandos.push(dir)
    memory.setValue(dir, p[-1])

def p_getvalue_b(p):
    '''getvalue_b : '''
    p[0] = memory.pushVarInMemory(Type.BOOL.value, 1)
    pTypes.push(Type.BOOL.value)
    pilaOperandos.push(p[0])
    memory.setValue(dir, p[-1])

def p_relop(p):
    '''relop : '''
    op = p[-1]
    if op == '<':
        pilaOperadores.push(Operations.LESSER.value)
    if op == '>':
        pilaOperadores.push(Operations.GREATER.value)
    if op == '<=':
        pilaOperadores.push(Operations.LESSEROREQUAL.value)
    if op == '==':
        pilaOperadores.push(Operations.EQUAL.value)
    if op == '>=':
        pilaOperadores.push(Operations.GREATEROREQUAL.value)
    if op == '!=':
        pilaOperadores.push(Operations.NOTEQUAL.value)

def p_top_relop(p):
    '''top_relop :'''
    operator = pilaOperadores.top()
    if operator == Operations.LESSER.value or operator == Operations.GREATER.value or operator == Operations.LESSEROREQUAL.value or operator == Operations.EQUAL.value or operator == Operations.GREATEROREQUAL.value or operator == Operations.NOTEQUAL.value:
        operator = pilaOperadores.pop()
        r_operand = pilaOperandos.pop()
        r_type = pTypes.pop()
        l_operand = pilaOperandos.pop()
        l_type = pTypes.pop()
        result_type = cube.getType(l_type, r_type, operator)
        if result_type != Type.ERROR.value:
            result = memory.pushVarInMemory(Type.BOOL.value, 1)
            q = Quad(operator, l_operand, r_operand, result)
            quadList.add_quad(q)
            pilaOperandos.push(result)
            pTypes.push(result_type)
        else:
            ErrorHandler.print(p.lineno(-1))

def p_push_sign(p):
    '''push_sign :'''
    if not p[-1] is None:
        sign = p[-1]
    if sign is "/":
        pilaOperadores.push(Operations.DIVIDE.value)
    elif sign is "*":
        pilaOperadores.push(Operations.TIMES.value)
    elif sign is "+":
        pilaOperadores.push(Operations.PLUS.value)
    elif sign is "-":
        pilaOperadores.push(Operations.MINUS.value)
    elif sign is "=":
        pilaOperadores.push(Operations.ASSIGN.value)

def p_false_bottom(p):
    '''false_bottom :'''
    if p[-1] is "(":
        pilaOperadores.push(Operations.LPAREN.value)

def p_end_par(p):
    '''end_par :'''
    if p[-1] is ")":
        pilaOperadores.pop()

def p_push_id(p):
    '''push_id : '''
    id = p[-1]
    try:
        var = currentFunc.varTable[id]
        pilaOperandos.push(var)
        pTypes.push(currentFunc.memory.getType(var))
    except:
        print("ID no encontrado", p[-1])
        ErrorHandler.exitWhenError()

def p_call(p):
    '''call : ID check_name LPAREN create_era call1 RPAREN check_params SEMICOLON gosub checkreturn'''

def p_checkreturn(p):
    '''checkreturn : '''
    #if func_calling.function_type == Type.INT.value or func_calling.function_type == Type.FLOAT.value or func_calling.function_type == Type.BOOL.value or func_calling.function_type == Type.STRING.value:
        #q = Quad(Operations.ASSIGN.value, )

def p_check_name(p):
    '''check_name : '''
    id = p[-1]
    try:
        global func_calling
        f = funcTable[id]
        func_calling = f
    except ErrorHandler as error:
        print('Funcion no declarada: ', id)
        error.exitWhenError()

def p_create_era(p):
     '''create_era : '''
     q = Quad(Operations.ERA.value, func_calling.memory.getSize(), None, func_calling.function_id)
     quadList.add_quad(q)

def p_gosub(p):
    '''gosub : '''
    q = Quad(Operations.GOSUB.value, func_calling.function_id, None, func_calling.starting_instruction)
    quadList.add_quad(q)

def p_call1(p):
    '''call1 : expression argument call2
	| call2'''

def p_call2(p):
    '''call2 : COMMA expression argument call2
	| empty'''

def p_argument(p):
    '''argument : '''
    global param_index
    argument = pilaOperandos.pop()
    argType = pTypes.pop()
    if param_index <= len(func_calling.parameters):
        if argType == func_calling.memory.getType(func_calling.parameters[param_index]):
            q = Quad(Operations.PARAM.value, argument, None, param_index)
            quadList.add_quad(q)
            param_index += 1
        else:
            print('Parameter: ', param_index + 1)
            print('Type mismatch on:', func_calling.function_id)
            ErrorHandler.exitWhenError()
    else:
        print('No coincide numero de parametros:', 'Esperados: ', len(func_calling.parameters), 'Recibidos: ',param_index )
        ErrorHandler.exitWhenError()

def p_check_params(p):
    '''check_params : '''
    global param_index
    if len(func_calling.parameters) == param_index:
        param_index = 0
    else:
        print('No coincide numero de parametros: ', 'Esperados:', len(func_calling.parameters), 'Recibidos:',param_index )
        ErrorHandler.exitWhenError()

def p_print(p):
    '''print : PRINT LPAREN expression to_screen print_multi RPAREN SEMICOLON'''

def p_print_multi(p):
    '''print_multi : COMMA expression to_screen print_multi
                    | empty'''

def p_to_screen(p):
    '''to_screen : '''
    val = pilaOperandos.pop()
    q = Quad(Functions.PRINT.value, None, None, val)
    quadList.add_quad(q)

def p_return(p):
    '''return : RETURN expression savereturn SEMICOLON'''

def p_savereturn(p):
    '''savereturn : '''
    f = currentFunc
    if f.function_type == pTypes.top():
        value = pilaOperandos.pop()
        q = Quad(Functions.RETURN.value, None, None, value)
        quadList.add_quad(q)
    else:
        print("Syntax error, returning a type different than the expected")
        ErrorHandler.exitWhenError()

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
            ErrorHandler.exitWhenError()
    else:
        print("No file to test found")
        ErrorHandler.exitWhenError()
