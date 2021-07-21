"""
Write a program to calculate and return the sum of distances between the adjacent numbers in an array of positive integers.

Example:
Input:
5
10 11 7 12 14
Output:
12

(Explanation: The first parameter(5) is the size of an array. Next is an array of integers.
The total of distances is 12 as per the calculation below:
10-11=1
11-7=4
7-12=5
12-14=2
Total distance = 1+4+5+2 =12)
"""

n = int(input())
arr = list(map(int, input().split()))[:n]

temp = arr[0]
total_distance = 0

for i in arr[1:]:
    total_distance += abs(temp - i)
    temp = i


print(total_distance)
