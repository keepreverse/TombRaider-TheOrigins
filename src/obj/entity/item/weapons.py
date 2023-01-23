import const
from src.obj.entity.item.weapon import Weapon


class Deagle(Weapon):
    def __init__(self):
        super().__init__("Desert Eagle", const.IMAGE['weapon'][0], 7, 50, 7, 90)

    @property
    def information(self):
        return '    Desert Eagle. pistol sometimes called a mini rifle, it has 7 points of damage.'


class HKUMP(Weapon):
    def __init__(self):
        super().__init__("HK UMP", const.IMAGE['weapon'][1], 8, 8, 25, 80)

    @property
    def information(self):
        return '    Heckler & Koch UMP. fast but not so powerful SMG, it has 8 points of damage.'


class SawedOff(Weapon):
    def __init__(self):
        super().__init__("Sawed Off", const.IMAGE['weapon'][2], 11, 70, 8, 130)

    @property
    def information(self):
        return '    Sawed Off. shotgun that can make anyone quiet in a second, it has 12 points of damage.'


class AK47(Weapon):
    def __init__(self):
        super().__init__("AK-47", const.IMAGE['weapon'][3], 9, 7, 30, 120)

    @property
    def information(self):
        return '    AK-47. soviet assault rifle, durable and glamorous, it has 9 points of damage.'


class AWP(Weapon):
    def __init__(self):
        super().__init__("AWP", const.IMAGE['weapon'][4], 20, 100, 5, 160)

    @property
    def information(self):
        return '    Arctic Warfare Police. the best sniper rifle in the world, it has 20 points of damage.'
