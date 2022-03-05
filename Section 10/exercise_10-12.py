# 10-12
import json

try:
    with open('favorite_number.json') as f:
        number = json.load(f)
except FileNotFoundError:
    favorite_number = input('Enter your favorite number: ')
    with open('favorite_number.json', 'w') as f:
        json.dump(favorite_number, f)
    print('We will remember your favorite number next time.')
else:
    print(f"I know your favorite number. It is {number}.")
