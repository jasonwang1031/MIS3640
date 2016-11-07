from session_18 import Person
from BabsonPerson import BabsonPerson


def main():
    b3 = BabsonPerson('Mark Zuckerberg')
    b3.setBirthday(5, 14, 84)
    b2 = BabsonPerson('Barack Obama')
    b2.setBirthday(8, 4, 61)
    b1 = BabsonPerson('Bill Gates')
    b1.setBirthday(10, 28, 55)

    BabsonPersonList = [b1, b2, b3]

    for everyone in BabsonPersonList:
        print(everyone)
        print(everyone.speak('how are you?'))

    BabsonPersonList.sort()

    for everyone in BabsonPersonList:
        print(everyone)
        print(everyone.speak('how are you?'))

    p4 = Person('Donald Trump')
    p5 = Person('Steve Wozniak')

    personList = BabsonPersonList + [p4, p5]

    for everyone in personList:
        print(everyone)
        print(everyone.speak('how are you?'))

if __name__ == '__main__':
    main()