"""
Write a Python program to calculate midpoints of a line
Sample Test:
(x1, y1) = (-6, 8)
(x2, y2) = (6, -7)
Answer = (0.0, 5.0)
"""

x1 = float(input('x1: '))
y1 = float(input('y1: '))
x2 = float(input('x2: '))
y2 = float(input('y2: '))

x = (x1 + x2) / 2
y = (y1 + y2) / 2

print(f'midpoint: {x, y}')
