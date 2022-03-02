# 7-10
print('--- Dream vacation poll ---')
print('When you are done enter \'quit\'.\n')

vacation_poll = {}

while True:
    name = input('Enter your name: ')

    if name == 'quit':
        break

    place = input(
        'If you could visit one place in the world, where would you go? ')

    if place == 'quit':
        break

    vacation_poll[name] = place

print('\nPoll results: ')
for k, v in vacation_poll.items():
    print(f"{k.title()} likes to visit {v.title()}.")
