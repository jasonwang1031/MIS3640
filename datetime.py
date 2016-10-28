from datetime import *


def today():
    n = date.today()
    day = n.isoweekday()
    print("today is the day %d of the week"%day)

today()

def time_to_birthday(birthday):
    now = datetime.today()
    if now > datetime(now.year,birthday.month,birthday.day):
        age = now.year - birthday.year
        next_birthday = datetime(now.year+1,birthday.month,birthday.day) - now
    else:
        age = now.year - birthday.year - 1
        next_birthday = datetime(now.year,birthday.month,birthday.day) - now
    hour,remaining = divmod(next_birthday.seconds,3600)
    minutes,seconds = divmod(remaining,60)
    print("you are %d years old"%age)
    print("You have %d days, %d hours, %d minutes, %d seconds left until your next birthday."%(next_birthday.days,hour,minutes,seconds))

birthday=datetime(1995,10,31)
time_to_birthday(birthday)


def Double_Day(people1,people2):
    #assume people1 is always order
    a = (people2 - people1).days
    i = 0
    while i*2 <a:
        i+=1
        a+=1
    double = people2 + timedelta(i)
    print('Their Double Day is:',double)


people1 = date(1995,10,28)
people2 = date(1995,10,31)
#Double_Day(people1,people2)


def n_day(people1,people2,n):
     #assume people1 is always order
    a = (people2 - people1).days
    i = 0
    while i*n <a:
        i+=1
        a+=1
        if i*n>a:
            print('this day does not exist')
            return None
    n_days = people2 + timedelta(i)
    print('On',n_days,', the person1 is %d times older than the person2.' %n)

people1 = date(1995,10,28)
people2 = date(1995,10,31)
n_day(people1,people2,5)
