"""
Write a Python program to get the third side of right angled triangle from two given sides.
"""
import math

side = input('type H to find Hypotenuse; type O to find Opposite side; type A to find Adjacent side: ')
if side == 'H':
    o, a = map(int, input('Enter opposite and adjacent sides:').split(','))
    h_sqr = o ** 2 + a ** 2
    h = math.sqrt(h_sqr)
    print(f'value of hypotenuse is:', h)
elif side == 'O':
    h, a = map(int, input('Enter hypotenuse and adjacent sides:').split(','))
    o_sqr = h ** 2 - a ** 2
    o = math.sqrt(o_sqr)
    print(f'value of opposite side is:', o)
elif side == 'A':
    h, o = map(int, input('Enter hypotenuse and opposite sides:').split(','))
    a_sqr = h ** 2 - o ** 2
    a = math.sqrt(a_sqr)
    print(f'value of adjacent side is:', a)
else:
    print('Invalid Input')
