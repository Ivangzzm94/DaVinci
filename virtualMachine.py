from turtle import *
from stack import Stack
from quads import Quads

# Crear memoria de ejecución
execMemory = Stack()

# Apuntador al cuádruplo en ejecición
instruction_pointer = 0

# Subir a memoria lista de cúadruplos, direccion de funciones y tablas de constantes ????

# Correr máquina virtual (LEER LA LISTA DE CUADRUPLOS)
while instruction_pointer <= Quads.index:
	ReadQuad(Quads.array[instruction_pointer].operator, 
		Quads.array[instruction_pointer].left_operand , 
		Quads.array[instruction_pointer].right_operand, 
		Quads.array[instruction_pointer].result)
	instruction_pointer += 1


# Operaciones del switch
def PLUS(op1, op2):
	op1_dir = Quads[instruction_pointer].rigth_operand
	op1 = Memory[left_operand_dir - Base(type)]
	op2_dir = Quads[instruction_pointer].left_operand
	op2 = Memory[rigth_operand_dir - Base(type)]
	aux = op1 + op2
	Memory[f(Quads[instruction_pointer].result)] = aux

def MINUS(op1, op2):
	op1_dir = Quads[instruction_pointer].rigth_operand
	op1 = Memory[left_operand_dir - Base(type)]
	op2_dir = Quads[instruction_pointer].left_operand
	op2 = Memory[rigth_operand_dir - Base(type)]
	aux = op1 - op2
	Memory[f(Quads[instruction_pointer].result)] = aux

def TIMES(op1, op2):
	op1_dir = Quads[instruction_pointer].rigth_operand
	op1 = Memory[left_operand_dir - Base(type)]
	op2_dir = Quads[instruction_pointer].left_operand
	op2 = Memory[rigth_operand_dir - Base(type)]
	aux = op1 * op2
	Memory[f(Quads[instruction_pointer].result)] = aux

def DIVIDE(op1, op2):
	op1_dir = Quads[instruction_pointer].rigth_operand
	op1 = Memory[left_operand_dir - Base(type)]
	op2_dir = Quads[instruction_pointer].left_operand
	op2 = Memory[rigth_operand_dir - Base(type)]
	aux = op1 / op2
	Memory[f(Quads[instruction_pointer].result)] = aux

def EQUAL(op1, op2):
	op1_dir = Quads[instruction_pointer].rigth_operand
	op1 = Memory[left_operand_dir - Base(type)]
	op2_dir = Quads[instruction_pointer].left_operand
	op2 = Memory[rigth_operand_dir - Base(type)]
	aux = op1 = op2
	Memory[f(Quads[instruction_pointer].result)] = aux

def NOTEQUAL(op1, op2):
	op1_dir = Quads[instruction_pointer].rigth_operand
	op1 = Memory[left_operand_dir - Base(type)]
	op2_dir = Quads[instruction_pointer].left_operand
	op2 = Memory[rigth_operand_dir - Base(type)]
	aux = op1 != op2
	Memory[f(Quads[instruction_pointer].result)] = aux

def GREATER(op1, op2):
	op1_dir = Quads[instruction_pointer].rigth_operand
	op1 = Memory[left_operand_dir - Base(type)]
	op2_dir = Quads[instruction_pointer].left_operand
	op2 = Memory[rigth_operand_dir - Base(type)]
	aux = op1 > op2
	Memory[f(Quads[instruction_pointer].result)] = aux

def LESSER(op1, op2):
	op1_dir = Quads[instruction_pointer].rigth_operand
	op1 = Memory[left_operand_dir - Base(type)]
	op2_dir = Quads[instruction_pointer].left_operand
	op2 = Memory[rigth_operand_dir - Base(type)]
	aux = op1 < op2
	Memory[f(Quads[instruction_pointer].result)] = aux

def GREATEROREQUAL(op1, op2):
	op1_dir = Quads[instruction_pointer].rigth_operand
	op1 = Memory[left_operand_dir - Base(type)]
	op2_dir = Quads[instruction_pointer].left_operand
	op2 = Memory[rigth_operand_dir - Base(type)]
	aux = op1 >= op2
	Memory[f(Quads[instruction_pointer].result)] = aux

def LESSEROREQUAL(op1, op2):
	op1_dir = Quads[instruction_pointer].rigth_operand
	op1 = Memory[left_operand_dir - Base(type)]
	op2_dir = Quads[instruction_pointer].left_operand
	op2 = Memory[rigth_operand_dir - Base(type)]
	aux = op1 <= op2
	Memory[f(Quads[instruction_pointer].result)] = aux

