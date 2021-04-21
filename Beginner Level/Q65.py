"""
Write a Python program to get numbers divisible by fifteen from a list.
"""
numbers = [15, 45, 15, 30, 60]

# Method-1
final_value = []
for number in numbers:
    a = final_value.append(round(number / 15))

print(final_value)


# Method-2 (List Comprehension)
final_value = [round(number / 15) for number in numbers]
print(final_value)
