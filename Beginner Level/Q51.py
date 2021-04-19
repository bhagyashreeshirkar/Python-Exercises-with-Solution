"""
Write a Python program to convert seconds to day, hour, minutes and seconds.
Sample Example:
Input time in seconds: 1234565
d:h:m:s-> 14:6:56:5
"""

seconds = int(input('Enter time in seconds: '))
# // takes the whole number before of decimal point

day = seconds // (24 * 60 * 60)  # 1234565 // (24 * 60 * 60) = 14 days
temp1 = day * 24 * 60 * 60   # but 14 days = 14 * 24 * 60 * 60 = 1209600 secs
value1 = seconds - temp1  # hence, 1234565 - 1209600 = 24965 secs left

hour = value1 // (60 * 60)  # so from remaining 24965 secs = 24965 // (60 * 60) = 6 hours
temp2 = hour * 60 * 60  # but 6 hours = 6 * 60 * 60 = 21600 secs
value2 = value1 - temp2  # hence, 24965 - 21600 = 3365 secs left

minutes = value2 // 60  # so from remaining 3365 secs = 3365 // 60 = 56 minutes
temp3 = minutes * 60  # but 56 minutes = 56 * 60 = 3360 secs
value3 = value2 - temp3  # hence, 3365 - 3360 = 5 secs left

remaining_seconds = value3  # so remaining secs = 5 secs


print(f'd:h:m:s = {day}:{hour}:{minutes}:{remaining_seconds}')
