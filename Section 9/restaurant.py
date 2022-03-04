class Restaurant:
    def __init__(self, name, cuisine) -> None:
        self.name = name
        self.cuisine = cuisine

    def describe_restaurant(self):
        print(f"\nRestaurant name is: {self.name.title()}")
        print(f"Restaurant cuisine type is: {self.cuisine.title()}")

    def open_restaurant(self):
        print('The restaurant is open.')
