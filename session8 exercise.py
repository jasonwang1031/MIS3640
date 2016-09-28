'''
cube = 54
epsilon = 0.01
num_guesses = 0
low = 0
high = cube
guess = (high + low) / 2.0

while abs(guess**3 - cube) >= epsilon:
    print('low ='+ str(low)+'high = '+ str(high) + 'guess =' + str(guess))
    num_guesses += 1
    if guess**3 < cube:
        low = guess
    else:
        high = guess
    guess = (low + high)/2

print('num_guesses = ' + str(num_guesses))
print(str(guess) + ' is close to cubic root of ' + str(cube))

# exercise 2
def count(word,A):
    count = 0
    for letter in word:
        if letter == A:
            count += 1
    print(count)

count('superjason','s')

# exercise 3

team = 'Boston-Celtics-Team'
print(team.split('-',1))
print(team.split('-',2))
print(team.split())
print(team)

print(team.strip())
print(team.strip('Bosam'))

print(team.replace('t','j'))
print(team.replace('t','j',2))

#exercise 4
def price(n):
    letter = 0
    p = 0 
    while letter < len(n):
        p += ord(n[letter]) - 96
        letter += 1
    print(n,'$'+str(p))

price('bananas')
price（'rice')
price('paprika')
price('potato chips')
print("------------------------")
print('Total','$237')

    
def price(n):
    letter = 0
    p = 0 
    while letter < len(n):
        p += ord(n[letter]) - 96
        letter += 1
    print('{:16}{:3}'.format(n,'$'+str(p)))
    

    
price('bananas')
price('rice')
price('paprika')
price('potato chips')
print("--------------------")
print('{:16}{:3}'.format('Total','$237'))

def price(n):
    letter = 0
    p = 0 
    while letter < len(n):
        p += ord(n[letter]) - 96
        letter += 1
    return p

def recepit(a,b,c):
    length = max(len(a),len(b),len(c))+4 
    
   
    print('{:i}{:3}'.format(a,price(a)))
    print('{:i}{:3}'.format(b,price(b)))
    print('{:i}{:3}'.format(c,price(c)))

recepit('bananas','rice','paprika')
'''

def rotate_letter(letter, a):
    b = ord(letter) - 97
    c = (a + b) % 26 + 97
    return chr (c)
def rotate_word(word,a):
    new_word = ''
    for letter in word:
        new_word += rotate_letter(letter,a)
    print(new_word)

rotate_word('cheer',7)

    