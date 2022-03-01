# 6-8
pet_0 = {
    'name': 'lucy',
    'kind': 'cat',
    'owner': 'mary watson'
}

pet_1 = {
    'name': 'sophia',
    'kind': 'dog',
    'owner': 'matthew jonathan'
}

pet_2 = {
    'name': 'daffy',
    'kind': 'bird',
    'owner': 'jack sparrow'
}

pets = [pet_0, pet_1, pet_2]

for pet in pets:
    print(
        f"{pet['name'].title()} is a {pet['kind']}. It's owner is {pet['owner'].title()}.")
