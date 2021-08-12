"""
Huma Khan is a graduate student at Slide Education. As a part of the regular assignment process, the students of Slide
Education are asked to display the last unique character in the given string. Help Huma Khan to solve the problem.
If no such unique character is present, display 'None'.

Input1:
iantarcticarn
Output1:
None

Input2:
Floccinaucinihilipification
Output2:
t
"""

def string(st):
    st = st.lower()
    char_count = {}
    for n in st:
        if n in char_count:
            char_count[n] += 1
        else:
            char_count[n] = 1


    a = list(char_count)[-1]
    # print(char_count[a])
    # print(char_count)

    if char_count[a] == 1:
        return a
    else:
        return None


print(string('iantarcticarn'))
print(string('Floccinaucinihilipification'))
