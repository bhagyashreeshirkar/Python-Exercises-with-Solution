"""
Write a Python program that will return true if the two given integer values are equal or their sum or difference is 5.
"""


def numbers(a, b):
    if a == b or abs(a - b) == 5 or a + b == 5:
        return True
    else:
        return False


print(numbers(7, 2))
print(numbers(3, 2))
print(numbers(2, 2))
print(numbers(45, 21))
