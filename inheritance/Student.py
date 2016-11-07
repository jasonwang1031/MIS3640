from BabsonPerson import BabsonPerson
from session_18 import Person


class Student(BabsonPerson):
    pass


class UG(Student):

    def __init__(self, name, classYear):
        BabsonPerson.__init__(self, name)
        self.year = classYear

    def getClass(self):
        return self.year

    def speak(self, utterance):
        return BabsonPerson.speak(self, " Dude, " + utterance)


class Grad(Student):
    pass


def isStudent(obj):
    return isinstance(obj, Student)


def main():
    s1 = UG('Hunter Schilb', 2017)
    s2 = UG('Wendy Posada', 2017)
    s3 = UG('Jason Wang', 2018)
    s4 = Grad('Matt Damon')

    studentList = [s1, s2, s3, s4]

    print(s1)

    print(s1.getClass())

    print(s1.speak('where is the quiz?'))

    print(s2.speak('I have no clue!'))

    print(s4.speak('I am not sure why I am here.'))

if __name__ == '__main__':
    main()