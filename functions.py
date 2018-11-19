from variables import *

class Function:

    def __init__(self, function_id, function_type, starting_instruction):
        self.function_id = function_id
        self.function_type = function_type
        self.parameters = []
        self.memory = Memory()
        self.starting_instruction = starting_instruction
        self.varTable = {} # llave = id, valor = dir_virt

    def declareVariable(self, id, type):
        memDir = self.memory.pushVarInMemory(type, 1)
        self.varTable[id] = memDir
        return memDir
