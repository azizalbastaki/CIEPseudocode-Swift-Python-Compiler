#   ~Abdulaziz Albastaki July 2021
class compiler():
    def __init__(self,lang):
        self.language = lang
        self.scope = 0
        self.currentLine = ""
    def compile(self,file):
        self.file = open(file,"r")
        for i in self.file:
            self.currentLine = i.strip()
            pass

    def __performDiagnosis(self,line):
        pass
    def __checkAssignment(self,line):
        self.assignmentHolder = self.currentLine.split()
        if self.assignmentHolder[0] == "DECLARE":
            pass

    def __checkSelection(self,line):
        pass
    def __checkIteration(self,line):
        pass
    def __checkMethods(self,line):
        pass
    def __checkOperations(self,line):
        pass
    def __checkFile(self,line):
        pass
    def __checkUserDataTypes(self,line):
        pass