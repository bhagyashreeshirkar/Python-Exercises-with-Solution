"""
Write a Python program to get a directory listing, sorted by creation date.
"""

import os
import glob

# '*/' pattern is used to return only directories.
directories = glob.glob('C:\\Users\\Rsc\\PycharmProjects\\pythonProject\\*/')
directories.sort(key=os.path.getmtime)  # It will sort considering modified time of all the directories.

print('\n'.join(directories))  # It will print a list of directories into a single directory on new line.
