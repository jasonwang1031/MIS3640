import math


epsilon = 0.0000001
def mysqrt(a):
    x = a/2+1
    while True:
        y = (x + a/x) / 2
        if abs(y-x) < epsilon:
            break
        x= y
    return y

def text_square_root():
    print('a   ', 'mysqrt(a)      ','math.sqrt(a)   ', '    diff')
    for a in range (1,10,1):
        r = float(a)
        t = str(mysqrt(a))
        f = math.sqrt(a)
        d = mysqrt(a)-math.sqrt(a)
        if len(t) > 3:
            print(r,t,f,d)
        else:
            print(r,t,'             ',f,'              ',d)
print(text_square_root())