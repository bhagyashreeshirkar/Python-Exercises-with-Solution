"""
Define a Python function student(). Using function attributes display the names of all arguments.
"""


def student(student_id, name, division):
    return student_id, name, division


# Method1
student1 = student(14, 'Raghav', 'C')
print(student1)

# Method2
print(student(62, 'Deny', 'A'))
