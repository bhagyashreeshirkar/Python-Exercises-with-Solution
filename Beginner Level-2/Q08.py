"""
Write a Python program to convert JSON data to Python object.
Note: To write json data it is mandatory; single quotes - outside dictionary and double quotes - inside dictionary
(you cannot apply python functions to the json file directly until loading it.)
"""
import json

json_data = '{"Name": "John", "Age": 18, "Subject": "Economics"}'
python_data = json.loads(json_data)  # It converts(loads) json data into python data

print(f'Loaded json data:', python_data)

print(f"Name: {python_data['Name']} \nAge: {python_data['Age']} \nSubject: {python_data['Subject']}")
