"""
Write a program to find a missing number of an array.
Example:
Input:
Array: 3 2 1 7 5 4 9
Output:
6 8
"""

array = list(map(int, input('Array: ').split(' ')))
num = max(array)
list = []
for n in range(1, num+1):
    if n not in array:
        print(n, end=' ')
