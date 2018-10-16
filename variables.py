class Variable:
	def __init__(self, var_id, var_type):
		self.var_id = var_id
		self.var_type = var_type
		self.address = None

# For test proposes only
def parse(self) :
    print({
        "var_id": self.var_id,
        "var_type": self.var_type,
        "address": self.address
    })