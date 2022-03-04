# 9-13
from random import randint


class Dice:
    def __init__(self, sides=6) -> None:
        self.sides = sides

    def roll_dice(self):
        print(randint(1, self.sides))


dice_1 = Dice()

for i in range(10):
    dice_1.roll_dice()

dice_2 = Dice(10)

for i in range(10):
    dice_2.roll_dice()
