import turtle
from stack import Stack
from quads import Quads
from random import randint

class VirtualMachine:

    def __init__(self):
        self.liveMemory = Stack()
        self.memory = []
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
                    List[x][y] = int(List[x][y])

        # Empezar la ejecución de la máquina virtual
        wn = turtle.Screen()
        while self.instruction_pointer < len(List):
            if List[self.instruction_pointer][0] == 15:  # GoTo
                self.instruction_pointer = List[self.instruction_pointer][3]
            else:
                self.ReadQuad(List[self.instruction_pointer][0], List[self.instruction_pointer][1],
                              List[self.instruction_pointer][2], List[self.instruction_pointer][3])
        wn.exitonclick()


    # IFSOTE
    def ReadQuad(self, operator, op1, op2, r):
        if operator == 1:
            self.PLUS(op1, op2, r)
        elif operator == 2:
            self.MINUS(op1, op2, r)
        elif operator == 3:
            self.TIMES(op1, op2, r)
        elif operator == 4:
            self.DIVIDE(op1, op2, r)
        elif operator == 5:
            self.ASSIGN(op1, r)
        elif operator == 6:
            self.EQUAL(op1, op2, r)
        elif operator == 7:
            self.NOTEQUAL(op1, op2, r)
        elif operator == 8:
            self.GREATER(op1, op2, r)
        elif operator == 9:
            self.LESSER(op1, op2, r)
        elif operator == 10:
            self.GREATEROREQUAL(op1, op2, r)
        elif operator == 11:
            self.LESSEROREQUAL(op1, op2, r)
        elif operator == 12:
            self.AND(op1, op2, r)
        elif operator == 13:
            self.OR(op1, op2, r)
        elif operator == 14:
            self.NOT(op1, r)
        elif operator == 18:
            self.ERA(op1, op2, r)
        elif operator == 19:
            self.GOSUB(op1, op2, r)
        elif operator == 20:
            self.ENDPROC(op1, op2, r)
        elif operator == 21:
            self.PARAM(op1, op2, r)
        elif operator == 22:
            self.VER(op1, op2, r)
        elif operator == 50:
            self.COLOR(op1)
        elif operator == 51:
            self.CIRCLE(op1)
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
    def PLUS(self, op1, op2, r):
        aux = self.memory.getValue(op1) + self.memory.getValue(op2)
        self.memory.setValue(r,aux)
        self.instruction_pointer += 1

    def MINUS(self, op1, op2, r):
        aux = self.memory.getValue(op1) - self.memory.getValue(op2)
        self.memory.setValue(r, aux)
        self.instruction_pointer += 1

    def TIMES(self, op1, op2, r):
        aux = self.memory.getValue(op1) * self.memory.getValue(op2)
        self.memory.setValue(r, aux)
        self.instruction_pointer += 1

    def DIVIDE(self, op1, op2, r):
        aux = self.memory.getValue(op1) / self.memory.getValue(op2)
        self.memory.setValue(r, aux)
        self.instruction_pointer += 1

    def ASSIGN(self, op1, r):
        self.memory.setValue(r, self.memory.getValue(op1))
        self.instruction_pointer += 1

    def EQUAL(self, op1, op2, r):
        if self.memory.getValue(op1) == self.memory.getValue(op2):
            aux = true
        else:
            aux = false

        self.memory.setValue(r, aux)
        self.instruction_pointer += 1

    def NOTEQUAL(self, op1, op, r):
        aux =  not (self.memory.getValue(op1) == self.memory.getValue(op2))

        self.memory.setValue(r, aux)
        self.instruction_pointer += 1

    def GREATER(self, op1, op2, r):
        aux =  self.memory.getValue(op1) > self.memory.getValue(op2)


        self.memory.setValue(r, aux)
        self.instruction_pointer += 1

    def LESSER(self, op1, op2, r):
        if self.memory.getValue(op1) < self.memory.getValue(op2):
            aux = true
        else:
            aux = false

        self.memory.setValue(r, aux)
        self.instruction_pointer += 1

    def GREATEROREQUAL(self, op1, op2, r):
        if self.memory.getValue(op1) >= self.memory.getValue(op2):
            aux = true
        else:
            aux = false

        self.memory.setValue(r, aux)
        self.instruction_pointer += 1

    def LESSEROREQUAL(self, op1, op2, r):
        if self.memory.getValue(op1) <= self.memory.getValue(op2):
            aux = true
        else:
            aux = false

        self.memory.setValue(r, aux)
        self.instruction_pointer += 1

    def AND(self, op1, op2, r):
        if self.memory.getValue(op1) and self.memory.getValue(op2):
            aux = true
        else:
            aux = false

        self.memory.setValue(r, aux)
        self.instruction_pointer += 1

    def OR(self, op1, op2):
        if self.memory.getValue(op1) or self.memory.getValue(op2):
            aux = true
        else:
            aux = false

        self.memory.setValue(r, aux)
        self.instruction_pointer += 1

    def NOT(self, op1):
        aux = self.memory.getValue(op1)
        aux = not aux
        self.memory.setValue(r, aux)
        self.instruction_pointer += 1

    def ERA(self):
        self.instruction_pointer += 1

    def GOSUB(self, fun):
        self.instruction_pointer += 1

    def COLOR(self, op1):
        aux = self.memory.getValue(op1)
        turtle.pencolor(aux)
        self.instruction_pointer += 1

    def CIRCLE(self, radius):
        r = self.memory.getValue(radius)
        turtle.circle(r, None, None)
        self.instruction_pointer += 1

    def SQUARE(self, len):
        l = self.memory.getValue(len)
        for i in range(4):
            turtle.forward(l)
            turtle.left(l)

        self.instruction_pointer += 1

    def TRIANGLE(self, b, a):
        base = self.memory.getValue(b)
        alt = self.memory.getValue(a)
        turtle.forward(base)
        turtle.left(base*1.1)
        turtle.forward(alt)
        turtle.left(base*1.1)
        turtle.forward(alt)

        self.instruction_pointer += 1

    def RECTANGLE(self, l, a):
        lon = self.memory.getValue(l)
        alt = self.memory.getValue(a)
        turtle.forward(lon)
        turtle.left(90)
        turtle.forward(alt)
        turtle.left(90)
        turtle.forward(lon)
        turtle.left(90)
        turtle.forward(alt)

        self.instruction_pointer += 1

    def POLIGON(self, sides, size):
        side = self.memory.getValue(sides)
        siz = self.memory.getValue(size)
        for i in range(1, side):
            turtle.forward(siz)
            turtle.left(360 / side)

        self.instruction_pointer += 1

    def ROTATE(self, degree):
        d = self.memory.getValue(degree)
        turtle.tilt(d)
        self.instruction_pointer += 1

    def PENSIZE(self, size):
        s = self.memory.getValue(size)
        turtle.dot(s)
        self.instruction_pointer += 1

    def PENFORWARD(self, distance):
        d = self.memory.getValue(distance)
        turtle.forward(distance)
        self.instruction_pointer += 1

    def PENBACK(self, distance):
        d = self.memory.getValue(distance)
        turtle.backward(d)
        self.instruction_pointer += 1

    def PENON(self):
        turtle.pendown()
        self.instruction_pointer += 1

    def PENOFF(self):
        turtle.penup()
        self.instruction_pointer += 1
