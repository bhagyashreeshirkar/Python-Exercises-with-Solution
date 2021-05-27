"""
Write a python program to check whether a number is prime or not.
"""


def check(number):
    for num in range(2, number):
        if number % num == 0:
            print(f'{number} is a not prime number')
            break
    else:
        print(f'{number} is a prime number')


a = int(input('Enter a number: '))
check(a)
