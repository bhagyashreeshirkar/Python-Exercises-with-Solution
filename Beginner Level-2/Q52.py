"""
GREATEST COMMON DIVISOR or HIGHEST COMMON FACTOR -
Write a Python program to find common divisors between two numbers in a given pair.

Sample Input:
number1 = 336
number2 = 360
Sample Output:
336 = 2*2*2*2*3*7
360 = 2*2*2*3*3*5
GCD of two Numbers: 2*2*2*3 = 24
"""

# Method1 (By using inbuilt function)
from math import *


def value(num1, num2):
    print(f'GCD of two Numbers: ', gcd(num1, num2))


value(360, 336)
value(12, 24)
value(8, 2)


# Method2 (Without using inbuilt function)
def gcd(number1, number2):
    num = max(number1, number2)
    a = []
    for n in range(2, num):
        if number1 % n == 0 and number2 % n == 0:
            a.append(n)
    print(max(a))


gcd(336, 360)
gcd(24, 12)
gcd(2, 8)
