# 9-8
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


class Privileges:
    def __init__(self) -> None:
        self.privileges = ['can add post', 'can delete post',
                           'can ban user', 'can make moderators']

    def show_privileges(self):
        print('Admin\'s privileges are:')

        for privilege in self.privileges:
            print(privilege)


class Admin(User):
    def __init__(self, fname, lname, age, location):
        super().__init__(fname, lname, age, location)
        self.privileges = Privileges()


admin_1 = Admin('denise', 'pittman', 32, 'pittsburgh')
admin_1.describe_user()
admin_1.privileges.show_privileges()
