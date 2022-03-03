# 8-16
# import making_car
from making_car import make_car
# from making_car import make_car as mc
# import making_car as mc
# from making_car import *

car = make_car('ford', 'ranger', color='red', price=25500)

for key, value in car.items():
    print(f"{key.title()}: {value}")
