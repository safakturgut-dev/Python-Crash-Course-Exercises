# 7-6
print('Enter your age and i will tell you how much your ticket will cost.')
print('When you are done enter \'quit\'.\n')

# 1st exercise
# is_active = True

# while is_active:
#     age = input('Your age: ')

#     if age == 'quit':
#         is_active = False
#         continue

#     age_int = int(age)

#     if age_int < 3:
#         print('Your ticket is free.')
#     elif age_int < 12:
#         print('Your ticket is $10.')
#     else:
#         print('Your ticket is $15.')

# 2nd exercise
# tickets_left = 3

# print(f"We have {tickets_left} tickets left for this movie.")

# while tickets_left:
#     age = int(input('Your age: '))

#     if age < 3:
#         print('Your ticket is free.')
#     elif age < 12:
#         print('Your ticket is $10.')
#     else:
#         print('Your ticket is $15.')

#     tickets_left -= 1

# 3rd exercise
while True:
    age = input('Your age: ')

    if age == 'quit':
        break

    age = int(age)

    if age < 3:
        print('Your ticket is free.')
    elif age < 12:
        print('Your ticket is $10.')
    else:
        print('Your ticket is $15.')
