"""
Write a Python program to convert height (in foot and inches) to centimeters.
Sample Example:
foot : 5
inches: 2.6
Your height in centimeters is 159.0
"""

print('Enter your height in foot and inches-')

height_ft = int(input('foot : '))
height_inches = float(input('inches: '))

inches = height_inches + height_ft * 12
cm = inches * 2.54

print('Your height in centimeters is', round(cm, 1))
