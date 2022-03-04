# 9-4
class Restaurant:
    def __init__(self, name, cuisine) -> None:
        self.name = name
        self.cuisine = cuisine
        self.number_served = 0

    def describe_restaurant(self):
        print(f"Restaurant name is: {self.name.title()}")
        print(f"Restaurant cuisine type is: {self.cuisine.title()}")

    def open_restaurant(self):
        print('The restaurant is open.')

    def set_number_served(self, number):
        self.number_served = number

    def increment_number_served(self, number):
        self.number_served += number


restaurant_1 = Restaurant('brass tacks', 'chinese')
print(restaurant_1.number_served)

restaurant_1.number_served = 5
print(restaurant_1.number_served)

restaurant_1.set_number_served(10)
print(restaurant_1.number_served)

restaurant_1.increment_number_served(10)
print(restaurant_1.number_served)
