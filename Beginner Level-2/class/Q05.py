"""
Write a Python class named Student with two attributes student_name, marks.
Modify the attribute values of the said class and print the original and modified values of the said attributes.
"""


class Student:
    student_name = 'kevin'
    marks = 89


# To get original values of attributes
print(getattr(Student, 'student_name'))
print(getattr(Student, 'marks'))


# To modify attributes
setattr(Student, 'student_name', 'Daisy')
print(getattr(Student, 'student_name'))

setattr(Student, 'marks', 90)
print(getattr(Student, 'marks'))
