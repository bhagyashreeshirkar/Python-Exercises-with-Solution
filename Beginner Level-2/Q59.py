"""
Write a python program that accepts an integer n and compute the value of n + nn + nnn.
Example:
Input:
n : 6
Output:
738 (6 + 66 + 666)

Input:
n : 5
Output:
615 (5 + 55 + 555)
"""

n = int(input('n: '))
a = n
b = (10*n) + a
c = (100*n) + b
print(a + b + c)
