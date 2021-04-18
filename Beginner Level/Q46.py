"""
Write a python program to find the sum of the first n positive integers.
Sample Input: n = 8
Sample Output: 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 = 36
"""
n = int(input('Enter the value of n: '))
sum = 0
for i in range(1, n+1):
    sum = sum + i
print(f'Sum upto {n} is {sum}')
