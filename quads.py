from typing import List, Any

from enum import Enum, IntEnum


class Operations(IntEnum):
    PLUS = 1
    MINUS = 2
    TIMES = 3
    DIVIDE = 4
    ASSIGN = 5
    EQUAL = 6
    NOTEQUAL = 7
    GREATER = 8
    LESSER = 9
    GREATEROREQUAL = 10
    LESSEROREQUAL = 11
    AND = 12
    OR = 13
    NOT = 14
    GOTO = 15
    GOTOF = 16
    GOTOV = 17
    ERA = 18
    GOSUB = 19


class Function(IntEnum):
    COLOR = 50
    CIRCLE = 51
    SQUARE = 52
    TRIANGLE = 53
    RECTANGLE = 54
    POLIGON = 55
    ROTATE = 56
    PENSIZE = 57
    PENFORWARD = 58
    PENBACK = 59
    PENON = 60
    PENOFF = 61


class Type(Enum):
    INT = 90
    FLOAT = 91
    STRING = 92
    BOOL = 93


class Quad:
    def __init__(self, operator, left_operand=None, right_operand=None, result=None):
        self.operator = operator
        self.left_operand = left_operand
        self.right_operand = right_operand
        self.result = result


class Quads:

    def __init__(self):
        self.index = 0
        self.array = []

    def add_quad(self, quad):
            self.array.append(quad)
            self.index += 1

    def delete_quad(self):
            self.array.pop()
            self.index -= 1

    def print_Quads(self):
            self.print(self.array)

    def fill(self, position, val):
            self.array[position].result = val
