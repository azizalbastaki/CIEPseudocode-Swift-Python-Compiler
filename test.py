class compiler():
    def __init__(self,lang):
        self.language = lang
        self.scope = 0
    def compile(self,file):
        self.file = open(file,"r")
        for i in self.file:
            pass

    def __performDiagnosis(self,line):
        pass
    def __checkAssignment(self,line):
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