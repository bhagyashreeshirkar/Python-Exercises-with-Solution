"""
Write a Python program to find the median among three given numbers.
"""

x, y, z = map(int, input('Enter three numbers: ').split())
a = [x, y, z]
b = sorted(a)
print('median among three given numbers is', b[1])
