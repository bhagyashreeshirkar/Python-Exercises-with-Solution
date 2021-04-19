"""
Write a Python program to convert the distance (in feet) to inches, yards, and miles.
Sample Test:
Enter the distance in feet: 100
inches: 1200.0
yards: 33.33
miles: 0.02
"""

feet = float(input('Enter the distance in feet: '))
inches = feet * 12
yards = feet / 3
miles = feet / 5280

print(f'inches: {round(inches,2)} \nyards: {round(yards, 2)} \nmiles: {round(miles, 2)}')
