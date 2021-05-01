"""
Write a Python program that prints all the numbers from 0 to 6 except 3 and 6.
Note : Use 'continue' statement.
Expected Output : 0 1 2 4 5
"""

'''Note: continue will skip mentioned condition and make remaining program executable
      break will stop entire program once mentioned condition gets satisfied'''

for i in range(0, 7):
    if i == 3 or i == 6:
        continue
    print(i, end=' ')

