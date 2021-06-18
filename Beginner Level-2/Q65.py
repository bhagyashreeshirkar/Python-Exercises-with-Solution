"""
Write a program to print sum of divisors of user entered number.
"""

def sum_of_divisors(num):
    divisors = []
    for i in range(1, num+1):
        if num % i == 0:
            divisors.append(i)
    print(f'sum of divisors:', sum(divisors))


n = int(input())
sum_of_divisors(n)
