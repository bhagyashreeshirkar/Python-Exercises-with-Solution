"""
Write a Python program to crate two empty classes, Student and Marks.
Now create some instances and check whether they are instances of the said classes or not.
"""


class Student:
    pass


class Marks:
    pass


student1 = Student()
marks1 = Marks()

print(isinstance(student1, Student))  # Is student1 is an instance/object of class Student?
print(isinstance(marks1, Student))  # Is marks1 is an instance/object of class Student?
