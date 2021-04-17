"""
Write a Python program to compute the simple interest and compound interest of a specified principle amount, rate of interest, and a number of years.
Test Data : principle amount = 10000, rate of interest = 3.5, no of years = 7
Expected Output :
2450.0
2722.79
"""


def data(p, r, n):
    SI = (p * r * n) / 100
    a = p * ((1 + r / 100) ** n)
    CI = a - p

    print('Simple Interest of specified data is', SI)
    print('Compound Interest of specified data is', round(CI, 2))


data(10000, 3.5, 7)
