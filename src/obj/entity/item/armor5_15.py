import const
from src.obj.entity.item.armor import Armor
"""
The number behind Armor is the defense.
"""


class Armor5(Armor):
    def __init__(self):
        super().__init__('Ordinary wooden shield', const.IMAGE['armor'][0], 5)

    @property
    def information(self):
        return '    Ordinary wooden shield, 5 points of defence.'


class Armor7(Armor):
    def __init__(self):
        super().__init__('Delicate wooden shield', const.IMAGE['armor'][1], 7)

    @property
    def information(self):
        return '    Delicate wooden shield, beautiful and with decoration, it has 7 points of defense. :D'


class Armor9(Armor):
    def __init__(self):
        super().__init__('Knight shield', const.IMAGE['armor'][2], 9)

    @property
    def information(self):
        return '    Shield used by knight in middle ages, it has 9 points of defense. :D'


class Armor11(Armor):
    def __init__(self):
        super().__init__('sapphire Armor', const.IMAGE['armor'][3], 11)

    @property
    def information(self):
        return '    A sapphire shield, durable and glamorous, it has 11 points of defense. :D'


class Armor13(Armor):
    def __init__(self):
        super().__init__('Moon shield', const.IMAGE['armor'][4], 13)

    @property
    def information(self):
        return '    A Moon shield. Made by rock of the moon, it has 13 points of defense. :D'


class Armor15(Armor):
    def __init__(self):
        super().__init__('King shield', const.IMAGE['armor'][5], 15)

    @property
    def information(self):
        return '    A King shield. the best shield in the world, it has 15 points of defense. :D'
