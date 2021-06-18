"""
Given an array, find the second largest integer. If there exists no second largest integer, return -1.
Example1:
Input:
arr: 34
Output:
-1

Example2:
Input:
arr: 4, 7, 8, 19, 10, 19, 7
Output:
10
"""
arr = list(map(int, input('arr: ').split(',')))
arr = set(arr)

if len(arr) > 1:
    sort_arr = sorted(list(arr))
    # print(sort_arr)
    print(f'second largest number in the list is:', sort_arr[-2])
else:
    print('-1')
