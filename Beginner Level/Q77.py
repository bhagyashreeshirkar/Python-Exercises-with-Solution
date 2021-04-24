"""
Write a python program to count each word repeated in a string.
"""
paragraph = 'As they went to go home, they noticed the rocks that they used to guide them into the forest were gone. They had nothing to lead them back; they were lost.'


# Method-1
counts = {}  # assigning an empty dictionary
words = paragraph.lower().split()

for word in words:
    if word in counts:  # This is the way you can add words into a dictionary(counts);
        counts[word] += 1  # if there's already a word present in it add 1 to its value whenever word repeats
    else:
        counts[word] = 1  # else by adding word to a dictionary assign its value as 1
print(counts)


# Method-2
words = paragraph.lower().split()  # they and They will be consider separately hence we make a statement into lower letters

for word in set(words):
    print(f'{word} = {words.count(word)}', end=',')  # since we're considering it as a set keys are unordered
