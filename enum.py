from enum import IntEnum

class Operator(IntEnum):
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

class Function(IntEnum):
	COLOR = 1
	CIRCLE = 2
	SQUARE = 3
	TRIANGLE = 4
	RECTANGLE = 5
	POLIGON = 6
	ROTATE = 7
	PENSIZE = 8
	PENFORWARD = 9
	PENBACK = 10
	PENON = 11
	PENOFF = 12

class Type(IntEnum):
	INT = 1
	FLOAT = 2
	STRING = 3
	BOOL = 4