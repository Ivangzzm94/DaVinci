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

    def run(self):
        # Lee lista de cúadruplos y meterlos a la lista "List"

        self.contextStack.push('DaVinci')
        self.liveMemory.push(self.memory[self.contextStack.top()])
        self.memSize += len(self.memory[self.contextStack.top()].items())
        print(self.memory)
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
        mem = self.liveMemory.top()
        aux = mem[op1] + mem[op2]
        mem[r] = aux
        self.instruction_pointer += 1

    def MINUS(self, op1, op2, r):
        mem = self.liveMemory.top()
        aux = mem[op1] - mem[op2]
        mem[r] = aux
        self.instruction_pointer += 1

    def TIMES(self, op1, op2, r):
        mem = self.liveMemory.top()
        aux = mem[op1] * mem[op2]
        mem[r] = aux
        self.instruction_pointer += 1

    def DIVIDE(self, op1, op2, r):
        mem = self.liveMemory.top()
        aux = mem[op1] / mem[op2]
        mem[r] = aux
        self.instruction_pointer += 1

    def ASSIGN(self, op1, r):
        mem = self.liveMemory.top()
        mem[r] = mem[op1]
        self.instruction_pointer += 1

    def EQUAL(self, op1, op2, r):
        mem = self.liveMemory.top()
        if mem[op1] == mem[op2]:
            aux = True
        else:
            aux = False

        mem[r] = aux
        self.instruction_pointer += 1

    def NOTEQUAL(self, op1, op2, r):
        mem = self.liveMemory.top()
        aux =  not (mem[op1] == mem[op2])

        mem[r] = aux
        self.instruction_pointer += 1

    def GREATER(self, op1, op2, r):
        mem = self.liveMemory.top()
        aux =  mem[op1] > mem[op2]
        mem[r] = aux
        self.instruction_pointer += 1

    def LESSER(self, op1, op2, r):
        mem = self.liveMemory.top()
        if mem[op1] < mem[op2]:
            aux = True
        else:
            aux = False
        mem[r] = aux
        self.instruction_pointer += 1

    def GREATEROREQUAL(self, op1, op2, r):
        mem = self.liveMemory.top()
        if mem[op1] >= mem[op2]:
            aux = True
        else:
            aux = False
        mem[r] = aux
        self.instruction_pointer += 1

    def LESSEROREQUAL(self, op1, op2, r):
        mem = self.liveMemory.top()
        if mem[op1] <= mem[op2]:
            aux = True
        else:
            aux = False

        mem[r] = aux
        self.instruction_pointer += 1

    def AND(self, op1, op2, r):
        mem = self.liveMemory.top()
        if mem[op1] and mem[op2]:
            aux = True
        else:
            aux = False

        mem[r] = aux
        self.instruction_pointer += 1

    def OR(self, op1, op2, r):
        mem = self.liveMemory.top()
        if mem[op1] or mem[op2]:
            aux = True
        else:
            aux = False

        mem[r] = aux
        self.instruction_pointer += 1

    def NOT(self, op1, r):
        mem = self.liveMemory.top()
        aux = mem[op1]
        aux = not aux
        mem[r] = aux
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
        mem = self.liveMemory.top()
        aux = mem[op1]
        turtle.pencolor(aux)
        self.instruction_pointer += 1

    def CIRCLE(self, r):
        mem = self.liveMemory.top()
        radio = int(mem[r])
        turtle.circle(radio, None, None)
        self.instruction_pointer += 1

    def SQUARE(self, len):
        mem = self.liveMemory.top()
        l = mem[len]
        for i in range(4):
            turtle.forward(l)
            turtle.left(l)
        self.instruction_pointer += 1

    def TRIANGLE(self, b, a):
        mem = self.liveMemory.top()
        base = mem[b]
        alt = mem[a]
        turtle.forward(base)
        turtle.left(base*1.1)
        turtle.forward(alt)
        turtle.left(base*1.1)
        turtle.forward(alt)
        self.instruction_pointer += 1

    def RECTANGLE(self, l, a):
        mem = self.liveMemory.top()
        lon = mem[l]
        alt = mem[a]
        turtle.forward(lon)
        turtle.left(90)
        turtle.forward(alt)
        turtle.left(90)
        turtle.forward(lon)
        turtle.left(90)
        turtle.forward(alt)

        self.instruction_pointer += 1

    def POLIGON(self, sides, size):
        mem = self.liveMemory.top()
        side = mem[sides]
        siz = mem[size]
        for i in range(1, side):
            turtle.forward(siz)
            turtle.left(360 / side)

        self.instruction_pointer += 1

    def ROTATE(self, degree):
        mem = self.liveMemory.top()
        d = mem[degree]
        turtle.tilt(d)
        self.instruction_pointer += 1

    def PENSIZE(self, size):
        mem = self.liveMemory.top()
        s = mem[size]
        turtle.dot(s)
        self.instruction_pointer += 1

    def PENFORWARD(self, distance):
        mem = self.liveMemory.top()
        d = mem[distance]
        turtle.forward(d)
        self.instruction_pointer += 1

    def PENBACK(self, distance):
        mem = self.liveMemory.top()
        d = mem[distance]
        turtle.backward(d)
        self.instruction_pointer += 1

    def PENON(self):
        turtle.pendown()
        self.instruction_pointer += 1

    def PENOFF(self):
        turtle.penup()
        self.instruction_pointer += 1

    def PRINT(self, r):
        mem = self.liveMemory.top()
        p = mem[r]
        print(p)
        self.instruction_pointer += 1

    def PARAM(self, op1, r):
        actualMemory = self.liveMemory.top()
        self.nextMem.setValue(self.nextFuncRunning.parameters[r], actualMemory[op1])
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
        mem = self.liveMemory.top()
        self.returnStack.push(mem[r])
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