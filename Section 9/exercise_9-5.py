# 9-5
class User:
    def __init__(self, fname, lname, age, location) -> None:
        self.fname = fname
        self.lname = lname
        self.age = age
        self.location = location
        self.login_attempts = 0

    def describe_user(self):
        print(f"\nInformation about the user:")
        print(f'\tFirst Name: {self.fname.title()}')
        print(f'\tLast Name: {self.lname.title()}')
        print(f'\tAge: {self.age}')
        print(f'\tLocation: {self.location.title()}')

    def greet_user(self):
        print(
            f"\nHello {self.fname.title()} {self.lname.title()}, welcome back to our website.")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


user_1 = User('john', 'doe', 33, 'paris')

print(user_1.login_attempts)
user_1.increment_login_attempts()
user_1.increment_login_attempts()
user_1.increment_login_attempts()
print(user_1.login_attempts)

user_1.reset_login_attempts()
print(user_1.login_attempts)
