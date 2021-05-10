"""
Write a Python program to find the mean, median and mode among user entered numbers.
"""
value = list(map(int, input('Enter numbers: ').split(',')))
occurrences = sorted(value)
print(f'Occurrences:', occurrences)


# Mean
mean = sum(occurrences) / len(occurrences)
print(f'Mean:', round(mean, 2))


# Mode
temp = dict()
for num in occurrences:
    if num in temp:
        temp[num] += 1
    else:
        temp[num] = 1
# print(temp)
mode = max(temp, key=temp.get)  # get key having maximum value.
print(f'Mode:', mode)

'''
Method 2

temp = 0
count = 0
for num in occurrences:
    if count > temp:
        temp = count
        mode = num
    else:
        count = occurrences.count(num)
print(f'Mode:', mode)
'''


# Median
if len(occurrences) % 2 != 0:  # when total no of occurrences is odd
    middle_index = (len(occurrences) - 1) / 2
    median = occurrences[round(middle_index)]
    print(f'Median:', median)

else:  # when total no of occurrences is even
    middle_index1 = (len(occurrences) - 1) / 2
    middle_index2 = middle_index1 - 1
    median = (occurrences[round(middle_index1)] + occurrences[round(middle_index2)]) / 2
    print(f'Median:', median)
