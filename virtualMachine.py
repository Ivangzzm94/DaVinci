import turtle
from stack import Stack
from quads import Quads
from random import randint
#from parser import quadList

class VirtualMachine:

	def __init__(self):
		self.memory = {}
		self.instruction_pointer = 0
		self.list = None
	
	def run(self):
		# Lee lista de cúadruplos y meterlos a la lista "List"
		with open("quads.txt") as file:
			text = file.read()

		List = [l for l in [lines.split(", ") for lines in text.split("\n")]]

		# Convertir la lista de cuádruplos a enteros
		for x in range(len(List)):
			for y in range(4):
				if not List[x][y] == "None":
					List[x][y] = List[x][y]

		# Empezar la ejecución de la máquina virtual
		wn = turtle.Screen()
		while self.instruction_pointer < len(List):
			if List[self.instruction_pointer][0] == 15:					#GoTo
				self.instruction_pointer = List[self.instruction_pointer][3]
			else:
				self.ReadQuad(List[self.instruction_pointer][0], List[self.instruction_pointer][1], List[self.instruction_pointer][2], List[self.instruction_pointer][3])
				self.instruction_pointer += 1
		wn.exitonclick()


# Crear memoria de ejecución

# Apuntador al cuádruplo en ejecición

# Subir a memoria lista de cúadruplos, direccion de funciones y tablas de constantes ????

