"""
 Write a Python program to create a histogram from a given list of integers.
"""

import matplotlib.pyplot as plot

numbers = [2, 10, 7, 3, 5, 99, 100, 22, 3, 50, 55, 60]
plot.hist(numbers)
plot.show()
