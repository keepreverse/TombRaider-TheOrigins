import const
from src.obj.entity.item.weapon import Weapon
"""
The number behind the weapon is it's damage. 
We didn't design the weapon carefully, their shoot interval time, clip and reload time are the same.
"""


class Glock18(Weapon):
    def __init__(self):
        super().__init__("Glock 18", const.IMAGE['weapon'][0], 8, 4, 17, 100)

    @property
    def information(self):
        return '    Glock 18. My grandma sent me when i 8 years old, it has 8 points of damage.'


class HKUMP(Weapon):
    def __init__(self):
        super().__init__("HK UMP", const.IMAGE['weapon'][1], 7, 7, 25, 150)

    @property
    def information(self):
        return '    Heckler & Koch UMP. my girlfriend sent me when i 19 years old, it has 10 points of damage.'


class BenelliNova(Weapon):
    def __init__(self):
        super().__init__("Benelli Nova", const.IMAGE['weapon'][2], 12, 70, 8, 200)

    @property
    def information(self):
        return '    Benelli Nova. my dad sent me when i 25 years old, it has 12 points of damage.'


class AK47(Weapon):
    def __init__(self):
        super().__init__("AK-47", const.IMAGE['weapon'][3], 10, 10, 30, 140)

    @property
    def information(self):
        return '    AK-47. durable and glamorous, it has 10 points of damage.'


class AWP(Weapon):
    def __init__(self):
        super().__init__("AWP", const.IMAGE['weapon'][4], 20, 100, 5, 250)

    @property
    def information(self):
        return '    Arctic Warfare Police,  the best sniper rifle in the world, it has 20 points of damage.'
