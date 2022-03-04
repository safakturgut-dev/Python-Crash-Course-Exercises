import user_2


class Privileges:
    def __init__(self) -> None:
        self.privileges = ['can add post', 'can delete post',
                           'can ban user', 'can make moderators']

    def show_privileges(self):
        print('Admin\'s privileges are:')

        for privilege in self.privileges:
            print(privilege)


class Admin(user_2.User):
    def __init__(self, fname, lname, age, location):
        super().__init__(fname, lname, age, location)
        self.privileges = Privileges()
