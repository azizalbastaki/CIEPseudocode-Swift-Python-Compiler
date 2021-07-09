#   ~Abdulaziz Albastaki July 2021
class compiler():
    def __init__(self,lang):
        self.language = lang
        self.scope = 0
        self.currentLine = ""
        print(self.checkAssignment("DECLARE SCm: STRING"))
    def compile(self,file):
        self.file = open(file,"r")
        for i in self.file:
            self.currentLine = i.strip()
    def __performDiagnosis(self,line):
        pass
    def checkAssignment(self,line):
        self.assignmentHolder = line.split()
        if self.assignmentHolder[0] == "DECLARE":
            identifer = self.assignmentHolder[1]
            datatype = ""
            if identifer[-1] == ":":
                identifer = identifer[0:-1]
                datatype = self.assignmentHolder[2]
            else:
                datatype = self.assignmentHolder[3]
            return (self.language.declareVariable(identifer, datatype))
    def checkSelection(line):
        pass
    def checkIteration(line):
        pass
    def checkMethods(line):
        pass
    def checkOperations(line):
        pass
    def checkFile(line):
        pass
    def checkUserDataTypes(line):
        pass
from swiftCompiler import swift5Compiler
from python3Compiler import python3Compiler
swiftComp = swift5Compiler()
pythonComp = python3Compiler()

swiftCom = compiler(swiftComp)
pythonComp = compiler(pythonComp)