# IFSOTE
	def ReadQuad(self, operator, op1, op2, r):
		if operator == 1:
			self.PLUS(op1 , op2, r)
		elif operator == 2:
			self.MINUS(op1 , op2, r)
		elif operator == 3:
			self.TIMES(op1 , op2, r)
		elif operator == 4:
			self.DIVIDE(op1 , op2, r)
		elif operator == 5:
			self.ASSIGN(op1 , op2, r)
		elif operator == 6:
			self.EQUAL(op1 , op2, r)
		elif operator == 7:
			self.NOTEQUAL(op1 , op2, r)
		elif operator == 8:
			self.GREATER(op1 , op2, r)
		elif operator == 9:
			self.LESSER(op1 , op2, r)
		elif operator == 10:
			self.GREATEROREQUAL(op1 , op2, r)
		elif operator == 11:
			self.LESSEROREQUAL(op1 , op2, r)
		elif operator == 12:
			self.AND(op1 , op2, r)
		elif operator == 13:
			self.OR(op1 , op2, r)
		elif operator == 14:
			self.NOT(op1 , op2, r)
		elif operator == 18:
			self.ERA(op1 , op2, r)
		elif operator == 19:
			self.GOSUB(op1 , op2, r)
		elif operator == 20:
			self.ENDPROC(op1 , op2, r)
		elif operator == 21:
			self.PARAM(op1 , op2, r)
		elif operator == 22:
			self.VER(op1 , op2, r)
		elif operator == 50:
			self.COLOR(op1)
		elif operator == 51:
			self.CIRCLE(memory[op1])
		elif operator == 52:
			self.SQUARE(op1)
		elif operator == 53:
			self.TRIANGLE(op1, op2)
		elif operator == 54:
			self.RECTANGLE(op1, op2)
		elif operator == 55:
			self.POLIGON(op1, op2)
		elif operator == 56:
			self.ROTATE(op1)
		elif operator == 57:
			self.PENSIZE(op1)
		elif operator == 58:
			self.PENFORWARD(op1)
		elif operator == 59:
			self.PENBACK(op1)
		elif operator == 60:
			self.PENON()
		elif operator == 61:
			self.PENOFF()
		else:
			print("Unknown operation code")

	# Operaciones
	def PLUS(self, op1, op2):
		op1_dir = List[self.instruction_pointer][op1]
		op1 = Memory[op1_dir - Base(type)]
		op2_dir = quadList[self.instruction_pointer].right_operand
		op2 = Memory[op2_dir - Base(type)]
		aux = op1 + op2
		Memory[f(quadList[self.instruction_pointer].result)] = aux
		self.instruction_pointer += 1

	def MINUS(self, op1, op2):
		op1_dir = quadList[self.instruction_pointer].left_operand
		op1 = Memory[op1_dir - Base(type)]
		op2_dir = quadList[self.instruction_pointer].right_operand
		op2 = Memory[op2_dir - Base(type)]
		aux = op1 - op2
		Memory[f(quadList[self.instruction_pointer].result)] = aux

	def TIMES(self, op1, op2):
		op1_dir = quadList[self.instruction_pointer].left_operand
		op1 = Memory[op1_dir - Base(type)]
		op2_dir = quadList[self.instruction_pointer].right_operand
		op2 = Memory[op2_dir - Base(type)]
		aux = op1 * op2
		Memory[f(quadList[self.instruction_pointer].result)] = aux

	def DIVIDE(self, op1, op2):
		op1_dir = quadList[self.instruction_pointer].left_operand
		op1 = Memory[op1_dir - Base(type)]
		op2_dir = quadList[self.instruction_pointer].right_operand
		op2 = Memory[op2_dir - Base(type)]
		aux = op1 / op2
		Memory[f(quadList[self.instruction_pointer].result)] = aux

	def ASSIGN(self, op1, op2):
		op1_dir = quadList[self.instruction_pointer].left_operand
		op1 = Memory[op1_dir - Base(type)]
		op2_dir = quadList[self.instruction_pointer].right_operand
		op2 = Memory[op2_dir - Base(type)]
		op1 = op2
		Memory[f(quadList[self.instruction_pointer].result)] = op1

	def EQUAL(self, op1, op2):
		op1_dir = quadList[self.instruction_pointer].left_operand
		op1 = Memory[op1_dir - Base(type)]
		op2_dir = quadList[self.instruction_pointer].right_operand
		op2 = Memory[op2_dir - Base(type)]
		aux = op1 == op2
		Memory[f(quadList[self.instruction_pointer].result)] = aux

	def NOTEQUAL(self, op1, op2):
		op1_dir = quadList[self.instruction_pointer].left_operand
		op1 = Memory[op1_dir - Base(type)]
		op2_dir = quadList[self.instruction_pointer].right_operand
		op2 = Memory[op2_dir - Base(type)]
		aux = op1 != op2
		Memory[f(quadList[self.instruction_pointer].result)] = aux

	def GREATER(self, op1, op2):
		op1_dir = quadList[self.instruction_pointer].left_operand
		op1 = Memory[op1_dir - Base(type)]
		op2_dir = quadList[self.instruction_pointer].right_operand
		op2 = Memory[op2_dir - Base(type)]
		aux = op1 > op2
		Memory[f(quadList[self.instruction_pointer].result)] = aux

	def LESSER(self, op1, op2):
		op1_dir = quadList[self.instruction_pointer].left_operand
		op1 = Memory[op1_dir - Base(type)]
		op2_dir = quadList[self.instruction_pointer].right_operand
		op2 = Memory[op2_dir - Base(type)]
		aux = op1 < op2
		Memory[f(quadList[self.instruction_pointer].result)] = aux

	def GREATEROREQUAL(self, op1, op2):
		op1_dir = quadList[self.instruction_pointer].left_operand
		op1 = Memory[op1_dir - Base(type)]
		op2_dir = quadList[self.instruction_pointer].right_operand
		op2 = Memory[op2_dir - Base(type)]
		aux = op1 >= op2
		Memory[f(quadList[self.instruction_pointer].result)] = aux

	def LESSEROREQUAL(self, op1, op2):
		op1_dir = quadList[self.instruction_pointer].left_operand
		op1 = Memory[op1_dir - Base(type)]
		op2_dir = quadList[self.instruction_pointer].right_operand
		op2 = Memory[op2_dir - Base(type)]
		aux = op1 <= op2
		Memory[f(quadList[self.instruction_pointer].result)] = aux

	def AND(self, op1, op2):
		op1_dir = quadList[self.instruction_pointer].left_operand
		op1 = Memory[op1_dir - Base(type)]
		op2_dir = quadList[self.instruction_pointer].right_operand
		op2 = Memory[op2_dir - Base(type)]
		aux = op1 and op2
		Memory[f(quadList[self.instruction_pointer].result)] = aux

	def OR(self, op1, op2):
		op1_dir = quadList[self.instruction_pointer].left_operand
		op1 = Memory[op1_dir - Base(type)]
		op2_dir = quadList[self.instruction_pointer].right_operand
		op2 = Memory[op2_dir - Base(type)]
		aux = op1 or op2
		Memory[f(quadList[self.instruction_pointer].result)] = aux

	def NOT(self, op1):
		op1_dir = quadList[self.instruction_pointer].left_operand
		op1 = Memory[op1_dir - Base(type)]
		aux = not op1
		Memory[f(quadList[self.instruction_pointer].result)] = aux

	def ERA(self):
		turtle.pendown()

	def GOSUB(self, fun):
		turtle.pendown()

	def COLOR(self, color):
		turtle.pencolor(color)

	def CIRCLE(self, radius):
		turtle.circle(radius, None, None)

	def SQUARE(self, len):
		for i in range(4):
			turtle.forward(80)
			turtle.left(90)

	def TRIANGLE(self, b, a):
		turte.forward(distance)

	def RECTANGLE(self, l, a):
		turte.forward(distance)

	def POLIGON(self, sides, size):
		wn = turtle.Screen()
		for i in range(1,sides):
			turtle.forward(size)
			turtle.left(360/sides)
		wn.exitonclick()

	def ROTATE(self, degree):
		turtle.tilt(degree)

	def PENSIZE(self, size):
		turtle.dot(size)

	def PENFORWARD(self, distance):
		turte.forward(distance)

	def PENBACK(self, distance):
		turtle.backward(distance)

	def PENON(self):
		turtle.pendown()

	def PENOFF(self):
		turtle.penup()

vm = VirtualMachine()
vm.run()