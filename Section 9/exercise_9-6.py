# 9-6
class Restaurant:
    def __init__(self, name, cuisine) -> None:
        self.name = name
        self.cuisine = cuisine

    def describe_restaurant(self):
        print(f"\nRestaurant name is: {self.name.title()}")
        print(f"Restaurant cuisine type is: {self.cuisine.title()}")

    def open_restaurant(self):
        print('The restaurant is open.')


class IceCreamStand(Restaurant):

    def __init__(self, name, cuisine) -> None:
        super().__init__(name, cuisine)
        self.flavors = ['chocolate', 'vanilin', 'strawberry']

    def available_flavors(self):
        print('Flavors that are available:')

        for flavor in self.flavors:
            print(f"- {flavor}")


ice_1 = IceCreamStand('ding dong', 'ice cream')
ice_1.describe_restaurant()
ice_1.available_flavors()
