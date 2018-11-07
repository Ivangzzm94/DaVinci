from quads import Type
from errors import ErrorHandler

class Variable:
	def __init__(self, var_id, var_type, dirV):
		self.var_id = var_id
		self.var_type = var_type
		self.address = None
		self.dirV = None

class Memory:
	def __init__(self):
		self.address = {
			Type.INT: 000000,
			Type.FLOAT: 100000,
			Type.STRING: 200000,
			Type.BOOL:250000
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
			self.address[kind] = self.address[kind] + 1


# For test proposes
def parse(self) :
    return({
        "var_id": self.var_id,
        "var_type": self.var_type,
        "address": self.address
    })