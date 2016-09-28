# question 3
def sum_squares(n):
    a = 0
    x = 1
    while x < n+1:
        a += x*x
        x += 1
    return a

print(sum_squares(5))