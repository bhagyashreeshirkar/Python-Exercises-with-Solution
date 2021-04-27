"""
Write a Python program find number of possible strings(non-repetitive characters).
Sample Example:
'a', 'e', 'i', 'o', 'u'
no of possible ways - 120
"""
# Method-1
import math


def count(characters):
    no_of_ways = math.factorial(len(characters))
    print(f"Number of ways {','.join(characters)} can be arranged are", no_of_ways)


count(['a', 'e', 'i', 'o', 'u'])
count(['D', 'I', 'S', 'P', 'L', 'A', 'Y'])


# Method-2
def count(characters):
    length = len(characters)
    temp = 1
    for n in range(1, length + 1):
        temp = temp * n
    print(f'No of ways:', temp)


count(['a', 'e', 'i', 'o', 'u'])
count(['D', 'I', 'S', 'P', 'L', 'A', 'Y'])
