"""
Write a Python program to print out a set containing all the colors from color_list_1 which are not present in color_list_2.
Test Data :
color_list_1 = {'White', 'Black', 'Red'}
color_list_2 = {'Red', 'Green'}
Expected Output :
{'Black', 'White'}
"""

color_list_1 = {'White', 'Black', 'Red'}
color_list_2 = {'Red', 'Green'}
set_of_colors = set()   # way of creating a blank set
for color in color_list_1:
    if color not in color_list_2:
        set_of_colors.add(color)
print(set_of_colors)  # method-1

print(color_list_1.difference(color_list_2))  # method-2
