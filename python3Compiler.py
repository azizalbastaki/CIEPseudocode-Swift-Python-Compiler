class python3Compiler():
    def __init__(self):
        pass
    def declareVariable(self,identifier,dataType):
        type = ""
        #   USE MATCH/CASE STATEMENT HERE IN PYTHON 3.10
        if dataType == "STRING":
            type = '""'
        elif dataType == "INTEGER":
            type = "0"
        elif dataType == "REAL":
            type = "0.0"
        elif dataType == "CHAR":
            type = '"A"'
        elif dataType == "BOOLEAN":
            type = "FALSE"
        elif dataType == "DATE":
            type = '"01/01/1970"'
        return str(identifier + " = " + type)
    def declareConstant(self,identifier,value):
        return str(identifier + " = " + value)
