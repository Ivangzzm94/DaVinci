from quads import Type
from errors import ErrorHandler

class Variable:

    def __init__(self, var_id, var_type, size):
        self.var_id = var_id
        self.var_type = var_type
        self.size = size

    def __repr__(self):
        return 'id: ' + str(self.var_id) +  ', ' + 'type: ' + str(self.var_type) + ', ' + 'size: ' + str(self.size) + ', ' + 'dv: ' + str(self.dir_virt)

class Memory:
    def __init__(self):
        self.memory = {}

    def getType(self, dir):
        if dir < 10000:
            return Type.INT.value
        elif dir < 12000:
            return  Type.FLOAT.value
        elif dir < 14000:
            return Type.BOOL.value
        elif dir < 16000:
            return Type.STRING.value
        elif dir < 82000:
            return Type.INT.value
        elif dir < 84000:
            return Type.FLOAT.value
        elif dir < 86000:
            return Type.BOOL.value
        elif dir < 88000:
            return Type.STRING.value
        elif dir < 402000:
            return Type.INT.value
        elif dir < 404000:
            return Type.FLOAT.value
        elif dir < 406000:
            return Type.BOOL.value
        elif dir < 408000:
            return Type.STRING.value
        elif dir < 802000:
            return Type.INT.value
        elif dir < 804000:
            return Type.FLOAT.value
        elif dir < 806000:
            return Type.BOOL.value
        elif dir < 808000:
            return Type.STRING.value


    def getSize(self):
        return len(self.memory.items())

    def getValue(self, dir):
        return self.memory[dir]

    def setValue(self, dir, value):
        self.memory[dir] = value

    def putVarInMemory(self, context_cont, type, size, value):
        #Cada contexto tiene 10,000 espacios en memoria
        offset = 0 + 8000 * context_cont
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

    def pushVarInMemory(self, type, size):
        #Cada contexto tiene 8,000 espacios en memoria
        offset = 0 + 8000
        if type == Type.INT.value:
            nextAvailable = offset + 0                              #el offset de cada tipo, aqui se llama nextAvailable

            for dir in self.memory.items():                         #este for cuenta cuantas casillas de este tipo estan ocupadas
                if not nextAvailable in self.memory:                #verifica si la direccion esta en memory
                    break
                elif self.memory[nextAvailable] == None:           #verifica si esta vacia
                    break
                nextAvailable += 1                                  #mientras estan ocupadas aumenta una y checa la próxima

            for dir in range(nextAvailable, nextAvailable + size):
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

    def pushArrayInMemory(self, type, size):
        #Cada contexto tiene 8,000 espacios en memoria
        offset = 0 + 8000 * 100
        if type == Type.INT.value:
            nextAvailable = offset + 0                              #el offset de cada tipo, aqui se llama nextAvailable

            for dir in self.memory.items():                         #este for cuenta cuantas casillas de este tipo estan ocupadas
                if not nextAvailable in self.memory:                #verifica si la direccion esta en memory
                    break
                elif self.memory[nextAvailable] == None:           #verifica si esta vacia
                    break
                nextAvailable += 1                                  #mientras estan ocupadas aumenta una y checa la próxima

            for dir in range(nextAvailable, nextAvailable + size):
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

    def pushLocalArrayInMemory(self, type, size):
        #Cada contexto tiene 8,000 espacios en memoria
        offset = 0 + 8000 * 50
        if type == Type.INT.value:
            nextAvailable = offset + 0                              #el offset de cada tipo, aqui se llama nextAvailable

            for dir in self.memory.items():                         #este for cuenta cuantas casillas de este tipo estan ocupadas
                if not nextAvailable in self.memory:                #verifica si la direccion esta en memory
                    break
                elif self.memory[nextAvailable] == None:           #verifica si esta vacia
                    break
                nextAvailable += 1                                  #mientras estan ocupadas aumenta una y checa la próxima

            for dir in range(nextAvailable, nextAvailable + size):
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

    def pushGlobalInMemory(self, type, size):
        #Cada contexto tiene 8,000 espacios en memoria
        offset = 0 + 8000 * 10
        if type == Type.INT.value:
            nextAvailable = offset + 0                              #el offset de cada tipo, aqui se llama nextAvailable

            for dir in self.memory.items():                         #este for cuenta cuantas casillas de este tipo estan ocupadas
                if not nextAvailable in self.memory:                #verifica si la direccion esta en memory
                    break
                elif self.memory[nextAvailable] == None:           #verifica si esta vacia
                    break
                nextAvailable += 1                                  #mientras estan ocupadas aumenta una y checa la próxima

            for dir in range(nextAvailable, nextAvailable + size):
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

    def printVars(self, id):
        print(id)
        print("MEMORIA")
        for key,val in self.memory.items():
            print(key, '->', val)
