from session_18 import Person
from BabsonPerson import BabsonPerson
from Student import *

# TODO: add more testing code


def main():
    s1 = UG('Hunter Schilb', 2017)
    s2 = UG('Wendy Posada', 2017)
    s3 = UG('Jason Wang', 2018)
    s4 = Grad('Matt Damon')
    s5 = UG('Mark Zuckerberg', 2019)
    p1 = BabsonPerson('Zhi Li')
    p2 = BabsonPerson('Shankar')
    p3 = BabsonPerson('Steve Gordon')
    q1 = Person('Bill Gates')
    q2 = Person('Beyonce')

    studentList = [s1, s2, s3, s5, s4]
    BabsonList = studentList + [p1, p2, p3]
    allList = BabsonList + [q1, q2]

    #for everyone in studentList:
     #   print(everyone)

    for everyone in BabsonList:
        print(everyone)
        print(everyone.speak('happy holidays'))


    #for everyone in allList:
     #   print(everyone)
if __name__ == '__main__':
    main()