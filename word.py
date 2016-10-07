'''
def read_long_words():
    fin = open('words.txt')
    for line in fin:
#https://docs.python.org/3/library/functions.html#repr
        word = line.strip()
        if len(word)>20:
            print(word)

read_long_words()


def has_no_e(word):
    for c in word:
        if c !='e':
            return True
        else:
            return False
print(has_no_e('jason'))


def avoids(word,letter):
    for c in word:
        if c != letter:
            return True
        else:
            return False

def uses_only(word,available):
    for c in word:
        if c not in available
            return True
        else:
            return False
'''
fin = open('words.txt')
for line in fin:
    word = line.strip()
    print(word)
    print(type(line))
