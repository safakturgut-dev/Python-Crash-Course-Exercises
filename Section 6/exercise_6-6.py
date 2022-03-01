# 6-6
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

should_take_poll = ['sandra', 'edward', 'donald', 'sarah', 'russell']

for name in should_take_poll:
    if name in favorite_languages:
        print(f"Thank you for your response, {name.title()}.")
    else:
        print(f'Please take our poll, {name.title()}.')
