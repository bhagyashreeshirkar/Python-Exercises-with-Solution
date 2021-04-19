"""
Write a Python program to convert all units(day, hour, minutes) of time into seconds
Sample Example:
days: 4
hours: 5
minutes: 20
seconds: 10
The amounts of seconds 364810
"""

days = int(input('days: '))
hours = int(input('hours: '))
minutes = int(input('minutes: '))
seconds = int(input('seconds: '))

secs = (days * 24 * 60 * 60) + (hours * 60 * 60) + (minutes * 60) + seconds

print('Total seconds for the above specified data is', secs)
