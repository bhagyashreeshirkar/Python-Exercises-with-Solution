"""
Write a python program to check whether a number is perfect square or not.
"""
import math

def check(num):
    a = int(math.sqrt(num))  # to avoid float values we convert it into int or a = int(num ** 0.5)
    if a * a == num:
        print(f'{num} is perfect square of {a}.')
    else:
        print(f'It is not perfect square.')


check(144)
check(529)
check(34)

'''
Logic- 
step1: first it takes a square root of user entered value 
step2: after that it checks, whether the square of value is equal to the user entered value or not.
       if is equal to the square of value then it is perfect square otherwise not.

consider, num = 144
          square root of 144 is 12
          if 12 * 12 == num then it is perfect square
          else It is not perfect square
'''
