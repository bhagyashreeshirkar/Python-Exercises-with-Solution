"""
Write a Python program that prints each item and its corresponding type from the following list.

Sample List : datalist = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12], {"class":'V', "section":'A'}]
"""

datalist = [1452, 11.23, 1 + 2j, True, 'Jack', (0, -2, 3), [3, 10, 5.6], {'subject1': 'Economics', 'serial no': 23}]

for n in datalist:
    print(f'{n} :- {type(n)}')
