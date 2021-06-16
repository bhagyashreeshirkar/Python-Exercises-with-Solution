"""
The first line contains the integer, the number of students' records.
The next  lines contain the names and marks obtained by a student, each value separated by a space.
The final line contains query_name, the name of a student to query.
Sample Input:
3
Krishna 67 68 69
Arjun 70 98 63
Malika 52 56 60
Malika

Sample Output:
56.00
"""

data = {}  # initializing a dictionary
for _ in range(int(input())):
    name, *marks = input().split()
    data[name] = [float(m) for m in marks]
scores = data[input()]  # initializing marks of user entered name to scores
result = sum(scores) / len(scores)
print(f'{result:.2f}')  # result:.2f will make result upto 2 decimal places if we want upto 3 then we've to make it 3f
