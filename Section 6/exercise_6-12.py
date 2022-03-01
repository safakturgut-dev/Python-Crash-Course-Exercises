# 6-12
pet_0 = {
    'name': 'lucy',
    'kind': 'cat',
    'owner': 'mary watson',
    'color': 'black',
    'weight': 15.4
}

pet_1 = {
    'name': 'sophia',
    'kind': 'dog',
    'owner': 'matthew jonathan',
    'color': 'white',
    'weight': 60.6
}

pet_2 = {
    'name': 'daffy',
    'kind': 'bird',
    'owner': 'jack sparrow',
    'color': 'yellow',
    'weight': 2.2
}

pets = [pet_0, pet_1, pet_2]

for pet in pets:
    print(
        f"{pet['name'].title()} is a {pet['color']} {pet['kind']}. It's owner is {pet['owner'].title()} and it is {pet['weight']} lb.")
