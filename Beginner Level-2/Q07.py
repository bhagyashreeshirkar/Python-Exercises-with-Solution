"""
Write a Python program to get a string from a given string,
where all occurrences of its first char have been changed to '$', except the first char itself.
Sample String : 'restart'
Expected Result : 'resta$t'
"""


def enter(string):
    first_ch = string[0]  # assigning first letter of string to a variable(first_ch) ie, r
    a = string[1:]  # assigning whole string except first letter of entered string
    s = ''
    for ch in string[1:]:  # from second char of string to whole string ie, estart
        if ch == first_ch:  # if ch from estart is equal to first_ch ie, r then replace every r in estart with $ and assigned it to a variable ie, s
            s = a.replace(ch, '$')
    print(first_ch + s)  # then concatenate r + esta$t = resta$t


enter('restart')
enter('template')
enter('initial')
