"""
Write a Python program to sort (ascending and descending) a dictionary by value.
"""

dictionary = {'carl': 40, 'alan': 2, 'bob': 1, 'danny': 3}

# Dictionary by Ascending Order of values
sorted_values = sorted(dictionary.values())
sorted_dict = {}

for k in sorted_values:
    for n in dictionary:
        if dictionary[n] == k:
            sorted_dict[n] = k
print(f'sorted dictionary:', sorted_dict)


# Dictionary by Descending Order of values
reversed_sorted_values = sorted(dictionary.values(), reverse=True)
reversed_dict = {}

for k in reversed_sorted_values:
    for n in dictionary:
        if dictionary[n] == k:
            reversed_dict[n] = k
print(f'reversed dictionary', reversed_dict)
