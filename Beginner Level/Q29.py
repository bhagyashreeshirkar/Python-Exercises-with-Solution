"""
Write a Python program to compute the greatest common divisor (GCD) of two positive integers.
HCF/GCD = Highest(Greatest) common factor/Divisor(number) which divides both the numbers entered.

Mathematical logic-
For eg; 30, 45
factors of 30 = (5 * 3 * 2 * 1) ie; 5, 3, 2, 1
factors of 45 = (5 * 3 * 3 * 1) ie; 5, 3, 3, 1
from above 5, 3, 1 is common hence (5 * 3 * 1) = 15 is HCF of 30, 45.

Programming logic-
A number from range(1, min(30, 45)) ie, from range 1 to 30; gets divisible by both the numbers will get printed
(But we want only highest number among them hence, we write print condition outside the for loop to print last value.
"""

# Method-1
import math


def gcd(a1, a2):
    print('gcd:', math.gcd(a1, a2))


gcd(30, 45)
gcd(17, 12)


# Method-2
def hcf(n1, n2):
    value = 1  # you cannot directly assign a variable inside for loop(line 11).
    minNum = min(n1, n2)
    for number in range(1, minNum):
        if n1 % number == 0 and n2 % number == 0:
            value = number

    print(f'HCF of two numbers is {value}')
    # as we need only final(highest) number hence we print function outside if loop.
    # otherwise it'll print every single number which divides both the numbers.


hcf(30, 45)
hcf(17, 12)
