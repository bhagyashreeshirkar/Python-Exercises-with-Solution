"""
Write a Python script to display the various Date Time formats
a) Current date and time b) Current year c) Month of year d) Date e) Day of week  f) Week number of the year g) Weekday of the week h) Day of year

Note:- strftime(): It returns the string representation of the date or time object.
"""
from datetime import *


print(f'Current date and time: ', datetime.now())
print(f'Current year: ', datetime.now().strftime('%Y'))  # Y- Year
print(f'Month of year: ', datetime.now().strftime('%B'))  # B - Month
print(f'Date: ', datetime.now().strftime('%d'))  # d - date
print(f'Day of week: ', datetime.now().strftime('%A'))  # D - Day of week
print(f'Week number of the year: ', datetime.now().strftime('%W'))  # W - Week number of year
print(f'Weekday of the week: ', datetime.now().strftime('%w'))  # w - week day of a week
print(f'Day of year: ', datetime.now().strftime('%j'))  # j - day of an year
