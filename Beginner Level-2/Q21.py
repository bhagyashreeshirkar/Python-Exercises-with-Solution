"""
Write a Python program to get the Fibonacci series between 0 to 50.
Note : The Fibonacci Sequence is the series of numbers :
0, 1, 1, 2, 3, 5, 8, 13, 21, ....
Every next number is found by adding up the two numbers before it.
Expected Output : 1 1 2 3 5 8 13 21 34
"""

# method-1

n1 = 0
n2 = 1
n3 = 1
while n3 < 50:
    print(n3, end=' ')
    n3 = n1 + n2
    n1 = n2
    n2 = n3


print()  # To print method-2 on next line


# Method-2
a, b = 0, 1
while b < 50:
    print(b, end=' ')
    a, b = b, a + b
