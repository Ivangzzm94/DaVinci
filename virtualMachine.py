import turtle
from stack import Stack
from variables import *
from quads import Quads
from random import randint

class VirtualMachine:

    def __init__(self):
        self.liveMemory = Stack()
        self.memory = {}
        self.instruction_pointer = 0
        self.list = None
        self.memSize = 0
        self.funcTable = {}
        self.contextStack = Stack()
        self.nextMem = Memory()
        self.nextFuncRunning = None
        self.returnStack = Stack()
        self.isArray = False

    def run(self):
        # Lee lista de cúadruplos y meterlos a la lista "List"

        self.contextStack.push('DaVinci')
        self.liveMemory.push(self.memory[self.contextStack.top()])
        self.memSize += len(self.memory[self.contextStack.top()].items())
        with open("quads.txt") as file:
            text = file.read()

        List = [l for l in [lines.split(", ") for lines in text.split("\n")]]

        # Convertir la lista de cuádruplos a enteros
        for x in range(len(List)):
            for y in range(4):
                if not List[x][y] == "None":
                    try:
                        List[x][y] = int(List[x][y])
                    except:
                        List[x][y] = List[x][y]

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
        elif operator == 16:
            self.GOTOF(op1, r)
        elif operator == 18:
            self.ERA(op1, r)
        elif operator == 19:
            self.GOSUB(op1, r)
        elif operator == 20:
            self.ENDPROC()
        elif operator == 21:
            self.PARAM(op1, r)
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
        elif operator == 62:
            self.PRINT(r)
        elif operator == 63:
            self.RETURN(r)
        elif operator == 64:
            self.SAVERETURN(r)
        else:
            print("Unknown operation code")

    # Operaciones
    def PLUS(self, op1, op2, r):
        left = self.getValueForDir(op1)
        rigth = self.getValueForDir(op2)
        res = left + rigth
        self.setValueForDir(r, res)
        self.instruction_pointer += 1

    def MINUS(self, op1, op2, r):
        left = self.getValueForDir(op1)
        rigth = self.getValueForDir(op2)
        res = left - rigth
        self.setValueForDir(r, res)
        self.instruction_pointer += 1

    def TIMES(self, op1, op2, r):
        left = self.getValueForDir(op1)
        rigth = self.getValueForDir(op2)
        res = left * rigth
        self.setValueForDir(r, res)
        self.instruction_pointer += 1

    def DIVIDE(self, op1, op2, r):
        left = self.getValueForDir(op1)
        rigth = self.getValueForDir(op2)
        res = left / rigth
        self.setValueForDir(r, res)
        self.instruction_pointer += 1

    def ASSIGN(self, op1, r):
        left = self.getValueForDir(op1)
        self.setValueForDir(r, left)
        self.instruction_pointer += 1

    def EQUAL(self, op1, op2, r):
        left = self.getValueForDir(op1)
        rigth = self.getValueForDir(op2)
        res = left == rigth
        self.setValueForDir(r, res)
        self.instruction_pointer += 1

    def NOTEQUAL(self, op1, op2, r):
        left = self.getValueForDir(op1)
        rigth = self.getValueForDir(op2)
        res = left != rigth
        self.setValueForDir(r, res)
        self.instruction_pointer += 1

    def GREATER(self, op1, op2, r):
        left = self.getValueForDir(op1)
        rigth = self.getValueForDir(op2)
        res = left > rigth
        self.setValueForDir(r, res)
        self.instruction_pointer += 1

    def LESSER(self, op1, op2, r):
        left = self.getValueForDir(op1)
        rigth = self.getValueForDir(op2)
        res = left < rigth
        self.setValueForDir(r, res)
        self.instruction_pointer += 1

    def GREATEROREQUAL(self, op1, op2, r):
        left = self.getValueForDir(op1)
        rigth = self.getValueForDir(op2)
        res = left >= rigth
        self.setValueForDir(r, res)
        self.instruction_pointer += 1

    def LESSEROREQUAL(self, op1, op2, r):
        left = self.getValueForDir(op1)
        rigth = self.getValueForDir(op2)
        res = left <= rigth
        self.setValueForDir(r, res)
        self.instruction_pointer += 1

    def AND(self, op1, op2, r):
        left = self.getValueForDir(op1)
        rigth = self.getValueForDir(op2)
        res = left and rigth
        self.setValueForDir(r, res)
        self.instruction_pointer += 1

    def OR(self, op1, op2, r):
        left = self.getValueForDir(op1)
        rigth = self.getValueForDir(op2)
        res = left or rigth
        self.setValueForDir(r, res)
        self.instruction_pointer += 1

    def NOT(self, op1, r):
        left = self.getValueForDir(op1)
        self.setValueForDir(r, not left)
        self.instruction_pointer += 1

    def ERA(self, op1, r):
        self.nextFuncRunning = self.funcTable[str(r)]
        nfr = self.nextFuncRunning

        if nfr.function_type == Type.INT.value or nfr.function_type == Type.FLOAT.value or nfr.function_type == Type.BOOL.value or nfr.function_type == Type.STRING.value:
            self.memSize += op1 + 2
        else:
            self.memSize += op1 + 1

        if self.memSize > 1000000:
            print("Stack Overflow, límite de memoria excedido(1,000,000)")
            exit(0)
        else:
            self.nextMem.memory = self.memory[r]

        self.instruction_pointer += 1

    def GOSUB(self, fun, r):
        self.liveMemory.push(self.instruction_pointer + 1)
        self.liveMemory.push(self.nextMem.memory)
        self.contextStack.push(fun)
        self.instruction_pointer = r

    def COLOR(self, op1):
        aux = op1
        color = None
        if aux == 100:
            color = 'red'
        elif aux == 101:
            color = 'blue'
        elif aux == 102:
            color = 'yellow'
        elif aux == 103:
            color = 'green'
        elif aux == 104:
            color = 'pink'
        elif aux == 105:
            color = 'purple'
        turtle.pencolor(color)
        self.instruction_pointer += 1

    def CIRCLE(self, r):
        left = self.getValueForDir(r)

        turtle.circle(left, None, None)
        self.instruction_pointer += 1

    def SQUARE(self, len):
        left = self.getValueForDir(len)

        for i in range(4):
            turtle.forward(left)
            turtle.left(90)
        self.instruction_pointer += 1

    def TRIANGLE(self, b, a):
        base = self.getValueForDir(b)
        alt = self.getValueForDir(a)

        turtle.forward(base)
        turtle.left(base*1.1)
        turtle.forward(alt)
        turtle.left(base*1.1)
        turtle.forward(alt)
        self.instruction_pointer += 1

    def RECTANGLE(self, l, a):
        lon = self.getValueForDir(l)
        alt = self.getValueForDir(a)

        turtle.forward(lon)
        turtle.left(90)
        turtle.forward(alt)
        turtle.left(90)
        turtle.forward(lon)
        turtle.left(90)
        turtle.forward(alt)

        self.instruction_pointer += 1

    def POLIGON(self, sides, size):
        side = self.getValueForDir(sides)
        siz = self.getValueForDir(size)
        for i in range(1, side):
            turtle.forward(siz)
            turtle.left(360 / side)

        self.instruction_pointer += 1

    def ROTATE(self, degree):
        turtle.left(degree)
        self.instruction_pointer += 1

    def PENSIZE(self, size):
        value = self.getValueForDir(size)
        turtle.dot(value)
        self.instruction_pointer += 1

    def PENFORWARD(self, distance):
        value = self.getValueForDir(distance)
        turtle.forward(value)
        self.instruction_pointer += 1

    def PENBACK(self, distance):
        value = self.getValueForDir(distance)
        turtle.backward(value)
        self.instruction_pointer += 1

    def PENON(self):
        turtle.pendown()
        self.instruction_pointer += 1

    def PENOFF(self):
        turtle.penup()
        self.instruction_pointer += 1

    def PRINT(self, r):
        value = self.getValueForDir(r)
        print(value)
        self.instruction_pointer += 1

    def PARAM(self, op1, r):
        value = self.getValueForDir(op1)
        self.nextMem.setValue(self.nextFuncRunning.parameters[r], value)
        self.instruction_pointer += 1

    def ENDPROC(self):
        nfr = self.funcTable[self.contextStack.top()]

        if nfr.function_type == Type.INT.value or nfr.function_type == Type.FLOAT.value or nfr.function_type == Type.BOOL.value or nfr.function_type == Type.STRING.value:
            self.memSize -= len(self.liveMemory.top().items()) + 2
        else:
            self.memSize -= len(self.liveMemory.top().items()) + 1

        self.liveMemory.pop()
        self.instruction_pointer = int(self.liveMemory.pop())
        self.contextStack.pop()

    def RETURN(self, r):
        value = self.getValueForDir(r)
        self.returnStack.push(value)
        self.instruction_pointer += 1

    def SAVERETURN(self, r):
        mem = self.liveMemory.top()
        if self.returnStack.size() > 0:
            mem[r] = self.returnStack.pop()
        self.instruction_pointer += 1

    def GOTOF(self, op1, r):
        mem = self.liveMemory.top()
        if mem[op1]:
            self.instruction_pointer += 1
        else:
            self.instruction_pointer = r

    def VER(self, op1, op2, r):
        value = self.getValueForDir(op1)
        if value < r and value >= 0:
            self.instruction_pointer += 1
        else:
            print('Valor fuera de rango')
            ErrorHandler.exitWhenError()

    def getValueForDir(self, dir):
        mem = self.liveMemory.top()
        if dir > 500000:
            value = self.memory['DaVinci'][dir]
            if value > 100000:
                value = self.memory[value]
        elif dir > 300000:
            value = mem[dir]
            if value > 100000:
                value = mem[value]
        elif dir > 50000:
            value = self.memory['DaVinci'][dir]
            if value > 100000:
                value = self.memory[value]
        else:
            value = mem[dir]
            if value > 100000:
                value = mem[value]
        return value

    def setValueForDir(self, dir, value):
        mem = self.liveMemory.top()
        if dir > 500000:
            self.memory['DaVinci'][dir] = value
        elif dir > 300000:
            mem[dir] = value
        elif dir > 50000:
            aux = self.memory['DaVinci'][dir]
            try:
                temp = aux > 100000
                if temp:
                    self.memory['DaVinci'][aux] = value
            except:
                self.memory['DaVinci'][dir] = value
        else:
            aux = mem[dir]
            try:
                temp = aux > 100000
                if temp:
                    mem[aux] = value
            except:
                mem[dir] = value