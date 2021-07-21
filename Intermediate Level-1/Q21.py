"""
Write a program to display following output.

Example:
Input: 1234
Output: 4321

Input: 1980
Output: 891

Input: 10400
Output: 401
(Note: If a number has trailing zeroes, then its reverse will not be include them.)
"""

s = input()

a = s[0]
final_s = ''
l = len(s)

if s[l-1] == '0':
    for i in s[1:]:
        if a == i:
            break
        else:
            final_s += a
            a = i
    print(final_s[::-1])
else:
    print(s[::-1])
