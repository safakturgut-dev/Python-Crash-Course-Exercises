# 3-7
guest_list = ['bessie mundy', 'john doe', 'anthony love',
              'jack sparrow', 'tamara dye', 'charlie chaplin', 'jordan curran']

print('My dinner table won\'t arrive in time. I can invite only two guest.\n')

guest_pop1 = guest_list.pop()
print(f'Sorry, i can\'t invite you {guest_pop1.title()}.')
guest_pop2 = guest_list.pop()
print(f'Sorry, i can\'t invite you {guest_pop2.title()}.')
guest_pop3 = guest_list.pop()
print(f'Sorry, i can\'t invite you {guest_pop3.title()}.')
guest_pop4 = guest_list.pop()
print(f'Sorry, i can\'t invite you {guest_pop4.title()}.')
guest_pop5 = guest_list.pop()
print(f'Sorry, i can\'t invite you {guest_pop5.title()}.')

print(f'\nYou are still invited to dinner, {guest_list[0].title()}.')
print(f'You are still invited to dinner, {guest_list[1].title()}.')

del guest_list[1]
del guest_list[0]

print(guest_list)
