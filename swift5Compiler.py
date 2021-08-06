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
    
    def assignVariable(self, *args):
            operations = ""
            for i in range(2,len(args[0])):
                operations+= str(args[0][i])
            return str(args[0][0] + " = " + str(self.translateOperations(operations)))

    def translateOperations(self, operationsParameter):
        operations = operationsParameter
        operations = operations.replace("<>", "!=")
        operations = operations.replace(" AND ", " and ")
        operations = operations.replace("&", "+")
        operations = operations.replace(" NOT ", " not ")
        operations = operations.replace(" OR ", " or ")
        operations = operations.replace("=", "==")
        self.operationChanges = True
        while self.operationChanges == True:
            self.operationChanges = False
            if "RIGHT(" in operations:
                parameters = self.findStringParameterValues(operations, "RIGHT(")
                replacementCode = str(parameters[0]) + ".prefix(" + str(int(parameters[1])) + ")"
                operations = operations.replace(self.findSelectedCode(operations, "RIGHT("),replacementCode)
                self.operationChanges = True
            if "LENGTH(" in operations:
                parameters = self.findStringParameterValues(operations, "LENGTH(")
                replacementCode = str(parameters[0]) + ".count"
                operations = operations.replace(self.findSelectedCode(operations, "LENGTH("),replacementCode)
                self.operationChanges = True
            if "MID(" in operations:
                parameters = self.findStringParameterValues(operations, "MID(")
                replacementCode = str(parameters[0]) + ".prefix(" + str(int(parameters[1]) + int(str(parameters[2])) - 1) + ").suffix(" + str(parameters[2]) + ")"
                operations = operations.replace(self.findSelectedCode(operations, "MID("),replacementCode)
                self.operationChanges = True
            if "LCASE(" in operations:
                parameters = self.findStringParameterValues(operations, "LCASE(")
                replacementCode = str(parameters[0]) + ".lowercased()"
                operations = operations.replace(self.findSelectedCode(operations, "LCASE("),replacementCode)
                self.operationChanges = True
            if "UCASE(" in operations:
                parameters = self.findStringParameterValues(operations, "UCASE(")
                replacementCode = str(parameters[0]) + ".uppercased()"
                operations = operations.replace(self.findSelectedCode(operations, "UCASE("),replacementCode)
                self.operationChanges = True
            operations = self.decreaseIndex(operations)
            return operations

    def findStringParameterValues(self, oper, stringOp):
        selectedCode = self.findSelectedCode(oper,stringOp)
        values = []
        opened = False
        currentValue = ''
        for char in selectedCode:
            if opened == True:
                if char == ',':
                    values.append(currentValue)
                    currentValue = ""
                else:
                    currentValue+= str(char)
            else:
                if char == "(":
                    opened = True
        values.append(currentValue)
        values[-1] = values[-1][:-1]
        return values

    def findSelectedCode(self,oper,stringOp):
        index = oper.find(stringOp)
        selectedCode = oper[index]
        while oper[index] != ")":
            index += 1
            selectedCode += oper[index]
        return selectedCode

    def decreaseIndex(self,oper):
        values = oper
        opened = False
        for i in range(0, len(values)):
            if not opened:
                if values[i] == "[":
                    opened = True
            else:
                if values[i] == "]":
                    opened = False
                else:
                    try:
                        newInt = str(int(values[i]) -1)
                        values = values[:i] + str(newInt) + values[i+1:]
                    except:
                        pass
        return values