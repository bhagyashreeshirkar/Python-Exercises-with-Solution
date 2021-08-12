"""
Largest Four

Have the function LargestFour(arr) take the array of integers stored in arr, and find the first four largest elements
and return their sum. For example if arr is [4, 5, -2, 3, 1, 2, 6, 6] then the four largest elements the array are
6, 6, 4 and 5 and the total sum of these numbers is 21, so your program should return 21.
If there are less than four numbers in the array your program should return the sum of all the numbers in the array.

Example1:
Input:
[1, 1, 1, -5]
Output:
-2

Example2:
Input:
[0, 0, 2, 3, 7, 1]
Output:
13
"""

def LargestFour(arr):
    sum1 = 0
    for i in arr:
        sum1 += i

    sorted_arr = sorted(arr, reverse=True)
    elements = sorted_arr[:4]
    sum2 = 0
    for j in elements:
        sum2 += j

    if len(arr) < 4:
        return sum1
    else:
        return sum2


print(LargestFour([4, 5, -2, 3, 1, 2, 6, 6]))
print(LargestFour([1, 1, 1, -5]))
print(LargestFour([0, 0, 2, 3, 7, 1]))
