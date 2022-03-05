# 10-4
filename = 'guest_book.txt'

print("When you are finished enter 'quit'.")
while True:
    name = input('Enter your name: ')

    if name == "quit":
        break

    print(f"Hello {name.title()} welcome back.")

    with open(filename, 'a') as f:
        f.write(f'{name}\n')
