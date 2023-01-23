from src.obj.entity.item.food_hp import FoodHP
from const import IMAGE


class PotionHP(FoodHP):
    def __init__(self, amount=1):
        super().__init__("Healing potion", IMAGE['potion'][0], amount, 3)

    @property
    def information(self):
        return '    This healing potion can restore 3 points of your HP.'
