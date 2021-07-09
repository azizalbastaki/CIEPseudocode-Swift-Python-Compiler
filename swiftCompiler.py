class swift5Compiler():
    def __init__(self):
        pass
    def declareVariable(self, identifier,dataType):
        type = ""
        #   USE MATCH/CASE STATEMENT HERE IN PYTHON 3.10
        if dataType == "STRING":
            type = 'String'
        elif dataType == "INTEGER":
            type = "Integer"
        elif dataType == "REAL":
            type = "Float"
        elif dataType == "CHAR":
            type = "Character"
        elif dataType == "BOOLEAN":
            type = "Bool"
        elif dataType == "DATE":
            type = 'Date'

        return str("var " + identifier + ": " + type)