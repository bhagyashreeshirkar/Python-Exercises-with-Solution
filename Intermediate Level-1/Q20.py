"""
Write a program to return the difference between the sum of odd numbers and even numbers from an array of positive numbers.

Example:
Input:
5
10 11 7 12 14
Output:
-18
(Explanation: The first parameter (5) is the size of the array. Next is an array of integers.
The calculation of difference between sum of odd and even numbers are as follows: (11+7) - (10+12+14) = 18 - 36 = -18
"""

n = int(input())
arr = list(map(int, input().split()))

odd = 0
even = 0

for i in arr:
    if i % 2 == 0:
        even += i
    else:
        odd += i


print(odd - even)
