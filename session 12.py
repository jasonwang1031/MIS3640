
'''
def sumall(*numbers):
    t = sum(numbers)
    return t

print(sumall(1, 2.0))

def most_frequent(string):
    d = dict()
    for key in string:
        if key not in d:
            d[key] = 1
        else:
            d[key] += 1
    sorted(d)
    return d

def angrams():
    fin = open('words.txt')
    a = []
    for word in fin:
        n1 = word.strip()
        n2 = sorted(n1)
        b = ''.join(n2) 
        if b not in a:
            a.append(b)

    return a

def modified_angrams:
    def angrams():
    fin = open('words.txt')
    a = []
    for word in fin:
        n1 = word.strip()
        n2 = sorted(n1)
        b = ''.join(n2) 
        if b not in a:
            for i in a:
                if len(b) < len(i):
                    a.insert(len(i),b)
'''
import random

ROSTER = {"Beshansky": 0,
          "Collins": 0,
          "Fischer": 1,
          "Giovanucci": 0,
          "Jain": 0,
          "Kim": 0,
          "Lauture": 0,
          "Lee": 0,
          "Maddox": 0,
          "Martinez": 0,
          "Mendez": 0,
          "Oh": 0,
          "Petrone": 1,
          "Posada": 0,
          "Rule": 1,
          "Schilb": 0,
          "Tariq": 0,
          "Wang": 0,
          "Wolf": 0}


def call(roster):
    """
    Among the names that are called least times,
    print one name
    roster: a dict of names and integers

    TO-DO: update dict after every call
    TP-DO: save dict 
    """
    value_list = roster.values()
    min_value = min(value_list)

    name = []
    for key,value in roster.items():
        if value == min_value:
            name.append(key)
    return random.choice(names)


print(call(ROSTER))
