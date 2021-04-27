"""
Write a Python program to count the number of strings where the string length is 2 or more and the first
and last character are same from a given list of strings. Go to the editor
Sample List : ['abc', 'xyz', 'aba', '1221']
Expected Result : 2
"""


def enter(values):
    temp = 0
    for string in values:
        if len(string) >= 2:
            if string[0] == string[-1]:
                temp += 1
    print(temp)


enter(['abc', 'xyz', 'aba', '1221'])
enter(['strips', 'pop', 'y', 'lemon', 'bomb'])
