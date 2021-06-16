"""
Write a program to find sum of uncommon numbers among two arrays.
Example1:
Input:
arr1: 9 -4 3 2 -5
arr2: 2 -5 7 9
Output:
6

Example2:
Input:
arr1: 4 8 3 6 2 7
arr2: 9 7 4 2 3 5 1
Output:
29
"""

arr1 = list(map(int, input('arr1: ').split(' ')))
arr2 = list(map(int, input('arr2: ').split(' ')))
num = []
for n in arr1:
    if n not in arr2:
        num.append(n)
for i in arr2:
    if i not in arr1:
        num.append(i)
# print(num)
print(sum(num))
