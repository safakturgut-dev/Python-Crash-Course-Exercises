# 7-8
sandwich_orders = ['potato', 'vegetarian', 'paneer', 'curd', 'grilled cheese']
finished_sandwiches = []

while sandwich_orders:
    current = sandwich_orders.pop()
    print(f'I made your {current.title()} sandwich.')
    finished_sandwiches.append(current)

print('\nFinished sandwiches:')
for sandwich in finished_sandwiches:
    print(f"- {sandwich.title()} sandwich.")
