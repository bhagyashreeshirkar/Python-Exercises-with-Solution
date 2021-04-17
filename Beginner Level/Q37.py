"""
Write a Python program to compute the distance between the points (x1, y1) and (x2, y2).
The distance formula is √[(x2-x1)²+(y2-y1)²].
"""

import math


P = [4, 0]  # x1, y1
Q = [6, 6]  # x2, y2
distance = math.sqrt(((Q[0] - P[0])**2) + (Q[1] - P[1])**2)
print(f'Distance between two points are {distance}')
