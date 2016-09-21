""""
Weight = 70
Height = 1.8

BMI = Weight / Height**2

if BMI >= 25:
    print('your bmi is %.1f. You need to burn your fat' %BMI)
elif BMI >= 18.5:
    print('your bmi is %.1f. You are all right' %BMI)
else:
    print('your bmi is %.1f. You need to gain more weight' %BMI)

def print_n(s, n):
    if n<=0:
        return
    print(s)
    print_n(s,n-1)

print_n("Jason",10)

def fact(n):
    result = 1
    if n == 1:
        return 1
    print(n)
    result = n * fact(n-1)
    return result
print(fact(5))


def fib(n):
    if n == 1:
        return 1
    if n == 2:
        retun 1
    return fib(n-1) + fib (n-2) 
"""
def countdown(n):
    if n <= 0:
        print('Blastoff!')
    else:
        countdown(n-1)        
        print(n)

print(countdown(5))
       