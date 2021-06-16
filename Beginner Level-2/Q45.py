"""
Methods for how to take Multiple Inputs:
"""


# How to take 2 inputs on a single line (if you want more then you can add more variables a, b, c, d, e, etc)
a, b = map(int, input('Enter two numbers: ').split(' '))
print(a, b)


# How to take list of multiple inputs
user = list(map(int, input('Numbers: ').split(' ')))
print(user)


# How to take multiple inputs in defined function
def value(*numbers):
    return numbers


print(value(9, 3, 2, 1, 5))


# How to take no of inputs with values from user
# Method 1 - using while loop
lines = int(input('Enter no of students: '))
a = ''
while lines > 0:
    a += input() + ' '
    lines -= 1

print(a)

# Method 2 - using for loop
lines = int(input('Enter no of students: '))
a = ''
for n in range(1, lines + 1):
    a += input() + ' '

print(a)

# get no of inputs decided prior by user
names = []
for _ in range(int(input())):
    name = input()
    names.append(name)

print(names)


# get no of inputs decided prior by user(2)
data = {}
for _ in range(int(input())):
    name, *marks = input().split()
    data[name] = [float(m) for m in marks]

print(data)
