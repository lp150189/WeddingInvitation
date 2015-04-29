class Record:
    def __init__(self, name, numPpl,maybe):
        self.name = name
        self.numPpl = numPpl
        self.maybe = maybe

    def getNumPpl(self):
        return self.numPpl

    def getName(self):
        return self.name
    
    def getMaybe(self):
        return self.maybe
