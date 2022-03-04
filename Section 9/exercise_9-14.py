# 9-14
from random import choice

possible_characters = [4, 5, 49, 12, 29, 35,
                       30, 44, 22, 3, 'c', 'e', 'g', 'x', 's']

winning_ticket = []

while len(winning_ticket) < 4:
    current = choice(possible_characters)
    if current in winning_ticket:
        continue
    else:
        winning_ticket.append(current)

print('Any ticket matching these four numbers or letters wins a prize:')

for i in winning_ticket:
    print(f'{i} ', end='')
