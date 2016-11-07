from BabsonPerson import BabsonPerson
from session_18 import Person

class Professor(BabsonPerson):
    def __init__(self, name, division):
        BabsonPerson.__init__(self,name)
        self.division = division

    def getdivision(self):
        return self.division
    
    def speak(self,utterance):
        return BabsonPerson.speak(self,'hi, everyone'+utterance)

p1 = Professor('Zhi Li','MIS')
print(p1)
print(p1.getdivision())