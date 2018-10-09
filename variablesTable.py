from DaVinci.variables import Variables
from DaVinci.errors import ErrorHandler
from DaVinci.functions import Functions

class VariablesTable

	def __init__(self):
		self._global = {}
		self._local = {}
		self._functions = {}

	def add_global(self, instance):
		if instance.var_id in self._global:
			raise ErrorHandler.redefined_variable(instance.var_id)
		else:
			self._global[instance.var_id] = instance

	def add_local(self, instance):
		if instance.var_id in self._local:
			raise ErrorHandler.redefined_variable(instance.var_id)
		else:
		 	self._local[instance.var_id] = instance

	def add_function(self, instance):
		if instance.var_id in self._functions:
			raise ErrorHandler.redefined_function('Function {} already defined'.format(instance.function_id))
		else:
		 	self._functions[instance.function_id] = instance

	def find_variable(self, varId):
		if varId in self._global:
			return self._global.get(varId)
		elif varId in self._local:
			return self._local.get(varId)
		else:
			raise ErrorHandler.undefined_variable('Variable not defined')

	def find_function(self, func_id):
		if func_id not in self._functions:
			raise ErrorHandler.undefined_function(func_id)
		else:
			return self._functions[func_id]