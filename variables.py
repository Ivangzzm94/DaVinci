from quads import Type
from errors import ErrorHandler


class Variable:

    def __init__(self, var_id, var_type, dir_virt = None):
        self.var_id = var_id
        self.var_type = var_type
        self.dir_virt = dir_virt

    def __repr__(self):
        return str(self.var_id) + ', ' + str(self.var_type) + ', ' + str(self.dir_virt)

class Memory:
    def __init__(self):
        self.address = {
            Type.INT: 000000,
            Type.FLOAT: 100000,
            Type.STRING: 200000,
            Type.BOOL: 250000
        }

    def getAddress(self, type):
        if type not in self.address:
            raise ErrorHandler.type_error("Type not defined");
        else:
            return self.address[type]

    def setAddress(self, type):
        if type not in self.address:
            raise ErrorHandler.type_error("Type not defined");
        else:
            self.address[type] = self.address[type] + 1


# For test proposes
def parse(self):
    return ({
        "var_id": self.var_id,
        "var_type": self.var_type,
        "address": self.address,
        "dir_virt": self.dir_virt
    })
