from quads import Type
from errors import ErrorHandler

class Variable:

    def __init__(self, var_id, var_type, size, value):
        self.var_id = var_id
        self.var_type = var_type
        self.dir_virt = None
        self.size = size
        self.value = value

    def __repr__(self):
        return str(self.var_id) +  ', ' + str(self.var_type) + ', ' + str(self.size) + ', ' + str(self.value) + ', ' + str(self.dir_virt)

class Memory:
    def __init__(self):
        self.memory = {}

    def putVarInMemory(self, context_cont, type, size, value):
        #Cada contexto tiene 10,000 espacios en memoria
        offset = 0 + 10000 * context_cont
        if type == Type.INT.value:
            nextAvailable = offset + 0                              #el offset de cada tipo, aqui se llama nextAvailable

            for dir in self.memory.items():                         #este for cuenta cuantas casillas de este tipo estan ocupadas
                if not nextAvailable in self.memory:                #verifica si la direccion esta en memory
                    break
                elif self.memory[nextAvailable] == None:           #verifica si esta vacia
                    break
                nextAvailable += 1                                  #mientras estan ocupadas aumenta una y checa la próxima

            for dir in range(nextAvailable, nextAvailable + size):
                if value != None:
                    self.memory[dir] = value                       #asigna el valor o "toma" la casilla/s para la variable
                else:
                    self.memory[dir] = "TAKEN"
            return nextAvailable

        elif type == Type.FLOAT.value:
            nextAvailable = offset + 2000
            for dir in self.memory.items():
                if not nextAvailable in self.memory:
                    break
                elif self.memory[nextAvailable] == None:
                    break
                nextAvailable += 1
            for dir in range(nextAvailable, nextAvailable + size):
                self.memory[dir] = "TAKEN"
            return nextAvailable

        elif type == Type.BOOL.value:
            nextAvailable = offset + 4000
            for dir in self.memory.items():
                if not nextAvailable in self.memory:
                    break
                elif self.memory[nextAvailable] == None:
                    break
                nextAvailable += 1
            for dir in range(nextAvailable, nextAvailable + size):
                self.memory[dir] = "TAKEN"
            return nextAvailable

        elif type == Type.STRING.value:
            nextAvailable = offset + 6000
            for dir in self.memory.items():
                if not nextAvailable in self.memory:
                    break
                elif self.memory[nextAvailable] == None:
                    break
                nextAvailable += 1
            for dir in range(nextAvailable, nextAvailable + size):
                self.memory[dir] = "TAKEN"
            return nextAvailable


    def putConsInMemory(self, type, value):
        offset = 500000

        if type == Type.INT.value:
            nextConstant = offset + 0                               # el offset de cada tipo, aqui se llama nextConstant

            for dir in self.memory.items():                         # este for cuenta cuantas casillas de este tipo estan ocupadas
                if not nextConstant in self.memory:                 # verifica si la direccion esta en memoria
                    break
                elif self.memory[nextConstant] == None:            # verifica si esta vacia
                    break
                nextConstant += 1                                   # mientras estan ocupadas aumenta una y checa la próxima
            self.memory[nextConstant] = value                      # asigna el valor en la casilla disponible
            return nextConstant

        elif type == Type.FLOAT.value:
            nextConstant = offset + 520000
            for dir in self.memory.items():
                if not nextConstant in self.memory:
                    break
                elif self.memory[nextConstant] == None:
                    break
                nextConstant += 1
            self.memory[nextConstant] = value
            return nextConstant

        elif type == Type.BOOL.value:
            nextConstant = offset + 540000
            for dir in self.memory.items():
                if not nextConstant in self.memory:
                    break
                elif self.memory[nextConstant] == None:
                    break
                nextConstant += 1
            self.memory[nextConstant] = value
            return nextConstant

        elif type == Type.STRING.value:
            nextConstant = offset + 560000
            for dir in self.memory.items():
                if not nextConstant in self.memory:
                    break
                elif self.memory[nextConstant] == None:
                    break
                nextConstant += 1
            self.memory[nextConstant] = value
            return nextConstant

    def printVars(self):
        for var in self.memory.items():
            print(self.memory[var])