

class compiler():
    def __init__(self,lang):
        self.language = lang

    def compile(self,file):
        self.file = open(file,"r")

        for i in self.file:
            pass