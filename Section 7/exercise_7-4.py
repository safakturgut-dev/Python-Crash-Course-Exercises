# 7-4
print('Enter your pizza topping to program.')
print('When you are done enter \'quit\'.\n')

while True:
    topping = input('Pizza topping: ')
    if topping == 'quit':
        break
    else:
        print(f"{topping.title()} added to your pizza.")
