# 10-7
print('Give me two numbers and i will add them.')
print('Enter \'q\' for quit.\n')

while True:
    num_1 = input('Enter first number: ')

    if num_1 == 'q':
        break

    num_2 = input('Enter second number: ')

    if num_2 == 'q':
        break

    try:
        result = int(num_1) + int(num_2)
    except ValueError:
        print('Please enter numbers only.')
    else:
        print(f'The additon result is {result}.')
