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
        self.varTable[id] = [memDir, size]
        return memDir

    def declareGlobalVariable(self, id, type, size):
        memDir = self.memory.pushGlobalInMemory(type, size)
        self.varTable[id] = [memDir, size]
        return memDir

    def declareArray(self, id, type, size):
        memDir = self.memory.pushArrayInMemory(type, size)
        self.varTable[id] = [memDir, size]
        return memDir

    def declareLocalArray(self, id, type, size):
        memDir = self.memory.pushLocalArrayInMemory(type, size)
        self.varTable[id] = [memDir, size]
        return memDir
