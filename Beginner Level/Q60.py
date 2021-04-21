"""
Write a Python program to calculate the sum over a container.
"""

container = [20, 11, 45, 2, 8, 34]

# Method-1
print(sum(container))

# Method-2
addition = 0
for n in container:
    addition = addition + n
print(addition)
