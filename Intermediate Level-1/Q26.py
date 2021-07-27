"""
Write a program to display following output.

Input format:
The first line of input contains N.
The second line of input contains N elements separated by a single white space.
The last line of input contains K.

Output Format:
The output contains the sum S.

Example:
Input:
6
198 567 345 9234 11 6
18

Output:
9999
(Explanation: Array A with the 6 elements is given and K=18.
The sum of digits of 198(1+9+8), 567(5+6+7) and 9234(9+2+3+4) is 18. The order elements digits do not add upto 18.
Therefore, the output is the sum of these three elements: 198+567+9234 = 9999.)
"""

n = int(input())
arr = list(map(int, input().split()))[:n]
k = int(input())

f = 0
possibilities= []

for num in arr:
    for i in str(num):
        f += int(i)
    # print(f)
    temp = f
    f = 0
    if temp == k:
        possibilities.append(num)  # thus it will append the num whose addition gets equal to k


# print(possibilities)
print(sum(possibilities))  # Method-1


# Method-2
addition = 0
for c in possibilities:
    addition += c
print(addition)
