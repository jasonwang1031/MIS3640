
list_1=[10,20]

AFC_east = ['New England Patriots', 'Buffalo Bills','Miami Dolphins','New York Jets']

a_nested_list = ['spam', 2.0, 5, [10, 20]]
print(AFC_east)
print(AFC_east)

print(AFC_east[0:2])
print(AFC_east[-3:])

'''
L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', ['Ruby','On Rail'], 'PHP'],
    ['Adam', 'Bart', 'Lisa']
    
]

print(L[1][2][1])

a = [1,2,3]
b=[4,5,6]
c = a + b
print (c)

'''



"""
    Computes the total of all numbers in a list of lists.
    t: list of list of numbers
    returns: number
    Expected output:
    >>> t = [[1, 2], [3], [4, 5, 6]]
    >>> nested_sum(t)
    21


def capitalize_all(t):
    res = []
    for s in t:
        res.append(s.capitalize())
    return res
print(capitalize_all('jason'))


t = ['a', 'b', 'c', 'd']
x = t.pop(1)
print(x)
print(t)

t = ['a', 'b', 'c', 'd', 'e']
del t[1:3]
print(t)

team = 'Patriots'
t = list(team)
print(t)

team = 'New England Patriots'
t = team.split()
print(t)

s = 'spam-spam-spam'
delimiter = '-'
t = s.split(delimiter)
print(t)

a = [1, 2, 3]
b = [1, 2, 3]
print(a is b)


a = b
b[0] = 'something else'
print(a)
"""

