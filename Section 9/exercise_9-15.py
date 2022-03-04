# 9-15
from random import choice

possible_characters = [4, 5, 49, 12, 29, 35,
                       30, 44, 22, 3, 'c', 'e', 'g', 'x', 's']

winning_ticket = []
my_ticket = [49, 'c', 22, 'x']
number_of_try = 0

while winning_ticket != my_ticket:
    winning_ticket.clear()
    while len(winning_ticket) < 4:
        current = choice(possible_characters)
        if current in winning_ticket:
            continue
        else:
            winning_ticket.append(current)

    number_of_try += 1

    print(number_of_try, winning_ticket)

print(f'It took {number_of_try} tries to win lottery.')
