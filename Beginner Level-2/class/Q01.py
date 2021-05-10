"""
Write a Python program to create an instance of a specified class and display the namespace of the said instance.
"""


class Person:
    def __init__(self, name, age, qualification, country):  # properties
        self.name = name
        self.age = age
        self.qualification = qualification
        self.county = country


# by using class we can create multiple objects/ instances
p1 = Person('Alexa', 21, 'B.com', 'USA')
p2 = Person('Hemal', 23, 'B.Tech', 'India')


print(p1.qualification)  # to print single data
print(p1.__dict__)  # to print dict
print(p1.__dict__.keys())  # to print keys
print(p2.__dict__.values())  # to print values
