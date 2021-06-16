"""
PALINDROME OF A NUMBER- (Palindrome numbers remain the same whether written forward or backwards)
Write a Python program to find a given number is palindrome or not.
Sample Input:
1221
11
74747
231

Sample Output:
1221 is a Palindrome number
11 is a Palindrome number
74747 is a Palindrome number
231 is not a Palindrome number
"""

def number(num):
    num = str(num)
    temp = str(num)[::-1]
    if num == temp:
        return f'{num} is a Palindrome number'
    else:
        return f'{num} is not a Palindrome number'


print(number(1221))
print(number(11))
print(number(74747))
print(number(231))
