"""
1. Write a Python program to create a set.
2. Write a Python program to add member(s) in a set.
3. Write a Python program to remove item(s) from set.
"""

# 1. Write a Python program to create a set.
number = set()
print(number)  # Empty set

number1 = {2, 3, 1, 4}
print(number1)  # set with integers

# 2. Write a Python program to add member(s) in a set.
values = {2, 4, 11, 34, 7}
values.add(7)
print(values)

# 3. Write a Python program to remove item(s) from set.
# Method-1
num = {34, 21, 'John', 45, 'Lisa'}
num.remove('John')
print(num)

# Method-2
num.pop()  # pop() function will remove any of item from the set by its own
print(num)
