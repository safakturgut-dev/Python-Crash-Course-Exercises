# 10-11
import json

favorite_number = input('Enter your favorite number: ')

with open('favorite_number.json', 'w') as f:
    json.dump(favorite_number, f)

with open('favorite_number.json') as f:
    number = json.load(f)

print(f"I know your favorite number. It is {number}.")
