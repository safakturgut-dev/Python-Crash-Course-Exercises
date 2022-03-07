class Employee:
    def __init__(self, fname, lname, salary) -> None:
        self.fname = fname
        self.lname = lname
        self.salary = salary

    def give_raise(self, raise_amount=5000):
        self.salary += raise_amount
