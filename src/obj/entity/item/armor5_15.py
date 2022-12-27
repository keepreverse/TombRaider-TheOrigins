import const
from src.obj.entity.item.armor import Armor
"""
The number behind Armor is the defense.
"""


class Armor5(Armor):
    def __init__(self):
        super().__init__('Ordinary wooden shield', const.IMAGE['armor'][0], 2)

    @property
    def information(self):
        return '    Ordinary wooden shield, 2 points of defence.'


class Armor7(Armor):
    def __init__(self):
        super().__init__('Delicate wooden shield', const.IMAGE['armor'][1], 4)

    @property
    def information(self):
        return '    Delicate wooden shield, beautiful and with decoration, it has 4 points of defense.'


class Armor9(Armor):
    def __init__(self):
        super().__init__('Knight shield', const.IMAGE['armor'][2], 6)

    @property
    def information(self):
        return '    Shield used by knight in middle ages, it has 6 points of defense.'


class Armor11(Armor):
    def __init__(self):
        super().__init__('sapphire Armor', const.IMAGE['armor'][3], 8)

    @property
    def information(self):
        return '    A sapphire shield, durable and glamorous, it has 8 points of defense.'


class Armor13(Armor):
    def __init__(self):
        super().__init__('Moon shield', const.IMAGE['armor'][4], 10)

    @property
    def information(self):
        return '    A Moon shield. Made by rock of the moon, it has 10 points of defense.'


class Armor15(Armor):
    def __init__(self):
        super().__init__('King shield', const.IMAGE['armor'][5], 12)

    @property
    def information(self):
        return '    A King shield. the best shield in the world, it has 12 points of defense.'
