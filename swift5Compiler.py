class swift5Compiler():
    def __init__(self):
        pass
    def declareVariable(self, identifier,dataType):
        dtype = ""
        #   USE MATCH/CASE STATEMENT HERE IN PYTHON 3.10
        if dataType == "STRING":
            dtype = 'String'
        elif dataType == "INTEGER":
            dtype = "Integer"
        elif dataType == "REAL":
            dtype = "Float"
        elif dataType == "CHAR":
            dtype = "Character"
        elif dataType == "BOOLEAN":
            dtype = "Bool"
        elif dataType == "DATE":
            dtype = 'Date'
        return str("var " + identifier + ": " + dtype)
    def declareConstant(self,identifier,value):
        return str("let " + identifier + " = " + value)
