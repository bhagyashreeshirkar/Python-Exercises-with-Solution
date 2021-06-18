"""
Write a program to sort an array of given integers.
Display the original array elements and sorted array elements as shown in sample output.

Example:
Input:
7
7 -5 3 2 1 0 45
Output:
Original Array
[7, -5, 3, 2, 1, 0, 45]
Sorted Array
[-5, 0, 1, 2, 3, 7, 45]
"""

num = int(input())
values = list(map(int, input().split(',')))[:num]
print('Original Array:\n', values)


# Method1 (by using function)
print('Sorted Array:\n', sorted(values))


# Method2 (without using function)
arr = []
for i in range(len(values)):
    min_num = min(values)
    arr.append(min_num)
    values.remove(min_num)
print(arr)
