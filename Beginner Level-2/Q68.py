"""
Write a program to replace brackets.

Example1:
Input:
[2, 5, 1, 67, 90, 21]
Output:
{2, 5, 1, 67, 90, 21}

Example2:
Input:
[4, 21, 34, 41]
Output:
(4, 21, 34, 41)

"""
x = [2, 5, 1, 67, 90, 21]
x = str(x)
print(x.replace('[', '{').replace(']', '}'))

y = [4, 21, 34, 41]
y = str(y)
print(y.replace('[', '(').replace(']', ')'))

'''
Note: replace function is only applicable for strings hence we covert a list in string to replace the brackets.
'''
