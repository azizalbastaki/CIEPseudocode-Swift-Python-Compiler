#   ~Abdulaziz Albastaki July 2021
class compiler():
    def __init__(self,lang):
        self.language = lang
        self.scope = 0
        self.currentLine = ""
        print(self.checkAssignment('HELLO <-- (WHAT+WHAT)<>23'))
    def compile(self,file):
        self.file = open(file,"r")
        for i in self.file:
            self.currentLine = i.strip()
    def performDiagnosis(self,line):
        pass
    def checkAssignment(self,line):
        self.assignmentHolder = line.split()
        if self.assignmentHolder[0] == "DECLARE":
            identifer = self.assignmentHolder[1]
            if identifer[-1] == ":":
                identifer = identifer[0:-1]
                datatype = self.assignmentHolder[2]
            else:
                datatype = self.assignmentHolder[3]
            return (self.language.declareVariable(identifer, datatype))
        if self.assignmentHolder[0] == "CONSTANT":
            identifer = self.assignmentHolder[1]
            constantValue = self.assignmentHolder[3]
            return (self.language.declareConstant(identifer, constantValue))
        if self.assignmentHolder[1] == "<--":
            return (self.language.assignVariable(self.assignmentHolder))

    def checkSelection(self,line):
        pass
    def checkIteration(self,line):
        pass
    def checkMethods(self,line):
        pass
    def checkOperations(self,line):
        pass
    def checkFile(self,line):
        pass
    def checkUserDataTypes(self,line):
        pass
    def checkComments(self,line):
        pass
from swift5Compiler import swift5Compiler
from python3Compiler import python3Compiler
swiftComp = swift5Compiler()
pythonComp = python3Compiler()

#swiftCom = compiler(swiftComp)
pythonComp = compiler(pythonComp)