"""
Write a Python function student_data () which will print the id of a student (student_id).
If the user passes an argument student_name or student_class the function will print the student name and class.
"""


def student_data(student_id, **kwargs):
    print(student_id)
    if 'student_name' in kwargs:
        print(f'{kwargs["student_name"]}')

    if 'student_class' in kwargs:
        print(f'{kwargs["student_class"]}')


student_data(student_id='SV12', student_name='Jean Garner')
student_data(student_id='SV12', student_name='Jean Garner', student_class='V')
