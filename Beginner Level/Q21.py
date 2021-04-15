"""
Write a Python program to get the n copies of the first 3 characters of a given string.
Return the n copies of the whole string if the length is less than 3.
Sample Input:
('This is Mike', 4), ('Hi', 3)
Sample Output:
ThiThiThiThi
HiHiHi
"""


def string_value(statement, n):
    for i in range(1, n + 1):
        if len(statement) >= 3:
            print(statement[0:3], end='')
        else:
            print(statement, end='')
    print()


string_value('This is Mike', 4)
string_value('Hi', 3)
