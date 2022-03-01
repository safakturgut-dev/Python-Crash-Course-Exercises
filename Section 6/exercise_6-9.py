# 6-9
favorite_places = {
    'john': ['rome', 'united states', 'france'],
    'sarah': ['bulgaria', 'sweden', 'germany'],
    'mary': ['netherlands', 'brazil', 'italy'],
}

for key, value in favorite_places.items():
    print(f"{key.title()}'s favorite places are: ")
    for i in value:
        print(f"\t{i.title()}")
    print('')
