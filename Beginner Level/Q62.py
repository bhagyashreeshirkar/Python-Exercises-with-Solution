"""
Write a Python program to check whether a file path is a file or a directory.
"""
import os


def value(path):
    if os.path.isfile(path):
        return 'Path entered is a file.'
    elif os.path.isdir(path):
        return 'Path entered is a directory.'
    else:
        return 'Invalid Path'


print(value('C:/Users/Rsc/PycharmProjects/pythonProject/venv'))
print(value('Gif.py'))
print(value('Q12.py'))
