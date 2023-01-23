from src.obj.entity.item.food_buff import FoodBuff
from const import IMAGE


class PotionBuff(FoodBuff):
    def __init__(self, amount=1):
        super().__init__("Buff potion", IMAGE['potion'][1], amount)

    @property
    def information(self):
        return '    This buff potion makes you move faster for a while.'
