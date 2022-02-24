# 3-6
guest_list = ['john doe', 'jack sparrow', 'tamara dye', 'charlie chaplin']

print("I found a bigger dinner table, we can have dinner with more people.\n")

guest_list.insert(0, 'bessie mundy')
guest_list.insert(2, 'anthony love')
guest_list.append('jordan curran')

print(f'Would you like to come to dinner, {guest_list[0].title()}?')
print(f'Would you like to come to dinner, {guest_list[1].title()}?')
print(f'Would you like to come to dinner, {guest_list[2].title()}?')
print(f'Would you like to come to dinner, {guest_list[3].title()}?')
print(f'Would you like to come to dinner, {guest_list[4].title()}?')
print(f'Would you like to come to dinner, {guest_list[5].title()}?')
print(f'Would you like to come to dinner, {guest_list[6].title()}?')

print(guest_list)
