# 7-9
# sandwich_orders = ['potato', 'pastrami', 'vegetarian',
#                    'pastrami', 'paneer', 'curd', 'pastrami', 'grilled cheese']
# finished_sandwiches = []

# print('Deli has ran out of pastrami.\n')

# while 'pastrami' in sandwich_orders:
#     sandwich_orders.remove('pastrami')

# while sandwich_orders:
#     current = sandwich_orders.pop()
#     print(f'I made your {current.title()} sandwich.')
#     finished_sandwiches.append(current)

# print('\nFinished sandwiches:')
# for sandwich in finished_sandwiches:
#     print(f"- {sandwich.title()} sandwich.")

# other way
sandwich_orders = ['potato', 'pastrami', 'vegetarian',
                   'pastrami', 'paneer', 'curd', 'pastrami', 'grilled cheese']
finished_sandwiches = []

print('Deli has ran out of pastrami.\n')

while sandwich_orders:
    current = sandwich_orders.pop()

    if current == 'pastrami':
        continue

    print(f'I made your {current.title()} sandwich.')
    finished_sandwiches.append(current)

print('\nFinished sandwiches:')
for sandwich in finished_sandwiches:
    print(f"- {sandwich.title()} sandwich.")
