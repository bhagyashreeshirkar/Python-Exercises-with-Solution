"""
Write a Python program to calculate the hypotenuse of a right angled triangle.
c = √(a² + b²)
"""
import math

side1 = int(input('Enter base side of a triangle: '))
side2 = int(input('Enter perpendicular side of a triangle: '))
hypotenuse = math.sqrt(side1 ** 2 + side2 ** 2)
print('Hypotenuse of specified triangle is', hypotenuse)
