class SemanticCube  :  

	def __init__(self) :  
		self.cube = {
            "Int" :  {
              "Int" :  {
                "+" : "Int",
                "-" : "Int",
                "*" : "Int",
                "/" : "Float",
                ">" : "Bool",
                ">=" : "Bool",
                "<=" : "Bool",
                "<" : "Bool",
                "=" : "Int",
                "==" :  "Bool",
                "!=" : "Bool",
                "&&" : "Error",
                "||" : "Error",
                },
              "Float" :  {
                "+" : "Float",
                "-" : "Float",
                "*" : "Float",
                "/" : "Float",
                ">" : "Bool",
                ">=" : "Bool",
                "<=" : "Bool",
                "<" : "Bool",
                "=" : "Int",
                "==" :  "Bool",
                "!=" : "Bool",
                "&&" : "Error",
                "||" : "Error",
                },
              "String" :  {
                "+" : "Error",
                "-" : "Error",
                "*" : "Error",
                "/" : "Error",
                ">" : "Error",
                ">=" : "Error",
                "<=" : "Error",
                "<" : "Error",
                "=" : "Error",
                "==" :  "Error",
                "!=" : "Error",
                "&&" : "Error",
                "||" : "Error",
                },
              "Bool" :  {
                "+" : "Error",
                "-" : "Error",
                "*" : "Error",
                "/" : "Error",
                ">" : "Error",
                ">=" : "Error",
                "<=" : "Error",
                "<" : "Error",
                "=" : "Error",
                "==" :  "Error",
                "!=" : "Error",
                "&&" : "Error",
                "||" : "Error",
                },
              },
            "Float" : {
              "Int" :  {
                "+" : "Float",
                "-" : "Float",
                "*" : "Float",
                "/" : "Float",
                ">" : "Bool",
                ">=" : "Bool",
                "<=" : "Bool",
                "<" : "Bool",
                "=" : "Float",
                "==" :  "Bool",
                "!=" : "Bool",
                "&&" : "Error",
                "||" : "Error",
                },
              "Float" :  {
                "+" : "Float",
                "-" : "Float",
                "*" : "Float",
                "/" : "Float",
                ">" : "Bool",
                ">=" : "Bool",
                "<=" : "Bool",
                "<" : "Bool",
                "=" : "Float",
                "==" :  "Bool",
                "!=" : "Bool",
                "&&" : "Error",
                "||" : "Error",
                },
              "String" :  {
                "+" : "Error",
                "-" : "Error",
                "*" : "Error",
                "/" : "Error",
                ">" : "Error",
                ">=" : "Error",
                "<=" : "Error",
                "<" : "Error",
                "=" : "Error",
                "==" :  "Error",
                "!=" : "Error",
                "&&" : "Error",
                "||" : "Error",
                },
              "Bool" :  {
                "+" : "Error",
                "-" : "Error",
                "*" : "Error",
                "/" : "Error",
                ">" : "Error",
                ">=" : "Error",
                "<=" : "Error",
                "<" : "Error",
                "=" : "Error",
                "==" :  "Error",
                "!=" : "Error",
                "&&" : "Error",
                "||" : "Error",
                },
              },
            "String" : {
              "Int" :  {
                "+" : "Error",
                "-" : "Error",
                "*" : "Error",
                "/" : "Error",
                ">" : "Error",
                ">=" : "Error",
                "<=" : "Error",
                "<" : "Error",
                "=" : "Error",
                "==" :  "Error",
                "!=" : "Error",
                "&&" : "Error",
                "||" : "Error",
                },
              "Float" :  {
                "+" : "Error",
                "-" : "Error",
                "*" : "Error",
                "/" : "Error",
                ">" : "Error",
                ">=" : "Error",
                "<=" : "Error",
                "<" : "Error",
                "=" : "Error",
                "==" :  "Error",
                "!=" : "Error",
                "&&" : "Error",
                "||" : "Error",
                },
              "String" :  {
                "+" : "String",
                "-" : "Error",
                "*" : "Error",
                "/" : "Error",
                ">" : "Error",
                ">=" : "Error",
                "<=" : "Error",
                "<" : "Error",
                "=" : "String",
                "==" :  "Bool",
                "!=" : "Bool",
                "&&" : "Error",
                "||" : "Error",
                },
              "Bool" :  {
                "+" : "Error",
                "-" : "Error",
                "*" : "Error",
                "/" : "Error",
                ">" : "Error",
                ">=" : "Error",
                "<=" : "Error",
                "<" : "Error",
                "=" : "Error",
                "==" :  "Error",
                "!=" : "Error",
                "&&" : "Error",
                "||" : "Error",
                },
              },
            "Bool" : {
              "Int" :  {
                "+" : "Error",
                "-" : "Error",
                "*" : "Error",
                "/" : "Error",
                ">" : "Error",
                ">=" : "Error",
                "<=" : "Error",
                "<" : "Error",
                "=" : "Error",
                "==" :  "Error",
                "!=" : "Error",
                "&&" : "Error",
                "||" : "Error",
                },
              "Float" :  {
                "+" : "Error",
                "-" : "Error",
                "*" : "Error",
                "/" : "Error",
                ">" : "Error",
                ">=" : "Error",
                "<=" : "Error",
                "<" : "Error",
                "=" : "Error",
                "==" :  "Error",
                "!=" : "Error",
                "&&" : "Error",
                "||" : "Error",
                },
              "String" :  {
                "+" : "Error",
                "-" : "Error",
                "*" : "Error",
                "/" : "Error",
                ">" : "Error",
                ">=" : "Error",
                "<=" : "Error",
                "<" : "Error",
                "=" : "Error",
                "==" : "Error",
                "!=" : "Error",
                "&&" : "Error",
                "||" : "Error",
                },
              "Bool" :  {
                "+" : "Error",
                "-" : "Error",
                "*" : "Error",
                "/" : "Error",
                ">" : "Error",
                ">=" : "Error",
                "<=" : "Error",
                "<" : "Error",
                "=" : "Bool",
                "==" : "Bool",
                "!=" : "Bool",
                "&&" : "Bool",
                "||" : "Bool",
                },
              },
            }
    def getType(self, type1, type2, operator) : 
    	return self.cube[type1][type2][operator]
