from turtle import *
from stack import Stack
from quads import Quads

# Crear memoria de ejecución
execMemory = Stack()
instruction_pointer = 0

# Subir a memoria lista de cúadruplos, direccion de funciones y tablas de constantes

# Operaciones del switch
def PLUS(op1, op2):
	op1_dir = cuad[instruction_pointer].rigth_operand
	op1 = Memory[left_operand_dir - Base(type)]
	op2_dir = cuad[instruction_pointer].left_operand
	op2 = Memory[rigth_operand_dir - Base(type)]
	aux = op1 + op2
	Memory[f(cuad[instruction_pointer].result)] = aux

def MINUS(op1, op2):
	op1_dir = cuad[instruction_pointer].rigth_operand
	op1 = Memory[left_operand_dir - Base(type)]
	op2_dir = cuad[instruction_pointer].left_operand
	op2 = Memory[rigth_operand_dir - Base(type)]
	aux = op1 - op2
	Memory[f(cuad[instruction_pointer].result)] = aux

def TIMES(op1, op2):
	op1_dir = cuad[instruction_pointer].rigth_operand
	op1 = Memory[left_operand_dir - Base(type)]
	op2_dir = cuad[instruction_pointer].left_operand
	op2 = Memory[rigth_operand_dir - Base(type)]
	aux = op1 * op2
	Memory[f(cuad[instruction_pointer].result)] = aux

def DIVIDE(op1, op2):
	op1_dir = cuad[instruction_pointer].rigth_operand
	op1 = Memory[left_operand_dir - Base(type)]
	op2_dir = cuad[instruction_pointer].left_operand
	op2 = Memory[rigth_operand_dir - Base(type)]
	aux = op1 / op2
	Memory[f(cuad[instruction_pointer].result)] = aux

def EQUAL(op1, op2):
	op1_dir = cuad[instruction_pointer].rigth_operand
	op1 = Memory[left_operand_dir - Base(type)]
	op2_dir = cuad[instruction_pointer].left_operand
	op2 = Memory[rigth_operand_dir - Base(type)]
	aux = op1 = op2
	Memory[f(cuad[instruction_pointer].result)] = aux

def NOTEQUAL(op1, op2):
	op1_dir = cuad[instruction_pointer].rigth_operand
	op1 = Memory[left_operand_dir - Base(type)]
	op2_dir = cuad[instruction_pointer].left_operand
	op2 = Memory[rigth_operand_dir - Base(type)]
	aux = op1 != op2
	Memory[f(cuad[instruction_pointer].result)] = aux

def GREATER(op1, op2):
	op1_dir = cuad[instruction_pointer].rigth_operand
	op1 = Memory[left_operand_dir - Base(type)]
	op2_dir = cuad[instruction_pointer].left_operand
	op2 = Memory[rigth_operand_dir - Base(type)]
	aux = op1 > op2
	Memory[f(cuad[instruction_pointer].result)] = aux

def LESSER(op1, op2):
	op1_dir = cuad[instruction_pointer].rigth_operand
	op1 = Memory[left_operand_dir - Base(type)]
	op2_dir = cuad[instruction_pointer].left_operand
	op2 = Memory[rigth_operand_dir - Base(type)]
	aux = op1 < op2
	Memory[f(cuad[instruction_pointer].result)] = aux

def GREATEROREQUAL(op1, op2):
	op1_dir = cuad[instruction_pointer].rigth_operand
	op1 = Memory[left_operand_dir - Base(type)]
	op2_dir = cuad[instruction_pointer].left_operand
	op2 = Memory[rigth_operand_dir - Base(type)]
	aux = op1 >= op2
	Memory[f(cuad[instruction_pointer].result)] = aux

def LESSEROREQUAL(op1, op2):
	op1_dir = cuad[instruction_pointer].rigth_operand
	op1 = Memory[left_operand_dir - Base(type)]
	op2_dir = cuad[instruction_pointer].left_operand
	op2 = Memory[rigth_operand_dir - Base(type)]
	aux = op1 <= op2
	Memory[f(cuad[instruction_pointer].result)] = aux

def AND(op1, op2):
	op1_dir = cuad[instruction_pointer].rigth_operand
	op1 = Memory[left_operand_dir - Base(type)]
	op2_dir = cuad[instruction_pointer].left_operand
	op2 = Memory[rigth_operand_dir - Base(type)]
	aux = op1 and op2
	Memory[f(cuad[instruction_pointer].result)] = aux

def OR(op1, op2):
	op1_dir = cuad[instruction_pointer].rigth_operand
	op1 = Memory[left_operand_dir - Base(type)]
	op2_dir = cuad[instruction_pointer].left_operand
	op2 = Memory[rigth_operand_dir - Base(type)]
	aux = op1 or op2
	Memory[f(cuad[instruction_pointer].result)] = aux

def NOT(op1):
	op1_dir = cuad[instruction_pointer].rigth_operand
	op1 = Memory[left_operand_dir - Base(type)]
	aux = not op1
	Memory[f(cuad[instruction_pointer].result)] = aux

def GOTO():
	instruction_pointer = cuad[instruction_pointer].result

def GOTOF():
	instruction_pointer = cuad[instruction_pointer].result

def COLOR(color):
	turtle.pencolor(color)

def CIRCLE(raidus):
	turtle.circle(radius, None, None)

def SQUARE():
	turtle.pendown()
	turtle.forward(100)
	turtle.tilt(90)
	turtle.forward(100)
	turtle.tilt(90)
	turtle.forward(100)
	turtle.tilt(90)
	turtle.forward(100)
	turtle.tilt(90)

def TRIANGLE():


def RECTANGLE():


def POLIGON():


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


# Switch
def opCode(arg):
	switch = {
	1: PLUS,
	2: MINUS,
	3: TIMES,
	4: DIVIDE,
	5: ASSIGN,
	6: EQUAL,
	7: NOTEQUAL,
	8: GREATER,
	9: LESSER,
	10: GREATEROREQUAL,
	11: LESSEROREQUAL,
	12: AND,
	13: OR,
	14: NOT,
	15: GOTO,
	16: GOTOF,
	17: COLOR,
	18: CIRCLE,
	19: SQUARE,
	20: TRIANGLE,
	21: RECTANGLE,
	22: POLIGON,
	23: ROTATE,
	24: PENSIZE,
	25: PENFORWARD,
	26: PENBACK,
	27: PENON,
	28: PENOFF
	}

# for testing
# Get the function from switcher dictionary
    func = switch.get(arg, lambda: "Invalid operation")

# Execute the function
    print func()
