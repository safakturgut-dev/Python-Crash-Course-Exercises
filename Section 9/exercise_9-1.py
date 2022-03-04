# 9-1
class Restaurant:
    def __init__(self, name, cuisine) -> None:
        self.name = name
        self.cuisine = cuisine

    def describe_restaurant(self):
        print(f"Restaurant name is: {self.name.title()}")
        print(f"Restaurant cuisine type is: {self.cuisine.title()}")

    def open_restaurant(self):
        print('The restaurant is open.')


restaurant_1 = Restaurant('brass tacks', 'chinese')

print(restaurant_1.name)
print(restaurant_1.cuisine)

restaurant_1.describe_restaurant()
restaurant_1.open_restaurant()
