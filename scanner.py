import ply.lex as lex

#prueba de push

# List of tokens
tokens = ['ID',     'CTE_INT',      'CTE_FLOAT',    'CTE_STRING',       'EXPRESSION',   'TIMES',
         'ST_CTE',  'OR',           'NOTEQUAL',     'PLUS',             'MINUS',  
         'ASSIGN',  'GREATER',      'LESSER',       'GREATEROREQUAL',   'AND',          'NOT', 
         'LPAREN',  'RPAREN',       'LBRACE',       'RBRACE',           'LBRACKET',     'RBRACKET',
         'COMMA',   'SEMICOLON',    'DIVIDE',       'LESSEROREQUAL',    'CTE_BOOL',     'TERM']

# Dictionary of reserved words
reserved = {
    'Int': 'INT',
    'Bool': 'BOOL',
    'Float': 'FLOAT',
    'String': 'STRING',
    'if': 'IF',
    'else': 'ELSE',
    'while': 'WHILE',
    'true': 'TRUE',
    'false': 'FALSE',
    'var': 'VAR',
    'rectangle': 'RECTANGLE',
    'circle': 'CIRCLE',
    'square': 'SQUARE',
    'triangle': 'TRIANGLE',
    'size': 'SIZE',
    'color': 'COLOR',
    'poligon': 'POLIGON',
    'penForward': 'PENFORWARD',
    'penBack': 'PENBACK',
    'penOn': 'PENON',
    'penOff': 'PENOFF',
    'penSize': 'PENSIZE',
    'equal': 'EQUAL',
    'red': 'RED',
    'blue': 'BLUE',
    'yellow': 'YELLOW',
    'green': 'GREEN',
    'pink': 'PINK',
    'purple': 'PURPLE',
    'program': 'PROGRAM',
    'DaVinci': 'DAVINCI',
    'void': 'VOID',
    'rotate': 'ROTATE',
    'return': 'RETURN',
    'func': 'FUNC'
    }

tokens = tokens+list(reserved.values())

# Ignored characters

#t_ignore = ' \t\r'

t_PLUS = r'\+'
t_MINUS = r'\-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_ASSIGN = r'='
t_EQUAL = r'\=='
t_NOTEQUAL = r'\!='
t_GREATER = r'\>'
t_LESSER = r'\<'
t_GREATEROREQUAL = r'>='
t_LESSEROREQUAL = r'<='
t_AND = r'&&'
t_OR = r'\|\|'
t_NOT = r'\!'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_COMMA = r','
t_SEMICOLON = r';'
t_CTE_STRING = r'\".*\"'

# ID token definition

def t_CTE_FLOAT(t):
    r'[0-9]*\.[0-9]+'
    t.value = float(t.value)
    return t

def t_CTE_INT(t):
    r'[0-9]+'
    t.value = int(t.value)
    return t

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value,'ID')    # Check for reserved words
    return t

t_ignore = " \t"

def t_newline(t):
	r'\n+'
	t.lexer.lineno += t.value.count("\n")

# Error handling rule
def t_error(t):
    print("Illegal character '{}' at: {}" .format(t.value[0], t.lexer.lineno))
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()


f = open("test2.txt")
# Give the lexer some input
lexer.input(f.read())
# Tokenize ##
while True:
    tok = lexer.token()
    if not tok:
        break      # No more input
    #print(tok)
print("\n")