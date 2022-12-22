import const
from src.obj.entity.item.weapon import Weapon
"""
The number behind the weapon is it's damage. 
We didn't design the weapon carefully, their shoot interval time, clip and reload time are the same.
"""


class Weapon7(Weapon):
    def __init__(self):
        super().__init__("Birch bow", const.IMAGE['weapon'][0], 7, 30, 10, 60)

    @property
    def information(self):
        return '    A birch weapon. my grandma sent me when i 7 years old, it has 7 points of damage. :D'


class Weapon9(Weapon):
    def __init__(self):
        super().__init__("Love bow", const.IMAGE['weapon'][1], 9, 30, 10, 60)

    @property
    def information(self):
        return '    A Love bow. my girlfriend sent me when i 19 years old, it has 9 points of damage. :D'


class Weapon11(Weapon):
    def __init__(self):
        super().__init__("simple cane", const.IMAGE['weapon'][2], 11, 30, 10, 60)

    @property
    def information(self):
        return '    A simple cane. my dad sent me when i 25 years old, it has 11 points of damage. :D'


class Weapon13(Weapon):
    def __init__(self):
        super().__init__("sapphire  cane", const.IMAGE['weapon'][3], 13, 30, 10, 60)

    @property
    def information(self):
        return '    A sapphire  cane. durable and glamorous, it has 13 points of damage. :D'


class Weapon15(Weapon):
    def __init__(self):
        super().__init__("king's sceptre", const.IMAGE['weapon'][4], 15, 30, 10, 60)

    @property
    def information(self):
        return '    king\'s sceptre,  the best weapon in the world, it has 15 points of damage :D.'
