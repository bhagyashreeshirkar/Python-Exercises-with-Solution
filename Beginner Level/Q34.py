"""
Write a Python program to add two objects if both objects are an integer type.
"""


# Method-1
def objects(x, y):
    if x == int(x) and y == int(y):
        return x + y
    else:
        raise TypeError('Inputs must be Integers')  # by using this you can throw your own exception
        # once after raising an exception below code does not executes


print(objects(4, 50))
print(objects(3.2, 78))

"""
Using Python isinstance(), you can do the followings:
1. Test whether an object/variable is an instance of the specified type or class such as list, dict, set, or tuple.
2. Verify whether a variable is a number or string.
3. Checks if the specified class is the parent class of an object.
"""


# Method-2
def values(a, b):
    if isinstance(a, int) and isinstance(b, int):
        return a + b
    else:
        raise TypeError('Inputs must be Integers')


print(values(4, 50))
print(values('Mike', 'John'))
