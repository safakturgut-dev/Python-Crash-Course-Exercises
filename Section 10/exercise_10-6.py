# 10-6
num_1 = input('Enter first number: ')
num_2 = input('Enter second number: ')

try:
    result = int(num_1) + int(num_2)
except ValueError:
    print('Please enter numbers only.')
else:
    print(f'The additon result is {result}.')
