"""
Write a Python program to sum of two given integers. However, if the sum is between 15 to 20 it will return 20.
"""


def sum(a, b):
    addition = a + b
    # if 15 < addition < 20:       # Method-1
    if addition in range(15, 20):  # Method-2
        return 20
    else:
        return addition


print(sum(15, 3))
print(sum(11, 6))
print(sum(90, 2))
