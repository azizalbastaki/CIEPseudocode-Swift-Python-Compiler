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
                parameters = self.findStringModValues(operations,"RIGHT(")
                replacementCode = str(parameters[0]) + "[-" + str(int(parameters[1])-1) + ":]"
                operations = operations.replace(self.findSelectedCode(operations, "RIGHT("),replacementCode)
                operationsChanges = True
            if "LENGTH(" in operations:
                parameters = self.findStringModValues(operations,"LENGTH(")
                replacementCode = "len(" + str(parameters[0]) + ")"
                operations = operations.replace(self.findSelectedCode(operations, "LENGTH("),replacementCode)
                operationsChanges = True
            if "MID(" in operations:
                parameters = self.findStringModValues(operations,"MID(")
                replacementCode = str(parameters[0]) + "[" + str(parameters[1] + ":" + str(int(parameters[1]) + int(parameters[2]))) + "]"
                operations = operations.replace(self.findSelectedCode(operations, "MID("),replacementCode)
                operationsChanges = True
            if "LCASE(" in operations:
                parameters = self.findStringModValues(operations,"LCASE(")
                replacementCode = str(parameters[0]) + ".lower()"
                operations = operations.replace(self.findSelectedCode(operations, "LCASE("),replacementCode)
                operationsChanges = True
            if "UCASE(" in operations:
                parameters = self.findStringModValues(operations,"UCASE(")
                replacementCode = str(parameters[0]) + ".upper()"
                operations = operations.replace(self.findSelectedCode(operations, "UCASE("),replacementCode)
                operationsChanges = True

        operations = self.decreaseIndex(operations)
        return str(args[0][0] + " = " + str(operations))

    def findStringModValues(self, oper, stringOp):
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