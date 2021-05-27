"""
Implement the unique_names method. When passed two lists of names,
it will return a list containing the names that appear in either or both lists.
The returned list should have no duplicates.
For Example;
calling unique_names(['Ava', 'Emma', 'Olivia'], ['Olivia', 'Sophia', 'Emma'])
should return a list containing Ava, Emma, Olivia, and Sophia in any order.
"""

# Method1
def unique_names(names1, names2):
    box = []
    for n1 in names1:
        if n1 not in box:
            box.append(n1)
    for n2 in names2:
        if n2 not in box:
            box.append(n2)
    return box


# Method2
'''    for n1 in names1:
        for n2 in names2:
            if n1 not in box:
                box.append(n1)
            if n2 not in box:
                box.append(n2)
    return box
'''

print(unique_names(['Ava', 'Emma', 'Olivia'], ['Olivia', 'Sophia', 'Emma']))
