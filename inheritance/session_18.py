import datetime


class Person(object):

    def __init__(self, name):
        """create a person called name"""
        self.name = name
        self.birthday = None
        self.lastName = name.split(' ')[-1]

    def setBirthday(self, month, day, year):
        """sets self's birthday to birthDate"""
        self.birthday = datetime.date(year, month, day)

    def getAge(self):
        """returns self's current age in days"""
        if self.birthday is None:
            raise ValueError
        return (datetime.date.today() - self.birthday).days

    def __lt__(self, other):
        """return True if self's name is lexicographically
           less than other's name, and False otherwise"""
        if self.lastName == other.lastName:
            return self.name < other.name
        return self.lastName < other.lastName

    # other methods

    def __str__(self):
        """return self's name"""
        return self.name


def main():
    p1 = Person('Mark Zuckerberg')
    p1.setBirthday(5, 14, 84)
    p2 = Person('Barack Obama')
    p2.setBirthday(8, 4, 61)
    p3 = Person('Bill Gates')
    p3.setBirthday(10, 28, 55)
    p4 = Person('Donald Trump')
    p5 = Person('Steve Wozniak')

    personList = [p1, p2, p3, p4]
    print(p1.__lt__(p2))

    for e in personList:
        print(e)

    personList.sort()

    print()

    for e in personList:
        print(e)

if __name__ == '__main__':
    main()  