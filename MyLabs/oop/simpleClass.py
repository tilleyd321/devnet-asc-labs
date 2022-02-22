class SimpleClass ():
    
    classVariable="same for all instances"

    def __init__ (self, pInstanceVariable):
        self.instanceVariable = pInstanceVariable

    def SimpleClassReportMethod(self):
        print("ClassVariable=", self.classVariable)
        print("instanceVariable=",self.instanceVariable)

class AnotherClass():
    def __init__ (self):
        print("Another Class")

