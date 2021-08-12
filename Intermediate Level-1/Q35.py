"""
Get the date of joining(as String) as input from the user. Calculate the number of years of experience and
display the same.
Assume
1. The given date is a valid date and the format is dd/mm/yyyy
2. The current date is 15/12/2020

Example:
Input1:
22/08/2006
Output1:
6days-4months-14years

Input2:
09/08/2011
Output2:
6days-4months-9years
"""

date = list(map(int, input().split('/')))
# print(date)

current_day = 15
current_month = 12
current_year = 2020

days = date[0] - current_day
months = date[1] - current_month
years = date[2] - current_year

print(f'{abs(days)}days-{abs(months)}months-{abs(years)}years')
