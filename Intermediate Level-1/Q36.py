"""
Write a program to find number of trailing zeroes in a given integer.

Example1:
Input:
1000
Output:
3

Example2:
Input:
201300000
Output:
5
"""

def trailingZeroes(num):
    new_num = ''

    for i in str(num)[::-1]:
        new_num += i
    # return new_num

    count = 0
    for n in new_num:
        if n != '0':
            break
        elif n == '0':
            count += 1
    return count

print(trailingZeroes(1000))
print(trailingZeroes(201300000))
print(trailingZeroes(90800210))
