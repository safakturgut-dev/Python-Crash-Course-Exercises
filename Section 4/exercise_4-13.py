# 4-13
foods = ('hamburger', 'pizza', 'lamb salad', 'fajitas', 'jambalaya')

print('Original menu is: ')
for food in foods:
    print(food.title())

# foods[1] = 'pizza' # error

foods = ('peanut butter sandwich', 'macaroni and cheese',
         'lamb salad', 'fajitas', 'jambalaya')

print('\nEdited menu is: ')
for food in foods:
    print(food.title())
