"""
Write a Python program to calculate the sum of the digits in an integer.
Sample Example:
5245 = 5+2+4+5 = 16
"""

number = input('Enter a number: ')  # It'll accept the number as a string
sum = 0
for n in number:  # hence from string, consider 5245 it'll take first char 5 then 2 and so on..
    sum = sum + int(n)
print(sum)

