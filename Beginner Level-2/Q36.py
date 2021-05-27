"""
Implement a group_by_owners function that:
1. Accepts a dictionary containing a list of the file names for each file name.
2. Returns a dictionary containing a list of file names for each owner name, in any order.

For Example,
for dictionary {'Input.txt': 'Randy', 'Code.py': 'Stan', 'Output.txt': 'Randy'}
output:
'Randy': ['Input.txt', 'Output.txt'], 'Stan': ['Code.py']}
"""

files = {'Input.txt': 'Randy', 'Code.py': 'Stan', 'Output.txt': 'Randy'}

dummy_dict = {}
for key, value in files.items():
    if value in dummy_dict:
        dummy_dict[value].append(key)
    else:
        dummy_dict[value] = [key]
print(dummy_dict)
