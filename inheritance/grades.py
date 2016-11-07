from session_18 import Person
from BabsonPerson import BabsonPerson
from Student import *

class Grades(Student):
    def __init__(self,name,grades):
        BabsonPerson.__init__(self,name)
        self.grades = grades
    
    def getGrades(self):
        return self.grades
