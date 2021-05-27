"""
Write a python program to find the addition of numbers upto n.
Sample Example:
if n = 4, then
output = 1 + 2 + 3 + 4 = 10
"""

n = int(input('Enter the value of n: '))
addition = 0
for num in range(1, n + 1):
    addition += num
print('Addition upto n is', addition)
