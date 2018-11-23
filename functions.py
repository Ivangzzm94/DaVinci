from variables import *

class Function:

    def __init__(self, function_id, function_type, starting_instruction):
        self.function_id = function_id
        self.function_type = function_type
        self.parameters = []
        self.memory = Memory()
        self.starting_instruction = starting_instruction
        self.varTable = {} # llave = id, valor = dir_virt
        self.retDir = None

    def declareVariable(self, id, type, size):
        memDir = self.memory.pushVarInMemory(type, size)
        self.varTable[id] = memDir
        return memDir

    def declareGlobalVariable(self, id, type, size):
        memDir = self.memory.pushGlobalInMemory(type, size)
        self.varTable[id] = memDir
        return memDir
