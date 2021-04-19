"""
Write a Python program to get file creation and modification date/times.

getctime = get created time
getmtime = get (last) modification time
The time.ctime() function takes seconds passed since file is been made, returns a string representing local time.
"""

import os
import time

print('Created time:', time.ctime(os.path.getctime('Q27.py')))
print('Modified time:', time.ctime(os.path.getmtime('Q27.py')))
