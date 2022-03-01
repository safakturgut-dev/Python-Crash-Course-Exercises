# 5-8
usernames = ['admin', 'venison', 'harmonica', 'peanuts', 'casanova']

for user in usernames:
    if user == 'admin':
        print(f"Hello {user}, would you like to see a status report?")
    else:
        print(f"Hello {user}, thank you for logging in again.")
