"""
Write a Python program that iterate over elements repeating each as many times as its count.
Sample Input: p = 4, r = 0, s = 1, q = 2
Sample Output: ['p', 'p', 'p', 'p', 'q', 'q','s']
"""

from collections import Counter

value = Counter(p=4, q=2, r=0, s=1)  # you can use any alphabets which you want to repeat
print(list(value.elements()))  # elements() function is use under Counter library
