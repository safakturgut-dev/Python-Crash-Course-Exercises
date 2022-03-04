# 9-3
class User:
    def __init__(self, fname, lname, age, location) -> None:
        self.fname = fname
        self.lname = lname
        self.age = age
        self.location = location

    def describe_user(self):
        print(f"\nInformation about the user:")
        print(f'\tFirst Name: {self.fname.title()}')
        print(f'\tLast Name: {self.lname.title()}')
        print(f'\tAge: {self.age}')
        print(f'\tLocation: {self.location.title()}')

    def greet_user(self):
        print(
            f"\nHello {self.fname.title()} {self.lname.title()}, welcome back to our website.")


user_1 = User('john', 'doe', 33, 'paris')
user_1.describe_user()
user_1.greet_user()

user_2 = User('sarah', 'thomas', 21, 'boston')
user_2.describe_user()
user_2.greet_user()

user_3 = User('brian', 'glover', 45, 'berlin')
user_3.describe_user()
user_3.greet_user()
