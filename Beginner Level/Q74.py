"""
Write a Python program to get the actual module object for a given object.
"""

from inspect import getmodule
from math import *
from datetime import *

print(getmodule(sqrt))
print(getmodule(prod))
print(getmodule(date))
