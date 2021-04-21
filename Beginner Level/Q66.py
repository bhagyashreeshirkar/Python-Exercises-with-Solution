"""
Write a Python program to make file lists from current directory.
"""
import glob

files = glob.glob('*.*')
print(files)
