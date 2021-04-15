"""
Write a Python program to get a new string from a given string where "Is" has been added to the front.
If the given string already begins with "Is" then return the string unchanged.
Sample Input :
Array    IsEmpty
Sample Output :
IsArray
IsEmpty
"""


def statement(string):
    if 'Is' in string:
        return string
    else:
        return f'Is{string}'


print(statement('Array'))
print(statement('IsEmpty'))
