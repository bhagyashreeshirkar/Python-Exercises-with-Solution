"""
Write a Python program to calculate body mass index.
"""

weight = float(input('Enter your weight in kg: '))
height = float(input('Enter your height in m: '))
bmi = (weight / (height * height))

print('Your body mass index(BMI) is', round(bmi, 2))
