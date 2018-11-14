from variables import Variable

class Function:

    def __init__(self, function_id = None, function_type = None):
        self.function_id = function_id
        self.function_type = function_type
        self.parameters = None
        self.paramcount = None
        self.dir_virt = None