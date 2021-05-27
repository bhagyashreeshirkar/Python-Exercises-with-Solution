"""
Write a python program to check whether a number is Fibonacci number or not
Fibonacci series: 0 1 1 2 3 5 8 13 21 ,..
"""


def check(num):
    a, b = 0, 1
    d = 1
    c = []
    while d <= num:
        d = a + b
        c.append(d)
        a, b = b, d
    if num in c:
        return True
    else:
        return False


print(check(13))
print(check(4))
print(check(23))
print(check(21))
