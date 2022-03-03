# 8-11
# lorem ipsum messages
short_messages = [
    'Donec tincidunt tortor sit amet risus aliquet, sit amet suscipit mi mollis.',
    'Quisque vitae lectus vulputate, aliquet nulla sit amet, lacinia dui.',
    'Mauris ornare sem rutrum, aliquet ante vel, interdum nisl.',
    'Fusce et ante tempor, laoreet arcu quis, condimentum nunc.',
    'Pellentesque porta odio vel erat ullamcorper rutrum.'
]

sent_messages = []


def send_messages(messages):
    while messages:
        current = messages.pop()
        print(f"Sending message: {current}")
        sent_messages.append(current)


send_messages(short_messages[:])
print(short_messages)
print(sent_messages)
