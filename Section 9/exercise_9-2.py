# 9-2
class Restaurant:
    def __init__(self, name, cuisine) -> None:
        self.name = name
        self.cuisine = cuisine

    def describe_restaurant(self):
        print(f"\nRestaurant name is: {self.name.title()}")
        print(f"Restaurant cuisine type is: {self.cuisine.title()}")

    def open_restaurant(self):
        print('The restaurant is open.')


restaurant_1 = Restaurant('brass tacks', 'chinese')
restaurant_2 = Restaurant('parallel 37', 'indian')
restaurant_3 = Restaurant('cibo matto', 'italian')

restaurant_1.describe_restaurant()
restaurant_2.describe_restaurant()
restaurant_3.describe_restaurant()
