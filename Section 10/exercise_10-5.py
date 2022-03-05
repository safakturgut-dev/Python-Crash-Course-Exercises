# 10-5
filename = 'favorite_fruits.txt'

print('When you are done enter \'q\'.')

while True:
    fruit = input('Enter your favorite fruits: ')

    if fruit == 'q':
        break

    with open(filename, 'a') as f:
        f.write(f"{fruit}\n")
