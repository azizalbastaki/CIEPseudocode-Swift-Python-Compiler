class python3Compiler():
    def __init__(self):
        pass
    def declareVariable(self,identifier,dataType):
        dtype = ""
        #   USE MATCH/CASE STATEMENT HERE IN PYTHON 3.10
        if dataType == "STRING":
            dtype = '""'
        elif dataType == "INTEGER":
            dtype = "0"
        elif dataType == "REAL":
            dtype = "0.0"
        elif dataType == "CHAR":
            dtype = '"A"'
        elif dataType == "BOOLEAN":
            dtype = "FALSE"
        elif dataType == "DATE":
            dtype = '"01/01/1970"'
        return str(identifier + " = " + dtype)
    def declareConstant(self,identifier,value):
        return str(identifier + " = " + value)
    def assignVariable(self, *args):
        operations = ""
        for i in range(2,len(args[0])):
            operations+= str(args[0][i])
        operations = operations.replace("<>", "!=")
        operations = operations.replace(" AND ", " and ")
        operations = operations.replace("&", "+")
        operations = operations.replace(" NOT ", " not ")
        operations = operations.replace(" OR ", " or ")
        operations = operations.replace("=", "==")

        operationsChanges = True
        while operationsChanges == True:
            operationsChanges = False
            if "RIGHT(" in operations:
                index = operations.find("RIGHT(")
                selectedCode = operations[index]
                while operations[index] != ")":
                    index += 1
                    selectedCode += operations[index]
                values = []
                opened = False
                currentValue = ''
                for char in selectedCode:
                    if opened == True:
                        if char == ',':
                            values.append(currentValue)
                        else:
                            currentValue+= str(char)
                    else:
                        if char == "(":
                            opened = True

                values[-1] = values[-1][:-1]

        return str(args[0][0] + " = " + str(operations))

    def findStringManip(self, oper, stringOp):
        pass