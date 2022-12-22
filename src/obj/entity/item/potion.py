from src.obj.entity.item.food import Food
from const import IMAGE
"""
It's the only kind of food.
It can recover 5 points of health.
"""


class Potion(Food):
    def __init__(self, amount=1):
        super().__init__("Potion", IMAGE['potion'][0], amount, 5)

    @property
    def information(self):
        return '    The little potion can recover 5 points of your HP. Use it before you die.'
