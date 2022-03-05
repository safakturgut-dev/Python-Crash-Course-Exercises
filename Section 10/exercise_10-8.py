# 10-8
try:
    with open('cats.txt') as f:
        contents = f.read().rstrip()
except FileNotFoundError:
    print('File does not exist...')
else:
    print('-- Cats --')
    print(contents)

try:
    with open('dogs.txt') as f:
        contents = f.read().rstrip()
except FileNotFoundError:
    print('File does not exist...')
else:
    print('\n-- Dogs --')
    print(contents)
