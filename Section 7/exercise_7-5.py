# 7-5
print('Enter your age and i will tell you how much your ticket will cost.')

while True:
    age = int(input('Your age: '))

    if age < 3:
        print('Your ticket is free.')
    elif age < 12:
        print('Your ticket is $10.')
    else:
        print('Your ticket is $15.')