def AND(op1, op2):
	op1_dir = Quads[instruction_pointer].rigth_operand
	op1 = Memory[left_operand_dir - Base(type)]
	op2_dir = Quads[instruction_pointer].left_operand
	op2 = Memory[rigth_operand_dir - Base(type)]
	aux = op1 and op2
	Memory[f(Quads[instruction_pointer].result)] = aux

def OR(op1, op2):
	op1_dir = Quads[instruction_pointer].rigth_operand
	op1 = Memory[left_operand_dir - Base(type)]
	op2_dir = Quads[instruction_pointer].left_operand
	op2 = Memory[rigth_operand_dir - Base(type)]
	aux = op1 or op2
	Memory[f(Quads[instruction_pointer].result)] = aux

def NOT(op1):
	op1_dir = Quads[instruction_pointer].rigth_operand
	op1 = Memory[left_operand_dir - Base(type)]
	aux = not op1
	Memory[f(Quads[instruction_pointer].result)] = aux

def GOTO(go):
	instruction_pointer = go

def GOTOF(go):
	instruction_pointer = go

def GOTOV(go):
	instruction_pointer = go

def ERA():
	turtle.pendown()

def GOSUB(fun):
	turtle.pendown()

def COLOR(color):
	turtle.pencolor(color)

def CIRCLE(raidus):
	turtle.circle(radius, None, None)

def SQUARE():
	turtle.pendown()
	for i in range(4):
		turtle.forward(80)
		turtle.left(90)

def TRIANGLE():
	turtle.pendown()
	for i in range(52):
		turtle.forward(100)
		turtle.left(175)
		turtle.forward(100)
		turtle.left(90)
		turtle.forward(10)
		turtle.left(90)
		turtle.right(2)

def RECTANGLE():
	turtle.pendown()
	turtle.forward(80)
	turtle.left(90)
	turtle.forward(40)
	turtle.left(90)
	turtle.forward(80)
	turtle.left(90)
	turtle.forward(40)

def POLIGON(sides, size):
	for i in range(1,sides):
		turtle.forward(size)
		turtle.left(360/sides)


def ROTATE(degree):
	turtle.tilt(degree)

def PENSIZE(size):
	turtle.dot(size)

def PENFORWARD(distance):
	turte.forward(distance)

def PENBACK(distance):
	turtle.backward(distance)

def PENON():
	turtle.pendown()

def PENOFF():
	turtle.penup()

def ReadQuad(operator, op1, op2, r):
	if operator == 1:
		PLUS(op1 , op2, r)
	elif operator == 2:
		MINUS(op1 , op2, r)
	elif operator == 3:
		TIMES(op1 , op2, r)
	elif operator == 4:
		DIVIDE(op1 , op2, r)
	elif operator == 5:
		ASSIGN(op1 , op2, r)
	elif operator == 6:
		EQUAL(op1 , op2, r)
	elif operator == 7:
		NOTEQUAL(op1 , op2, r)
	elif operator == 8:
		GREATER(op1 , op2, r)
	elif operator == 9:
		LESSER(op1 , op2, r)
	elif operator == 10:
		GREATEROREQUAL(op1 , op2, r)
	elif operator == 11:
		LESSEROREQUAL(op1 , op2, r)
	elif operator == 12:
		AND(op1 , op2, r)
	elif operator == 13:
		OR(op1 , op2, r)
	elif operator == 14:
		NOT(op1 , op2, r)
	elif operator == 15:
		GOTO(op1, op2, r)
	elif operator == 16:
		GOTOF(op1 , op2, r)
	elif operator == 17:
		GOTOV(op1 , op2, r)
	elif operator == 18:
		ERA(op1 , op2, r)
	elif operator == 19:
		GOSUB(op1 , op2, r)
	elif operator == 20:
		ENDPROC(op1 , op2, r)
	elif operator == 21:
		PARAM(op1 , op2, r)
	elif operator == 22:
		VER(op1 , op2, r)
	elif operator == 50:
		COLOR(op1 , op2, r)
	elif operator == 51:
		CIRCLE(op1 , op2, r)
	elif operator == 52:
		SQUARE(op1, op2, r)
	elif operator == 53:
		TRIANGLE(op1, op2, r)
	elif operator == 54:
		RECTANGLE(op1, op2, r)
	elif operator == 55:
		POLIGON(op1, op2, r)
	elif operator == 56:
		ROTATE(op1, op2, r)
	elif operator == 57:
		PENSIZE(op1, op2, r)
	elif operator == 58:
		PENFORWARD(op1, op2, r)
	elif operator == 59:
		PENBACK(op1, op2, r)
	elif operator == 60:
		PENON()
	elif operator == 61:
		PENOFF()
	else:
		print("Unknown operation code")
