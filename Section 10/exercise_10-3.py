# 10-3
name = input('Enter your name: ')
filename = 'guest.txt'

with open(filename, 'w') as f:
    f.write(name)
