# 5-10
current_users = ['jadeite', 'whiskey', 'floral', 'astronout', 'rocky']
new_users = ['badminton', 'whiskey', 'Rocky', 'FLORAL', 'harmonica']

for user in new_users:
    if user in current_users:
        print(f"'{user}' username already exists. Please enter new username.")
    else:
        print(f"'{user}' username available.")

current_lower = []
for user in current_users:
    current_lower.append(user.lower())

for user in new_users:
    if user.lower() in current_lower:
        print(f"'{user}' username already exists. Please enter new username.")
    else:
        print(f"'{user}' username available.")
