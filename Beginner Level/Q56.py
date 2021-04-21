"""
Write a Python program to sort files by date.
"""

import os
import glob

# glob (short for global) is used to return all file paths that match a specific pattern.
files = glob.glob('*.*')
files.sort(key=os.path.getmtime)  # it will sort files by modified time.


print('\n'.join(files))  # It will print a list of files into a single file on new line.
