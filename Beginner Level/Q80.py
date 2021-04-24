"""
Write a Python program to list home directory without absolute path.
"""

import os

print(os.path.expanduser('~'))
