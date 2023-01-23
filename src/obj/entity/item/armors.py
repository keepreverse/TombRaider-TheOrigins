import const
from src.obj.entity.item.armor import Armor
"""
The number behind Armor is the defense.
"""


class ArmorKevlar(Armor):
    def __init__(self):
        super().__init__('Kevlar vest', const.IMAGE['armor'][0], 3)

    @property
    def information(self):
        return '    Kevlar vest, it has 3 points of defence.'


class ArmorPolice(Armor):
    def __init__(self):
        super().__init__('Police black vest', const.IMAGE['armor'][1], 6)

    @property
    def information(self):
        return '    Police black vest, it has 6 points of defense.'


class ArmorTiger(Armor):
    def __init__(self):
        super().__init__('Tiger colored vest', const.IMAGE['armor'][2], 8)

    @property
    def information(self):
        return '    Tiger colored vest, it has 8 points of defense.'


class ArmorSapphire(Armor):
    def __init__(self):
        super().__init__('Sapphire vest', const.IMAGE['armor'][3], 22)

    @property
    def information(self):
        return '    Sapphire vest, it has 10 points of defense.'


class ArmorSandstorm(Armor):
    def __init__(self):
        super().__init__('Sandstorm vest', const.IMAGE['armor'][4], 44)

    @property
    def information(self):
        return '    Sandstorm vest, it has 12 points of defense.'


class ArmorAbsolute(Armor):
    def __init__(self):
        super().__init__('Absolute vest', const.IMAGE['armor'][5], 16)

    @property
    def information(self):
        return '    Absolute vest, it has 16 points of defense.'
