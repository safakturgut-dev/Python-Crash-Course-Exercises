# 3-5
guest_list = ['john doe', 'jack sparrow', 'tamara dye', 'charlie chaplin']

print(
    f'{guest_list[0].title()} is busy. He can\'t come. I will invite someone else.\n')

guest_list[0] = 'willie price'

print(f'Would you like to come to dinner, {guest_list[0].title()}?')
print(f'Would you like to come to dinner, {guest_list[1].title()}?')
print(f'Would you like to come to dinner, {guest_list[2].title()}?')
print(f'Would you like to come to dinner, {guest_list[3].title()}?')
