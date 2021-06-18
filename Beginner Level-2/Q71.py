"""
Write a program to count number of 1's in binary code of a number.

Example:
Input:
Number: 3
Output:
Number of 1's are in 0b11 are: 2
"""

num = int(input('Number: '))

binary_value = bin(num)
ones = 0
for n in str(binary_value):
    if n == '1':
        ones += 1

print(f"Number of 1's are in {binary_value} are:", ones)
