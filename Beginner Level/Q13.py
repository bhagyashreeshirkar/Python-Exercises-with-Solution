"""
Write a Python program to calculate number of days between two dates.
Sample dates : (2021, 4, 15), (2021, 5, 16)
Expected output : 31
"""

from datetime import date

a = date(2021, 4, 15)
b = date(2021, 5, 16)
c = b - a
print('number of days between two dates are', abs(c.days))
