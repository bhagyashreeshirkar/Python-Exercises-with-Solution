"""
Write a Python program to determine whether a given year is a leap year.
"""

def verify(year):
    if (year % 4 == 0 and year % 100 == 0 and year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        print(f'{year} is a leap year.')
    else:
        print(f'{year} is not a leap year.')


verify(2017)
verify(1900)
verify(2012)
verify(2000)
verify(1992)
verify(1997)

'''
leap year : (year is divisible by 4) and (year is divisible by 100) and (year is divisible by 400)
            or
            (year is divisible by 4) but/or (year is not divisible by 100) 
'''
