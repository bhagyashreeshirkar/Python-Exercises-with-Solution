"""
Write a Python program to find the number of zeros at the end of a factorial of a given positive number.
Range of the number(n): (1 ≤ n ≤ 2*109).
Sample Example:
5! = 120, Output = 1
12! = 479001600, Output = 2
"""

def fact_end_zero(num):
    fact = 1
    count = 0
    for i in range(1, num+1):
        fact *= i
    print(f'factorial of {num} is', fact)

    fact = str(fact)  # as we need to use list comprehension which can only applied on strings thus, we covert factorial into string

    for n in fact[::-1]:  # to run a string in reverse direction
        if n != '0':
            break  # it'll exit the loop as soon as it'll rectify any non-zero number from back(reverse)
        else:
            count +=1
    print(f'total zeroes at the end of factorial is', count)


fact_end_zero(5)
fact_end_zero(12)
fact_end_zero(100)
