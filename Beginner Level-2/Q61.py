"""
Write a python program to execute following conditions:
Print 'Yes' if the second number B is the last digits of A. Print 'No' otherwise.

Example1:
Input:
A: 5434554
B: 543
Output:
No

Example2:
Input:
A: 1234567
B: 567
Output:
Yes
"""

A = int(input('A: '))
B = int(input('B: '))

A = str(A)
B = str(B)
length = len(B)
reverse_of_A = A[-length:]
if reverse_of_A == B:
    print('Yes')
else:
    print('No')
