'''
def histogram(s):
    d = dict()
    
    for c in s:
        d[c] = d.get(c,0) + 1
    return d

h = histogram('Bookkeeper')
print(h)

def fib(n):
    global numFibCalls
    numFibCalls += 1
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return fib(n - 1) + fib(n - 2)


known = {1: 1, 2: 2}


def fib_efficient(n):
    global numFibCalls
    numFibCalls += 1
    if n in known:
        return known[n]
    else:
        ans = fib_efficient(n - 1) + fib_efficient(n - 2)
        known[n] = ans
        return ans


numFibCalls = 0
fibArg = 10


print(fib(fibArg))
print('function calls', numFibCalls)

numFibCalls = 0


print(fib_efficient(fibArg))
print('function calls', numFibCalls)


global variables is declared in the function
knowen is declared in the function


def store_word():
    d = dict()
    i = 0
    fin = open('words.txt')    
    for line in fin:
        d[line] = i
        i+=1
    return d
print(store_word())
'''
def has_duplicates(word_list):
    for a in word_list:
        if word_list.count(a)>0:
            return True
        else:
            return False

print(has_duplicates(list('bookkeeper')))
