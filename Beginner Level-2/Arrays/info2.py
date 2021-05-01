"""
type code -
https://www.geeksforgeeks.org/array-python-set-1-introduction-functions/
(must be b, B, u, h, H, i, I, l, L, q, Q, f or d)
"""

from array import *

# int
a = array('i', [-10, 34, -12, 22, 90])
b = array('I', [10, 34, 12, 22, 90])
print(a)
print(b)

# float
c = array('f', [10, -3.4, 1.2, -22.0, -9.0])
d = array('f', [10, 3.4, 1.2, 22.0, 9.0])
print(c)
print(d)

# unicode character
e = array('u', ['a', '7', 'c'])
print(e)
