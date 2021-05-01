"""
Write a Python program to construct the following pattern.
*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*
"""

number = int(input(f'number: '))

# without using nested for loop
for i in range(1, number):
    print('* ' * i)
for j in range(number, 0, -1):
    print('* ' * j)
