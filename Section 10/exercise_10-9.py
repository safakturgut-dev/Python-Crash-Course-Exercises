# 10-9
try:
    with open('cats.txt') as f:
        contents = f.read().rstrip()
except FileNotFoundError:
    pass
else:
    print('-- Cats --')
    print(contents)

try:
    with open('dogs.txt') as f:
        contents = f.read().rstrip()
except FileNotFoundError:
    pass
else:
    print('\n-- Dogs --')
    print(contents)
