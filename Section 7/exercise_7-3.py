# 7-3
print('Ask me if a number multiple of 10 and i will answer.')
number = int(input('Number: '))

if number % 10:
    print(f'{number} is NOT multiple of ten.')
else:
    print(f'{number} is multiple of ten.')
